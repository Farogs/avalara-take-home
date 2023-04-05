import requests
import argparse

API_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
API_KEY = 'dbc89193-6862-4496-ade1-19d36ea9a8ce'

def get_word_definition(word):
    url = API_URL + word + '?key=' + API_KEY
    response = requests.get(url)
    if response.status_code == 200:
        try:
            definition = response.json()[0]['shortdef'][0]
            formatted_response = f'{word.capitalize()} ({response.json()[0]["fl"]}): {definition}'
            return formatted_response
        except (KeyError, IndexError):
            return 'No definition found'
    else:
        return 'Word not found'
