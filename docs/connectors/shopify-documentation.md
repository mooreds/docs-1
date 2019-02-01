---
id: shopify-documentation
title: Shopify (version v2.*.*)
sidebar_label: Shopify
---

## delete_blogs_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_blogs_id_articles_id



<details><summary>Parameters</summary>

#### article_id (required)

**Type:** string

#### blog_id (required)

**Type:** string

</details>

## delete_carrier_services_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_collects_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_countries_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_custom_collections_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_customer_saved_searches_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_customers_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_customers_id_addresses_id



<details><summary>Parameters</summary>

#### address_id (required)

**Type:** string

#### customer_id (required)

**Type:** string

</details>

## delete_discounts_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_order_fulfillment_events_id



<details><summary>Parameters</summary>

#### event_id (required)

**Type:** string

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## delete_order_risks_id



<details><summary>Parameters</summary>

#### order_id (required)

**Type:** string

#### risk_id (required)

**Type:** string

</details>

## delete_orders_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_pages_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_product_variant_by_id



<details><summary>Parameters</summary>

#### product_id (required)

**Type:** string

#### variant_id (required)

**Type:** string

</details>

## delete_products_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_products_id_images_id



<details><summary>Parameters</summary>

#### image_id (required)

**Type:** string

#### product_id (required)

**Type:** string

</details>

## delete_products_metafields_by_id



<details><summary>Parameters</summary>

#### field_id (required)

**Type:** string

#### product_id (required)

**Type:** string

</details>

## delete_recurring_application_charges_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_redirects_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_script_tags_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_themes_id_assets



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_webhooks_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_application_charges



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_application_charges_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_application_credits



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_application_credits_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_articles_authors



*This operation has no parameters*

## get_articles_tags



<details><summary>Parameters</summary>

#### limit

The number of tags to return

**Type:** string

#### popular

A flag to indicate only to a certain number of the most popular tags

**Type:** string

</details>

## get_blogs



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### handle

Filter by blog handle

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_blogs_count



*This operation has no parameters*

## get_blogs_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_blogs_id_articles



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### created_at_max

Show articles created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show articles created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### handle

Filter by article handle

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### published_at_max

Show articles published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show articles published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published articles    unpublished - Show only unpublished articles    any - Show all articles (default)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### updated_at_max

Show articles last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show articles last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_blogs_id_articles_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### created_at_max

Count articles created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Count articles created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_max

Count articles published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Count articles published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Count only published articles    unpublished - Count only unpublished articles    any - Count all articles (default)

**Type:** string

#### updated_at_max

Count articles last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Count articles last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_blogs_id_articles_id



<details><summary>Parameters</summary>

#### article_id (required)

**Type:** string

#### blog_id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_carrier_services



*This operation has no parameters*

## get_carrier_services_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_checkouts



<details><summary>Parameters</summary>

#### created_at_max

Show checkouts created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show checkouts created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### status

open - All open abandoned checkouts (default)    closed - Show only closed abandoned checkouts

**Type:** string

#### updated_at_max

Show checkouts last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show checkouts last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_checkouts_count



<details><summary>Parameters</summary>

#### created_at_max

Show checkouts created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show checkouts created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### status

open - All open abandoned checkouts (default)    closed - Show only closed abandoned checkouts

**Type:** string

#### updated_at_max

Show checkouts last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show checkouts last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_collects



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Collects per page  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

</details>

## get_collects_count



*This operation has no parameters*

## get_collects_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_comments



<details><summary>Parameters</summary>

#### created_at_max

Show comments created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show comments created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### published_at_max

Show comments published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show comments published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published comments    unpublished - Show only unpublished comments    any - Show all comments (default)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### status

pending - All pending comments    published - Show only published comments    unapproved - Show only unapproved comments

**Type:** string

#### updated_at_max

Show comments last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show comments last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_comments_count



<details><summary>Parameters</summary>

#### created_at_max

Count comments created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Count comments created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_max

