def get_last_daily_date(postgree_object):
    """
    Function to get last date in daily table to insert in api request.

    INPUT:
        postgree_object - Instance of object to execute queries in DB.
    OUTPUT:
        start_date - String of date formated to API request.

    Author: Gutelvam Rodrigues
    """
    query = """SELECT datereg from public.daily 
             order by datereg desc 
             limit 1;"""
    start_date = postgree_object.search(query)
    return start_date[0][0].strftime('%Y-%m-%dT00:00:00Z')


if __name__ == '__main__':
    from postgres import Postgres
    p = Postgres()

    from get_last_daily_date import get_last_daily_date
    from_date = get_last_daily_date(p)
    print(from_date)
