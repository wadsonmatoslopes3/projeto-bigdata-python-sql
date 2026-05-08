import pandas as pd
from sqlalchemy import create_engine

# Conexão com o seu banco existente
engine = create_engine("mysql+pymysql://root:@localhost/projeto_de_leitura")

# Caminho do arquivo que você mostrou no print
caminho_nat = r'C:\Users\wadso\OneDrive\Documentos\phyton\2 semestre\trabalho final\06 - Naturezas\F.K03200Z.D30812.NATUCNSV'

try:
    print("Importando dicionário de Naturezas Jurídicas...")

    # Lendo o arquivo. O separador parece ser ';' e os textos estão entre aspas
    df_nat = pd.read_csv(caminho_nat, sep=';',
                         encoding='latin1', header=None, quotechar='"')

    # Nomeando as colunas para facilitar o cruzamento depois
    df_nat.columns = ['codigo', 'descricao_natureza']

    # Salvando no MySQL em uma nova tabela chamada 'tab_naturezas'
    df_nat.to_sql('tab_naturezas', con=engine,
                  if_exists='replace', index=False)

    print(f"Sucesso! {len(df_nat)} naturezas importadas.")

except Exception as e:
    print(f"Erro ao importar naturezas: {e}")
