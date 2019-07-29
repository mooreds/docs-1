---
id: mailchimp-documentation
title: Mailchimp (version v1.*.*)
sidebar_label: Mailchimp
layout: docs.mustache
---

## add_cart_to_store

Add a new cart to a store.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific cart.

**Type:** object

```json
{
  "checkout_url" : "The URL for the cart. This parameter is required for [Abandoned Cart](http://kb.mailchimp.com/automation/create-an-abandoned-cart-email) automations.",
  "tax_total" : "The total tax for the cart.",
  "order_total" : "The order total for the cart.",
  "id" : "A unique identifier for the cart.",
  "lines" : [ {
    "quantity" : "The quantity of a cart line item.",
    "price" : "The price of a cart line item.",
    "product_id" : "A unique identifier for the product associated with the cart line item.",
    "id" : "A unique identifier for the cart line item.",
    "product_variant_id" : "A unique identifier for the product variant associated with the cart line item."
  } ],
  "campaign_id" : "A string that uniquely identifies the campaign for a cart.",
  "currency_code" : "The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code for the currency that the cart uses.",
  "customer" : {
    "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "email_address" : "The customer's email address.",
    "address" : {
      "country" : "The customer's country.",
      "country_code" : "The two-letter code for the customer's country.",
      "province" : "The customer's state name or normalized province.",
      "address2" : "An additional field for the customer's mailing address.",
      "city" : "The city the customer is located in.",
      "address1" : "The mailing address of the customer.",
      "province_code" : "The two-letter code for the customer's province or state.",
      "postal_code" : "The customer's postal or zip code."
    },
    "last_name" : "The customer's last name.",
    "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
    "company" : "The customer's company.",
    "id" : "A unique identifier for the customer.",
    "first_name" : "The customer's first name."
  }
}
```

</details>

## add_customer_to_store

Add a new customer to a store.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific customer. Orders for existing customers should include only the `id` parameter in the `customer` object body.

**Type:** object

```json
{
  "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
  "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
  "email_address" : "The customer's email address.",
  "address" : {
    "country" : "The customer's country.",
    "country_code" : "The two-letter code for the customer's country.",
    "province" : "The customer's state name or normalized province.",
    "address2" : "An additional field for the customer's mailing address.",
    "city" : "The city the customer is located in.",
    "address1" : "The mailing address of the customer.",
    "province_code" : "The two-letter code for the customer's province or state.",
    "postal_code" : "The customer's postal or zip code."
  },
  "last_name" : "The customer's last name.",
  "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
  "company" : "The customer's company.",
  "id" : "A unique identifier for the customer.",
  "first_name" : "The customer's first name."
}
```

</details>

## add_feedback_to_campaign

Add feedback on a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### $body

A specific feedback message from a specific campaign.

**Type:** object

```json
{
  "is_complete" : "The status of feedback.",
  "message" : "The content of the feedback.",
  "block_id" : "The block id for the editable block that the feedback addresses."
}
```

</details>

## add_interest_to_interest_category

Create a new interest or 'group name' for a specific category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Assign subscribers to interests to group them together. Interests are referred to as 'group names' in the MailChimp application.

**Type:** object

```json
{
  "name" : "The name of the interest. This can be shown publicly on a subscription form.",
  "display_order" : "The display order for interests."
}
```

</details>

## add_line_item_to_cart

Add a new line item to an existing cart.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific cart line item.

**Type:** object

```json
{
  "quantity" : "The quantity of a cart line item.",
  "price" : "The price of a cart line item.",
  "product_id" : "A unique identifier for the product associated with the cart line item.",
  "id" : "A unique identifier for the cart line item.",
  "product_variant_id" : "A unique identifier for the product variant associated with the cart line item."
}
```

</details>

## add_line_item_to_order_in_store

Add a new line item to an existing order.

<details><summary>Parameters</summary>

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific order line.

**Type:** object

```json
{
  "quantity" : "The quantity of an order line item.",
  "price" : "The price of an order line item.",
  "product_id" : "A unique identifier for the product associated with the order line item.",
  "id" : "A unique identifier for the order line item.",
  "product_variant_id" : "A unique identifier for the product variant associated with the order line item."
}
```

</details>

## add_member_to_list

Add a new member to the list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed.

**Type:** object

```json
{
  "email_address" : "Email address for a subscriber.",
  "email_type" : "Type of email this member asked to get ('html' or 'text').",
  "timestamp_opt" : "The date and time the subscribe confirmed their opt-in status.",
  "merge_fields" : { },
  "timestamp_signup" : "The date and time the subscriber signed up for the list.",
  "ip_opt" : "The IP address the subscriber used to confirm their opt-in status.",
  "language" : "If set/detected, the [subscriber's language](http://kb.mailchimp.com/lists/managing-subscribers/view-and-edit-subscriber-languages?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
  "location" : {
    "latitude" : "The location latitude.",
    "longitude" : "The location longitude."
  },
  "ip_signup" : "IP address the subscriber signed up from.",
  "interests" : "The key of this object's properties is the ID of the interest in question.",
  "vip" : "[VIP status](http://kb.mailchimp.com/lists/managing-subscribers/designate-and-send-to-vip-subscribers?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for subscriber.",
  "status" : "Subscriber's current status."
}
```

</details>

## add_member_to_segment

Add a member to a static segment.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

### $body

**Type:** object

```json
{
  "email_address" : "Email address for a subscriber."
}
```

</details>

## add_merge_field_to_list

Add a new merge field for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

A merge field (formerly merge vars) for a specific list. These correspond to merge fields in MailChimp's lists and subscriber profiles.

**Type:** object

```json
{
  "public" : "Whether the merge field is displayed on the signup form.",
  "name" : "The name of the merge field.",
  "display_order" : "The order that the merge field displays on the list signup form.",
  "options" : {
    "size" : "In a text field, the default length of the text field.",
    "date_format" : "In a date or birthday field, the format of the date.",
    "choices" : [ "string" ],
    "default_country" : "In an address field, the default country code if none supplied.",
    "phone_format" : "In a phone field, the phone number type: US or International."
  },
  "default_value" : "The default value for the merge field if `null`.",
  "tag" : "The tag used in MailChimp campaigns and for the /members endpoint.",
  "type" : "The type for the merge field.",
  "required" : "The boolean value if the merge field is required.",
  "help_text" : "Extra text to help the subscriber fill out the form."
}
```

</details>

## add_order_in_store

Add a new order to a store.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific order.

**Type:** object

```json
{
  "fulfillment_status" : "The fulfillment status for the order. For example: `partial`, `fulfilled`, etc.",
  "tax_total" : "The tax total for the order.",
  "shipping_total" : "The shipping total for the order.",
  "processed_at_foreign" : "The date and time the order was processed.",
  "billing_address" : {
    "country" : "The country in the billing address.",
    "address2" : "An additional field for the billing address.",
    "city" : "The city in the billing address.",
    "address1" : "The billing address for the order.",
    "latitude" : "The latitude for the billing address location.",
    "province_code" : "The two-letter code for the province in the billing address.",
    "country_code" : "The two-letter code for the country in the billing address.",
    "province" : "The state or normalized province in the billing address.",
    "phone" : "The phone number for the billing address",
    "name" : "The name associated with the billing address.",
    "company" : "The company associated with the billing address.",
    "postal_code" : "The postal or zip code in the billing address.",
    "longitude" : "The longitude for the billing address location."
  },
  "tracking_code" : "The MailChimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.",
  "currency_code" : "The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code for the currency that the store accepts.",
  "landing_site" : "The URL for the page where the buyer landed when entering the shop.",
  "financial_status" : "The order status. For example: `refunded`, `processing`, `cancelled`, etc.",
  "order_total" : "The total for the order.",
  "id" : "A unique identifier for the order.",
  "shipping_address" : {
    "country" : "The country in the shipping address.",
    "address2" : "An additional field for the shipping address.",
    "city" : "The city in the order's shipping address.",
    "address1" : "The shipping address for the order.",
    "latitude" : "The latitude for the shipping address location.",
    "province_code" : "The two-letter code for the province or state in the shipping address.",
    "country_code" : "The two-letter code for the country in the shipping address.",
    "province" : "The state or normalized province in the order's shipping address.",
    "phone" : "The phone number for the order's shipping address.",
    "name" : "The name associated with an order's shipping address.",
    "company" : "The company associated with the shipping address.",
    "postal_code" : "The postal or zip code in the shipping address.",
    "longitude" : "The longitude for the shipping address location."
  },
  "updated_at_foreign" : "The date and time the order was updated.",
  "lines" : [ {
    "quantity" : "The quantity of an order line item.",
    "price" : "The price of an order line item.",
    "product_id" : "A unique identifier for the product associated with the order line item.",
    "id" : "A unique identifier for the order line item.",
    "product_variant_id" : "A unique identifier for the product variant associated with the order line item."
  } ],
  "campaign_id" : "A string that uniquely identifies the campaign for an order.",
  "customer" : {
    "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "email_address" : "The customer's email address.",
    "address" : {
      "country" : "The customer's country.",
      "country_code" : "The two-letter code for the customer's country.",
      "province" : "The customer's state name or normalized province.",
      "address2" : "An additional field for the customer's mailing address.",
      "city" : "The city the customer is located in.",
      "address1" : "The mailing address of the customer.",
      "province_code" : "The two-letter code for the customer's province or state.",
      "postal_code" : "The customer's postal or zip code."
    },
    "last_name" : "The customer's last name.",
    "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
    "company" : "The customer's company.",
    "id" : "A unique identifier for the customer.",
    "first_name" : "The customer's first name."
  },
  "cancelled_at_foreign" : "The date and time the order was cancelled."
}
```

</details>

## add_product_to_store

Add a new product to a store.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific product.

**Type:** object

```json
{
  "vendor" : "The vendor for a product.",
  "image_url" : "The image URL for a product.",
  "description" : "The description of a product.",
  "handle" : "The handle of a product.",
  "published_at_foreign" : "The date and time the product was published.",
  "id" : "A unique identifier for the product.",
  "variants" : [ {
    "inventory_quantity" : "The inventory quantity of a product variant.",
    "visibility" : "The visibility of a product variant.",
    "backorders" : "The backorders of a product variant.",
    "price" : "The price of a product variant.",
    "image_url" : "The image URL for a product variant.",
    "id" : "A unique identifier for the product variant.",
    "title" : "The title of a product variant.",
    "sku" : "The stock keeping unit (SKU) of a product variant.",
    "url" : "The URL for a product variant."
  } ],
  "title" : "The title of a product.",
  "type" : "The type of product.",
  "url" : "The URL for a product."
}
```

</details>

## add_subscriber_to_email_workflow

