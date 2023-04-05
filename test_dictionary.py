import unittest
from unittest.mock import patch
from dictioncli import get_word_definition

class TestDictionary(unittest.TestCase):
    @patch('dictioncli.requests.get')
    def test_get_word_definition(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'shortdef': ['a small, furry, nocturnal mammal'], 'fl': 'noun'}]
        response = get_word_definition('squirrel')
        self.assertEqual(response, 'Squirrel (noun): a small, furry, nocturnal mammal')