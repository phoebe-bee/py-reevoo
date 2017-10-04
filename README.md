# py-reevoo
A Python library for the Reevoo API. Made with the help of the [Reevoo API docs](http://reevoo.github.io/docs/reevooapi/)

## Methods

###`__init__(api_key, api_secret)`

Set the credentials to query the API

| Argument | Requirement | Type |
| --- | --- | --- |
| `api_key` | mandatory | String |
| `api_secret` | mandatory | String |


###`get_organisation_list()`

Allows a user to retrieve information for all organisations associated with their API key

###`get_organisation_detail(self, trkref, branch_code)`

Allows a user to retrieve information for a specific organisation assigned to their API key

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |

###`get_reviewable_list(self, trkref, branch_code, short_format, skus)`

Returns a list of reviewables (products) for the given organisation. If short_format is True, any organisation
may request the reviewables (although short data contains only the SKU, review count and the average score).

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |
| `short_format` | optional | Boolean | `False` |
| `branch_code` | optional | String | `None` |

###`get_reviewable_detail(self, trkref, branch_code, locale, sku, short_format)`

Return the details of a single reviewable (product)

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |
| `locale` | optional | String | `None` |
| `sku` | optional | String | `None` |
| `short_format` | optional | Boolean | `False` |

###`get_review_list(self, trkref, locale, branch_code, sku, region, page, per_page, automotive_options)`

Returns a list of published reviews for an organisation.

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `locale` | mandatory | String |  |
| `branch_code` | optional | String | `None` |
| `sku` | optional | String | `None` |
| `region` | optional | String | `None` |
| `page` | optional | Integer | `1` |
| `per_page` | optional (min 15, max 30) | Integer | `15` |
| `automotive_options` | optional | dict | `None` |

##### Options
###### Region
Filter reviews by region by setting the `region` parameter to one of the following strings:

| Value | Description |
| --- | --- |
| `"my-locale"` | Return all reviews having same locale as locale parameter |
| `"my-locale"` | Return all reviews having same country code as locale parameter |
| `"my-locale"` | Return all reviews having same language code as locale parameter |
| `"english"` |  |
| `"worldwide"` |  |

###### Automotive Options
A dictionary to be used when an organisation has automotive reviewables. If the organisation does not need to use
this options, leave the argument blank and it will default to `None`.

| Value | Requirement | Type | Examples |
| --- | --- | --- | --- |
| `"manufacturer"` | mandatory | String | `"Reliant"` |
| `"model"` | mandatory | String | `"Robin"` |
| `"model_variant"` | optional | String | `"Mk1"` |
| `"model_year"` | optional | Integer | `1981` |
| `"image_url"` | optional | String |  |
| `"body_type"` | optional | String | `"hatchback"`, `"saloon"` |
| `"doors"` | optional | Integer | `3` |
| `"used"` | optional | Boolean |  |
| `"vehicle_type"` | optional | String | `"car"`, `"van"` |
| `"fuel_type"` | optional | String | `"petrol"`, `"diesel"` |
| `"transmission"` | optional | String | `"manual"`, `"automatic"` |
| `"model_display"` | optional | String | `"1981 Reliant Robin Mk1"` |
| `"spec_description"` | optional | String | `"Reliant Robin Mk1 - 3 doors"` |
| `"engine_size_in_liters"` | optional | Integer | `0.8` |


###`get_review_detail(self, trkref, review_id, branch_code, locale)`

Get the details for a single review

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `review_id` | optional | String | `False` |
| `branch_code` | optional | String | `None` |
| `locale` | optional | String | `None` |

###`set_review_upvote_review(self, review_id, trkref)`

Increments the 'helpful' attribute of the review by 1. [IMPORTANT: The Reevoo API cannot detect the same user
incrementing the same review repeatedly.](http://reevoo.github.io/docs/reevooapi/review/upvote-review/)
Make sure your code prevents this.

###`set_review_downvote_review(self, review_id, trkref)`

Decrements the 'helpful' attribute of the review by 1. [IMPORTANT: The Reevoo API cannot detect the same user
decrementing the same review repeatedly.](http://reevoo.github.io/docs/reevooapi/review/downvote-review/)
Make sure your code prevents this.

###`get_customer_experience_review_list(self, trkref, branch_code, older_reviews)`

Fetch a list of reviews for an organisation

###`get_customer_experience_review_detail(self, review_id, trkref, branch_code)`

Fetch a single review by its ID

###`get_conversation_list(self, trkref, locale, sku)`

Returns a list of conversations associated with a certain product

###`get_conversation_detail(self, trkref, conversation_id)`

Returns the details for a single conversation

###`set_conversation_create(self, trkref, conversation_details)`

###`set_conversation_upvote_question(self, trkref, question_id)`

Increments the 'helpful' attribute of the question by 1. [IMPORTANT: The Reevoo API cannot detect the same user
incrementing the same question repeatedly.](http://reevoo.github.io/docs/reevooapi/review/conversation-upvote-question/)
Make sure your code prevents this.

###`set_conversation_downvote_question(self, trkref, question_id)`

Decrements the 'helpful' attribute of the question by 1. [IMPORTANT: The Reevoo API cannot detect the same user
decrementing the same question repeatedly.](http://reevoo.github.io/docs/reevooapi/review/conversation-downvote-question/)
Make sure your code prevents this.

###`set_conversation_upvote_answer(self, trkref, answer_id)`

Increments the 'helpful' attribute of the answer by 1. [IMPORTANT: The Reevoo API cannot detect the same user
incrementing the same answer repeatedly.](http://reevoo.github.io/docs/reevooapi/review/conversation-upvote-answer/)
Make sure your code prevents this.

###`set_conversation_downvote_answer(self, trkref, answer_id)`

Decrements the 'helpful' attribute of the answer by 1. [IMPORTANT: The Reevoo API cannot detect the same user
decrementing the same answer repeatedly.](http://reevoo.github.io/docs/reevooapi/review/conversation-downvote-answer/)
Make sure your code prevents this.

###`set_customer_order_single_submission(self, trkref, customer_order_json)`

###`set_customer_order_batch_submission(self, customer_order_batch_json)`

###`get_purchaser_detail(self, trkref, email)`

###`set_purchaser_create(self, trkref, purchaser_json)`

###`set_purchaser_update(self, trkref, email, purchaser_json)`

###`get_purchaser_list(self, trkref, email)`

###`get_purchaser_match(self, trkref, email, purchases)`

###`get_questionnaire_detail(self, trkref, email, sku, order_ref, first_name, redirect)`
