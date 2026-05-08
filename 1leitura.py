import pandas as pd
from sqlalchemy import create_engine
import time

# 1. Configuração da Conexão (Utilizando SQLAlchemy para maior velocidade)
# formato: mysql+pymysql://usuario:senha@host/nome_do_banco
engine = create_engine("mysql+pymysql://root:@localhost/projeto_de_leitura")

# 2. Caminho do seu arquivo de 1GB (ajustado conforme sua imagem)
caminho_arquivo = r'C:\Users\wadso\OneDrive\Documentos\phyton\2 semestre\trabalho final\06 - Empresas0\K3241.K03200Y0.D30812.EMPRECSV'

print("Iniciando a leitura do arquivo de 1GB... Isso pode levar alguns minutos.")
inicio = time.time()

try:
    # 3. Lendo o arquivo em 'pedações' (chunks) de 50.000 linhas por vez
    # Isso evita que a memória do seu computador fique cheia e o PC trave.
    chunk_size = 50000

    # O arquivo CNPJ usa ';' como separador e codificação latin1
    for i, chunk in enumerate(pd.read_csv(caminho_arquivo, sep=';', encoding='latin1', chunksize=chunk_size, header=None)):

        # Definindo os nomes das colunas conforme o seu PDF (Captura de Tela 1)
        chunk.columns = ['cnpj_basico', 'razao_social',
                         'natureza_juridica', 'qualificacao', 'capital', 'porte', 'ente']

        # 4. Enviando o pedaço para a tabela 'empresas' no MySQL
        chunk.to_sql('empresas', con=engine, if_exists='append', index=False)

        print(f"Lote {i+1}: {(i+1) * chunk_size} linhas processadas...")

    fim = time.time()
    print(f"\n--- IMPORTAÇÃO CONCLUÍDA COM SUCESSO ---")
    print(f"Tempo total: {(fim - inicio) / 60:.2f} minutos.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