Count comments published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Count comments published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Count only published comments    unpublished - Count only unpublished comments    any - Count all comments (default)

**Type:** string

#### status

pending - All pending comments    published - Count only published comments    unapproved - Count only unapproved comments

**Type:** string

#### updated_at_max

Count comments last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Count comments last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_comments_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_countries



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_countries_count



*This operation has no parameters*

## get_countries_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_countries_id_provinces



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### country_id

The id of the country the province belongs to

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_countries_id_provinces_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_countries_provinces_by_id



<details><summary>Parameters</summary>

#### country_id (required)

**Type:** string

#### province_id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_custom_collections



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### handle

Filter by custom collection handle

**Type:** string

#### ids

A comma-separated list of collection ids

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### product_id

Show custom collections that includes given product

**Type:** string

#### published_at_max

Show custom collections published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show custom collections published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published custom collections    unpublished - Show only unpublished custom collections    any - Show all custom collections (default)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### title

Show custom collections with given title

**Type:** string

#### updated_at_max

Show custom collections last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show custom collections last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_custom_collections_count



<details><summary>Parameters</summary>

#### product_id

Count custom collections that includes given product

**Type:** string

#### published_at_max

Show custom collections published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show custom collections published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published custom collections    unpublished - Show only unpublished custom collections    any - Show all custom collections (default)

**Type:** string

#### title

Count custom collections with given title

**Type:** string

#### updated_at_max

Count custom collections last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Count custom collections last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_custom_collections_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_customer_saved_searches



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_customer_saved_searches_count



<details><summary>Parameters</summary>

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_customer_saved_searches_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_customers



<details><summary>Parameters</summary>

#### created_at_max

Show customers created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show customers created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### ids

A comma-separated list of customer ids

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### updated_at_max

Show customers last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show customers last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_customers_count



*This operation has no parameters*

## get_customers_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_customers_id_addresses



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_customers_id_addresses_id



<details><summary>Parameters</summary>

#### address_id (required)

**Type:** string

#### customer_id (required)

**Type:** string

</details>

## get_customers_search



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### order

Field and direction to order results by  (default: last_order_date DESC)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### query

Text to search customers

**Type:** string

</details>

## get_discounts



<details><summary>Parameters</summary>

#### limit

Number of results per page  (default: 15)  (maximum: 200)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

</details>

## get_discounts_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_events



<details><summary>Parameters</summary>

#### created_at_max

