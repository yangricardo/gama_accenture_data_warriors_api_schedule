def get_top_deaths_confirmed_contries(summary_dataframe, country_dataframe, n=30):
    '''
    Function get top countries in deaths and confirmed cases.

    INPUT:
        summary_dataframe - Dataframe cointaing a summary of all COVID-19 cases.
        country_dataframe - Dataframe cointaing name of country, slug and ISO2 code.
        n (optional) - Integer number refered to top countries to return.
    OUTPUT:
        top_countries - List of strings containg top countries in both categories.

    Author: Gutelvam Rodrigues
    '''

    # top rank Countries by confirmed cases
    top_TotalConfirmed = summary_dataframe.sort_values(
        by=['TotalConfirmed'], ascending=False).head(n)
    list_top_confirmed = list(top_TotalConfirmed['CountryCode'].unique())

    # top rank Countries by death
    top_deaths = summary_dataframe.sort_values(
        by=['TotalDeaths'], ascending=False).head(n)
    list_top_deaths = list(top_deaths['CountryCode'].unique())

    # List with tops Death and Confirmed cases
    countries_ISO = list(set(list_top_confirmed+list_top_deaths))

    # get name of countries in Slug
    top_countries = list(country_dataframe[country_dataframe['ISO2'].isin(
        countries_ISO)]['Slug'].unique())

    return top_countries
