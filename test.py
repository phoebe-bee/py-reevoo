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
REVIEW_ID (choose a review ID you know is in the dataset)
CONVERSATION_ID
QUESTION_ID
ANSWER_ID
EMAIL

You will also need to set some dummy data for a test conversation in
"""


class Test(unittest.TestCase):
    def test_verify_api_keys(self):
        """
        Test the function that verifies the API keys works. Should return True if valid API keys are provided.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        api_keys_valid = reevoo.verify_api_keys()
        self.assertEqual(api_keys_valid, True)

    def test_verify_wrong_api_keys(self):
        """
        Test the function that verifies the API keys works. Uses invalid API keys and should return False.
        """
        reevoo = ReevooAPI('QWERTYUIOP', 'ASDFGHJKL')
        api_keys_valid = reevoo.verify_api_keys()
        self.assertEqual(api_keys_valid, False)

    def test_get_organisation_list(self):
        """
        
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_organisation_list()
        self.assertEqual(response.status_code, 200, 'test_get_organisation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_organisation_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_organisation_detail(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'test_get_organisation_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_list(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_list(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'test_get_reviewable_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_list_short_format(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_list(environ.get('TRKREF'), short_format=True)
        content = json.loads(response.content)
        self.assertEqual(len(content['reviewables'][0]), 3,
                         'test_get_reviewable_list_short_format failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_detail(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'test_get_reviewable_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_detail_short_format(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_detail(environ.get('TRKREF'), environ.get('SKU'), short_format=True)
        self.assertEqual(response.status_code, 200,
                         'test_get_reviewable_detail_short_format failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_review_list(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_review_list(environ.get('TRKREF'), environ.get('LOCALE'))
        self.assertEqual(response.status_code, 200, 'test_get_review_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_review_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_review_detail(environ.get('TRKREF'), environ.get('LOCALE'))
        self.assertEqual(response.status_code, 200, 'test_get_review_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_review_upvote_review(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_review_upvote_review(environ.get('REVIEW_ID'), environ.get('TRKREF'))
        self.assertEqual(response.status_code, 202, 'test_set_review_upvote_review failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_review_downvote_review(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_review_downvote_review(environ.get('REVIEW_ID'), environ.get('TRKREF'))
        self.assertEqual(response.status_code, 202, 'test_set_review_downvote_review failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_customer_experience_review_list(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_customer_experience_review_list(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200,
                         'test_get_customer_experience_review_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_customer_experience_review_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_customer_experience_review_detail(environ.get('REVIEW_ID'))
        self.assertEqual(response.status_code, 200,
                         'test_get_customer_experience_review_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_conversation_list(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_conversation_list(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200,
                         'test_get_conversation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_conversation_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_conversation_detail(environ.get('TRKREF'), environ.get('CONVERSATION_ID'))
        self.assertEqual(response.status_code, 200,
                         'test_get_conversation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_create(self):
        """

        """
        dummy_conversation = {
            'sku': '00001',
            'first_name': 'Clark',
            'email': 'clark.kent@dailyplanet.mtpls',
            'question': 'Will this product withstand re-entry from low orbit?'
        }
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_create(environ.get('TRKREF'), dummy_conversation)
        self.assertEqual(response.status_code, 200,
                         'test_get_conversation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_upvote_question(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_upvote_question(environ.get('TRKREF'), environ.get('QUESTION_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_upvote_question failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_downvote_question(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_downvote_question(environ.get('TRKREF'), environ.get('QUESTION_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_downvote_question failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_upvote_answer(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_upvote_answer(environ.get('TRKREF'), environ.get('ANSWER_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_upvote_answer failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_downvote_answer(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_downvote_answer(environ.get('TRKREF'), environ.get('ANSWER_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_downvote_answer failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_customer_order_single_submission(self):
        """

        """
        dummy_order = {

        }
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_customer_order_single_submission(environ.get('TRKREF'), dummy_order)
        self.assertEqual(response.status_code, 202,
                         'test_set_customer_order_single_submission failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_customer_order_batch_submission(self):
        """

        """
        dummy_order_batch = [

        ]
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_customer_order_batch_submission(dummy_order_batch)
        self.assertEqual(response.status_code, 202,
                         'test_set_customer_order_batch_submission failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_purchaser_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_purchaser_detail(environ.get('TRKREF'), environ.get('EMAIL'))
        self.assertEqual(response.status_code, 200,
                         'test_get_purchaser_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_purchaser_create(self):
        """

        """
        purchaser_data = {

        }
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_purchaser_create(environ.get('TRKREF'), purchaser_data)
        self.assertEqual(response.status_code, 202,
                         'test_get_purchaser_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_purchaser_update(self):
        """

        """
        purchaser_data = {

        }
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_purchaser_update(environ.get('TRKREF'), environ.get('EMAIL'), purchaser_data)
        self.assertEqual(response.status_code, 202,
                         'test_set_purchaser_create failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_purchaser_list(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_purchaser_list(environ.get('TRKREF'), environ.get('EMAIL'))
        self.assertEqual(response.status_code, 200,
                         'test_get_purchaser_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_purchaser_match(self):
        """

        """
        purchases = [

        ]
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_purchaser_match(environ.get('TRKREF'), environ.get('EMAIL'), purchases)
        self.assertEqual(response.status_code, 200,
                         'test_get_purchaser_match failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_questionnaire_detail(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_questionnaire_detail(environ.get('TRKREF'), environ.get('EMAIL'), environ.get('SKU'),
                                                   environ.get('ORDER_REF'))
        self.assertEqual(response.status_code, 200,
                         'test_set_conversation_downvote_answer failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_customer_experience_review_list_in_date_range_no_dates(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_customer_experience_review_list_in_date_range(environ.get('TRKREF'))
        self.assertEqual(response, "Please provide at least one of: start_date, end_date. Otherwise use get_customer_experience_review_list()")

    def test_get_customer_experience_review_list_in_date_range(self):
        """

        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        list_in_date_range = reevoo.get_customer_experience_review_list_in_date_range(environ.get('TRKREF'),
                                                                            start_date='2016-01-01', end_date='2017-03-31')
        self.assertIs(list, list_in_date_range)