Show events created at or before date and time (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show events created at or after date and time (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### filter

Only show events specified in filter

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### verb

Only show events of a certain kind

**Type:** string

</details>

## get_events_count



<details><summary>Parameters</summary>

#### created_at_max

Count events created at or before date and time (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Count events created at or after date and time (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_events_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_gift_cards



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### status

enabled - Restrict results to only enabled gift cards    disabled - Restrict results to only disabled gift cards

**Type:** string

</details>

## get_gift_cards_count



<details><summary>Parameters</summary>

#### status

enabled - Count only enabled gift cards    disabled - Count only disabled gift cards

**Type:** string

</details>

## get_gift_cards_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_gift_cards_search



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### order

Field and direction to order results by  (default: disabled_at DESC)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### query

Text to search gift cards

**Type:** string

</details>

## get_locations



*This operation has no parameters*

## get_locations_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_metafields



*This operation has no parameters*

## get_order_fulfillment_events



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## get_order_fulfillment_events_id



<details><summary>Parameters</summary>

#### event_id (required)

**Type:** string

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## get_order_fulfillments



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### created_at_max

Show fulfillments created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show fulfillments created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### updated_at_max

Show fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_order_fulfillments_by_id



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_order_fulfillments_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### created_at_max

Count fulfillments created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Count fulfillments created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_max

Count fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Count fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_order_refunds



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

Comma-separated list of fields to include in the response

**Type:** string

</details>

## get_order_refunds_id



<details><summary>Parameters</summary>

#### order_id (required)

**Type:** string

#### refund_id (required)

**Type:** string

#### fields

Comma-separated list of fields to include in the response

**Type:** string

</details>

## get_order_risks



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_order_risks_id



<details><summary>Parameters</summary>

#### order_id (required)

**Type:** string

#### risk_id (required)

**Type:** string

</details>

## get_order_transactions



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_order_transactions_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_order_transactions_id



<details><summary>Parameters</summary>

#### order_id (required)

**Type:** string

#### transaction_id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_orders



<details><summary>Parameters</summary>

#### created_at_max

Show orders created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show orders created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### financial_status

authorized - Show only authorized orders    pending - Show only pending orders    paid - Show only paid orders    partially_paid - Show only partially paid orders    refunded - Show only refunded orders    voided - Show only voided orders    partially_refunded - Show only partially_refunded orders    any - Show all authorized, pending, and paid orders (default). This is a filter, not a value.    unpaid - Show all authorized, or partially_paid orders. This is a filter, not a value.

**Type:** string

#### fulfillment_status

shipped - Show orders that have been shipped    partial - Show partially shipped orders    unshipped - Show orders that have not yet been shipped    any - Show orders with any fulfillment_status. (default)

**Type:** string

#### ids

A comma-separated list of order ids

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### processed_at_max

Show orders imported before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### processed_at_min

Show orders imported after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### status

open - All open orders (default)    closed - Show only closed orders    cancelled - Show only cancelled orders    any - Any order status

**Type:** string

#### updated_at_max

Show orders last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show orders last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_orders_count



<details><summary>Parameters</summary>

#### created_at_max

Count orders created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Count orders created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### financial_status

authorized - Only authorized orders    pending - Only pending orders    paid - Only paid orders    refunded - Show only refunded orders    voided - Show only voided orders    any - All authorized, pending, and paid orders (default)

**Type:** string

#### fulfillment_status

shipped - Orders that have been shipped    partial - Partially shipped orders    unshipped - Orders that have not yet been shipped    any - Orders with any fulfillment_status. (default)

**Type:** string

#### status

open - Open orders (default)    closed - Only closed orders    any - Any order status

**Type:** string

#### updated_at_max

Count orders last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Count orders last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_orders_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_pages



<details><summary>Parameters</summary>

#### created_at_max

Show pages created before date (format: 2008-12-31)

**Type:** string

#### created_at_min

Show pages created after date (format: 2008-12-31)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### handle

Filter by Page handle

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### published_at_max

Show pages published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show pages published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published pages    unpublished - Show only unpublished pages    any - Show all pages (default)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### title

Show pages by Title

**Type:** string

#### updated_at_max

Show pages last updated before date (format: 2008-12-31)

**Type:** string

#### updated_at_min

Show pages last updated after date (format: 2008-12-31)

**Type:** string

</details>

## get_pages_count



<details><summary>Parameters</summary>

#### created_at_max

Pages created before date (format: 2008-12-31)

**Type:** string

#### created_at_min

Pages created after date (format: 2008-12-31)

**Type:** string

#### published_at_max

Show pages published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show pages published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Only published pages    unpublished - Only unpublished pages    any - All pages (default)

**Type:** string

#### title

Pages with a given title

**Type:** string

#### updated_at_max

Pages last updated before date (format: 2008-12-31)

**Type:** string

#### updated_at_min

Pages last updated after date (format: 2008-12-31)

**Type:** string

</details>

## get_pages_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_policies



*This operation has no parameters*

## get_products



<details><summary>Parameters</summary>

#### collection_id

Filter by collection id

**Type:** string

#### created_at_max

Show products created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show products created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### handle

Filter by product handle

**Type:** string

#### ids

A comma-separated list of product ids

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### product_type

Filter by product type

**Type:** string

#### published_at_max

Show products published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show products published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published products    unpublished - Show only unpublished products    any - Show all products (default)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### title

Filter by product title

**Type:** string

#### updated_at_max

Show products last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show products last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### vendor

Filter by product vendor

**Type:** string

</details>

## get_products_count



<details><summary>Parameters</summary>

#### collection_id

Filter by collection id

**Type:** string

#### created_at_max

Show products created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show products created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### product_type

Filter by product type

**Type:** string

#### published_at_max

Show products published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show products published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published products    unpublished - Show only unpublished products    any - Show all products (default)

**Type:** string

#### updated_at_max

Show products last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show products last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### vendor

Filter by product vendor

**Type:** string

</details>

## get_products_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_products_id_images



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_products_id_images_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### created_at_max

Count articles created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Count articles created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_max

Count articles published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Count articles published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### updated_at_max

Count articles last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Count articles last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_products_id_images_id



<details><summary>Parameters</summary>

#### image_id (required)

**Type:** string

#### product_id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_products_id_metafields_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_products_id_variants



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_products_id_variants_count



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_products_metafields_by_id



<details><summary>Parameters</summary>

#### field_id (required)

**Type:** string

#### product_id (required)

**Type:** string

</details>

## get_recurring_application_charges



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

</details>

## get_recurring_application_charges_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_recurring_application_charges_id_usage_charges



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_recurring_application_charges_id_usage_charges_id



<details><summary>Parameters</summary>

#### recurring_application_charge_id (required)

**Type:** string

#### usage_charge_id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_redirects



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### path

Show Redirects with given path

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### target

Show Redirects with given target

**Type:** string

</details>

## get_redirects_count



<details><summary>Parameters</summary>

#### path

Count Redirects with given path

**Type:** string

#### target

Count Redirects with given target

**Type:** string

</details>

## get_redirects_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_script_tags



<details><summary>Parameters</summary>

#### created_at_max

Show script_tags created before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### created_at_min

Show script_tags created after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### src

Show script tags with a given URL

**Type:** string

#### updated_at_max

Show script_tags last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show script_tags last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_script_tags_count



<details><summary>Parameters</summary>

#### src

Count script tags with given URL

**Type:** string

</details>

## get_script_tags_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_shipping_zones



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_shop



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_smart_collections



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

#### handle

Filter by smart collection handle

**Type:** string

#### ids

A comma-separated list of collection ids

**Type:** string

#### limit

Amount of results  (default: 50)  (maximum: 250)

**Type:** string

#### page

Page to show  (default: 1)

**Type:** string

#### product_id

Show smart collections that includes given product

**Type:** string

#### published_at_max

Show smart collections published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show smart collections published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published smart collections    unpublished - Show only unpublished smart collections    any - Show all smart collections (default)

**Type:** string

#### since_id

Restrict results to after the specified ID

**Type:** string

#### title

Show smart collections with given title

**Type:** string

#### updated_at_max

Show smart collections last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show smart collections last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_smart_collections_count



<details><summary>Parameters</summary>

#### product_id

Show smart collections that includes given product

**Type:** string

#### published_at_max

Show smart collections published before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_at_min

Show smart collections published after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### published_status

published - Show only published smart collections    unpublished - Show only unpublished smart collections    any - Show all smart collections (default)

**Type:** string

#### title

Show smart collections with given title

**Type:** string

#### updated_at_max

Show smart collections last updated before date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

#### updated_at_min

Show smart collections last updated after date (format: 2014-04-25T16:15:47-04:00)

**Type:** string

</details>

## get_themes



<details><summary>Parameters</summary>

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_themes_id_assets



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_users



*This operation has no parameters*

## get_users_current



*This operation has no parameters*

## get_users_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_variants_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

comma-separated list of fields to include in the response

**Type:** string

</details>

## get_webhooks



<details><summary>Parameters</summary>

#### address

Use this parameter to retrieve only webhooks that possess the URI where the webhook sends the POST request when the event occurs.

**Type:** string

#### created_at_max

Use this parameter to retrieve only webhooks that were created before a given date and time (format: 2014-04-25T16:15:47-04:00).

**Type:** string

#### created_at_min

Use this parameter to retrieve only webhooks that were created after a given date and time (format: 2014-04-25T16:15:47-04:00).

**Type:** string

#### fields

A comma-separated list of the properties you want returned for each item in the result list. Use this parameter to restrict the returned list of items to showing only those properties you specify.

**Type:** string

#### limit

The maximum number of webhooks that should be returned. Setting this parameter outside the maximum range will result in an error.  (default: 50)  (maximum: 250)

**Type:** string

#### page

The page number of the result list to retrieve. Use this in tandem with limit to page through the webhooks in a shop.  (default: 1)

**Type:** string

#### since_id

Use this parameter to restrict the returned list to only webhooks whose id is greater than the specified id.

**Type:** string

#### topic

Show webhooks with a given topic. Valid topics are:           carts/create, carts/update, checkouts/create, checkouts/delete, checkouts/update, collections/create, collections/delete, collections/update, customer_groups/create, customer_groups/delete, customer_groups/update, customers/create, customers/delete, customers/disable, customers/enable, customers/update, disputes/create, disputes/update, fulfillment_events/create, fulfillment_events/delete, fulfillments/create, fulfillments/update, order_transactions/create, orders/cancelled, orders/create, orders/delete, orders/fulfilled, orders/paid, orders/partially_fulfilled, orders/updated, products/create, products/delete, products/update, refunds/create, shop/update, themes/create, themes/delete, themes/publish, themes/update

**Type:** string

#### updated_at_max

Use this parameter to retrieve only webhooks that were updated after a given date and time (format: 2014-04-25T16:15:47-04:00).

**Type:** string

#### updated_at_min

Use this parameter to retrieve only webhooks that were updated before a given date and time (format: 2014-04-25T16:15:47-04:00).

**Type:** string

</details>

## get_webhooks_count



<details><summary>Parameters</summary>

#### address

Use this parameter to retrieve only webhooks that possess the URI where the webhook sends the POST request when the event occurs.

**Type:** string

#### topic

Show webhooks with a given topic. Valid topics are:           carts/create, carts/update, checkouts/create, checkouts/delete, checkouts/update, collections/create, collections/delete, collections/update, customer_groups/create, customer_groups/delete, customer_groups/update, customers/create, customers/delete, customers/disable, customers/enable, customers/update, disputes/create, disputes/update, fulfillment_events/create, fulfillment_events/delete, fulfillments/create, fulfillments/update, order_transactions/create, orders/cancelled, orders/create, orders/delete, orders/fulfilled, orders/paid, orders/partially_fulfilled, orders/updated, products/create, products/delete, products/update, refunds/create, shop/update, themes/create, themes/delete, themes/publish, themes/update

**Type:** string

</details>

## get_webhooks_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### fields

A comma-separated list of the properties you want returned for each item in the result list. Use this parameter to restrict the returned list of items to showing only those properties you specify.

**Type:** string

</details>

## post_application_charges



*This operation has no parameters*

## post_application_charges_id_activate



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_application_credits



*This operation has no parameters*

## post_blogs



*This operation has no parameters*

## post_blogs_id_articles



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_carrier_services



*This operation has no parameters*

## post_collects



*This operation has no parameters*

## post_comments



*This operation has no parameters*

## post_countries



*This operation has no parameters*

## post_custom_collections



*This operation has no parameters*

## post_customer_saved_searches



*This operation has no parameters*

## post_customers_id_addresses



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_discounts



*This operation has no parameters*

## post_discounts_id_disable



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_discounts_id_enable



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_gift_cards



*This operation has no parameters*

## post_gift_cards_id_disable



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_order_close



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_order_fulfillment_cancel



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## post_order_fulfillment_complete



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## post_order_fulfillment_events



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## post_order_fulfillment_open



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## post_order_fulfillments



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_order_open



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_order_refunds



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### discrepancy_reason

An optional comment, used if there is a discrepancy between calculated and actual refund amounts (one of: restock, damage, customer, other)

**Type:** string

#### note

An optional comment attached to a refund.

**Type:** string

#### notify

Boolean, set to true to send a refund notification to the customer.

**Type:** string

#### refund_line_items

Array of line item IDs and quantities to refund

**Type:** string

#### restock

Boolean, whether or not to add the line items back to the store inventory.

**Type:** string

#### shipping

Object to specify how much shipping to refund    full_refund - Boolean, set to true to refund all remaining shipping    amount - Set specific amount of shipping to refund. Takes precedence over full_refund .

**Type:** string

#### transactions

Array of transactions to process as refunds

**Type:** string

</details>

## post_order_refunds_calculate



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### refund_line_items

Array of line item IDs and quantities to refund

**Type:** string

#### shipping

Object to specify how much shipping to refund    full_refund - Boolean, set to true to refund all remaining shipping    amount - Set specific amount of shipping to refund. Takes precedence over full_refund .

**Type:** string

</details>

## post_order_risks



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_order_transactions



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_orders



<details><summary>Parameters</summary>

#### order

In addition to the properties defined earlier, you can use the following flags    send_receipt - Determines whether an order confirmation will be sent to the customer.  Default: false.    send_fulfillment_receipt - Determines whether a fulfillment confirmation will be sent to the customer.  Default: false.    inventory_behaviour -             Determines which inventory updating behaviour is used. The following values are available:   bypass (default) : Do not claim inventory.   decrement_ignoring_policy : Ignore the product's inventory policy and claim amounts no matter what.   decrement_obeying_policy : Obey the product's inventory policy.

**Type:** string

</details>

## post_pages



*This operation has no parameters*

## post_products



*This operation has no parameters*

## post_products_id_images



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_products_id_metafields



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_products_id_variants



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_recurring_application_charges



*This operation has no parameters*

## post_recurring_application_charges_id_activate



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_recurring_application_charges_id_usage_charges



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_redirects



*This operation has no parameters*

## post_script_tags



*This operation has no parameters*

## post_smart_collections



*This operation has no parameters*

## post_themes



*This operation has no parameters*

## post_webhooks



<details><summary>Parameters</summary>

#### format

Use this parameter to select the format to receive the data in. Valid values are json and xml.  (default: json)

**Type:** string

</details>

## put_blogs_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_blogs_id_articles_id



<details><summary>Parameters</summary>

#### article_id (required)

**Type:** string

#### blog_id (required)

**Type:** string

</details>

## put_carrier_services_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_comments_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_countries_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_countries_provinces_by_id



<details><summary>Parameters</summary>

#### country_id (required)

**Type:** string

#### province_id (required)

**Type:** string

</details>

## put_custom_collections_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_customer_saved_searches_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_customers_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_customers_id_addresses_id



<details><summary>Parameters</summary>

#### address_id (required)

**Type:** string

#### customer_id (required)

**Type:** string

</details>

## put_customers_id_addresses_id_default



<details><summary>Parameters</summary>

#### address_id (required)

**Type:** string

#### customer_id (required)

**Type:** string

</details>

## put_gift_cards_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_order_fulfillments_by_id



<details><summary>Parameters</summary>

#### fulfillment_id (required)

**Type:** string

#### order_id (required)

**Type:** string

</details>

## put_order_risks_id



<details><summary>Parameters</summary>

#### order_id (required)

**Type:** string

#### risk_id (required)

**Type:** string

</details>

## put_orders_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### order

Change an order’s attributes such as note, email, buyer-accepts-marketing,
        or remove the customer association.  You can also send the shipping_address object as part of an order
         to update any shipping_address parameter.    shipping_address - Enables you to update shipping address parameters

**Type:** string

</details>

## put_pages_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_products_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_products_id_images_id



<details><summary>Parameters</summary>

#### image_id (required)

**Type:** string

#### product_id (required)

**Type:** string

</details>

## put_products_metafields_by_id



<details><summary>Parameters</summary>

#### field_id (required)

**Type:** string

#### product_id (required)

**Type:** string

</details>

## put_recurring_application_charges_id_customize



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_redirects_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_script_tags_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_themes_id_assets



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_variants_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## put_webhooks_id



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

