import json
import requests
import pandas as pd
import datetime
import time
from postgres import Postgres
from df_to_database import ParseDFToDatabase

url_all_country = 'https://api.covid19api.com/countries'
summary_url = 'https://api.covid19api.com/summary'


def request_url(urls, return_response=False):
    '''
    Function to make request given an url.

    INPUT:
        urls - String of a given API address. 
    OUTPUT:
        r - String of response in Json  format.

    Author: Gutelvam Rodrigues
    '''
    try:
        r = requests.get(url=urls)
        if return_response:
            return r
        return r.json()
    except Exception as e:
        print(e)
        print(f"Houve um erro ao tentar fazer a requisicao da url: {urls}")


def request_data_by_country(country_name, from="2020-01-01T00:00:00Z", cases=["confirmed", "deaths"]):
    '''
    Function to make request and get response for more than one country in a given standard API URL
    since 2020-01-01.

    INPUT:
        country_name - List of String containing country Slugs.
        from - List of String containing country Slugs.
        cases(Optional) - List of Strings containing type of update "confirmed","deaths" or "recovery".
    OUTPUT:
        json_list - String of response in Json  format.
        country_request_err - List of String with Slugs that did not reach an API response or returned an error.

    Author: Gutelvam Rodrigues
    '''
    today = datetime.datetime.utcnow().strftime('%Y-%m-%dT00:00:00Z')
    json_list = []
    country_request_reprocess = []

    for name in country_name:
        for case_type in cases:
            try:
                print(f'pais: {name} e tipo de caso:{case_type}')
                counter = 0
                urls = f'https://api.covid19api.com/country/{name}/status/{case_type}?from={from}&to={today}'
                response = request_url(urls, True)

                # Try to make the request 5 times if you don't get a response the first time
                while response.status_code != 200:
                    counter += 1
                    response = request_url(urls, True)
                    time.sleep(30)
                    if counter == 5:
                        break

                if len(response) > 0:
                    json_list.append(response.json())
                else:
                    country_request_reprocess.append(name)

                # timer to avoid request limit
                time.sleep(6*60)
            except Exception as e:
                country_request_reprocess.append(name)
                print(e)
                print(
                    f"Houve um erro ao tentar fazer a requisicao da url com o pais: {name} e tipo de caso:{case_type}")

    return json.dumps(json_list), country_request_reprocess


def cleanDailyDataFrame(df):
    '''
    Prepare data from a pandas dataframe that will have data inserted on `DAILY` data table

    INPUT:
        df - Pandas dataframe
    OUTPUT:
        cleaned df to have data inserted on `DAILY` data table

    Author: Carlos Lima Dias
    '''
    df.drop(columns=['Country', 'Province',
                     'City', 'CityCode', 'Lat', 'Lon', "message"], inplace=True)
    df["TOTALDEATHS"] = df["Cases"][df["Status"] == "deaths"]
    df["TOTALDEATHS"] = df["Cases"][df["Status"] == "deaths"]
    df["TOTALCONFIRMED"] = df["Cases"][df["Status"] == "confirmed"]
    df.fillna(0, inplace=True)
    df.drop(columns=["Cases", "Status"], inplace=True)
    df = df.groupby(["Date", "CountryCode"])[
        ["TOTALDEATHS", "TOTALCONFIRMED"]].sum()
    df = df.reset_index()
    df = df.rename({"Date": "DATEREG",
                    "CountryCode": "COUNTRYCODE"},
                   axis=1)
    df["DATEREG"] = pd.to_datetime(df['DATEREG']).dt.date
    df["DATEREG"] = df["DATEREG"].astype(str)
    grouped = df.groupby('COUNTRYCODE')
    df_novo = pd.DataFrame()
    for _, country in grouped:
        country["NEWCONFIRMED"] = country["TOTALCONFIRMED"].diff(1)
        country["NEWDEATHS"] = country["TOTALDEATHS"].diff(1)
        df_novo = pd.concat([df_novo, country], ignore_index=True)
    df = df_novo.fillna(0)
    df = df.astype({"TOTALCONFIRMED": int, "TOTALDEATHS": int,
                    "NEWCONFIRMED": int, "NEWDEATHS": int})
    df = df[['DATEREG',
             'COUNTRYCODE',
             'TOTALCONFIRMED',
             'TOTALDEATHS',
             'NEWCONFIRMED',
             'NEWDEATHS']]
    return df


def cleanSummaryDataFrame(df):
    '''
    Prepare data from a pandas dataframe that will have data inserted on `SUMMARY` data table

    INPUT:
        df - Pandas dataframe
    OUTPUT:
        cleaned df to have data inserted on `SUMMARY` data table

    Author: Carlos Lima Dias
    '''
    grouped = df.groupby('COUNTRYCODE')
    df_summary = pd.DataFrame()
    for _, country in grouped:
        reg = country.tail(1)
        df_summary = pd.concat([df_summary, reg], ignore_index=True)
    df_summary = df_summary.rename({"DATEREG": "LASTUPDATED"},
                                   axis=1)

    return df_summary


def insertDataFrameValuesToDatabaseTable(df, table_name):
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
