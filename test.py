import json
import unittest
from pyreevoo import ReevooAPI
from os import environ

"""
Test suite for py-reevoo.
To test, set the following environment variables:
API_KEY
API_SECRET
TRKREF
LOCALE
SKU (choose a SKU you know is in the dataset)
"""


class Test(unittest.TestCase):
    def test_verify_api_keys(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        api_keys_valid = reevoo.verify_api_keys()
        self.assertEqual(api_keys_valid, True)

    def test_verify_wrong_api_keys(self):
        reevoo = ReevooAPI('QWERTYUIOP', 'ASDFGHJKL')
        api_keys_valid = reevoo.verify_api_keys()
        self.assertEqual(api_keys_valid, False)

    def test_get_organisation_list(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_organisation_list()
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_organisation_detail(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_organisation_detail(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_reviewable_list(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_list(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_reviewable_list_short_format(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_list(environ.get('TRKREF'), short_format=True)
        content = json.loads(response.content)
        self.assertEqual(len(content['reviewables'][0]), 3, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_reviewable_detail(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_detail(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_reviewable_detail_short_format(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_detail(environ.get('TRKREF'), '10035', short_format=True)
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_review_list(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_review_list(environ.get('TRKREF'), environ.get('LOCALE'))
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))

    def test_get_review_detail(self):
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_review_list(environ.get('TRKREF'), environ.get('LOCALE'))
        self.assertEqual(response.status_code, 200, 'Response code %d, %s' % (response.status_code, response.reason))
