# py-reevoo
A Python library for the Reevoo API. Made with the help of the [Reevoo API docs](http://reevoo.github.io/docs/reevooapi/)

## Methods
`__init__(api_key, api_secret)`

`get_organisation_list()`

`get_organisation_detail(self, trkref, branch_code)`

`get_reviewable_list(self, trkref, branch_code, short_format, skus)`

`get_reviewable_detail(self, trkref, branch_code, locale, sku, short_format)`

`get_review_list(self, trkref, locale, branch_code, sku, region, page, per_page, automotive_options)`

`get_review_detail(self, trkref, review_id, branch_code, locale)`

`set_review_upvote_review(self, review_id, trkref)`

`set_review_downvote_review(self, review_id, trkref)`

`get_customer_experience_review_list(self, trkref, branch_code, older_reviews)`

`get_customer_experience_review_detail(self, review_id, trkref, branch_code)`

`get_conversation_list(self, trkref, locale, sku)`

`get_conversation_detail(self, trkref, conversation_id)`

`set_conversation_create(self, trkref)`

`set_conversation_upvote_question(self, trkref, question_id)`

`set_conversation_downvote_question(self, trkref, question_id)`

`set_conversation_upvote_answer(self, trkref, answer_id)`

`set_conversation_downvote_answer(self, trkref, answer_id)`

`set_customer_order_single_submission(self, trkref, customer_order_json)`

`set_customer_order_batch_submission(self, customer_order_batch_json)`

`get_purchaser_detail(self, trkref, email)`

`set_purchaser_create(self, trkref, purchaser_json)`

`set_purchaser_update(self, trkref, email, purchaser_json)`

`get_purchaser_list(self, trkref, email)`

`get_purchaser_match(self, trkref, email, purchases)`

`get_questionnaire_detail(self, trkref, email, sku, order_ref, first_name, redirect)`
