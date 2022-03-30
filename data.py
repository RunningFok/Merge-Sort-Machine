import requests

RANDOM_NUMBER_API = "http://www.randomnumberapi.com/api/v1.0/random"
parameters = {
                "min": 1,
                "max": 1000,
                "count": 50,
        }


def get_new_numbers():
        response = requests.get(RANDOM_NUMBER_API, params=parameters)
        response.raise_for_status()
        new_random_numbers = response.json()
        print(new_random_numbers)
        return new_random_numbers








