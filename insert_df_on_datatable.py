from postgres import Postgres
from df_to_database import ParseDFToDatabase


def insert_df_on_datatable(df, table_name):
    '''
    Parse a cleaned dataframe and insert it's data to a table in database

    INPUT:
        df - Pandas dataframe
        table_name - A string that represents given table name that will receive tuple list insertions

    Author: Yang Miranda
    '''
    cleaned_df = ParseDFToDatabase(df, table_name)
    database = Postgres()
    database.insertMany(cleaned_df.insert_query, cleaned_df.tuple_list)
