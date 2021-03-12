import pandas as pd
from postgres import Postgres


class Scenery (object):
    '''
    Class to get Scenery of

    methods:
        - daily_cases
        - daily_deaths
        - total_cases
        - total_deaths

    Authors: Gabriel Rangel
    '''

    def __init__(self, database=Postgres()):
        super()
        self.database = database

    def get_query_dataframe(self, query, columns):
        response = self.database.search(query)
        return pd.DataFrame(response, columns=columns)

    def daily_cases(self):
        query = '''
            select c.countryname as Pais ,
            s.newconfirmed as Numero_Diario_Casos, 
            s.lastupdated as Data_Atualizacao from summary as s
            inner join country as c
            on s.countrycode = c.countrycode 
            order by s.newconfirmed desc 
            limit 10;
        '''
        columns = ['País', 'Casos Diários', 'Data de Atualização']
        title = 'Número de casos confirmados de Covid-19 registrados na data mais recente: '
        return title, self.get_query_dataframe(query, columns)

    def daily_deaths(self):
        query = '''
            select  c.countryname as Pais,
            s.newdeaths as Numero_de_mortes_diario,
            s.lastupdated as Data_de_atualizacao
            from summary as s 
            inner join country as c 
            on s.countrycode = c.countrycode 
            order by s.newdeaths desc 
            limit 10;
        '''
        columns = ['País', 'Mortes Diárias', 'Data de Atualização']
        title = 'Número de mortes por Covid-19 registradas na data mais recente: '
        return title, self.get_query_dataframe(query, columns)

    def total_cases(self):
        query = '''
            select c.countryname as Pais,
            s.totalconfirmed as "Número_de_mortes_total",
            s.lastupdated as "Data_de_atualização"
            from summary as s 
            inner join country as c 
            on s.countrycode = c.countrycode
            order by s.totalconfirmed desc
            limit 10;
        '''
        columns = ['País', 'Total de Casos', 'Data de Atualização']
        title = 'Total acumulado de casos confirmados de Covid-19 registrados até a data mais recente: '
        return title, self.get_query_dataframe(query, columns)

    def total_deaths(self):
        query = '''
            select  c.countryname as Pais,
            s.totaldeaths as Numero_de_casos_total,
            s.lastupdated as Data_de_atualizacao
            from summary as s
            inner join country as c 
            on s.countrycode = c.countrycode
            order by s.totaldeaths desc
            limit 10;
        '''
        columns = ['País', 'Total de Mortes', 'Data de Atualização']
        title = 'Total acumulado de mortes por Covid-19 registradas até a data mais recente: '
        return title, self.get_query_dataframe(query, columns)


if __name__ == '__main__':
    def handle_user_option():
        option = 0

        print("""
Panorama DataWarriors - Gama Accenture 2021
Digite a opção que deseja executar:
    1. Panorama diário de quantidade de casos confirmados de COVID-19 dos 10 países do mundo com mais casos.
    2. Panorama diário de quantidade de mortes de COVID-19 dos 10 países do mundo com mais mortes.
    3. Total de mortes por COVID-19 dos 10 países do mundo com mais casos.
    4. Total de casos confirmados por COVID-19 dos 10 países do mundo com maiores números.
    5. Sair.
        """)

        while option < 1 or option > 5:
            try:
                option = int(input("\nDigite uma opção de 1 a 5: "))
            except:
                print("\nOpção inválida. Digite novamente\n")

        return option

    def print_response(scenery_response_tuple):
        print(scenery_response_tuple[0])
        print(scenery_response_tuple[1])

    option = handle_user_option()
    scenery = Scenery()

    while option >= 1 and option <= 5:
        if option == 1:
            print_response(scenery.daily_cases())

        elif option == 2:
            print_response(scenery.daily_deaths())

        elif option == 3:
            print_response(scenery.total_deaths())

        elif option == 4:
            print_response(scenery.total_cases())

        else:
            print("\nEncerrando Panorama DataWarriors - Gama Accenture 2021 \n")
            break

        if option != 5:
            option = handle_user_option()
