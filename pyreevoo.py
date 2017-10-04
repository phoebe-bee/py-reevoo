import requests
from requests.auth import HTTPBasicAuth


class ReevooAPI:
    """
    Library to query the Reevoo API. When initialising, do NOT hard-code your API keys, make sure they are stored in an
    environment variable.
    Further documentation can be found at the GitHub repo for py-reevoo (https://github.com/phoebe-bee/py-reevoo).
    """

    def __init__(self, api_key=None, api_secret=None):
        """
        Set the API URI (constant) and set the credentials to query the API
        :param api_key:
        :type api_key: str
        :param api_secret:
        :type api_secret: str
        """
        self.URI = 'https://api.reevoocloud.com'
        self.api_key = api_key
        self.api_secret = api_secret

        # create Auth object to attach to all requests made to the API
        auth = HTTPBasicAuth(self.api_key, self.api_secret)
        self.session = requests.Session()
        self.session.auth = auth

    def get_organisation_list(self):
        """
        Allows a user to retrieve information for all organisations associated with their API key
        """
        return

    def get_organisation_detail(self, trkref, branch_code=None):
        """
        Allows a user to retrieve information for a specific organisation assigned to their API key
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        """
        return

    def get_reviewable_list(self, trkref, branch_code=None, short_format=False, skus=None):
        """
        Returns a list of reviewables (products) for the given organisation. If short_format is True, any organisation
        may request the reviewables (although short data contains only the SKU, review count and the average score).
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        :param short_format: Return the short format of the list (optional, defaults to False)
        :type short_format: bool
        :param skus: The list of SKUs to find (optional, max length 80, defaults to None)
        :type skus: list
        """
        return

    def get_reviewable_detail(self, trkref, branch_code=None, locale=None, sku=None, short_format=False):
        """
        Return the details of a single reviewable (product)
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        :param locale: The locale (e.g. en-GB, optional, defaults to None)
        :type locale: str
        :param sku: The SKU to find (optional, defaults to None)
        :type sku: str
        :param short_format: Return the short format of the list (optional, defaults to False)
        :type short_format: bool
        """
        return

    def get_review_list(self, trkref, locale, branch_code=None, sku=None, region=None, page=1, per_page=15,
                        automotive_options=None):
        """
        Returns a list of published reviews for an organisation
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param locale: The locale (e.g. en-GB, optional, defaults to None)
        :type locale: str
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        :param sku: The SKU to find (optional, defaults to None)
        :type sku: str
        :param region: 'my-locale', 'my-country', 'my-languages', 'english' or 'worldwide'
        :type region: str
        :param page: The index of the paginated results to return
        :type page: int
        :param per_page: The number of results to display per page
        :type per_page: int
        :param automotive_options: Options for organisations with automotive reviewables
                {
                    manufacturer: str,
                    model: str,
                    model_variant: str (optional),
                    model_year: int (optional),
                    image_url: str (optional),
                    body_type: str (optional),
                    doors: int (optional),
                    used: bool (optional),
                    vehicle_type: str (optional),
                    fuel_type: str (optional - 'diesel' or 'petrol')
                    transmission: str (optional),
                    model_display: str (optional),
                    spec_description: str (optional),
                    engine_size_in_liters: float (optional)
                }
        :type automotive_options: dict
        """
        return

    def get_review_detail(self, trkref, review_id, branch_code=None, locale=None):
        """
        Get the details for a single review
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param review_id: The ID of the review to fetch
        :type review_id: str
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        :param locale: The locale (e.g. en-GB, optional, defaults to None)
        :type locale: str
        """
        return

    def set_review_upvote_review(self, review_id, trkref=None):
        """
        Increments the 'helpful' attribute of the review by 1
        IMPORTANT: The Reevoo API cannot detect the same user incrementing the same review repeatedly. Make sure that
        your code prevents this (http://reevoo.github.io/docs/reevooapi/review/upvote-review/).
        :param review_id: The ID of the review to fetch
        :type review_id: str
        :param trkref: The three-character identifier for the organisation
        :type trkref: str (optional, defaults to None)
        """
        return

    def set_review_downvote_review(self, review_id, trkref=None):
        """
        Decrements the 'helpful' attribute of the review by 1
        IMPORTANT: The Reevoo API cannot detect the same user decrementing the same review repeatedly. Make sure that
        your code prevents this (http://reevoo.github.io/docs/reevooapi/review/downvote-review/).
        :param review_id: The ID of the review to fetch
        :type review_id: str
        :param trkref: The three-character identifier for the organisation
        :type trkref: str (optional, defaults to None)
        """
        return

    def get_customer_experience_review_list(self, trkref, branch_code=None, older_reviews=False):
        """
        Fetch a list of reviews for an organisation
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        :param older_reviews: Retrieves all reviews if True, otherwise retrieves only reviews within a certain window
                                (optional, defaults to False)
        :type older_reviews: bool
        """
        return

    def get_customer_experience_review_detail(self, review_id, trkref=None, branch_code=None):
        """
        Fetch a single review by its ID
        :param review_id: The ID of the review to fetch
        :type review_id: str
        :param trkref: The three-character identifier for the organisation
        :type trkref: str (optional, defaults to None)
        :param branch_code: The identifier for a branch of the organisation (optional, defaults to None)
        :type branch_code: str
        """
        return

    def get_conversation_list(self, trkref, locale=None, sku=None):
        """
        Returns a list of conversations associated with a certain product
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param locale: The locale (e.g. en-GB, optional, defaults to None)
        :type locale: str
        :param sku: The SKU to find (optional, defaults to None)
        :type sku: str
        """
        return

    def get_conversation_detail(self, trkref, conversation_id):
        """
        Returns the details for a single conversation
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param conversation_id: The ID of the conversation to fetch
        :type conversation_id: str
        """
        return

    def set_conversation_create(self, trkref, conversation_data):
        """
        Creates a new conversation question
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param conversation_data: The details for the question
        :type conversation_data: dict
        """
        return

    def set_conversation_upvote_question(self, trkref, question_id):
        """
        Increments the 'helpful' attribute of the question by 1
        IMPORTANT: The Reevoo API cannot detect the same user incrementing the same question repeatedly. Make sure that
        your code prevents this (http://reevoo.github.io/docs/reevooapi/review/conversation-upvote-question/).
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param question_id: The ID of the question
        :type question_id: str
        """
        return

    def set_conversation_downvote_question(self, trkref, question_id):
        """
        Decrements the 'helpful' attribute of the question by 1
        IMPORTANT: The Reevoo API cannot detect the same user decrementing the same question repeatedly. Make sure that
        your code prevents this (http://reevoo.github.io/docs/reevooapi/review/conversation-downvote-question/).
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param question_id: The ID of the question
        :type question_id: str
        """
        return

    def set_conversation_upvote_answer(self, trkref, answer_id):
        """
        Increments the 'helpful' attribute of the answer by 1
        IMPORTANT: The Reevoo API cannot detect the same user incrementing the same answer repeatedly. Make sure that
        your code prevents this (http://reevoo.github.io/docs/reevooapi/review/conversation-upvote-answer/).
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param answer_id: The ID of the answer
        :type answer_id: str
        """
        return

    def set_conversation_downvote_answer(self, trkref, answer_id):
        """
        Decrements the 'helpful' attribute of the answer by 1
        IMPORTANT: The Reevoo API cannot detect the same user decrementing the same answer repeatedly. Make sure that
        your code prevents this (http://reevoo.github.io/docs/reevooapi/review/conversation-downvote-answer/).
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param answer_id: The ID of the answer
        :type answer_id: str
        """
        return

    def set_customer_order_single_submission(self, trkref, customer_order_data):
        """
        Submit customer order details as a JSON object. See Reevoo documentation for fields to include -
        http://reevoo.github.io/docs/reevooapi/customer-order/customer-order-single-submission/
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param customer_order_data: The customer order data
        :type customer_order_data: dict
        """
        return

    def set_customer_order_batch_submission(self, customer_order_batch_data):
        """
        Submit a batch of customer order details as a JSON list. See Reevoo documentation for fields to include -
        http://reevoo.github.io/docs/reevooapi/customer-order/customer-order-batch-submission/
        :param customer_order_batch_data: The customer order data
        :type customer_order_batch_data: dict
        """
        return

    def get_purchaser_detail(self, trkref, email):
        """
        Returns a purchaser resource identified by a customer email
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param email: The email of the customer
        :type email: str
        """
        return

    def set_purchaser_create(self, trkref, purchaser_data):
        """
        Creates a purchaser record from a JSON string. See Reevoo documentation for fields to include -
        http://reevoo.github.io/docs/reevooapi/purchaser/purchaser-create/
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param purchaser_data: The purchaser data
        :type purchaser_data: dict
        """
        return

    def set_purchaser_update(self, trkref, email, purchaser_data):
        """
        Update a purchaser record using an email to identify the purchaser
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param email: The email of the customer
        :type email: str
        :param purchaser_data: The purchaser data
        :type purchaser_data: dict
        """
        return

    def get_purchaser_list(self, trkref, email):
        """
        Returns a list of all purchases made by a purchaser with a given email address
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param email: The email address of the purchaser
        :type email: str
        """
        return

    def get_purchaser_match(self, trkref, email, purchases):
        """
        Returns a list of all purchases made by a purchaser with a given email address. The purchases will match the
        provided order references and SKUs.
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param email: The email address of the purchaser
        :type email: str
        :param purchases: An array of order references and SKUs to match in the format
                            [{'order_ref': str, 'sku': str}, ...]
        :type purchases: list
        """
        return

    def get_questionnaire_detail(self, trkref, email, sku, order_ref, first_name=None, redirect=False):
        """
        Returns a questionnaire state or redirects to a questionnaire if redirect=True
        :param trkref: The three-character identifier for the organisation
        :type trkref: str
        :param email: The email address of the purchaser
        :type email: str
        :param sku: The SKU to find
        :type sku: str
        :param order_ref: The order reference code
        :type order_ref: str
        :param first_name: The first name of the purchaser (optional, defaults to None)
        :type first_name: str
        :param redirect: Redirects to the questionnaire if True
        :type redirect: bool
        """
        return
