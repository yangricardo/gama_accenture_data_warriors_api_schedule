import pandas as pd


def build_dataframe(json_agg):
    '''
    Function to consolidate all countries in json into a single dataframe.

    INPUT:
        json_agg - list of Json containg data from all top countries.   
    OUTPUT:
        dataframe_top_contries - String of response in Json  format.

    Author: Gutelvam Rodrigues
    '''
    # iterate thru json and get all data
    dataframe_top_contries = pd.DataFrame()
    for element in json_agg:
        dataframe_top_contries = dataframe_top_contries.append(
            pd.json_normalize(element), ignore_index=True)

    return dataframe_top_contries
