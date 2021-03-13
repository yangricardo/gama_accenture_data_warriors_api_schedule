# Gama Accenture 2021 - Api de Captura dos dados da Covid

## Overview
Esse Projeto faz parte do treinamento de Engenheiro de dados ministrado pela Accenture em parceria com a Gamma Academy.

Neste projeto foi dado a oportunidade de aplicar as tecnologias abordados no curso como Python, SQL, Databricks, tratamento de dados e consumo de API. A ideia foi consumir a API com dados do [COVID-19](https://documenter.getpostman.com/view/10808728/SzS8rjbc), provisionar um banco de dados relacional na Microsoft Azure para receber a carga de dados, consumir os dados do Banco via Databricks, criar Pipilines de transformação de dados e então  criar vizualizaçãos dos mesmos. 

## Summary

A API traz dados de diversas formas do COVID-19, as funcionalidades escolhidas para ser utilizada no projeto, foram 3:

* Summary:
    ![SummaryGet](https://i.ibb.co/10rk7Wg/summary.jpg)

* Country:
    ![CountryGet](https://i.ibb.co/F0qjL1W/country.jpg)

* By Country:
    ![ByCountryGet](https://i.ibb.co/wWQKhBD/byday.jpg)

Fases do projeto:

***Parte 1: Projeto SQL, Python e Azure***

> - Criação de um Script SQL para criação de um DataBase com um Schema para armazenar os registros de países e os dados de COVID-19 por todo o mundo. Na tabela que será armazenada os dados de países, 2 campos são obrigatórios de serem consistidos: Nome do País e Código ISO2. Em outros repositórios devem ser armazenados a quantidade de casos confirmados e mortes de cada um dos países do mundo, desde o dia 01/01/2020.
>- Criação de um banco de dados relacional no provedor de nuvem Azure para armazenamento dos dados em questão, estabelecidos pelo script com o dito schema, criado na etapa anterior. O banco de dados pode ser SQL Server, MySQL, MariaDB, Postgres ou algum outro SQL. 
>- Desenvolvimento de um script Python que faça leitura da API determinada para realizar o armazenamento de países e dos casos confirmados e de mortes da COVID-19. O armazenamento destas informações deverá ser em BD SQL, consistido no Azure através do schema definido na etapa 1 desta atividade. Após armazenamento dos valores no BD, este dito script Python deverá retornar as seguintes informações em tela, caso o usuário escolha:
    1) Panorama diário de quantidade de casos confirmados de COVID-19 dos 10 países do mundo com maiores números.
    2) Panorama diário de quantidade de mortes de COVID-19 dos 10 países do mundo com números.
    3) Total de mortes por COVID-19 dos 10 países do mundo com maiores números.
    4) Total de casos confirmados por COVID-19 dos 10 países do mundo com maiores números.
A impressão das 4 informações citadas acima deverá acontecer em tela, através do prompt de comando de execução do programa.

***Parte 2: Projeto de Engenharia de dados***

Com base nos conhecimentos obtidos durante o módulo de Engenharia de Dados com o Apache Spark, foi necessário elaborar um projeto de construção de um mini data lake utilizando a plataforma da Databricks para armazenamento, processamento e visualização dos dados. 
Assim sendo, foi requisitado a capacidade de desenvolver um pipeline de transformação de dados com as seguintes etapas:

- ***Ingestão***

	Realizar a ingestão dos datasets da parte anterior (parte 1) que estão no banco SQL na Azure em um diretório de arquivos raw dentro do DBFS.

- ***Transformações***

	Realizar transformações nos datasets acima, utilizando as APIs do PySpark, de modo a converter o dado ingestado previamente no formato mais otimizado para Big Data, o formato parquet, particionando-o fisicamente quando necessário. Salvar os dados em um diretório de arquivos ready dentro do DBFS.

- ***Visualizações***

	Criar as visualizações que permitam ter bons insights e acompanhamentos em relação a pandemia do COVID-19.

### Organização do data lake no DBFS

* A organização do data lake, ou estrutura de diretórios para o armazenamento dos dados, proposto para o projeto deve foi definida seguindo o padrão abaixo:

![data-lake-tree](https://i.ibb.co/BsRRymP/img-tree.jpg)




# Indicie

1. [Requisitos do Projeto](#requiriments)
2. [Processo de Desenvolvimento](#processo)
3. [Diagrama de Entidade e Relacionamento](#diagrama)
4. [Arquitetura de Solução](#arquitetura)
5. [Problema encontrados](#problemas)
6. [Melhoras futuras](#melhoras)
7. [Licensing and Acknowledgements](#Licensing)


## Requisitos do Projeto <a name="requiriments"></a>

### API

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

##### Solução

> Ao tirar dúvidas com o mentor Igor Uchôa, identificamos a necessidade de salvar o spark dataframe como uma tabela no databricks usando o comando de exemplo`df.write.saveAsTable("default.test")`. Após esse passo conseguimos concluir a integração.


## Processo de Desenvolvimento <a name="processo"></a>

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

## Diagrama de Entidade e Relacionamento <a name="diagrama"></a>

![Diagrama de Entidade e Relacionamento](docs/DataWarriors-MER.png)
> [SQL](scripts/part_1/01_sql_schemas.sql)

## Arquitetura de Solução <a name="arquitetura"></a>

![Arquitetura de Solução](docs/DataWarriors-Arquitetura.png)

## Problema encontrados <a name="problemas"></a>

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

## Melhoras futuras <a name="melhoras"></a>


## Licensing and Acknowledgements <a name="Licensing"></a>

[MIT License](https://github.com/git/git-scm.com/blob/master/MIT-LICENSE.txt).

Thanks for Udacity for give the oportunity to work with this data.
