import requests

def fetch_books(topic,pages):
    result = []
    url = 'https://openlibrary.org/search.json'

    for page in range(1, pages + 1):
        params = {'q': topic, 'page': page}
        try:
            response = requests.get(url, params=params)
            data = response.json()
            result.extend(data['docs'])
        except requests.exceptions.HTTPError:
            print("Http error")
        except requests.exceptions.ConnectionError:
            print("Connection error")

    return result
