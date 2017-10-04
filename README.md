# py-reevoo
A Python library for the Reevoo API. Made with the help of the [Reevoo API docs](http://reevoo.github.io/docs/reevooapi/)

## Methods

### \_\_init\_\_(api_key, api_secret)

Set the credentials to query the API

| Argument | Requirement | Type |
| --- | --- | --- |
| `api_key` | mandatory | String |
| `api_secret` | mandatory | String |


### get_organisation_list()

Allows a user to retrieve information for all organisations associated with their API key

### get_organisation_detail(self, trkref, branch_code)

Allows a user to retrieve information for a specific organisation assigned to their API key

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |

### get_reviewable_list(self, trkref, branch_code, short_format, skus)

Returns a list of reviewables (products) for the given organisation. If short_format is True, any organisation
may request the reviewables (although short data contains only the SKU, review count and the average score).

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |
| `short_format` | optional | Boolean | `False` |
| `branch_code` | optional | String | `None` |

### get_reviewable_detail(self, trkref, branch_code, locale, sku, short_format)

Return the details of a single reviewable (product)

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |
| `locale` | optional | String | `None` |
| `sku` | optional | String | `None` |
| `short_format` | optional | Boolean | `False` |

### get_review_list(self, trkref, locale, branch_code, sku, region, page, per_page, automotive_options)

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


### get_review_detail(self, trkref, review_id, branch_code, locale)

Get the details for a single review

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `review_id` | optional | String | `False` |
| `branch_code` | optional | String | `None` |
| `locale` | optional | String | `None` |

### set_review_upvote_review(self, review_id, trkref)

Increments the 'helpful' attribute of the review by 1. [IMPORTANT: The Reevoo API cannot detect the same user
incrementing the same review repeatedly.](http://reevoo.github.io/docs/reevooapi/review/upvote-review/)
Make sure your code prevents this.

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `review_id` | mandatory | String |  |
| `trkref` | optional | String | `None` |

### set_review_downvote_review(self, review_id, trkref)

Decrements the 'helpful' attribute of the review by 1. [IMPORTANT: The Reevoo API cannot detect the same user
decrementing the same review repeatedly.](http://reevoo.github.io/docs/reevooapi/review/downvote-review/)
Make sure your code prevents this.

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `review_id` | mandatory | String |  |
| `trkref` | optional | String | `None` |

### get_customer_experience_review_list(self, trkref, branch_code, older_reviews)

Fetch a list of reviews for an organisation

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `branch_code` | optional | String | `None` |
| `older_reviews` | optional | Boolean | `False` |

### get_customer_experience_review_detail(self, review_id, trkref, branch_code)

Fetch a single review by its ID

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `review_id` | mandatory | String |  |
| `trkref` | optional | String | `None` |
| `branch_code` | optional | String | `None` |

### get_conversation_list(self, trkref, locale, sku)

Returns a list of conversations associated with a certain product

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `review_id` | mandatory | String |  |
| `locale` | optional | String | `None` |
| `sku` | optional | String | `None` |

### get_conversation_detail(self, trkref, conversation_id)

Returns the details for a single conversation

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `review_id` | mandatory | String |  |
| `locale` | optional | String | `None` |
| `sku` | optional | String | `None` |

### set_conversation_create(self, trkref, conversation_data)

Create a new conversation question

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `conversation_data` | mandatory | dict |

###### conversation_data
The dict should contain the following data.

| Argument | Requirement | Type |
| --- | --- | --- |
| `sku` | mandatory | String |
| `first_name` | mandatory | String |
| `email` | mandatory | String |
| `question` | mandatory | String |

### set_conversation_upvote_question(self, trkref, question_id)

Increments the 'helpful' attribute of the question by 1. [IMPORTANT: The Reevoo API cannot detect the same user
incrementing the same question repeatedly.](http://reevoo.github.io/docs/reevooapi/conversation/conversation-upvote-question/)
Make sure your code prevents this.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `question_id` | mandatory | String |

### set_conversation_downvote_question(self, trkref, question_id)

Decrements the 'helpful' attribute of the question by 1. [IMPORTANT: The Reevoo API cannot detect the same user
decrementing the same question repeatedly.](http://reevoo.github.io/docs/reevooapi/conversation/conversation-downvote-question/)
Make sure your code prevents this.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `question_id` | mandatory | String |

### set_conversation_upvote_answer(self, trkref, answer_id)

Increments the 'helpful' attribute of the answer by 1. [IMPORTANT: The Reevoo API cannot detect the same user
incrementing the same answer repeatedly.](http://reevoo.github.io/docs/reevooapi/conversation/conversation-upvote-answer/)
Make sure your code prevents this.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `answer_id` | mandatory | String |

### set_conversation_downvote_answer(self, trkref, answer_id)

Decrements the 'helpful' attribute of the answer by 1. [IMPORTANT: The Reevoo API cannot detect the same user
decrementing the same answer repeatedly.](http://reevoo.github.io/docs/reevooapi/conversation/conversation-downvote-answer/)
Make sure your code prevents this.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `answer_id` | mandatory | String |

### set_customer_order_single_submission(self, trkref, customer_order_data)

Submit customer order details as a JSON object.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `customer_order_data` | mandatory | dict |

###### customer_order_data
The dict should contain the following data.

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `order_ref` | mandatory | String |  |
| `order_date` | optional | String | `None` |
| `fulfilment_date` | optional | String | `None` |
| `language` | optional | String | `None` |
| `locale` | optional | String | `None` |
| `customer` | mandatory | String |  |
| ...`email` | mandatory | String |  |
| ...`customer_ref` | optional | String | `None` |
| ...`title` | optional | String | `None` |
| ...`first_name` | optional | String | `None` |
| ...`surname` | optional | String | `None` |
| ...`postcode` | optional | String | `None` |
| ...`country` | optional | String | `None` |
| `order_items` | mandatory | Array |  |
| ...`sku` | mandatory | String |  |
| ...`price` | optional | String | `None` |
| ...`currency` | optional - Use ISO4217 code | String | `None` |
| ...`metadata` | optional | String | `None` |
| ......`key_with_underscore` | optional | String | `None` |

### set_customer_order_batch_submission(self, customer_order_batch_data)

Submit a batch of customer order details as a JSON list.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `customer_order_batch_data` | mandatory | Array |

###### customer_order_batch_data
The argument should be a list of dicts as specified in `set_customer_order_submission()` | `customer_order_data`

### get_purchaser_detail(self, trkref, email)

Returns a purchaser resource identified by a customer email.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `email` | mandatory | String |

### set_purchaser_create(self, trkref, purchaser_data)

Creates a purchaser record from a JSON string.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `purchaser_data` | mandatory | String |

###### purchaser_data
The dict should contain the following data.

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `email` | mandatory | String |  |
| `title` | optional | String | `None` |
| `first_name` | optional | String | `None` |
| `surname` | optional | String | `None` |
| `country` | optional | String | `None` |
| `postcode` | optional | String | `None` |

### set_purchaser_update(self, trkref, email, purchaser_data)

Update a purchaser record using an email to identify the purchaser

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `purchaser_data` | mandatory | String |

###### purchaser_data
The dict should contain the following data.

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `email` | mandatory | String |  |
| `title` | optional | String | `None` |
| `first_name` | optional | String | `None` |
| `surname` | optional | String | `None` |
| `country` | optional | String | `None` |
| `postcode` | optional | String | `None` |

### get_purchaser_list(self, trkref, email)

Returns a list of all purchases made by a purchaser with a given email address

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `email` | mandatory | String |

### get_purchaser_match(self, trkref, email, purchases)

Returns a list of all purchases made by a purchaser with a given email address. The purchases will match the
provided order references and SKUs.

| Argument | Requirement | Type |
| --- | --- | --- |
| `trkref` | mandatory | String |
| `email` | mandatory | String |
| `purchases` | mandatory | Array |

###### purchases
The array should contain objects with the following information:

| Argument | Requirement | Type |
| --- | --- | --- |
| `order_ref` | mandatory | String |
| `sku` | mandatory | String |

### get_questionnaire_detail(self, trkref, email, sku, order_ref, first_name, redirect)

Returns a questionnaire state or redirects to a questionnaire if redirect=True

| Argument | Requirement | Type | Default |
| --- | --- | --- | --- |
| `trkref` | mandatory | String |  |
| `email` | mandatory | String |  |
| `sku` | mandatory | String |  |
| `order_ref` | mandatory | String |  |
| `first_name` | optional | String | `None` |
| `redirect` | optional | String | `None` |
