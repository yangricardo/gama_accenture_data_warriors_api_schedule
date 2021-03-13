# Gama Accenture 2021 - Api de Captura dos dados da Covid

> [Enunciado](scripts/ENUNCIADO.md)

## Processo de Desenvolvimento

![Processo de Desenvolvimento](docs/DataWarriors-Processo%20de%20Desenvolvimento.png)

> Parte 1
>
> - [1. Tratamento e Carga Inicial](scripts/part_1/01_initial_upload.ipynb)
> - [2. Menu](scripts/part_1/02_menu.ipynb)
> - [3. Extra - Automação das requisições com FastAPI e Thread de Captura de Dados](clean_summary_dataFrame.py)

> Parte 2
>
> - [1. Ingestão de Dados no Databricks](scripts/parte_2/01_Databricks_Ingestion_db_raw.ipynb)
> - [2. Transformação e Desnormalização](scripts/parte_2/02_Databricks_TransformationDesnormalization_raw_ready.ipynb)

## Diagrama de Entidade e Relacionamento

![Diagrama de Entidade e Relacionamento](docs/DataWarriors-MER.png)
> [SQL](scripts/part_1/01_sql_schemas.sql)

## Arquitetura de Solução

![Arquitetura de Solução](docs/DataWarriors-Arquitetura.png)

## Dificuldades

1. Dificuldade de coleta dos dados EUA;
2. Limitação da quantidade de requisições da API em `curto período de tempo` X `alta granularidade`;
3. Limitação de visualização de 1000 linhas na feature do display do Databricks

### Extras

#### Integração entre Databricks e PowerBI

![1](docs/dificuldades/1.png)
> Input de dados de conexão:
> host: `community.cloud.databricks.com`
> http path: `sql/protocolv1/o/1025248272368135/0313-145733-sags119`

![2](docs/dificuldades/2.png)
> Os dados não foram reconhecidos

##### Solução

> Ao tirar dúvidas com o mentor Igor Uchôa, identificamos a necessidade de salvar o spark dataframe como uma tabela no databricks usando o comando de exemplo`df.write.saveAsTable("default.test")`. Após esse passo conseguimos concluir a integração.

## API

### Requisitos

- Python 3.7.10

### Comandos

#### Ambiente

- `asdf install python 3.7.10`: instala versão mais estável do python para as dependências do projeto
  > necessário instalar o `asdf`, ferramenta que ajuda a ter várias versões de linguagens e outras ferramentas no ambiente e alternar
- `sudo apt-get install pipenv`: instala pipenv para gerenciamento das dependências do projeto
  - `pipenv --python 3.7`: gera ambiente python do projeto
  - `pipenv shell`: ativa ambiente python pelo pipenv
  - `pipenv install`: instala dependências a partir do arquivo `Pipfile`
  - `pipenv install -r .pipenv`: instala dependências a partir de um arquivo gerado via comando `pip freeze > .pipenv`
  - caso não seja possível, por conta do sistema, crie um virtualenv `python -m virtualenv venv`:
    - `source ./venv/bin/activate`: ativar ambiente python
    - `pip install -r .pipenv`:
- `pipenv install fastapi`: instala dependências do [FastAPI](https://fastapi.tiangolo.com/)
- `pipenv install uvicorn`: instala ASGI server para execução da api
- `pipenv install psycopg2-binary`: Dependências para conexão com Postgres
- `pipenv install pandas`: Dependência para manipulação de dataframes
- `pipenv install requests`: Dependência para execução de requisições http
- `pipenv install schedule`: Dependência para execução de jobs escalonados

#### Lançamento da API
  
- `uvicorn main:app --reload`: executa servidor de API
