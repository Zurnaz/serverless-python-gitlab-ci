from os.path import abspath
import json
import unittest
from src.handler import post_request, get_request
# import sys
# sys.path.insert(0, '../src')


class TestPost(unittest.TestCase):

    def setUp(self):
        pass

    def test_returns_number(self):
        event = {}
        event['body'] = json.dumps(1234)
        resp = post_request(event, None)
        expected = {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(1234)
        }
        self.assertEqual(resp, expected)

    def test_post_bulk(self):
        # more just to copy paste scenarios that caused issues quickly, to be later refactored for better tests
        path = abspath('tests/testdata.json')
        json_file = open(path).read()
        for item in json.loads(json_file):
            event = {}
            event['body'] = json.dumps(item['inputBody'])
            resp = post_request(event, None)
            expected = {
                'statusCode': 200,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps(item['outputBody'])
            }
            self.assertEqual(resp, expected)


class TestGet(unittest.TestCase):

    def setUp(self):
        pass

    def test_call_get(self):
        event = {}
        resp = get_request(event, None)
        expected = {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps("This is a get request")
        }
        self.assertEqual(resp, expected)


if __name__ == '__main__':
    unittest.main()
