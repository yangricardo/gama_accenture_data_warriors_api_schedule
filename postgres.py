import psycopg2


class Postgres():
    '''
    Returns a object prepared to connect with an Postgres Database

    INPUT:
        database - string that represents the database name
        user - string that represents an user from a given database
        password - string that authenticates the connection with a given database
        host - string that represents the host to access a given database
        port - string that represents the port to access a given database
        sslmode - string that ssl connection mode based on psycopg2

    Author: Yang Miranda
    '''

    def __init__(self, database='postgres', user='DataWarriorsAdmin@data-warriors-postgresql', password='DataWarriorsPassword!', host='data-warriors-postgresql.postgres.database.azure.com', port='5432', sslmode='require'):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password, port=port, sslmode=sslmode)
        self.new_cursor()

    def get_connection(self):
        '''
        Returns the connection object
        '''
        return self.connection

    def new_cursor(self):
        '''
        Returns the cursor object from connection
        '''
        self.cursor = self.connection.cursor()
        return self.cursor

    def commit(self):
        '''
        commits the transaction to a connected database
        '''
        self.connection.commit()

    def rollback(self):
        '''
        rollbacks the transaction in case of failure
        '''
        self.connection.rollback()

    def fetchall(self):
        '''
        fetch all values resulted from a query execution
        '''
        return self.cursor.fetchall()

    def execute(self, query):
        '''
        execute and commit a transaction query
        '''
        self.cursor.execute(query)
        self.commit()

    def search(self, query):
        '''
        execute a search query, like an select
        '''
        self.new_cursor()
        self.cursor.execute(query)
        self.commit()
        return self.fetchall()

    def insertMany(self, query, data_list):
        '''
        insert a tuple list based on a insert query
            INPUT:
                - query - string that represents a insert query like
                - data_list - tuple list that will be inserted by a query
            OUTPUT:
                - success - print('Execução da transação conclída com sucesso:', query) 
                - failure - print('Transação falhou:', error)
        '''
        try:
            self.new_cursor()
            self.cursor.executemany(query, data_list)
            self.commit()
            print('Execução da transação conclída com sucesso:', query)
        except Exception as error:
            self.rollback()
            print('Transação falhou:', error)

    def closeConnection(self):
        '''
        close connection of object
        '''
        self.connection.close()


if __name__ == '__main__':
    import pprint
    p = Postgres()
    select_all_country_query = 'select * from country;'
    countries = p.search(select_all_country_query)
    pp = pprint.PrettyPrinter(indent=4)
    print(select_all_country_query, '==> slice [:5]')
    pp.pprint(countries[:5])
