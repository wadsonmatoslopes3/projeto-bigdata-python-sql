# Processamento de Big Data - Dados.BR

Este projeto foi desenvolvido como parte do 2º semestre da faculdade, focado em engenharia de dados e performance de banco de dados.

## 🚀 Objetivo do Projeto
O objetivo principal é a automação do processo de ETL (Extração, Transformação e Carga) de dados públicos da plataforma Dados.BR.

## 📊 Destaques Técnicos
- **Volume de Dados:** Processamento de mais de 14 milhões de registros de empresas.
- **Performance:** Leitura otimizada de arquivos CSV de aproximadamente 1GB utilizando Python e Pandas.
- **Banco de Dados:** Estruturação e cruzamento de dados (JOIN/UPDATE) via MySQL para correlacionar naturezas jurídicas.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** Pandas, SQLAlchemy, PyMySQL
- **Ambiente:** XAMPP / phpMyAdmin (MySQL)

## 📁 Estrutura de Arquivos
- `leitura.py`: Script principal para leitura e carga dos dados.
- `importar_naturezas.py`: Automação da importação de tabelas auxiliares.
- `docs/`: Relatório técnico detalhado do projeto.
