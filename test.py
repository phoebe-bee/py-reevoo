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
        Test the function that verifies the API keys works. Uses invalid API keys. Should return False.
        """
        reevoo = ReevooAPI('QWERTYUIOP', 'ASDFGHJKL')
        api_keys_valid = reevoo.verify_api_keys()
        self.assertEqual(api_keys_valid, False)

    def test_get_organisation_list(self):
        """
        Test the function that gets a list of organisations associated with a TRKREF. Should return response code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_organisation_list()
        self.assertEqual(response.status_code, 200, 'test_get_organisation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_organisation_detail(self):
        """
        Test the function that gets detailed info of an organisation from a TRKREF. Should return response code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_organisation_detail(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'test_get_organisation_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_list(self):
        """
        Test the function that gets a list of reviewables (products). Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_list(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200, 'test_get_reviewable_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_list_short_format(self):
        """
        Test the function that gets a list of reviewables (products). Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_list(environ.get('TRKREF'), short_format=True)
        content = json.loads(response.content)
        self.assertEqual(len(content['reviewables'][0]), 3,
                         'test_get_reviewable_list_short_format failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_detail(self):
        """
        Test the function that gets the detailed information for a reviewable (product). Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_detail(environ.get('TRKREF'), environ.get('SKU'))
        self.assertEqual(response.status_code, 200, 'test_get_reviewable_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_reviewable_detail_short_format(self):
        """
        Test the function that gets the detailed information for a reviewable (product). Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_reviewable_detail(environ.get('TRKREF'), environ.get('SKU'), short_format=True)
        self.assertEqual(response.status_code, 200,
                         'test_get_reviewable_detail_short_format failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_review_list(self):
        """
        Test the function that gets the list of reviews for a TRKREF. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_review_list(environ.get('TRKREF'), environ.get('LOCALE'), sku=environ.get('SKU'))
        self.assertEqual(response.status_code, 200, 'test_get_review_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_review_detail(self):
        """
        Test the function that gets the detail of a review from its ID. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_review_detail(environ.get('TRKREF'), environ.get('REVIEW_ID'))
        self.assertEqual(response.status_code, 200, 'test_get_review_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_review_upvote_review(self):
        """
        Test the function that upvotes a review. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_review_upvote_review(environ.get('REVIEW_ID'), environ.get('TRKREF'))
        self.assertEqual(response.status_code, 202, 'test_set_review_upvote_review failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_review_downvote_review(self):
        """
        Test the function that downvotes a review. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_review_downvote_review(environ.get('REVIEW_ID'), environ.get('TRKREF'))
        self.assertEqual(response.status_code, 202, 'test_set_review_downvote_review failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_customer_experience_review_list(self):
        """
        Test the function that gets a list of customer experience reviews. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_customer_experience_review_list(environ.get('TRKREF'))
        self.assertEqual(response.status_code, 200,
                         'test_get_customer_experience_review_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_customer_experience_review_detail(self):
        """
        Test the function that gets a detailed customer experience review from its ID. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_customer_experience_review_detail(environ.get('REVIEW_ID'))
        self.assertEqual(response.status_code, 200,
                         'test_get_customer_experience_review_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_conversation_list(self):
        """
        Test the function that gets a list of conversations. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_conversation_list(environ.get('TRKREF'), locale=environ.get('LOCALE'), sku=environ.get('SKU'))
        self.assertEqual(response.status_code, 200,
                         'test_get_conversation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_conversation_detail(self):
        """
        Test the function that gets a detailed conversation from its ID. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_conversation_detail(environ.get('TRKREF'), environ.get('CONVERSATION_ID'))
        self.assertEqual(response.status_code, 200,
                         'test_get_conversation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_create(self):
        """
        Test the function that creates a new conversation. Should return status code 202.
        """
        dummy_conversation = {

        }
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_create(environ.get('TRKREF'), dummy_conversation)
        self.assertEqual(response.status_code, 202,
                         'test_get_conversation_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_upvote_question(self):
        """
        Test the function that upvotes a question by ID. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_upvote_question(environ.get('TRKREF'), environ.get('QUESTION_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_upvote_question failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_downvote_question(self):
        """
        Test the function that downvotes a question by ID. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_downvote_question(environ.get('TRKREF'), environ.get('QUESTION_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_downvote_question failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_upvote_answer(self):
        """
        Test the function that upvotes an answer by ID. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_upvote_answer(environ.get('TRKREF'), environ.get('ANSWER_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_upvote_answer failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_conversation_downvote_answer(self):
        """
        Test the function that downvotes an answer by ID. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_conversation_downvote_answer(environ.get('TRKREF'), environ.get('ANSWER_ID'))
        self.assertEqual(response.status_code, 202,
                         'test_set_conversation_downvote_answer failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_customer_order_single_submission(self):
        """
        Test the function that submits the details of a single customer order. Should return status code 202.
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
        Test the function that submits the details of a batch of customer orders. Should return status code 202 or 206.
        """
        dummy_order_batch = [

        ]
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.set_customer_order_batch_submission(dummy_order_batch)
        self.assertIn(response.status_code, [202, 206],
                         'test_set_customer_order_batch_submission failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_purchaser_detail(self):
        """
        Test the function that gets the details of a purchaser. Should return status code 202.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_purchaser_detail(environ.get('TRKREF'), environ.get('EMAIL'))
        self.assertEqual(response.status_code, 200,
                         'test_get_purchaser_detail failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_set_purchaser_create(self):
        """
        Test the function that creates a new purchaser. Should return status code 202.
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
        Test the function that updates an existing purchaser's details. Should return status code 202.
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
        Test the function that gets a list of purchases associated with an email address. Should return status code 200.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_purchaser_list(environ.get('TRKREF'), environ.get('EMAIL'))
        self.assertEqual(response.status_code, 200,
                         'test_get_purchaser_list failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_purchaser_match(self):
        """
        Test the function that gets the purchases associated with the email address, skus and order references. Should
        return status code 200.
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
        Test the function that gets detailed information for a questionnaire.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_questionnaire_detail(environ.get('TRKREF'), environ.get('EMAIL'), environ.get('SKU'),
                                                   environ.get('ORDER_REF'))
        self.assertEqual(response.status_code, 200,
                         'test_set_conversation_downvote_answer failed - Response code %d, %s'
                         % (response.status_code, response.reason))

    def test_get_customer_experience_review_list_in_date_range_no_dates(self):
        """
        Test that the function which returns customer experience reviews within a date range throws an error when given
        no dates. Should return an error string.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        response = reevoo.get_customer_experience_review_list_in_date_range(environ.get('TRKREF'))
        self.assertEqual(response, "Please provide at least one of: start_date, end_date. Otherwise use get_customer_experience_review_list()")

    def test_get_customer_experience_review_list_in_date_range(self):
        """
        Test the function that gets a list of customer experience reviews from within a date range.
        Should return a list.
        """
        reevoo = ReevooAPI(environ.get('API_KEY'), environ.get('API_SECRET'))
        list_in_date_range = reevoo.get_customer_experience_review_list_in_date_range(environ.get('TRKREF'),
                                                                                      start_date='2016-01-01',
                                                                                      end_date='2017-03-31')
        self.assertIsInstance(list_in_date_range, list)
