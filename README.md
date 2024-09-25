# ETL Google Shopping

Este projeto é um ETL (Extração, Transformação e Carga) para coletar dados de produtos do Google Shopping e inseri-los em um banco de dados SQL Server. O projeto utiliza a biblioteca `Playwright` para extração de dados e `Pyodbc` para inserção no banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Playwright**: Biblioteca para automação de navegadores.
- **Pyodbc**: ORM (Object-Relational Mapping) para interagir com o banco de dados.
- **Poetry**: Gerenciador de dependências e empacotamento de projetos.

## Requisitos

- Python 3.8 ou superior
- SQL Server
- Dependências do projeto (gerenciadas pelo Poetry)

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Gomes027/ETL-Google-Shopping
   cd seu-repositorio

2. **Instale o Poetry (se ainda não estiver instalado):**

   Para instalar o Poetry, execute:

   ```bash
   pip install poetry

3. **Instale as dependências do projeto**

    Execute o seguinte comando para instalar todas as dependências:

    ```bash
    poetry install

4. **Crie um arquivo `.env`:**

    Na raiz do projeto, crie um arquivo chamado `.env` e adicione as seguintes variáveis de conexão:

    ```env
    DB_SERVER= SeuServidor
    DB_DATABASE= SeuBanco
    DB_USERNAME= SeuUsuario
    DB_PASSWORD= SuaSenha

## Execução do Projeto

    Para executar o projeto, utilize o seguinte comando:
    
    poetry run python src/Main.py

## Estrutura do Projeto

    ETL-Google-Shopping/
    │
    ├── src/
    │   ├── DataExtractor.py      # Código responsável pela extração de dados
    │   ├── DB_Manager.py         # Código responsável pela interação com o banco de dados
    │   └── Main.py               # Código principal que orquestra o ETL
    │
    ├── .env                      # Arquivo de configuração com variáveis de ambiente
    ├── pyproject.toml            # Arquivo de configuração do Poetry
    └── README.md                 # Este arquivo

## Contribuição

    Se você deseja contribuir para este projeto, fique à vontade para abrir um pull request ou um issue.