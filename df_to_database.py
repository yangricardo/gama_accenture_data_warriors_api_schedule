import json


class ParseDFToDatabase(object):
    def __init__(self, df, table_name):
        '''
        Class to parse a insert query and tuple list from a Pandas Dataframe

        INPUT:
            df - A Pandas Dataframe Object
            table_name - A string that represents given table name that will receive tuple list insertions
        OUTPUT:
            ParseDFToDatabase object
            Public Atributes:
                - tuple_list - tuple list generated with self.dfToTupleList()
                - insert_query - string that represents the insert query based on dataframe columns
                - format_colums - string used to build insert_query attribute

        Author: Yang Miranda
        '''
        self.df = df
        self.table_name = table_name
        self.tuple_list = self.dfToTupleList()
        self.columns = tuple(df.columns.to_list())
        self.format_colums = str(
            tuple([''.join('%s') for column in self.columns])).replace("'", "")
        self.columns = str(tuple(self.columns)).replace("'", "").upper()
        self.insert_query = f'INSERT INTO {self.table_name}{self.columns} VALUES{self.format_colums}'

    def dfToTupleList(self):
        df_json = json.loads(self.df.to_json(orient='records'))
        return list(map(lambda row: tuple(row.values()), df_json))

    def get(self):
        '''
        Returns a tuple to be used on Postgres::insertMany(query=insert_query,data_list=tuple_list)

        OUTPUT:
            ParseDFToDatabase object
            Tuple:
                - 0 = insert_query - string that represents the insert query based on dataframe columns
                - 1 = tuple_list - tuple list generated with self.dfToTupleList()
        '''
        return self.insert_query, self.tuple_list
