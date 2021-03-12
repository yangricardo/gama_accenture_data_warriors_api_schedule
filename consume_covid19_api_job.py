import pandas as pd
import json
from request_url import request_url
from postgres import Postgres
from get_last_daily_date import get_last_daily_date
from get_top_deaths_confirmed_contries import get_top_deaths_confirmed_contries
from request_data_by_country import request_data_by_country
from build_dataframe import build_dataframe
from clean_daily_dataFrame import clean_daily_dataFrame
from clean_summary_dataFrame import clean_summary_dataFrame
from insert_df_on_datatable import insert_df_on_datatable


def consume_covid19_api_job():
    # request countries
    data_country = pd.json_normalize(request_url(
        'https://api.covid19api.com/countries'))

    # request summary
    data_sum = request_url('https://api.covid19api.com/summary')
    top = pd.json_normalize(data_sum['Countries'])

    # get a list containing top 30 countries with confirmed and death cases
    list_top_countries = get_top_deaths_confirmed_contries(top, data_country)

    # Connecta no banco
    database = Postgres()

    from_date = get_last_daily_date(database)

    # make requestget and aggregate all top 30 countries in a single json
    aggregate, list_to_reprocess = request_data_by_country(
        list_top_countries, from_date=from_date)
    aggregate_json = json.loads(aggregate)

    # make a datafrane of json file
    df_top_30_by_cases = build_dataframe(aggregate_json)
    df = df_top_30_by_cases.dropna(subset=['Country'])

    # Clean dataframe to access to insert data do Daily datatable
    df_daily = clean_daily_dataFrame(df)

    # Clean dataframe to access to insert data do summary datatable
    df_summary = clean_summary_dataFrame(df)

    insert_df_on_datatable(df_daily, "DAILY", database)
    insert_df_on_datatable(df_summary, "SUMMARY", database)

    print(list_to_reprocess)
