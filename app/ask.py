import requests
import pprint
BASE_URL = 'https://jservice.io/api'
query_params = {"count": 1}


def get_one_quest():
    try:
        response = requests.get(f"{BASE_URL}/random", params=query_params)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    pprint.pprint(response.json())
    return response.json()