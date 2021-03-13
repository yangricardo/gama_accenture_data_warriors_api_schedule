# Projeto Final Módulo 1 e 2 - Entrega em Grupo

## Parte 1: Projeto SQL, Python e Azure

Armazenamento de dados d COVID-19 de todos os países do mundo através da API: <https://documenter.getpostman.com/view/10808728/SzS8rjbc>.

1. Crie um Script SQL para criação de um DataBase com um Schema para armazenar os registros de países e os dados de COVID-19 por todo o mundo. Na tabela que será armazenada os dados de países, 2 campos são obrigatórios de serem consistidos:
Nome do país
Código ISO2
Em outros repositórios devem ser armazenados a quantidade de casos confirmados e mortes de cada um dos países do mundo, desde o dia 01/01/2020.
2. Crie um banco de dados relacional no provedor de nuvem Azure para armazenamento dos dados em questão, estabelecidos pelo script com o dito schema, criado na etapa anterior. O banco de dados pode ser SQL Server, MySQL, MariaDB, Postgres ou algum outro SQL.

3. Desenvolva um script Python que faça leitura da API determinada no enunciado inicial desta atividade para realizar o armazenamento de países e dos casos confirmados e de mortes da COVID-19. O armazenamento destas informações deverá ser em BD SQL, consistido no Azure através do schema definido na etapa 1 desta atividade.
Após armazenamento dos valores no BD, este dito script Python deverá retornar as seguintes informações em tela, caso o usuário escolha:
   1. Panorama diário de quantidade de casos confirmados de COVID-19 dos 10 países do mundo com maiores números.
   2. Panorama diário de quantidade de mortes de COVID-19 dos 10 países do mundo com números.
   3. Total de mortes por COVID-19 dos 10 países do mundo com maiores números.
   4. Total de casos confirmados por COVID-19 dos 10 países do mundo com maiores números.
A impressão das 4 informações citadas acima deverá acontecer em tela, através do prompt de comando de execução do programa.

## Parte 2: Projeto de Engenharia de dados

Com base nos conhecimentos obtidos durante o módulo de Engenharia de Dados com o Apache Spark, é necessário elaborar um projeto de construção de um mini data lake utilizando a plataforma da Databricks para armazenamento, processamento e visualização dos dados.

Pré-requisitos

- Cadastro na plataforma da Databricks Community Edition: <https://community.cloud.databricks.com/>

- Acesso a API <https://api.covid19api.com>

Roteiro:

Montaremos por meio desse projeto, um mini data lake tendo como meta realizar algumas análises exploratórias com os dados de acompanhamento diário da evolução da pandemia do COVID-19 no Brasil e no mundo. Assim sendo, é esperado que o grupo seja capaz de desenvolver um pipeline de transformação de dados seguindo o fluxo abaixo (a estrutura de diretórios está definida na última seção desse documento):

Ingestão

Realizar a ingestão dos datasets da parte anterior (parte 1) que estão no banco SQL na Azure em um diretório de arquivos raw dentro do DBFS.

Observações:

- utilize um notebook específico para realizar a ingestão do dado, com textos e comentários explicativos;

- programe a leitura do banco de dados utilizando o driver JDBC disponível para o Spark. Para ler do SQL na Azure, basta rodar o seguinte comando:

```python
jdbcDF = spark.read \

.format("com.microsoft.sqlserver.jdbc.spark") \

.option("driver",

"com.microsoft.sqlserver.jdbc.SQLServerDriver") \

.option("url", "JDBC_URL") \

.option("dbtable", "table_name") \

.option("user", "username") \

.option("password", "password").load()
```

Mais informações em relação ao conector spark-sql-server, veja em: <https://docs.microsoft.com/pt-br/sql/connect/spark/connector?view=sql-server-ver15> - ao programar, tenha em mente que a ingestão é uma etapa que ocorre diariamente, sempre trazendo os dados atualizados a cada novo dia;

- salve o dado em formato JSON no diretório raw

Transformações

Realizar transformações nos datasets acima, utilizando as APIs do PySpark, de modo a converter o dado ingestado previamente no formato mais otimizado para Big Data, o formato parquet, particionando-o fisicamente quando necessário. Salvar os dados em um diretório de arquivos ready dentro do DBFS

Observações:

- utilize um notebook específico para realizar a transformação do dado, com textos e comentários explicativos;

- salve o dado em formato de arquivo e posteriormente, crie uma tabela a partir do dado salvo para facilitar as visualizações (temporária ou definitiva). Durante o processo de escrita dos arquivos, perceba se o tipo de consulta exige um tipo de particionamento diferente e aplique se for o caso

- atente-se a modularização do código, pensando que podem ser realizadas esse tipo de transformação em centenas de tabelas no futuro

Visualizações

Criar as visualizações que permitam ter bons insights e acompanhamentos em relação a pandemia do COVID-19.

Observações:

- utilize um notebook específico para realizar as consultas para exibição do dado, com textos e comentários explicativos;

- se possível utilize o recurso de dashboards

Apresentação

O grupo deverá apresentar para o professor:

- o código dos 3 notebooks,

- um diagrama da arquitetura da solução utilizando o site draw.io

- as decisões tomadas em cada etapa,

- as dificuldades encontradas e as experiências obtidas com o uso da plataforma e do framework Pyspark.

Organização do data lake no DBFS

A organização do data lake, ou estrutura de diretórios para o armazenamento dos dados, proposto para o projeto deve ser definida seguindo o padrão abaixo:

```
/dbfs/FileStore/

|_covid_data_lake/

    |_raw/

        |_ tabela1

        |_ jsons

        |_ tabela2

        |_ jsons

        |_ ...

    |_ready/

        |_ tabela1

        |_ parquets

        |_ tabela2

        |_ parquets

        |_ ...
```
