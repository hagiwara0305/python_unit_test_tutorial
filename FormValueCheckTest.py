from webtest import TestApp
import unittest
import requests
import json

def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False

class FormValueCheckTest(unittest.TestCase):
    def test_test(self):
        self.assertEqual(1, 1)

    def test_access(self):
        r = requests.get('http://localhost:8080')
        self.assertEqual(r.status_code, 200, 'アクセスできない')

    def test_form_value(self):
        r = requests.post(
            'http://localhost:8080',
            {
                'name' : '萩原',
                'gender': 'men',
                'date' : '2019/01/01'
            }
        )
        self.assertEqual(r.status_code, 200, 'アクセスできない')

        post_data = json.loads(r.text)
        self.assertEqual(type('string'), type(post_data['name']), 'str以外の値が入っている')
        self.assertEqual(type('string'), type(post_data['gender']), 'str以外の値が入っている')
        self.assertTrue(is_date(post_data['date']), 'dateに変換できない値が入っている')

if __name__ == '__main__':
    unittest.main()