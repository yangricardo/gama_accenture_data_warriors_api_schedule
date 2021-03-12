import requests


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
