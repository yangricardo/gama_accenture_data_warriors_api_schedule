import psycopg2


class Postgres():
    def __init__(self, database='postgres', user='DataWarriorsAdmin@data-warriors-postgresql', password='DataWarriorsPassword!', host='data-warriors-postgresql.postgres.database.azure.com', port='5432'):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password, port=port, sslmode='require')
        self.new_cursor()

    def get_connection(self):
        return self.connection

    def new_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, query):
        self.cursor.execute(query)
        self.commit()

    def search(self, query):
        self.new_cursor()
        self.cursor.execute(query)
        self.commit()
        return self.fetchall()

    def insertMany(self, query, data_list):
        try:
            self.new_cursor()
            self.cursor.executemany(query, data_list)
            self.commit()
            print('Execução da transação conclída com sucesso:', query)
        except Exception as error:
            self.rollback()
            print('Transação falhou:', error)

    def closeConnection(self):
        self.connection.close()


if __name__ == '__main__':
    import pprint
    p = Postgres()
    select_all_country_query = 'select * from country;'
    countries = p.search(select_all_country_query)
    pp = pprint.PrettyPrinter(indent=4)
    print(select_all_country_query, '==> slice [:5]')
    pp.pprint(countries[:5])
