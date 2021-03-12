import datetime
import request_url
import time


def request_data_by_country(country_name, from_date="2020-01-01T00:00:00Z", cases=["confirmed", "deaths"]):
    '''
    Function to make request and get response for more than one country in a given standard API URL
    since 2020-01-01.

    INPUT:
        country_name - List of String containing country Slugs.
        from - List of String containing country Slugs.
        cases(Optional) - List of Strings containing type of update "confirmed","deaths" or "recovery".
    OUTPUT:
        json_list - String of response in Json  format.
        country_request_reprocess - List of String with Slugs that did not reach an API response or returned an error.

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
                urls = f'https://api.covid19api.com/country/{name}/status/{case_type}?from={from_date}&to={today}'
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