Manually add a subscriber to a workflow, bypassing the default trigger settings. You can also use this endpoint to trigger a series of automated emails in an [API 3.0 workflow type](http://kb.mailchimp.com/automation/about-automation-workflow-types?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Using-the-API) or add subscribers to an automated email queue that uses the [API request delay type](http://kb.mailchimp.com/automation/about-automation-workflow-types?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Using-the-API).

<details><summary>Parameters</summary>

### workflow_email_id (required)

The unique id for the Automation workflow email.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

### $body

Information about subscribers in an Automation email queue.

**Type:** object

```json
{
  "email_address" : "The list member's email address."
}
```

</details>

## add_variant_to_product_in_store

Add a new variant to the product.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific product variant.

**Type:** object

```json
{
  "inventory_quantity" : "The inventory quantity of a product variant.",
  "visibility" : "The visibility of a product variant.",
  "backorders" : "The backorders of a product variant.",
  "price" : "The price of a product variant.",
  "image_url" : "The image URL for a product variant.",
  "id" : "A unique identifier for the product variant.",
  "title" : "The title of a product variant.",
  "sku" : "The stock keeping unit (SKU) of a product variant.",
  "url" : "The URL for a product variant."
}
```

</details>

## batch_update_members_in_list

Batch subscribe or unsubscribe list members.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Members to subscribe to or unsubscribe from a list.

**Type:** object

```json
{
  "members" : [ {
    "email_address" : "Email address for a subscriber.",
    "email_type" : "Type of email this member asked to get ('html' or 'text').",
    "timestamp_opt" : "The date and time the subscribe confirmed their opt-in status.",
    "merge_fields" : { },
    "timestamp_signup" : "The date and time the subscriber signed up for the list.",
    "ip_opt" : "The IP address the subscriber used to confirm their opt-in status.",
    "language" : "If set/detected, the [subscriber's language](http://kb.mailchimp.com/lists/managing-subscribers/view-and-edit-subscriber-languages?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
    "location" : {
      "country_code" : "The unique code for the location country.",
      "dstoff" : "The offset for timezones where daylight saving time is observed.",
      "timezone" : "The timezone for the location.",
      "latitude" : "The location latitude.",
      "gmtoff" : "The time difference in hours from GMT.",
      "longitude" : "The location longitude."
    },
    "ip_signup" : "IP address the subscriber signed up from.",
    "interests" : "The key of this object's properties is the ID of the interest in question.",
    "vip" : "[VIP status](http://kb.mailchimp.com/lists/managing-subscribers/designate-and-send-to-vip-subscribers?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for subscriber.",
    "status" : "Subscriber's current status."
  } ],
  "update_existing" : "Whether this batch operation will change existing members' subscription status."
}
```

</details>

## batch_update_members_in_segment

Batch add/remove list members to static segment

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

### $body

Members to add/remove to/from a static segment

**Type:** object

```json
{
  "members_to_add" : [ "string" ],
  "members_to_remove" : [ "string" ]
}
```

</details>

## cancel_campaign

Cancel a Regular or Plain-Text Campaign after you send, before all of your recipients receive it. This feature is included with [MailChimp Pro](http://mailchimp.com/pro?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## create_campaign

Create a new MailChimp campaign.

<details><summary>Parameters</summary>

### $body

A summary of an individual campaign's settings and content.

**Type:** object

```json
{
  "settings" : {
    "auto_footer" : "Automatically append MailChimp's [default footer](http://kb.mailchimp.com/campaigns/design/theres-a-gray-footer-added-to-my-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to the campaign.",
    "subject_line" : "The subject line for the campaign.",
    "use_conversation" : "Use MailChimp Conversation feature to manage out-of-office replies.",
    "authenticate" : "Whether MailChimp [authenticated](http://kb.mailchimp.com/delivery/deliverability-research/set-up-mailchimp-authentication?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) the campaign. Defaults to `true`.",
    "to_name" : "The campaign's custom 'To' name. Typically the first name [merge field](http://kb.mailchimp.com/merge-tags/using/getting-started-with-merge-tags?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
    "title" : "The title of the campaign.",
    "from_name" : "The 'from' name on the campaign (not an email address).",
    "auto_tweet" : "Automatically tweet a link to the [campaign archive](http://kb.mailchimp.com/campaigns/archives/set-up-your-campaign-archive?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) page when the campaign is sent.",
    "auto_fb_post" : [ "string" ],
    "fb_comments" : "Allows Facebook comments on the campaign (also force-enables the Campaign Archive toolbar). Defaults to `true`.",
    "reply_to" : "The reply-to email address for the campaign.",
    "inline_css" : "Automatically inline the CSS included with the campaign content.",
    "folder_id" : "If the campaign is listed in a folder, the id for that folder."
  },
  "variate_settings" : {
    "send_times" : [ "date-time" ],
    "wait_time" : "The number of minutes to wait before choosing the winning campaign. The value of wait_time must be greater than 0 and in whole hours, specified in minutes.",
    "subject_lines" : [ "string" ],
    "test_size" : "The percentage of recipients to send the test combinations to, must be a value between 10 and 100.",
    "reply_to_addresses" : [ "string" ],
    "winner_criteria" : "The combination that performs the best. This may be determined automatically by click rate, open rate, or total revenue—or you may choose manually based on the reporting data you find the most valuable. For Multivariate Campaigns testing send_time, winner_criteria is ignored. For Multivariate Campaigns with 'manual' as the winner_criteria, the winner must be chosen in the MailChimp web application.",
    "from_names" : [ "string" ]
  },
  "ab_split_opts" : {
    "pick_winner" : "How we should evaluate a winner. Based on 'opens', 'clicks', or 'manual'.",
    "wait_time" : "The amount of time to wait before picking a winner. This cannot be changed after a campaign is sent.",
    "wait_units" : "How unit of time for measuring the winner ('hours' or 'days'). This cannot be changed after a campaign is sent.",
    "subject_b" : "For campaigns split on 'Subject Line', the subject line for Group B.",
    "subject_a" : "For campaigns split on 'Subject Line', the subject line for Group A.",
    "split_test" : "The type of AB split to run.",
    "from_name_a" : "For campaigns split on 'From Name', the name for Group A.",
    "from_name_b" : "For campaigns split on 'From Name', the name for Group B.",
    "send_time_winner" : "The send time for the winning version.",
    "reply_email_b" : "For campaigns split on 'From Name', the reply-to address for Group B.",
    "reply_email_a" : "For campaigns split on 'From Name', the reply-to address for Group A.",
    "send_time_a" : "The send time for Group A.",
    "send_time_b" : "The send time for Group B.",
    "split_size" : "The size of the split groups. Campaigns split based on 'schedule' are forced to have a 50/50 split. Valid split integers are between 1-50."
  },
  "rss_opts" : {
    "schedule" : {
      "hour" : "The hour to send the campaign in local time. Acceptable hours are 0-23. For example, '4' would be 4am in [your account's default time zone](http://kb.mailchimp.com/accounts/account-setup/how-to-set-account-defaults?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
      "weekly_send_day" : "The day of the week to send a weekly RSS Campaign.",
      "daily_send" : {
        "sunday" : "Sends the daily RSS Campaign on Sundays.",
        "saturday" : "Sends the daily RSS Campaign on Saturdays.",
        "tuesday" : "Sends the daily RSS Campaign on Tuesdays.",
        "wednesday" : "Sends the daily RSS Campaign on Wednesdays.",
        "thursday" : "Sends the daily RSS Campaign on Thursdays.",
        "friday" : "Sends the daily RSS Campaign on Fridays.",
        "monday" : "Sends the daily RSS Campaign on Mondays."
      },
      "monthly_send_date" : "The day of the month to send a monthly RSS Campaign. Acceptable days are 0-31, where '0' is always the last day of a month. Months with fewer than the selected number of days will not have an RSS campaign sent out that day. For example, RSS Campaigns set to send on the 30th will not go out in February."
    },
    "constrain_rss_img" : "Whether to add CSS to images in the RSS feed to constrain their width in campaigns.",
    "feed_url" : "The URL for the RSS feed.",
    "frequency" : "The frequency of the RSS Campaign."
  },
  "social_card" : {
    "image_url" : "The url for the header image for the card.",
    "description" : "A short summary of the campaign to display.",
    "title" : "The title for the card. Typically the subject line of the campaign."
  },
  "recipients" : {
    "segment_opts" : {
      "match" : "Segment match type.",
      "saved_segment_id" : "The id for an existing saved segment.",
      "conditions" : [ {
        "op" : "The segment operator.",
        "field" : "The field to segment on.",
        "condition_type" : "The type of segment, for example: date, language, Mandrill, static, and more."
      } ]
    },
    "list_id" : "The unique list id."
  },
  "type" : "There are four types of [campaigns](http://kb.mailchimp.com/campaigns?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) you can create in MailChimp. A/B Split campaigns have been deprecated and variate campaigns should be used instead.",
  "tracking" : {
    "salesforce" : {
      "notes" : "Update contact notes for a campaign based on subscriber email addresses.",
      "campaign" : "Create a campaign in a connected Salesforce account."
    },
    "highrise" : {
      "notes" : "Update contact notes for a campaign based on subscriber email addresses.",
      "campaign" : "Create a campaign in a connected Highrise account."
    },
    "goal_tracking" : "Whether to enable [Goal](http://kb.mailchimp.com/integrations/other-integrations/integrate-goal-with-mailchimp?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) tracking.",
    "capsule" : {
      "notes" : "Update contact notes for a campaign based on subscriber email addresses."
    },
    "clicktale" : "The custom slug for [ClickTale](http://kb.mailchimp.com/integrations/other-integrations/additional-tracking-options-for-campaigns?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Click-Tale) tracking (max of 50 bytes).",
    "text_clicks" : "Whether to [track clicks](http://kb.mailchimp.com/reports/about-click-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in the plain-text version of the campaign. Defaults to `true`. Cannot be set to false for variate campaigns.",
    "ecomm360" : "Whether to enable [eCommerce360](http://kb.mailchimp.com/integrations/other-integrations/about-ecommerce360?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) tracking.",
    "opens" : "Whether to [track opens](http://kb.mailchimp.com/reports/about-open-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs). Defaults to `true`. Cannot be set to false for variate campaigns.",
    "google_analytics" : "The custom slug for [Google Analytics](http://kb.mailchimp.com/integrations/other-integrations/integrate-google-analytics-with-mailchimp?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) tracking (max of 50 bytes).",
    "html_clicks" : "Whether to [track clicks](http://kb.mailchimp.com/reports/about-click-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in the HTML version of the campaign. Defaults to `true`. Cannot be set to false for variate campaigns."
  }
}
```

</details>

## create_campaign_folder

Create a new campaign folder.

<details><summary>Parameters</summary>

### $body

A folder used to organize campaigns.

**Type:** object

```json
{
  "name" : "Name to associate with the folder."
}
```

</details>

## create_interest_category_for_list

Create a new interest category.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Interest categories organize interests, which are used to group subscribers based on their preferences. These correspond to Group Titles the application.

**Type:** object

```json
{
  "display_order" : "The order that the categories are displayed in the list. Lower numbers display first.",
  "title" : "The text description of this category. This field appears on signup forms and is often phrased as a question.",
  "type" : "Determines how this category’s interests appear on signup forms."
}
```

</details>

## create_list

Create a new list in your MailChimp account.

<details><summary>Parameters</summary>

### $body

Information about a specific list.

**Type:** object

```json
{
  "notify_on_subscribe" : "The email address to send [subscribe notifications](http://kb.mailchimp.com/lists/managing-subscribers/change-subscribe-and-unsubscribe-notifications?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to.",
  "email_type_option" : "Whether the list supports [multiple formats for emails](http://kb.mailchimp.com/lists/growth/how-to-change-list-name-and-defaults?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Change-Subscription-Settings). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.",
  "permission_reminder" : "The [permission reminder](http://kb.mailchimp.com/accounts/compliance-tips/edit-the-permission-reminder?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for the list.",
  "use_archive_bar" : "Whether campaigns for this list use the [Archive Bar](http://kb.mailchimp.com/campaigns/archives/about-the-archive-bar?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in archives by default.",
  "notify_on_unsubscribe" : "The email address to send [unsubscribe notifications](http://kb.mailchimp.com/lists/managing-subscribers/change-subscribe-and-unsubscribe-notifications?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to.",
  "visibility" : "Whether this list is [public or private](http://kb.mailchimp.com/lists/growth/about-publicity-settings?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
  "contact" : {
    "zip" : "The postal or zip code for the list contact.",
    "country" : "A two-character ISO3166 country code. Defaults to US if invalid.",
    "address2" : "The street address for the list contact.",
    "city" : "The city for the list contact.",
    "phone" : "The phone number for the list contact.",
    "address1" : "The street address for the list contact.",
    "company" : "The company name for the list.",
    "state" : "The state for the list contact."
  },
  "name" : "The name of the list.",
  "campaign_defaults" : {
    "from_email" : "The default from email for campaigns sent to this list.",
    "subject" : "The default subject line for campaigns sent to this list.",
    "language" : "The default language for this lists's forms.",
    "from_name" : "The default from name for campaigns sent to this list."
  }
}
```

</details>

## create_note_for_member_of_list

Add a new note for a specific subscriber.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### $body

A specific note for a specific member.

**Type:** object

```json
{
  "email_id" : "The MD5 hash of the lowercase version of the list member's email address.",
  "note" : "The content of the note.",
  "updated_at" : "The date and time the note was last updated.",
  "list_id" : "The unique id for the list.",
  "created_at" : "The date and time the note was created.",
  "id" : "The note id.",
  "created_by" : "The author of the note."
}
```

</details>

## create_segment_for_list

Create a new segment in a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Information about a specific list segment.

**Type:** object

```json
{
  "name" : "The name of the segment.",
  "options" : {
    "match" : "Match type.",
    "conditions" : [ {
      "op" : "The segment operator.",
      "field" : "The field to segment on.",
      "condition_type" : "The type of segment, for example: date, language, Mandrill, static, and more."
    } ]
  },
  "static_segment" : [ "string" ]
}
```

</details>

## create_store

Add a new store to your MailChimp account.

<details><summary>Parameters</summary>

### $body

An individual store in an account.

**Type:** object

```json
{
  "is_syncing" : "Whether the e-commerce store is currently [syncing](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#syncing-an-e-commerce-store).",
  "address" : {
    "country" : "The store's country.",
    "country_code" : "The two-letter code for to the store's country.",
    "province" : "The store's state name or normalized province.",
    "address2" : "An additional field for the store's mailing address.",
    "city" : "The city the store is located in.",
    "address1" : "The store's mailing address.",
    "latitude" : "The latitude of the store location.",
    "province_code" : "The two-letter code for the store's province or state.",
    "postal_code" : "The store's postal or zip code.",
    "longitude" : "The longitude of the store location."
  },
  "list_id" : "The unique identifier for the [MailChimp List](http://developer.mailchimp.com/documentation/mailchimp/reference/lists/) associated with the store. The `list_id` for a specific store cannot change.",
  "timezone" : "The timezone for the store.",
  "primary_locale" : "The primary locale for the store. For example: `en`, `de`, etc.",
  "platform" : "The e-commerce platform of the store.",
  "currency_code" : "The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code for the currency that the store accepts.",
  "money_format" : "The currency format for the store. For example: `$`, `£`, etc.",
  "email_address" : "The email address for the store.",
  "phone" : "The store phone number.",
  "domain" : "The store domain.",
  "name" : "The name of the store.",
  "id" : "The unique identifier for the store."
}
```

</details>

## create_template

Create a new template for the account. Only [Classic templates](http://kb.mailchimp.com/templates/basic-and-themes/types-of-templates?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) are supported.

<details><summary>Parameters</summary>

### $body

Information about a specific template.

**Type:** object

```json
{
  "name" : "The name of the template.",
  "html" : "The raw HTML for the template. We support the MailChimp [Template Language](http://kb.mailchimp.com/templates/code/getting-started-with-mailchimps-template-language?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in any HTML code passed via the API.",
  "folder_id" : "The id of the folder the template is currently in."
}
```

</details>

## create_template_folder

Create a new template folder.

<details><summary>Parameters</summary>

### $body

A folder used to organize templates.

**Type:** object

```json
{
  "name" : "The name of the folder."
}
```

</details>

## create_twitter_lead_gen_card_for_list

Create a new Twitter Lead Generation Card for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Twitter Lead Generation Card.

**Type:** object

```json
{
  "privacy_policy_url" : "Your site's privacy policy URL. If you don’t have a privacy policy, link to your website’s homepage instead.",
  "twitter_account_id" : "The [Twitter Ads](https://ads.twitter.com/login) account ID.",
  "cta_text" : "Text (up to the 20-character limit) to display on the card's Call-to-Action button.",
  "list_id" : "The unique identifier for the MailChimp list.",
  "image_url" : "A URL for the header image. The image size must be 800 x 200px.",
  "preview_url" : "The Twitter Lead Generation Card Preview URL.",
  "twitter_card_id" : "The Twitter-assigned Lead Generation Card ID.",
  "name" : "The name of the Twitter Lead Generation Card.",
  "custom_key_name" : "A custom key name used to store the Twitter display name of a subscriber.",
  "id" : "The unique MailChimp ID for the Twitter Lead Generation Card.",
  "title" : "The Twitter Lead Generation Card title."
}
```

</details>

## create_webhook_in_list

Create a new webhook for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Configure a webhook for the given list.

**Type:** object

```json
{
  "sources" : {
    "admin" : "Whether the webhook is triggered by admin-initiated actions in the web interface.",
    "api" : "Whether the webhook is triggered by actions initiated via the API.",
    "user" : "Whether the webhook is triggered by subscriber-initiated actions."
  },
  "url" : "A valid URL for the Webhook.",
  "events" : {
    "subscribe" : "Whether the webhook is triggered when a list subscriber is added.",
    "unsubscribe" : "Whether the webhook is triggered when a list member unsubscribes.",
    "profile" : "Whether the webhook is triggered when a subscriber's profile is updated.",
    "cleaned" : "Whether the webhook is triggered when a subscriber's email address is cleaned from the list.",
    "campaign" : "Whether the webhook is triggered when a campaign is sent or cancelled.",
    "upemail" : "Whether the webhook is triggered when a subscriber's email address is changed."
  }
}
```

</details>

## customize_signup_form_for_list

Customize a list's default signup form.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

List signup form.

**Type:** object

```json
{
  "contents" : [ {
    "section" : "The content section name.",
    "value" : "The content section text."
  } ],
  "header" : {
    "image_height" : "Image height, in pixels.",
    "image_link" : "The URL that the header image will link to.",
    "image_align" : "Image alignment.",
    "image_border_color" : "Image border color.",
    "image_url" : "Header image URL.",
    "image_border_style" : "Image border style.",
    "image_alt" : "Alt text for the image.",
    "text" : "Header text.",
    "image_width" : "Image width, in pixels.",
    "image_target" : "Image link target.",
    "image_border_width" : "Image border width."
  },
  "styles" : [ {
    "options" : [ {
      "property" : "A string that identifies the property.",
      "value" : "A string that identifies value of the property."
    } ],
    "selector" : "A string that identifies the element selector."
  } ]
}
```

</details>

## delete_batch_request

Stops a batch request from running. Since only one batch request is run at a time, this can be used to cancel a long running request. The results of any completed operations will not be available after this call.

<details><summary>Parameters</summary>

### batch_id (required)

The unique id for the batch operation.

**Type:** string

</details>

## delete_campaign

Remove a campaign from your MailChimp account.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## delete_campaign_folder

Delete a specific campaign folder, and mark all the campaigns in the folder as 'unfiled'.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

</details>

## delete_cart_in_store

Delete a cart.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### store_id (required)

The store id.

**Type:** string

</details>

## delete_customer_from_store

Delete a customer from a store.

<details><summary>Parameters</summary>

### customer_id (required)

The id for the customer of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

</details>

## delete_feedback_from_campaign

Remove a specific feedback message for a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### feedback_id (required)

The unique id for the feedback message.

**Type:** string

</details>

## delete_file_from_file_manager

Remove a specific file from the File Manager.

<details><summary>Parameters</summary>

### file_id (required)

The unique id for the File Manager file.

**Type:** string

</details>

## delete_folder_from_file_manager

Delete a specific folder in the File Manager.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

</details>

## delete_interest_category_from_list

Delete a specific interest category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

</details>

## delete_interests_in_category_of_list

Delete interests or group names in a specific category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### interest_id (required)

The specific interest or 'group name'.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

</details>

## delete_line_item_from_cart_in_store

Delete a specific cart line item.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### line_id (required)

The id for the line item.

**Type:** string

### store_id (required)

The store id.

**Type:** string

</details>

## delete_line_item_from_order_in_store

Delete a specific order line item.

<details><summary>Parameters</summary>

### line_id (required)

The id for the line item.

**Type:** string

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

</details>

## delete_list

Delete a list from your MailChimp account. If you delete a list, you'll lose the list history—including subscriber activity, unsubscribes, complaints, and bounces. You’ll also lose subscribers’ email addresses, unless you [exported and backed up your list](http://kb.mailchimp.com/lists/managing-subscribers/view-or-export-a-list?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#View-or-Export-a-List).

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

</details>

## delete_member_from_list

Delete a member from a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

</details>

## delete_member_from_segment

Remove a member from the specified static segment.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

</details>

## delete_merge_field_from_list

Delete a specific merge field in a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### merge_id (required)

The id for the merge field.

**Type:** string

</details>

## delete_note_for_member_of_list

Delete a specific note for a specific list member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### note_id (required)

The id for the note.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

</details>

## delete_order_from_store

Delete an order.

<details><summary>Parameters</summary>

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

</details>

## delete_product_from_store

Delete a product.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

</details>

## delete_segment_from_list

Delete a specific segment in a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

</details>

## delete_store

Delete a store. Deleting a store will also delete any associated subresources, including Customers, Orders, Products, and Carts.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

</details>

## delete_subscriber_from_workflow

[Remove a subscriber](http://kb.mailchimp.com/automation/add-or-remove-subscribers-from-automation-workflow?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) from a specific Automation workflow. You can remove a subscriber at any point in an Automation workflow, regardless of how many emails they've been sent from that workflow. Once they're removed, they can never be added back to the same workflow.

<details><summary>Parameters</summary>

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

### $body

Information about subscribers in an Automation email queue.

**Type:** object

```json
{
  "email_address" : "The list member's email address."
}
```

</details>

## delete_template

Delete a specific template.

<details><summary>Parameters</summary>

### template_id (required)

The unique id for the template.

**Type:** string

</details>

## delete_template_folder

Delete a specific template folder, and mark all the templates in the folder as 'unfiled'.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

</details>

## delete_variant_for_product_in_store

Delete a product variant.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### variant_id (required)

The id for the product variant.

**Type:** string

</details>

## delete_webhook_from_list

Delete a specific webhook in a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### webhook_id (required)

The unique ID for the webhook.

**Type:** string

</details>

## get_abuse_report_from_campaign

Get information about a specific abuse report for a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### report_id (required)

The id for the abuse report.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_abuse_report_from_list

Get details about a specific abuse report.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### report_id (required)

The id for the abuse report.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_audiences_dashboard

Get all the audiences info for the mobile dashboard

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_authorized_app

Get information about a specific authorized application.

<details><summary>Parameters</summary>

### app_id (required)

The unique id for the connected authorized application.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_batch_status

Get the status of a batch request.

<details><summary>Parameters</summary>

### batch_id (required)

The unique id for the batch operation.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_campaign

Get information about a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_campaign_folder

Get information about a specific folder used to organize campaigns.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_cart_for_store

Get information about a specific cart.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_click_details_for_campaign

Get information about [clicks](http://kb.mailchimp.com/reports/about-click-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) on specific links in your MailChimp campaigns.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_click_details_for_link_in_campaign

Get click details for a specific link in a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### link_id (required)

The id for the link.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_content_from_campaign

Get the the HTML and plain-text content for a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_conversation

Get details about an individual conversation.

<details><summary>Parameters</summary>

### conversation_id (required)

The unique id for the conversation.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_customer_information

Get information about a specific customer.

<details><summary>Parameters</summary>

### customer_id (required)

The id for the customer of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_default_content_for_template

Get the sections that you can edit in a template, including each section's default content.

<details><summary>Parameters</summary>

### template_id (required)

The unique id for the template.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_domain_performance_stats

Get statistics for the top-performing email domains in a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_ecommerce_dashboard

Get all the ecommerce info for the mobile dashboard

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_ecommerce_endpoint



*This operation has no parameters*

## get_eepurl_activity

Get a summary of social activity for the campaign, tracked by EepURL.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_email_activity_for_member_in_campaign

Get a specific list member's activity in a campaign including opens, clicks, and bounces.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_email_from_workflow

Get information about an individual Automation workflow email.

<details><summary>Parameters</summary>

### workflow_email_id (required)

The unique id for the Automation workflow email.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## get_engagement_dashboard

Get all the engagement info for the mobile dashboard

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_feedback_from_campaign

Get a specific feedback message from a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### feedback_id (required)

The unique id for the feedback message.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_feedback_report_for_campaign

Get feedback based on a campaign's statistics. Advice feedback is based on campaign stats like opens, clicks, unsubscribes, bounces, and more.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_file_from_file_manager

Get information about a specific file in the File Manager.

<details><summary>Parameters</summary>

### file_id (required)

The unique id for the File Manager file.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_file_manager_endpoint



*This operation has no parameters*

## get_folder_in_file_manager

Get information about a specific folder in the File Manager.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_growth_history_by_month_for_list

Get a summary of a specific list's growth activity for a specific month and year.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### month (required)

A specific month of list growth history.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_growth_history_data_for_list

Get a month-by-month summary of a specific list's growth activity.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_interest_category_from_list

Get information about a specific interest category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_interest_in_interest_category

Get interests or 'group names' for a specific category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### interest_id (required)

The specific interest or 'group name'.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_line_item_for_cart_in_store

Get information about a specific cart line item.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### line_id (required)

The id for the line item.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_line_item_in_order_in_store

Get information about a specific order line item.

<details><summary>Parameters</summary>

### line_id (required)

The id for the line item.

**Type:** string

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_list

Get information about a specific list in your MailChimp account. Results include list members who have signed up but haven't confirmed their subscription yet and [unsubscribed or cleaned](http://kb.mailchimp.com/lists/managing-subscribers/view-unsubscribed-and-cleaned-addresses?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_lists_id_members_id_goals

Get the last 50 Goal events for a member on a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_member_from_click_details

Get information about a specific subscriber who clicked a link in a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### link_id (required)

The id for the link.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_member_from_list

Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_merge_field_from_list

Get information about a specific merge field in a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### merge_id (required)

The id for the merge field.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_message_in_conversation

Get an individual message in a conversation.

<details><summary>Parameters</summary>

### conversation_id (required)

The unique id for the conversation.

**Type:** string

### message_id (required)

The unique id for the conversation message.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_note_for_member_of_list

Get a specific note for a specific list member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### note_id (required)

The id for the note.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_onboarding_ads_dashboard

Get all the onboarding ads info for the mobile dashboard

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### num

Restrict results to this number of ads (if we have that many. Default is 3.

**Type:** integer

### platform

Restrict results to ads compatible with the given platform. Default is ios

**Type:** string

</details>

## get_order_for_store

Get information about a specific order.

<details><summary>Parameters</summary>

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_product_in_store

Get information about a specific product.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_recipient_from_campaign

Get information about a specific campaign recipient.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_removed_subscriber_from_workflow

Get information about a specific subscriber who was [removed from an Automation workflow](http://kb.mailchimp.com/automation/add-or-remove-subscribers-from-automation-workflow?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## get_report_for_campaign

Get report details for a specific sent campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_segment_of_list

Get information about a specific segment.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_send_checklist_for_campaign

Review the send checklist for a campaign, and resolve any issues before sending.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_store

Get information about a specific store.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_subscriber_in_email_queue

Get information about a specific subscriber in an Automation email queue.

<details><summary>Parameters</summary>

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### workflow_email_id (required)

The unique id for the Automation workflow email.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## get_template

Get information about a specific template.

<details><summary>Parameters</summary>

### template_id (required)

The unique id for the template.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_template_folder

Get information about a specific folder used to organize templates.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_twitter_lead_gen_card_for_list

Get information about a specific Twitter Lead Generation Card.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### twitter_card_id (required)

The unique ID for the Twitter Lead Generation Card.

**Type:** string

</details>

## get_unsubscribed_member_from_list

Get information about a specific list member who unsubscribed from a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_variant_for_product_in_store

Get information about a specific product variant.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### variant_id (required)

The id for the product variant.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## get_webhook_for_list

Get information about a specific webhook.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### webhook_id (required)

The unique ID for the webhook.

**Type:** string

</details>

## get_workflow

Get a summary of an individual Automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.

<details><summary>Parameters</summary>

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## link_authorized_app

Retrieve OAuth2-based credentials to associate API calls with your application.

<details><summary>Parameters</summary>

### $body

Use this endpoint to link your application and retrieve OAuth2-based credentials. This is useful if you can't implement the OAuth2 flow but still want to associate calls with your application.

**Type:** object

```json
{
  "client_secret" : "The client password for authorization.",
  "client_id" : "The client's unique id/username for authorization."
}
```

</details>

## list_abuse_reports_for_campaign

Get a list of [abuse complaints](http://kb.mailchimp.com/accounts/compliance-tips/about-abuse-complaints?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_abuse_reports_for_list

Get all abuse reports for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_activity_for_list

Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_activity_for_member_in_list

Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_api_resources

Get links to all other resources available in the API.

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_authorized_apps

Get a list of an account's registered, connected applications.

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_automations

Get a summary of an account's Automations.

<details><summary>Parameters</summary>

### before_create_time

Restrict the response to automations created before the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### before_send_time

Restrict the response to automations sent before the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### since_create_time

Restrict the response to automations created after the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### since_send_time

Restrict the response to automations sent after the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### status

Restrict the results to automations with the specified status.

**Type:** string

**Potential values:** save, paused, sending

</details>

## list_batches

Get a summary of batch requests that have been made.

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_campaign_folders

Get all folders used to organize campaigns.

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_campaigns

Get all campaigns in an account.

<details><summary>Parameters</summary>

### before_create_time

Restrict the response to campaigns created before the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### before_send_time

Restrict the response to campaigns sent before the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### folder_id

The unique folder id.

**Type:** string

### list_id

The unique id for the list.

**Type:** string

### since_create_time

Restrict the response to campaigns created after the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### since_send_time

Restrict the response to campaigns sent after the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### status

The status of the campaign.

**Type:** string

**Potential values:** save, paused, schedule, sending, sent

### type

The campaign type.

**Type:** string

**Potential values:** regular, plaintext, absplit, rss, variate

</details>

## list_carts_for_store

Get information about a store's carts.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_conversations

Get a list of conversations for the account.

<details><summary>Parameters</summary>

### campaign_id

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### has_unread_messages

Whether the conversation has any unread messages.

**Type:** string

**Potential values:** true, false

### list_id

The unique id for the list.

**Type:** string

</details>

## list_customers_for_store

Get information about a store's customers.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### email_address

Restrict the response to customers with the email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_dashboard_charts

Get info about which dashboard charts to show for this user

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_email_activity

Get a list of member's subscriber activity in a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_emails_in_email_workflow

Get a summary of the emails in an Automation workflow.

<details><summary>Parameters</summary>

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## list_feedback_for_campaign

Get team feedback while you're [working together on a MailChimp campaign](http://kb.mailchimp.com/campaigns/design/collaborate-on-campaigns?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_files_in_file_manager

Get a list of available images and files stored in the File Manager for the account.

<details><summary>Parameters</summary>

### before_created_at

Restrict the response to files created before the set date.

**Type:** string

### created_by

The MailChimp account user who created the File Manager file.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### since_created_at

Restrict the response to files created after the set date.

**Type:** string

### sort_dir

Determines the order direction for sorted results.

**Type:** string

**Potential values:** ASC, DESC

### sort_field

Returns files sorted by the specified field.

**Type:** string

**Potential values:** added_date

### type

The file type for the File Manager file.

**Type:** string

</details>

## list_folders_in_file_manager

Get a list of all folders in the File Manager.

<details><summary>Parameters</summary>

### before_created_at

Restrict the response to files created before the set date.

**Type:** string

### created_by

The MailChimp account user who created the File Manager file.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### since_created_at

Restrict the response to files created after the set date.

**Type:** string

</details>

## list_interest_categories_for_list

Get information about a list's interest categories.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### type

Restrict results a type of interest group

**Type:** string

</details>

## list_interests_in_interest_category

Get a list of this category's interests.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_line_items_for_cart

Get information about a cart's line items.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_line_items_from_order_in_store

Get information about an order's line items.

<details><summary>Parameters</summary>

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_lists

Get information about all lists in the account.

<details><summary>Parameters</summary>

### before_campaign_last_sent

Restrict results to lists created before the last campaign send date.

**Type:** string

### before_date_created

Restrict response to lists created before the set date.

**Type:** string

### email

Restrict results to lists that include a specific subscriber's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### since_campaign_last_sent

Restrict results to lists created after the last campaign send date.

**Type:** string

### since_date_created

Restrict results to lists created after the set date.

**Type:** string

</details>

## list_members_click_details_for_campaign

Get information about list members who clicked on a specific link in a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### link_id (required)

The id for the link.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_members_in_list

Get information about members in a specific MailChimp list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### before_last_changed

Restrict results to subscribers whose information changed before the set timeframe.

**Type:** string

### before_timestamp_opt

Restrict results to subscribers who opted-in before the set timeframe.

**Type:** string

### email_type

The email type.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### interest_category_id

The unique id for the interest category.

**Type:** string

### interest_ids

Used to filter list members by interests. Must be accompanied by interest_category_id and interest_match. The value must be a comma separated list of interest ids present for the given interest category.

**Type:** string

### interest_match

Used to filter list members by interests. Must be accompanied by interest_category_id and interest_ids. "any" will match a member with any of the interest supplied, "all" will only match members with every interest supplied, and "none" will match members without any of the interest supplied.

**Type:** string

**Potential values:** any, all, none

### since_last_changed

Restrict results to subscribers whose information changed after the set timeframe.

**Type:** string

### since_timestamp_opt

Restrict results to subscribers who opted-in after the set timeframe.

**Type:** string

### status

The subscriber's status.

**Type:** string

### unique_email_id

A unique identifier for the email address across all MailChimp lists. This parameter can be found in any links with [Ecommerce Tracking](http://kb.mailchimp.com/integrations/e-commerce/how-to-use-mailchimp-for-e-commerce?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) enabled.

**Type:** string

### vip_only

A filter to return only the list's VIP members. Passing `true` will restrict results to VIP list members, passing `false` will return all list members.

**Type:** boolean

</details>

## list_members_in_segment_of_list

Get information about members in a [saved segment](http://kb.mailchimp.com/segments/how-to-use-saved-segments?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_merge_fields_for_list

Get a list of all merge fields (formerly merge vars) for a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### required

The boolean value if the merge field is required.

**Type:** boolean

### type

The merge field type.

**Type:** string

</details>

## list_messages_in_conversation

Get messages from a specific conversation.

<details><summary>Parameters</summary>

### conversation_id (required)

The unique id for the conversation.

**Type:** string

### before_timestamp

Restrict the response to messages created before the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### is_read

Whether a conversation message has been marked as read.

**Type:** string

**Potential values:** true, false

### since_timestamp

Restrict the response to messages created after the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

</details>

## list_notes_for_member_in_list

Get recent notes for a specific list member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_orders_for_store

Get information about a store's orders.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### campaign_id

Restrict results to orders with a specific `campaign_id` value.

**Type:** string

### customer_id

Restrict results to orders made by a specific customer.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_products_for_store

Get information about a store's products.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_queued_subscribers_for_email_workflow

Get information about an Automation email queue.

<details><summary>Parameters</summary>

### workflow_email_id (required)

The unique id for the Automation workflow email.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## list_recipients_of_campaign

Get information about campaign recipients.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_removed_subscribers_from_workflow

Get information about subscribers who were [removed from an Automation workflow](http://kb.mailchimp.com/automation/add-or-remove-subscribers-from-automation-workflow?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## list_reports_for_campaign

Get campaign reports.

<details><summary>Parameters</summary>

### before_send_time

Restrict the response to campaigns sent before the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### since_send_time

Restrict the response to campaigns sent after the set time. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.

**Type:** date-time

### type

The campaign type.

**Type:** string

**Potential values:** regular, plaintext, absplit, rss, variate

</details>

## list_segments_for_list

Get information about all available segments for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### before_created_at

Restrict results to segments created before the set time.

**Type:** string

### before_updated_at

Restrict results to segments update before the set time.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### since_created_at

Restrict results to segments created after the set time.

**Type:** string

### since_updated_at

Restrict results to segments update after the set time.

**Type:** string

### type

Limit results based on segment type.

**Type:** string

</details>

## list_signup_forms_for_list

Get signup forms for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

</details>

## list_stores

Get information about all stores in the account.

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_subreports_for_campaign

Get a list of reports with child campaigns for a specific parent campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_template_folders

Get all folders used to organize templates.

<details><summary>Parameters</summary>

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_templates

Get a list of an account's available templates.

<details><summary>Parameters</summary>

### before_created_at

Restrict the response to templates created before the set date.

**Type:** string

### created_by

The MailChimp account user who created the template.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### folder_id

The unique folder id.

**Type:** string

### since_created_at

Restrict the response to templates created after the set date.

**Type:** string

### type

Limit results based on template type.

**Type:** string

</details>

## list_top_email_clients

Get a list of the top email clients based on user-agent strings.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_top_open_locations_for_campaign

Get top open locations for a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_twitter_lead_gen_cards_for_list

Get information about all Twitter Lead Generation Cards for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

</details>

## list_unsubscribed_members_from_list

Get information about members who have unsubscribed from a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_variants_for_product_in_store

Get information about a product's variants.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## list_webhooks_for_list

Get information about all webhooks for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

</details>

## patch_customer_in_store

Update a customer.

<details><summary>Parameters</summary>

### customer_id (required)

The id for the customer of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific customer. Orders for existing customers should include only the `id` parameter in the `customer` object body.

**Type:** object

```json
{
  "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
  "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
  "email_address" : "The customer's email address.",
  "address" : {
    "country" : "The customer's country.",
    "country_code" : "The two-letter code for the customer's country.",
    "province" : "The customer's state name or normalized province.",
    "address2" : "An additional field for the customer's mailing address.",
    "city" : "The city the customer is located in.",
    "address1" : "The mailing address of the customer.",
    "province_code" : "The two-letter code for the customer's province or state.",
    "postal_code" : "The customer's postal or zip code."
  },
  "last_name" : "The customer's last name.",
  "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
  "company" : "The customer's company.",
  "first_name" : "The customer's first name."
}
```

</details>

## patch_member_in_list

Update information for a specific list member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### $body

Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed.

**Type:** object

```json
{
  "email_address" : "Email address for a subscriber.",
  "email_type" : "Type of email this member asked to get ('html' or 'text').",
  "timestamp_opt" : "The date and time the subscribe confirmed their opt-in status.",
  "merge_fields" : { },
  "timestamp_signup" : "The date and time the subscriber signed up for the list.",
  "ip_opt" : "The IP address the subscriber used to confirm their opt-in status.",
  "language" : "If set/detected, the [subscriber's language](http://kb.mailchimp.com/lists/managing-subscribers/view-and-edit-subscriber-languages?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
  "location" : {
    "latitude" : "The location latitude.",
    "longitude" : "The location longitude."
  },
  "ip_signup" : "IP address the subscriber signed up from.",
  "interests" : "The key of this object's properties is the ID of the interest in question.",
  "vip" : "[VIP status](http://kb.mailchimp.com/lists/managing-subscribers/designate-and-send-to-vip-subscribers?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for subscriber.",
  "status" : "Subscriber's current status."
}
```

</details>

## patch_variant_for_product_in_store

Update a product variant.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### variant_id (required)

The id for the product variant.

**Type:** string

### $body

Information about a specific product variant.

**Type:** object

```json
{
  "inventory_quantity" : "The inventory quantity of a product variant.",
  "visibility" : "The visibility of a product variant.",
  "backorders" : "The backorders of a product variant.",
  "price" : "The price of a product variant.",
  "image_url" : "The image URL for a product variant.",
  "title" : "The title of a product variant.",
  "sku" : "The stock keeping unit (SKU) of a product variant.",
  "url" : "The URL for a product variant."
}
```

</details>

## pause_automated_email

Pause an automated email.

<details><summary>Parameters</summary>

### workflow_email_id (required)

The unique id for the Automation workflow email.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## pause_emails_in_email_workflow

Pause all emails in a specific Automation workflow.

<details><summary>Parameters</summary>

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## post_campaigns_id_actions_resume

[Resume an RSS-Driven campaign](http://kb.mailchimp.com/campaigns/rss-in-campaigns/pause-or-reactivate-an-rss-driven-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## post_file_manager_folders

Create a new folder in the File Manager.

<details><summary>Parameters</summary>

### $body

An individual folder listed in the File Manager.

**Type:** object

```json
{
  "name" : "The name of the folder."
}
```

</details>

## post_message_to_conversation

Post a new message to a conversation.

<details><summary>Parameters</summary>

### conversation_id (required)

The unique id for the conversation.

**Type:** string

### $body

An individual message in a conversation. Conversation tracking is a feature available to paid accounts that lets you view replies to your campaigns in your MailChimp account.

**Type:** object

```json
{
  "from_email" : "A label representing the email of the sender of this message",
  "read" : "Whether this message has been marked as read",
  "subject" : "The subject of this message",
  "message" : "The plain-text content of the message"
}
```

</details>

## puase_campaign

[Pause an RSS-Driven campaign](http://kb.mailchimp.com/campaigns/rss-in-campaigns/pause-or-reactivate-an-rss-driven-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## replicate_campaign

[Replicate a campaign](http://kb.mailchimp.com/campaigns/ways-to-build/replicate-a-campaign-or-automation-workflow?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in saved or send status.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## schedule_campaign

[Schedule a campaign](http://kb.mailchimp.com/campaigns/confirmation-and-sending/schedule-pause-or-send-a-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for delivery. If you're using [Multivariate Campaigns](http://kb.mailchimp.com/campaigns/multivariate/about-multivariate-campaigns?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to test send times or sending [RSS Campaigns](http://kb.mailchimp.com/campaigns/rss-in-campaigns/create-an-rss-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs), use the [send](http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/#action-post_campaigns_campaign_id_actions_send) action instead.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### $body

**Type:** object

```json
{
  "schedule_time" : "The date and time in UTC to schedule the campaign for delivery. Campaigns may only be scheduled to send on the quarter-hour (:00, :15, :30, :45).",
  "batch_delivery" : {
    "batch_delay" : "The delay, in minutes, between batches.",
    "batch_count" : "The number of batches for the campaign send."
  },
  "timewarp" : "Choose whether the campaign should use [Timewarp](http://kb.mailchimp.com/campaigns/confirmation-and-sending/use-timewarp-to-optimize-sending-by-time-zone?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) when sending. Campaigns scheduled with Timewarp are localized based on the recipients' time zones. For example, a Timewarp campaign with a `schedule_time` of 13:00 will be sent to each recipient at 1:00pm in their local time. Cannot be set to `true` for campaigns using [Batch Delivery](http://kb.mailchimp.com/campaigns/confirmation-and-sending/schedule-batch-delivery?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs)."
}
```

</details>

## search_campaigns

Search all campaigns for the specified query terms.

<details><summary>Parameters</summary>

### query (required)

The search query used to filter results.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

</details>

## search_members_in_list

Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.

<details><summary>Parameters</summary>

### query (required)

The search query used to filter results.

**Type:** string

### exclude_fields

A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### fields

A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

**Type:** array

```json
[ "string" ]
```

### list_id

The unique id for the list.

**Type:** string

</details>

## send_campaign

Send a MailChimp campaign. For [RSS Campaigns](http://kb.mailchimp.com/campaigns/rss-in-campaigns/create-an-rss-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs), the campaign will send according to its schedule. All other campaigns will send immediately.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## send_test_email_for_campaign

Send a [test email](http://kb.mailchimp.com/campaigns/previews-and-tests/preview-and-test-your-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### $body

**Type:** object

```json
{
  "test_emails" : [ "string" ],
  "send_type" : "Choose the type of test email to send."
}
```

</details>

## set_content_for_campaign

Set the content for a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### $body

The HTML and plain-text content for a campaign

**Type:** object

```json
{
  "template" : {
    "id" : "The id of the template to use.",
    "sections" : { }
  },
  "plain_text" : "The plain-text portion of the campaign. If left unspecified, we'll generate this automatically.",
  "variate_contents" : [ {
    "content_label" : "The label used to identify the content option.",
    "template" : {
      "id" : "The id of the template to use.",
      "sections" : { }
    },
    "plain_text" : "The plain-text portion of the campaign. If left unspecified, we'll generate this automatically.",
    "html" : "The raw HTML for the campaign.",
    "archive" : {
      "archive_content" : "The base64-encoded representation of the archive file.",
      "archive_type" : "The type of encoded file. Defaults to zip."
    },
    "url" : "When importing a campaign, the URL for the HTML."
  } ],
  "html" : "The raw HTML for the campaign.",
  "archive" : {
    "archive_content" : "The base64-encoded representation of the archive file.",
    "archive_type" : "The type of encoded file. Defaults to zip."
  },
  "url" : "When importing a campaign, the URL where the HTML lives."
}
```

</details>

## start_all_emails_in_email_workflow

Start all emails in an Automation workflow.

<details><summary>Parameters</summary>

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## start_batch_operation

Begin processing a batch operations request.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "operations" : [ {
    "path" : "The relative path to use for the operation.",
    "method" : "The HTTP method to use for the operation.",
    "operation_id" : "An optional client-supplied id returned with the operation results.",
    "params" : { },
    "body" : "A string containing the JSON body to use with the request."
  } ]
}
```

</details>

## start_email_workflow

Start an automated email.

<details><summary>Parameters</summary>

### workflow_email_id (required)

The unique id for the Automation workflow email.

**Type:** string

### workflow_id (required)

The unique id for the Automation workflow.

**Type:** string

</details>

## unschedule_campaign

[Unschedule](http://kb.mailchimp.com/campaigns/confirmation-and-sending/schedule-pause-or-send-a-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Pause-a-Scheduled-Campaign) a scheduled campaign that hasn't started sending.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

</details>

## update_campaign

Update some or all of the settings for a specific campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### $body

A summary of an individual campaign's settings and content.

**Type:** object

```json
{
  "settings" : {
    "auto_footer" : "Automatically append MailChimp's [default footer](http://kb.mailchimp.com/campaigns/design/theres-a-gray-footer-added-to-my-campaign?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to the campaign.",
    "subject_line" : "The subject line for the campaign.",
    "use_conversation" : "Use MailChimp Conversation feature to manage out-of-office replies.",
    "authenticate" : "Whether MailChimp [authenticated](http://kb.mailchimp.com/delivery/deliverability-research/set-up-mailchimp-authentication?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) the campaign. Defaults to `true`.",
    "to_name" : "The campaign's custom 'To' name. Typically the first name [merge field](http://kb.mailchimp.com/merge-tags/using/getting-started-with-merge-tags?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
    "title" : "The title of the campaign.",
    "from_name" : "The 'from' name on the campaign (not an email address).",
    "auto_tweet" : "Automatically tweet a link to the [campaign archive](http://kb.mailchimp.com/campaigns/archives/set-up-your-campaign-archive?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) page when the campaign is sent.",
    "auto_fb_post" : [ "string" ],
    "fb_comments" : "Allows Facebook comments on the campaign (also force-enables the Campaign Archive toolbar). Defaults to `true`.",
    "reply_to" : "The reply-to email address for the campaign.",
    "inline_css" : "Automatically inline the CSS included with the campaign content.",
    "folder_id" : "If the campaign is listed in a folder, the id for that folder."
  },
  "variate_settings" : {
    "send_times" : [ "date-time" ],
    "combinations" : [ {
      "subject_line" : "The index of `variate_settings.subject_lines` used.",
      "send_time" : "The index of `variate_settings.send_times` used.",
      "reply_to" : "The index of `variate_settings.reply_to_addresses` used.",
      "recipients" : "The number of recipients for this combination.",
      "id" : "Unique ID for the combination.",
      "from_name" : "The index of `variate_settings.from_names` used.",
      "content_description" : "The index of `variate_settings.contents` used."
    } ],
    "wait_time" : "The number of minutes to wait before choosing the winning campaign. The value of wait_time must be greater than 0 and in whole hours, specified in minutes.",
    "subject_lines" : [ "string" ],
    "test_size" : "The percentage of recipients to send the test combinations to, must be a value between 10 and 100.",
    "reply_to_addresses" : [ "string" ],
    "winner_criteria" : "The combination that performs the best. This may be determined automatically by click rate, open rate, or total revenue—or you may choose manually based on the reporting data you find the most valuable. For Multivariate Campaigns testing send_time, winner_criteria is ignored. For Multivariate Campaigns with 'manual' as the winner_criteria, the winner must be chosen in the MailChimp web application.",
    "from_names" : [ "string" ]
  },
  "ab_split_opts" : {
    "pick_winner" : "How we should evaluate a winner. Based on 'opens', 'clicks', or 'manual'.",
    "wait_time" : "The amount of time to wait before picking a winner. This cannot be changed after a campaign is sent.",
    "wait_units" : "How unit of time for measuring the winner ('hours' or 'days'). This cannot be changed after a campaign is sent.",
    "subject_b" : "For campaigns split on 'Subject Line', the subject line for Group B.",
    "subject_a" : "For campaigns split on 'Subject Line', the subject line for Group A.",
    "split_test" : "The type of AB split to run.",
    "from_name_a" : "For campaigns split on 'From Name', the name for Group A.",
    "from_name_b" : "For campaigns split on 'From Name', the name for Group B.",
    "send_time_winner" : "The send time for the winning version.",
    "reply_email_b" : "For campaigns split on 'From Name', the reply-to address for Group B.",
    "reply_email_a" : "For campaigns split on 'From Name', the reply-to address for Group A.",
    "send_time_a" : "The send time for Group A.",
    "send_time_b" : "The send time for Group B.",
    "split_size" : "The size of the split groups. Campaigns split based on 'schedule' are forced to have a 50/50 split. Valid split integers are between 1-50."
  },
  "rss_opts" : {
    "schedule" : {
      "hour" : "The hour to send the campaign in local time. Acceptable hours are 0-23. For example, '4' would be 4am in [your account's default time zone](http://kb.mailchimp.com/accounts/account-setup/how-to-set-account-defaults?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
      "weekly_send_day" : "The day of the week to send a weekly RSS Campaign.",
      "daily_send" : {
        "sunday" : "Sends the daily RSS Campaign on Sundays.",
        "saturday" : "Sends the daily RSS Campaign on Saturdays.",
        "tuesday" : "Sends the daily RSS Campaign on Tuesdays.",
        "wednesday" : "Sends the daily RSS Campaign on Wednesdays.",
        "thursday" : "Sends the daily RSS Campaign on Thursdays.",
        "friday" : "Sends the daily RSS Campaign on Fridays.",
        "monday" : "Sends the daily RSS Campaign on Mondays."
      },
      "monthly_send_date" : "The day of the month to send a monthly RSS Campaign. Acceptable days are 0-31, where '0' is always the last day of a month. Months with fewer than the selected number of days will not have an RSS campaign sent out that day. For example, RSS Campaigns set to send on the 30th will not go out in February."
    },
    "constrain_rss_img" : "Whether to add CSS to images in the RSS feed to constrain their width in campaigns.",
    "feed_url" : "The URL for the RSS feed.",
    "frequency" : "The frequency of the RSS Campaign."
  },
  "social_card" : {
    "image_url" : "The url for the header image for the card.",
    "description" : "A short summary of the campaign to display.",
    "title" : "The title for the card. Typically the subject line of the campaign."
  },
  "recipients" : {
    "segment_opts" : {
      "match" : "Segment match type.",
      "saved_segment_id" : "The id for an existing saved segment.",
      "conditions" : [ {
        "op" : "The segment operator.",
        "field" : "The field to segment on.",
        "condition_type" : "The type of segment, for example: date, language, Mandrill, static, and more."
      } ]
    },
    "list_id" : "The unique list id."
  },
  "tracking" : {
    "salesforce" : {
      "notes" : "Update contact notes for a campaign based on subscriber email addresses.",
      "campaign" : "Create a campaign in a connected Salesforce account."
    },
    "highrise" : {
      "notes" : "Update contact notes for a campaign based on subscriber email addresses.",
      "campaign" : "Create a campaign in a connected Highrise account."
    },
    "goal_tracking" : "Whether to enable [Goal](http://kb.mailchimp.com/integrations/other-integrations/integrate-goal-with-mailchimp?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) tracking.",
    "capsule" : {
      "notes" : "Update contact notes for a campaign based on subscriber email addresses."
    },
    "clicktale" : "The custom slug for [ClickTale](http://kb.mailchimp.com/integrations/other-integrations/additional-tracking-options-for-campaigns?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Click-Tale) tracking (max of 50 bytes).",
    "text_clicks" : "Whether to [track clicks](http://kb.mailchimp.com/reports/about-click-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in the plain-text version of the campaign. Defaults to `true`. Cannot be set to false for variate campaigns.",
    "ecomm360" : "Whether to enable [eCommerce360](http://kb.mailchimp.com/integrations/other-integrations/about-ecommerce360?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) tracking.",
    "opens" : "Whether to [track opens](http://kb.mailchimp.com/reports/about-open-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs). Defaults to `true`. Cannot be set to false for variate campaigns.",
    "google_analytics" : "The custom slug for [Google Analytics](http://kb.mailchimp.com/integrations/other-integrations/integrate-google-analytics-with-mailchimp?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) tracking (max of 50 bytes).",
    "html_clicks" : "Whether to [track clicks](http://kb.mailchimp.com/reports/about-click-tracking?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in the HTML version of the campaign. Defaults to `true`. Cannot be set to false for variate campaigns."
  }
}
```

</details>

## update_campaign_folder

Update a specific folder used to organize campaigns.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

### $body

A folder used to organize campaigns.

**Type:** object

```json
{
  "name" : "Name to associate with the folder."
}
```

</details>

## update_cart_in_store

Update a specific cart.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific cart.

**Type:** object

```json
{
  "checkout_url" : "The URL for the cart. This parameter is required for [Abandoned Cart](http://kb.mailchimp.com/automation/create-an-abandoned-cart-email) automations.",
  "tax_total" : "The total tax for the cart.",
  "order_total" : "The order total for the cart.",
  "lines" : [ {
    "quantity" : "The quantity of a cart line item.",
    "price" : "The price of a cart line item.",
    "product_id" : "A unique identifier for the product associated with the cart line item.",
    "product_variant_id" : "A unique identifier for the product variant associated with the cart line item."
  } ],
  "campaign_id" : "A string that uniquely identifies the campaign associated with a cart.",
  "currency_code" : "The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code for the currency that the cart uses.",
  "customer" : {
    "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "email_address" : "The customer's email address.",
    "address" : {
      "country" : "The customer's country.",
      "country_code" : "The two-letter code for the customer's country.",
      "province" : "The customer's state name or normalized province.",
      "address2" : "An additional field for the customer's mailing address.",
      "city" : "The city the customer is located in.",
      "address1" : "The mailing address of the customer.",
      "province_code" : "The two-letter code for the customer's province or state.",
      "postal_code" : "The customer's postal or zip code."
    },
    "last_name" : "The customer's last name.",
    "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
    "company" : "The customer's company.",
    "first_name" : "The customer's first name."
  }
}
```

</details>

## update_customer_in_store

Add or update a customer.

<details><summary>Parameters</summary>

### customer_id (required)

The id for the customer of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific customer. Orders for existing customers should include only the `id` parameter in the `customer` object body.

**Type:** object

```json
{
  "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
  "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
  "email_address" : "The customer's email address.",
  "address" : {
    "country" : "The customer's country.",
    "country_code" : "The two-letter code for the customer's country.",
    "province" : "The customer's state name or normalized province.",
    "address2" : "An additional field for the customer's mailing address.",
    "city" : "The city the customer is located in.",
    "address1" : "The mailing address of the customer.",
    "province_code" : "The two-letter code for the customer's province or state.",
    "postal_code" : "The customer's postal or zip code."
  },
  "last_name" : "The customer's last name.",
  "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
  "company" : "The customer's company.",
  "id" : "A unique identifier for the customer.",
  "first_name" : "The customer's first name."
}
```

</details>

## update_feedback_message_for_campaign

Update a specific feedback message for a campaign.

<details><summary>Parameters</summary>

### campaign_id (required)

The unique id for the campaign.

**Type:** string

### feedback_id (required)

The unique id for the feedback message.

**Type:** string

### $body

A specific feedback message from a specific campaign.

**Type:** object

```json
{
  "is_complete" : "The status of feedback.",
  "message" : "The content of the feedback.",
  "block_id" : "The block id for the editable block that the feedback addresses."
}
```

</details>

## update_file_in_file_manager

Update a file in the File Manager.

<details><summary>Parameters</summary>

### file_id (required)

The unique id for the File Manager file.

**Type:** string

### $body

An individual file listed in the File Manager.

**Type:** object

```json
{
  "name" : "The name of the file.",
  "folder_id" : "The id of the folder.",
  "file_data" : "The base64-encoded contents of the file."
}
```

</details>

## update_folder_in_file_manager

Update a specific File Manager folder.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

### $body

An individual folder listed in the File Manager.

**Type:** object

```json
{
  "name" : "The name of the folder."
}
```

</details>

## update_interest_category_for_list

Update a specific interest category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Interest categories organize interests, which are used to group subscribers based on their preferences. These correspond to Group Titles the application.

**Type:** object

```json
{
  "display_order" : "The order that the categories are displayed in the list. Lower numbers display first.",
  "title" : "The text description of this category. This field appears on signup forms and is often phrased as a question.",
  "type" : "Determines how this category’s interests appear on signup forms."
}
```

</details>

## update_interests_for_interest_category_in_list

Update interests or 'group names' for a specific category.

<details><summary>Parameters</summary>

### interest_category_id (required)

The unique id for the interest category.

**Type:** string

### interest_id (required)

The specific interest or 'group name'.

**Type:** string

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Assign subscribers to interests to group them together. Interests are referred to as 'group names' in the MailChimp application.

**Type:** object

```json
{
  "name" : "The name of the interest. This can be shown publicly on a subscription form.",
  "display_order" : "The display order for interests."
}
```

</details>

## update_line_item_for_order_in_store

Update a specific order line item.

<details><summary>Parameters</summary>

### line_id (required)

The id for the line item.

**Type:** string

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific order line.

**Type:** object

```json
{
  "quantity" : "The quantity of an order line item.",
  "price" : "The price of an order line item.",
  "product_id" : "A unique identifier for the product associated with the order line item.",
  "product_variant_id" : "A unique identifier for the product variant associated with the order line item."
}
```

</details>

## update_line_item_in_cart

Update a specific cart line item.

<details><summary>Parameters</summary>

### cart_id (required)

The id for the cart.

**Type:** string

### line_id (required)

The id for the line item.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific cart line item.

**Type:** object

```json
{
  "quantity" : "The quantity of a cart line item.",
  "price" : "The price of a cart line item.",
  "product_id" : "A unique identifier for the product associated with the cart line item.",
  "product_variant_id" : "A unique identifier for the product variant associated with the cart line item."
}
```

</details>

## update_list

Update the settings for a specific list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### $body

Information about a specific list.

**Type:** object

```json
{
  "notify_on_subscribe" : "The email address to send [subscribe notifications](http://kb.mailchimp.com/lists/managing-subscribers/change-subscribe-and-unsubscribe-notifications?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to.",
  "email_type_option" : "Whether the list supports [multiple formats for emails](http://kb.mailchimp.com/lists/growth/how-to-change-list-name-and-defaults?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs#Change-Subscription-Settings). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.",
  "permission_reminder" : "The [permission reminder](http://kb.mailchimp.com/accounts/compliance-tips/edit-the-permission-reminder?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for the list.",
  "use_archive_bar" : "Whether campaigns for this list use the [Archive Bar](http://kb.mailchimp.com/campaigns/archives/about-the-archive-bar?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in archives by default.",
  "notify_on_unsubscribe" : "The email address to send [unsubscribe notifications](http://kb.mailchimp.com/lists/managing-subscribers/change-subscribe-and-unsubscribe-notifications?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) to.",
  "visibility" : "Whether this list is [public or private](http://kb.mailchimp.com/lists/growth/about-publicity-settings?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
  "contact" : {
    "zip" : "The postal or zip code for the list contact.",
    "country" : "A two-character ISO3166 country code. Defaults to US if invalid.",
    "address2" : "The street address for the list contact.",
    "city" : "The city for the list contact.",
    "phone" : "The phone number for the list contact.",
    "address1" : "The street address for the list contact.",
    "company" : "The company name for the list.",
    "state" : "The state for the list contact."
  },
  "name" : "The name of the list.",
  "campaign_defaults" : {
    "from_email" : "The default from email for campaigns sent to this list.",
    "subject" : "The default subject line for campaigns sent to this list.",
    "language" : "The default language for this lists's forms.",
    "from_name" : "The default from name for campaigns sent to this list."
  }
}
```

</details>

## update_member_in_list

Add or update a list member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### $body

Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed.

**Type:** object

```json
{
  "email_type" : "Type of email this member asked to get ('html' or 'text').",
  "timestamp_opt" : "The date and time the subscribe confirmed their opt-in status.",
  "merge_fields" : { },
  "timestamp_signup" : "The date and time the subscriber signed up for the list.",
  "language" : "If set/detected, the [subscriber's language](http://kb.mailchimp.com/lists/managing-subscribers/view-and-edit-subscriber-languages?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs).",
  "ip_signup" : "IP address the subscriber signed up from.",
  "email_address" : "Email address for a subscriber. This value is required only if the email address is not already present on the list.",
  "status_if_new" : "Subscriber's status. This value is required only if the email address is not already present on the list.",
  "ip_opt" : "The IP address the subscriber used to confirm their opt-in status.",
  "location" : {
    "latitude" : "The location latitude.",
    "longitude" : "The location longitude."
  },
  "interests" : "The key of this object's properties is the ID of the interest in question.",
  "vip" : "[VIP status](http://kb.mailchimp.com/lists/managing-subscribers/designate-and-send-to-vip-subscribers?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) for subscriber.",
  "status" : "Subscriber's current status."
}
```

</details>

## update_merge_field_in_list

Update a specific merge field in a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### merge_id (required)

The id for the merge field.

**Type:** string

### $body

A merge field (formerly merge vars) for a specific list. These correspond to merge fields in MailChimp's lists and subscriber profiles.

**Type:** object

```json
{
  "public" : "Whether the merge field is displayed on the signup form.",
  "name" : "The name of the merge field.",
  "display_order" : "The order that the merge field displays on the list signup form.",
  "options" : {
    "date_format" : "In a date or birthday field, the format of the date.",
    "choices" : [ "string" ],
    "default_country" : "In an address field, the default country code if none supplied.",
    "phone_format" : "In a phone field, the phone number type: US or International."
  },
  "default_value" : "The default value for the merge field if `null`.",
  "tag" : "The tag used in MailChimp campaigns and for the /members endpoint.",
  "required" : "The boolean value if the merge field is required.",
  "help_text" : "Extra text to help the subscriber fill out the form."
}
```

</details>

## update_note_for_member_in_list

Update a specific note for a specific list member.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### note_id (required)

The id for the note.

**Type:** string

### subscriber_hash (required)

The MD5 hash of the lowercase version of the list member's email address.

**Type:** string

### $body

A specific note for a specific member.

**Type:** object

```json
{
  "email_id" : "The MD5 hash of the lowercase version of the list member's email address.",
  "note" : "The content of the note.",
  "updated_at" : "The date and time the note was last updated.",
  "list_id" : "The unique id for the list.",
  "created_at" : "The date and time the note was created.",
  "id" : "The note id.",
  "created_by" : "The author of the note."
}
```

</details>

## update_order_in_store

Update a specific order.

<details><summary>Parameters</summary>

### order_id (required)

The id for the order in a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific order.

**Type:** object

```json
{
  "fulfillment_status" : "The fulfillment status for the order. For example: `partial`, `fulfilled`, etc.",
  "tax_total" : "The tax total associated with an order.",
  "shipping_total" : "The shipping total for the order.",
  "processed_at_foreign" : "The date and time the order was processed.",
  "billing_address" : {
    "country" : "The country in the billing address.",
    "address2" : "An additional field for the billing address.",
    "city" : "The city in the billing address.",
    "address1" : "The billing address for the order.",
    "latitude" : "The latitude for the billing address location.",
    "province_code" : "The two-letter code for the province or state in the billing address.",
    "country_code" : "The two-letter code for the country in the billing address.",
    "province" : "The state or normalized province in the billing address.",
    "phone" : "The phone number for the billing address.",
    "name" : "The name associated with an order's billing address.",
    "company" : "The company associated with the billing address.",
    "postal_code" : "The postal or zip code in the billing address.",
    "longitude" : "The longitude for the billing address location."
  },
  "tracking_code" : "The MailChimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.",
  "currency_code" : "The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code for the currency that the store accepts.",
  "landing_site" : "The URL for the page where the buyer landed when entering the shop.",
  "financial_status" : "The order status. For example: `refunded`, `processing`, `cancelled`, etc.",
  "order_total" : "The order total associated with an order.",
  "id" : "A unique identifier for the order.",
  "shipping_address" : {
    "country" : "The country in the order's shipping address.",
    "address2" : "An additional field for the shipping address.",
    "city" : "The city in the order's shipping address.",
    "address1" : "The shipping address for the order.",
    "latitude" : "The latitude for the shipping address location.",
    "province_code" : "The two-letter code for the province or state the order's shipping address is located in.",
    "country_code" : "The two-letter code for the country in the shipping address.",
    "province" : "The state or normalized province in the order's shipping address.",
    "phone" : "The phone number for the order's shipping address",
    "name" : "The name associated with an order's shipping address.",
    "company" : "The company associated with an order's shipping address.",
    "postal_code" : "The postal or zip code in the order's shipping address.",
    "longitude" : "The longitude for the shipping address location."
  },
  "updated_at_foreign" : "The date and time the order was updated.",
  "lines" : [ {
    "quantity" : "The quantity of an order line item.",
    "price" : "The price of an order line item.",
    "product_id" : "A unique identifier for the product associated with the order line item.",
    "product_variant_id" : "A unique identifier for the product variant associated with the order line item."
  } ],
  "campaign_id" : "A string that uniquely identifies the campaign associated with an order.",
  "customer" : {
    "total_spent" : "The total amount the customer has spent. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "orders_count" : "The customer's total order count. [Learn More](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#orders_count-and-total_spent) about using this data.",
    "email_address" : "The customer's email address.",
    "address" : {
      "country" : "The customer's country.",
      "country_code" : "The two-letter code for the customer's country.",
      "province" : "The customer's state name or normalized province.",
      "address2" : "An additional field for the customer's mailing address.",
      "city" : "The city the customer is located in.",
      "address1" : "The mailing address of the customer.",
      "province_code" : "The two-letter code for the customer's province or state.",
      "postal_code" : "The customer's postal or zip code."
    },
    "last_name" : "The customer's last name.",
    "opt_in_status" : "The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing MailChimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your MailChimp list [will be added as `Transactional` members](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#about-subscribers-and-customers).",
    "company" : "The customer's company.",
    "first_name" : "The customer's first name."
  },
  "cancelled_at_foreign" : "The date and time the order was cancelled."
}
```

</details>

## update_product_in_store

Update a specific product.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### $body

Information about a specific product.

**Type:** object

```json
{
  "vendor" : "The vendor for a product.",
  "image_url" : "The image URL for a product.",
  "description" : "The description of a product.",
  "handle" : "The handle of a product.",
  "published_at_foreign" : "The date and time the product was published.",
  "variants" : [ {
    "inventory_quantity" : "The inventory quantity of a product variant.",
    "visibility" : "The visibility of a product variant.",
    "backorders" : "The backorders of a product variant.",
    "price" : "The price of a product variant.",
    "image_url" : "The image URL for a product variant.",
    "title" : "The title of a product variant.",
    "sku" : "The stock keeping unit (SKU) of a product variant.",
    "url" : "The URL for a product variant."
  } ],
  "title" : "The title of a product.",
  "type" : "The type of product.",
  "url" : "The URL for a product."
}
```

</details>

## update_segment_for_list

Update a specific segment in a list.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### segment_id (required)

The unique id for the segment.

**Type:** string

### $body

Information about a specific list segment.

**Type:** object

```json
{
  "name" : "The name of the segment.",
  "options" : {
    "match" : "Match type.",
    "conditions" : [ {
      "op" : "The segment operator.",
      "field" : "The field to segment on.",
      "condition_type" : "The type of segment, for example: date, language, Mandrill, static, and more."
    } ]
  },
  "static_segment" : [ "string" ]
}
```

</details>

## update_store

Update a store.

<details><summary>Parameters</summary>

### store_id (required)

The store id.

**Type:** string

### $body

An individual store in an account.

**Type:** object

```json
{
  "is_syncing" : "Whether the e-commerce store is currently [syncing](http://developer.mailchimp.com/documentation/mailchimp/guides/getting-started-with-ecommerce/#syncing-an-e-commerce-store).",
  "address" : {
    "country" : "The store's country.",
    "country_code" : "The two-letter code for to the store's country.",
    "province" : "The store's state name or normalized province.",
    "address2" : "An additional field for the store's mailing address.",
    "city" : "The city the store is located in.",
    "address1" : "The store's mailing address.",
    "latitude" : "The latitude of the store location.",
    "province_code" : "The two-letter code for the store's province or state.",
    "postal_code" : "The store's postal or zip code.",
    "longitude" : "The longitude of the store location."
  },
  "list_id" : "The unique identifier for the [MailChimp List](http://developer.mailchimp.com/documentation/mailchimp/reference/lists/) that's associated with the store. The `list_id` for a specific store can't change.",
  "timezone" : "The timezone for the store.",
  "primary_locale" : "The primary locale for the store. For example: `en`, `de`, etc.",
  "platform" : "The e-commerce platform of the store.",
  "currency_code" : "The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code for the currency that the store accepts.",
  "money_format" : "The currency format for the store. For example: `$`, `£`, etc.",
  "email_address" : "The email address for the store.",
  "phone" : "The store phone number.",
  "domain" : "The store domain.",
  "name" : "The name of the store.",
  "id" : "The unique identifier for the store."
}
```

</details>

## update_template

Update the name, HTML, or `folder_id` of an existing template.

<details><summary>Parameters</summary>

### template_id (required)

The unique id for the template.

**Type:** string

### $body

Information about a specific template.

**Type:** object

```json
{
  "name" : "The name of the template.",
  "html" : "The raw HTML for the template. We support the MailChimp [Template Language](http://kb.mailchimp.com/templates/code/getting-started-with-mailchimps-template-language?utm_source=mc-api&amp;utm_medium=docs&amp;utm_campaign=apidocs) in any HTML code passed via the API.",
  "folder_id" : "The id of the folder the template is currently in."
}
```

</details>

## update_template_folder

Update a specific folder used to organize templates.

<details><summary>Parameters</summary>

### folder_id (required)

The unique folder id.

**Type:** string

### $body

A folder used to organize templates.

**Type:** object

```json
{
  "name" : "The name of the folder."
}
```

</details>

## update_variant_for_product_in_store

Add or update a product variant.

<details><summary>Parameters</summary>

### product_id (required)

The id for the product of a store.

**Type:** string

### store_id (required)

The store id.

**Type:** string

### variant_id (required)

The id for the product variant.

**Type:** string

### $body

Information about a specific product variant.

**Type:** object

```json
{
  "inventory_quantity" : "The inventory quantity of a product variant.",
  "visibility" : "The visibility of a product variant.",
  "backorders" : "The backorders of a product variant.",
  "price" : "The price of a product variant.",
  "image_url" : "The image URL for a product variant.",
  "id" : "A unique identifier for the product variant.",
  "title" : "The title of a product variant.",
  "sku" : "The stock keeping unit (SKU) of a product variant.",
  "url" : "The URL for a product variant."
}
```

</details>

## update_webhook_for_list

Update the settings for an existing webhook.

<details><summary>Parameters</summary>

### list_id (required)

The unique id for the list.

**Type:** string

### webhook_id (required)

The unique ID for the webhook.

**Type:** string

### $body

Configure a webhook for the given list.

**Type:** object

```json
{
  "sources" : {
    "admin" : "Whether the webhook is triggered by admin-initiated actions in the web interface.",
    "api" : "Whether the webhook is triggered by actions initiated via the API.",
    "user" : "Whether the webhook is triggered by subscriber-initiated actions."
  },
  "url" : "A valid URL for the Webhook.",
  "events" : {
    "subscribe" : "Whether the webhook is triggered when a list subscriber is added.",
    "unsubscribe" : "Whether the webhook is triggered when a list member unsubscribes.",
    "profile" : "Whether the webhook is triggered when a subscriber's profile is updated.",
    "cleaned" : "Whether the webhook is triggered when a subscriber's email address is cleaned from the list.",
    "campaign" : "Whether the webhook is triggered when a campaign is sent or cancelled.",
    "upemail" : "Whether the webhook is triggered when a subscriber's email address is changed."
  }
}
```

</details>

## upload_file_to_file_manager

Upload a new image or file to the File Manager.

<details><summary>Parameters</summary>

### $body

An individual file listed in the File Manager.

**Type:** object

```json
{
  "name" : "The name of the file.",
  "folder_id" : "The id of the folder.",
  "file_data" : "The base64-encoded contents of the file."
}
```

</details>

