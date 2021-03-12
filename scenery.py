import pandas as pd
from postgres import Postgres
database = Postgres()
database.search()


class Scenery (object):
    '''
    Class to get Scenery of

    methods:
        - daily_cases
        - daily_deaths
        - total_cases
        - total_deaths

    Authors: Gabriel Rangel and Yang Miranda
    '''

    def __init__(self, database=Postgres()):
        super()
        self.database = database

    def daily_cases(self):
        daily_cases_query = '''
            select c.countryname as Pais ,
            s.newconfirmed as Numero_Diario_Casos, 
            s.lastupdated as Data_Atualizacao from summary as s
            inner join country as c
            on s.countrycode = c.countrycode 
            order by s.newconfirmed desc 
            limit 10;
        '''
        response = self.database.search(daily_cases_query)
        daily_cases_df = pd.DataFrame(response, columns=[
            'País', 'Casos Diários', 'Data de Atualização'])
        title = 'Número de casos confirmados de Covid-19 registrados na data mais recente: '
        return title, daily_cases_df

    def daily_deaths(self):
        daily_deaths_query = '''
            select  c.countryname as Pais,
            s.newdeaths as Numero_de_mortes_diario,
            s.lastupdated as Data_de_atualizacao
            from summary as s 
            inner join country as c 
            on s.countrycode = c.countrycode 
            order by s.newdeaths desc 
            limit 10;
        '''
        response = self.database.search(daily_deaths_query)
        daily_deaths_df = pd.DataFrame(
            response, columns=['País', 'Mortes Diárias', 'Data de Atualização'])
        title = 'Número de mortes por Covid-19 registradas na data mais recente: '
        return title, daily_deaths_df

    def total_cases(self):
        total_cases_query = '''
            select c.countryname as Pais,
            s.totalconfirmed as "Número_de_mortes_total",
            s.lastupdated as "Data_de_atualização"
            from summary as s 
            inner join country as c 
            on s.countrycode = c.countrycode
            order by s.totalconfirmed desc
            limit 10;
        '''
        response = self.database.search(total_cases_query)
        total_cases_df = pd.DataFrame(
            response, columns=['País', 'Total de Casos', 'Data de Atualização'])
        title = 'Total acumulado de casos confirmados de Covid-19 registrados até a data mais recente: '
        return title, total_cases_df

    def total_deaths(self):
        total_deaths_query = '''
            select  c.countryname as Pais,
            s.totaldeaths as Numero_de_casos_total,
            s.lastupdated as Data_de_atualizacao
            from summary as s
            inner join country as c 
            on s.countrycode = c.countrycode
            order by s.totaldeaths desc
            limit 10;
        '''
        response = self.database.search(total_deaths_query)
        total_deaths_df = pd.DataFrame(
            response, columns=['País', 'Total de Mortes', 'Data de Atualização'])
        title = 'Total acumulado de mortes por Covid-19 registradas até a data mais recente: '
        return title, total_deaths_df
