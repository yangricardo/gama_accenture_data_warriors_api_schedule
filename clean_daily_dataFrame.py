import pandas as pd


def clean_daily_dataFrame(df):
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
