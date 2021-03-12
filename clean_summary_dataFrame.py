import pandas as pd


def clean_summary_dataFrame(df):
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
