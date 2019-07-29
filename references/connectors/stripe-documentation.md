---
id: stripe-documentation
title: Stripe (version v2.*.*)
sidebar_label: Stripe
layout: docs.mustache
---

## cancel_payment_intent

A PaymentIntent object can be canceled when it is in one of these statues: requires_source, requires_capture, requires_confirmation, or requires_source_action. 
Once canceled, no additional charges will be made by the PaymentIntent and any operations on the PaymentIntent will fail with an error. For PaymentIntents with status='requires_capture', the remaining amount_capturable will automatically be refunded.

<details><summary>Parameters</summary>

### intent (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ]
}
```

</details>

## cancel_payout

A previously created payout can be canceled if it has not yet been paid out. Funds will be refunded to your available balance. You may not cancel automatic Stripe payouts.

<details><summary>Parameters</summary>

### payout (required)

The identifier of the payout to be canceled.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ]
}
```

</details>

## cancel_topup

Cancels a top-up. Only pending top-ups can be canceled.

<details><summary>Parameters</summary>

### topup (required)

The ID of the top-up to cancel.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ]
}
```

</details>

## charge_capture

Capture the payment of an existing, uncaptured, charge. This is the second half of the two-step payment flow, where first you created a charge with the capture option set to false.
Uncaptured payments expire exactly seven days after they are created. If they are not captured by that point in time, they will be marked as refunded and will no longer be capturable.

<details><summary>Parameters</summary>

### charge (required)

**Type:** string

### $body

**Type:** object

```json
{
  "statement_descriptor" : "An arbitrary string to be displayed on your customer's credit card statement. This may be up to *22 characters*. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket`. The statement description must contain at least one letter, may not include `&lt;&gt;\"'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. Updating this value will overwrite the previous statement descriptor of this charge. While most banks display this information consistently, some may display it incorrectly or not at all.",
  "amount" : "The amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.",
  "expand" : [ "string" ],
  "transfer_group" : "A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](/docs/connect/charges-transfers#grouping-transactions) for details.",
  "receipt_email" : "The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.",
  "destination" : {
    "amount" : "integer"
  },
  "application_fee" : "An application fee to add on to this charge. Can only be used with Stripe Connect."
}
```

</details>

## close_dispute

Closing the dispute for a charge indicates that you do not have any evidence to submit and are essentially dismissing the dispute, acknowledging it as lost.
The status of the dispute will change from needs_response to lost. Closing a dispute is irreversible.

<details><summary>Parameters</summary>

### dispute (required)

ID of the dispute to close.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ]
}
```

</details>

## create_account

With Connect, you can create Stripe accounts for your users.To do this, you’ll first need to register your platform.
For Standard accounts, parameters other than country, email, and typeare used to prefill the account application that we ask the account holder to complete.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "business_logo" : "(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for this account (at least 128px x 128px)",
  "debit_negative_balances" : "A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](/docs/connect/account-balances).",
  "tos_acceptance" : {
    "date" : "Required integer",
    "ip" : "Required string",
    "user_agent" : "string"
  },
  "country" : "The country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you're creating an account is legally represented in Canada, you would use `CA` as the country for the account being created.",
  "metadata" : { },
  "from_recipient" : "string",
  "payout_schedule" : {
    "weekly_anchor" : "string. Possible values: friday | monday | saturday | sunday | thursday | tuesday | wednesday",
    "interval" : "string. Possible values: daily | four_times_monthly | manual | monthly | weekly",
    "delay_days" : "integer",
    "monthly_anchor" : "integer"
  },
  "support_phone" : "A publicly shareable support phone number for the business.",
  "account_token" : "An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account.",
  "type" : "Whether you'd like to create a [Standard or Custom](/docs/connect/accounts) account. Standard accounts are normal Stripe accounts: Stripe will email the account holder to set up a username and password, and will handle all account management directly with them. Custom accounts have extra parameters available to them, and require that you, the platform, handle all communication with the account holder. Possible values are `standard` and `custom`.",
  "statement_descriptor" : "The default text that appears on credit card statements when a charge is made [directly on the account](/docs/connect/direct-charges)",
  "support_url" : "A publicly shareable URL that provides support for this account.",
  "legal_entity" : {
    "business_vat_id" : "string",
    "personal_address_kana" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "gender" : "string",
    "address_kana" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "type" : "string",
    "personal_address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "address_kanji" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "ssn_last_4" : "string",
    "first_name" : "string",
    "first_name_kana" : "string",
    "personal_id_number" : "string",
    "verification" : {
      "document" : "string"
    },
    "last_name_kanji" : "string",
    "personal_address_kanji" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "business_name" : "string",
    "maiden_name" : "string",
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "business_tax_id" : "string",
    "first_name_kanji" : "string",
    "last_name" : "string",
    "business_name_kana" : "string",
    "tax_id_registrar" : "string",
    "dob" : {
      "month" : "Required integer",
      "year" : "Required integer",
      "day" : "Required integer"
    },
    "additional_owners" : {
      "<string>" : {
        "maiden_name" : "string",
        "address" : {
          "country" : "string",
          "city" : "string",
          "state" : "string",
          "postal_code" : "string",
          "line2" : "string",
          "line1" : "string"
        },
        "dob" : {
          "month" : "Required integer",
          "year" : "Required integer",
          "day" : "Required integer"
        },
        "last_name" : "string",
        "first_name" : "string",
        "personal_id_number" : "string",
        "verification" : {
          "document" : "string"
        }
      }
    },
    "last_name_kana" : "string",
    "business_name_kanji" : "string",
    "phone_number" : "string"
  },
  "business_url" : "The URL that best shows the service or product provided by this account.",
  "product_description" : "Internal-only description of the product sold by, or service provided by, the business. Used by Stripe for risk and underwriting purposes.",
  "email" : "The email address of the account holder. For Standard accounts, Stripe will email your user with instructions on how to set up their account. For Custom accounts, this is only to make the account easier to identify to you: Stripe will never directly email your users.",
  "bank_account" : { },
  "business_name" : "The publicly sharable name for this account.",
  "decline_charge_on" : {
    "avs_failure" : "boolean",
    "cvc_failure" : "boolean"
  },
  "expand" : [ "string" ],
  "support_email" : "A publicly shareable support email address for the business.",
  "external_account" : { },
  "business_primary_color" : "A CSS hex color value representing the primary branding color for this account.",
  "default_currency" : "Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts).",
  "payout_statement_descriptor" : "The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard."
}
```

</details>

## create_bank_account



<details><summary>Parameters</summary>

### account (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "external_account" : { },
  "default_for_currency" : "When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.",
  "bank_account" : { }
}
```

</details>

## create_card_token

Creates a single-use token that represents a bank account’s details.This token can be used in place of a bank account dictionary with any API method.These tokens can be used only once: by attaching them to a recipient or Custom account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "amount" : "integer",
  "payment_user_agent" : "string",
  "ip" : "string",
  "external_id" : "string",
  "pii" : {
    "ssn_last_4" : "string",
    "personal_id_number" : "string",
    "tax_id" : "string"
  },
  "referrer" : "string",
  "validation_type" : "string. Possible values: amount | card | none",
  "expand" : [ "string" ],
  "iovation_blackbox" : "string",
  "recipient" : "string",
  "currency" : "string",
  "request_id" : "string",
  "account" : {
    "tos_shown_and_accepted" : "boolean",
    "legal_entity" : {
      "business_vat_id" : "string",
      "personal_address_kana" : {
        "country" : "string",
        "town" : "string",
        "city" : "string",
        "state" : "string",
        "postal_code" : "string",
        "line2" : "string",
        "line1" : "string"
      },
      "gender" : "string",
      "address_kana" : {
        "country" : "string",
        "town" : "string",
        "city" : "string",
        "state" : "string",
        "postal_code" : "string",
        "line2" : "string",
        "line1" : "string"
      },
      "type" : "string",
      "personal_address" : {
        "country" : "string",
        "city" : "string",
        "state" : "string",
        "postal_code" : "string",
        "line2" : "string",
        "line1" : "string"
      },
      "address_kanji" : {
        "country" : "string",
        "town" : "string",
        "city" : "string",
        "state" : "string",
        "postal_code" : "string",
        "line2" : "string",
        "line1" : "string"
      },
      "ssn_last_4" : "string",
      "first_name" : "string",
      "first_name_kana" : "string",
      "personal_id_number" : "string",
      "verification" : {
        "document" : "string"
      },
      "last_name_kanji" : "string",
      "personal_address_kanji" : {
        "country" : "string",
        "town" : "string",
        "city" : "string",
        "state" : "string",
        "postal_code" : "string",
        "line2" : "string",
        "line1" : "string"
      },
      "business_name" : "string",
      "maiden_name" : "string",
      "address" : {
        "country" : "string",
        "city" : "string",
        "state" : "string",
        "postal_code" : "string",
        "line2" : "string",
        "line1" : "string"
      },
      "business_tax_id" : "string",
      "first_name_kanji" : "string",
      "last_name" : "string",
      "business_name_kana" : "string",
      "tax_id_registrar" : "string",
      "dob" : {
        "month" : "Required integer",
        "year" : "Required integer",
        "day" : "Required integer"
      },
      "additional_owners" : {
        "<string>" : {
          "maiden_name" : "string",
          "address" : {
            "country" : "string",
            "city" : "string",
            "state" : "string",
            "postal_code" : "string",
            "line2" : "string",
            "line1" : "string"
          },
          "dob" : {
            "month" : "Required integer",
            "year" : "Required integer",
            "day" : "Required integer"
          },
          "last_name" : "string",
          "first_name" : "string",
          "personal_id_number" : "string",
          "verification" : {
            "document" : "string"
          }
        }
      },
      "last_name_kana" : "string",
      "business_name_kanji" : "string",
      "phone_number" : "string"
    }
  },
  "card" : {
    "token_cryptogram_currency" : "string",
    "pk_token" : "string",
    "token_cryptogram" : "string",
    "token_cryptogram_requestor" : "string",
    "address_country" : "string",
    "token_cryptogram_used" : "boolean",
    "address_state" : "string",
    "address_city" : "string",
    "address_line2" : "string",
    "address_line1" : "string",
    "token_cryptogram_amount" : "integer",
    "name" : "string",
    "address_zip" : "string",
    "object" : "string. Possible values: card"
  },
  "email" : "string",
  "user_agent" : "string",
  "bank_account" : { },
  "customer" : "The customer (owned by the application's account) for which to create a token. For use only with [Stripe Connect](/docs/connect). Also, this can be used only with an [OAuth access token](/docs/connect/standard-accounts) or [Stripe-Account header](/docs/connect/authentication). For more details, see [Shared Customers](/docs/connect/shared-customers)."
}
```

</details>

## create_charge

To charge a credit card or other payment source, you create a Charge object. If your API key is in test mode, the supplied payment source (e.g., card) won’t actually be charged, although everything else will occur as if in live mode. (Stripe assumes that the charge would have completed successfully).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "metadata" : { },
  "destination" : {
    "amount" : "integer",
    "account" : "Required string"
  },
  "description" : "An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.",
  "external_id" : "string",
  "source" : { },
  "invoice_source" : "string",
  "statement_descriptor" : { },
  "shipping" : {
    "carrier" : "string",
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string",
    "tracking_number" : "string"
  },
  "alternate_statement_descriptors" : {
    "kanji" : "string",
    "kana" : "string"
  },
  "idempotency_key" : "string",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "payment_method" : "string",
  "user_agent" : "string",
  "order" : "string",
  "include" : [ "string" ],
  "amount" : "A positive integer representing how much to charge, in the [smallest currency unit](/docs/currencies#zero-decimal) (e.g., `100` cents to charge $1.00, or `100` to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 USD or [equivalent in charge currency](/docs/currencies#minimum-and-maximum-charge-amounts).",
  "payment_user_agent" : "string",
  "transfer_group" : "A string that identifies this transaction as part of a group. For details, see [Grouping transactions](/docs/connect/charges-transfers#grouping-transactions).",
  "device_id" : "string",
  "exchange_rate" : "number",
  "on_behalf_of" : "The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](/docs/connect/charges-transfers#on-behalf-of).",
  "recurring" : "boolean",
  "ip" : "string",
  "cross_border_classification" : "string. Possible values: export",
  "capture" : "Whether to immediately capture the charge. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](#capture_charge) later. Uncaptured charges expire in _seven days_. For more information, see the [authorizing charges and settling later](/docs/charges#auth-and-capture) documentation.",
  "referrer" : "string",
  "expand" : [ "string" ],
  "application" : "string",
  "receipt_email" : "The email address to which this charge's [receipt](/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a customer, the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).",
  "statement_address" : {
    "city" : "Required string",
    "state" : "Required string",
    "postal_code" : "Required string",
    "line2" : "string",
    "line1" : "Required string"
  },
  "uncaptured" : "boolean",
  "application_fee" : "A fee in %s that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](/docs/connect/direct-charges#collecting-fees).",
  "invoice" : "string",
  "card_program" : "string",
  "card" : { },
  "level3" : {
    "shipping_amount" : "integer",
    "merchant_reference" : "Required string",
    "customer_reference" : "string",
    "shipping_address_zip" : "string",
    "line_items" : [ {
      "tax_amount" : "integer",
      "quantity" : "integer",
      "discount_amount" : "integer",
      "unit_cost" : "integer",
      "product_code" : "Required string",
      "product_description" : "Required string"
    } ],
    "shipping_from_zip" : "string"
  },
  "customer" : "The ID of an existing customer that will be charged in this request."
}
```

</details>

## create_coupon

You can create coupons easily via the coupon management page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.
A coupon has either a percent_off or an amount_off and currency. If you set an amount_off, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of 100 will have a final total of 0 if a coupon with an amount_off of 200 is applied to it and an invoice with a subtotal of 300 will have a final total of 100 if a coupon with an amount_off of 200 is applied to it.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "duration" : "Specifies how long the discount will be in effect. Can be `forever`, `once`, or `repeating`.",
  "duration_in_months" : "Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect.",
  "redeem_by" : "Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers.",
  "expand" : [ "string" ],
  "metadata" : { },
  "max_redemptions" : "A positive integer specifying the number of times the coupon can be redeemed before it's no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use.",
  "name" : "Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.",
  "currency" : "Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed).",
  "percent_off" : "A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed).",
  "id" : "Unique string of your choice that will be used to identify this coupon when applying it to a customer. This is often a specific code you'll give to your customer to use when signing up (e.g., `FALL25OFF`). If you don't want to specify a particular code, you can leave the ID blank and we'll generate a random code for you.",
  "amount_off" : "A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed)."
}
```

</details>

## create_customer

Creates a new customer object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "metadata" : { },
  "account_balance" : "An integer amount in %s that represents the account balance for your customer. Account balances only affect invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.",
  "coupon" : "string",
  "default_source" : "ID of the source to make the customer's new default.",
  "invoice_prefix" : "The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.",
  "description" : "An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.",
  "source" : { },
  "expand" : [ "string" ],
  "shipping" : {
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string"
  },
  "tax_info" : {
    "type" : "Required string. Possible values: vat",
    "tax_id" : "Required string"
  },
  "id" : "A custom ID to use for the customer",
  "email" : "Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.",
  "customer" : "string"
}
```

</details>

## create_customer_source

When you create a new credit card, you must specify a customer or recipient on which to create it.
If the card’s owner has no default card, then the new card will become the default.However, if the owner already has a default, then it will not change.To change the default, you should either update the customer to have a new default_source,or update the recipient to have a new default_card.

<details><summary>Parameters</summary>

### customer (required)

**Type:** string

### $body

**Type:** object

```json
{
  "alipay_account" : { },
  "expand" : [ "string" ],
  "metadata" : { },
  "source" : { },
  "card" : { },
  "bank_account" : { }
}
```

</details>

## create_customer_subscription

Creates a new subscription on an existing customer.

<details><summary>Parameters</summary>

### customer (required)

The identifier of the customer to subscribe.

**Type:** string

### $body

**Type:** object

```json
{
  "metadata" : { },
  "cancel_at_period_end" : "Boolean indicating whether this subscription should cancel at the end of the current period.",
  "coupon" : "The code of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription.",
  "days_until_due" : "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `billing` is set to `send_invoice`.",
  "trial_end" : "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately.",
  "trial_period_days" : "Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan.",
  "application_fee_percent" : "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account. The request must be made with an OAuth key in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).",
  "billing_cycle_anchor" : "A future timestamp to anchor the subscription's [billing cycle](/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.",
  "billing" : "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions. Defaults to `charge_automatically`.",
  "tax_percent" : "A non-negative decimal (with at most four decimal places) between 0 and 100. This represents the percentage of the subscription invoice subtotal that will be calculated and added as tax to the final amount in each billing period. For example, a plan which charges $10/month with a `tax_percent` of `20.0` will charge $12 per invoice. To unset a previously-set value, pass an empty string.",
  "expand" : [ "string" ],
  "trial_from_plan" : "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed.",
  "items" : [ {
    "quantity" : "integer",
    "plan" : "Required string"
  } ],
  "prorate" : "Boolean (defaults to `true`) telling us whether to [credit for unused time](/docs/subscriptions/billing-cycle#prorations) when the billing cycle changes (e.g. when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial). If `false`, the anchor period will be free (similar to a trial) and no proration adjustments will be created."
}
```

</details>

## create_file_link

Creates a new file link object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "expires_at" : "A future timestamp after which the link will no longer be usable.",
  "file" : "The ID of the file."
}
```

</details>

## create_invoice

If you need to invoice your customer outside the regular billing cycle, you can create an invoice that pulls in all pending invoice items, including prorations. The customer’s billing cycle and regular subscription won’t be affected.
Once you create the invoice, Stripe will attempt to collect payment according to your subscriptions settings, though you can choose to pay it right away.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "statement_descriptor" : "Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`.",
  "tax_percent" : "The percent tax rate applied to the invoice, represented as a decimal number.",
  "expand" : [ "string" ],
  "metadata" : { },
  "due_date" : "The date on which payment for this invoice is due. Only valid for invoices where `billing=send_invoice`.",
  "days_until_due" : "The number of days from which the invoice is created until it is due. Only valid for invoices where `billing=send_invoice`.",
  "description" : "string",
  "application_fee" : "A fee in %s that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](/docs/connect/subscriptions#working-with-invoices).",
  "subscription" : "The ID of the subscription to invoice. If not set, the created invoice will include all pending invoice items for the customer. If set, the created invoice will exclude pending invoice items that pertain to other subscriptions.",
  "billing" : "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to `charge_automatically`.",
  "customer" : "Required string"
}
```

</details>

## create_invoice_item

Adds an arbitrary charge or credit to the customer’s upcoming invoice.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "amount" : "The integer amount in **%s** of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.",
  "expand" : [ "string" ],
  "metadata" : { },
  "quantity" : "Non-negative integer. The quantity of units for the invoice item.",
  "description" : "An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "invoice" : "The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. Use this when adding invoice items in response to an invoice.created webhook. You cannot add an invoice item to an invoice that has already been paid, attempted or closed.",
  "subscription" : "The ID of a subscription to add this invoice item to. When left blank, the invoice item will be be added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.",
  "unit_amount" : "The integer unit amount in **%s** of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer's account, pass a negative unit_amount.",
  "discountable" : "Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.",
  "customer" : "The ID of the customer who will be billed when this invoice item is billed."
}
```

</details>

## create_issuing_card

Creates an Issuing Card object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "shipping" : {
    "address" : {
      "country" : "Required string",
      "city" : "Required string",
      "state" : "string",
      "postal_code" : "Required string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "name" : "Required string"
  },
  "currency" : "The currency for the card. This currently must be `usd`.",
  "cardholder" : "The [Cardholder](/docs/api#issuing_cardholder_object) object with which the card will be associated.",
  "type" : "The type of card to issue. Possible values are `physical` or `virtual`.",
  "authorization_controls" : {
    "max_approvals" : "integer",
    "allowed_categories" : [ "string. Possible values: ac_refrigeration_repair | accounting_bookkeeping_services | advertising_services | agricultural_cooperative | airlines_air_carriers | airports_flying_fields | ambulance_services | amusement_parks_carnivals | antique_reproductions | antique_shops | aquariums | architectural_surveying_services | art_dealers_and_galleries | artists_supply_and_craft_shops | auto_and_home_supply_stores | auto_body_repair_shops | auto_paint_shops | auto_service_shops | automated_cash_disburse | automated_fuel_dispensers | automobile_associations | automotive_parts_and_accessories_stores | automotive_tire_stores | bail_and_bond_payments | bakeries | bands_orchestras | barber_and_beauty_shops | betting_casino_gambling | bicycle_shops | billiard_pool_establishments | boat_dealers | boat_rentals_and_leases | book_stores | books_periodicals_and_newspapers | bowling_alleys | bus_lines | business_secretarial_schools | buying_shopping_services | cable_satellite_and_other_pay_television_and_radio | camera_and_photographic_supply_stores | candy_nut_and_confectionery_stores | car_and_truck_dealers_new_used | car_and_truck_dealers_used_only | car_rental_agencies | car_washes | carpentry_services | carpet_upholstery_cleaning | caterers | charitable_and_social_service_organizations_fundraising | chemicals_and_allied_products | chidrens_and_infants_wear_stores | child_care_services | chiropodists_podiatrists | chiropractors | cigar_stores_and_stands | civic_social_fraternal_associations | cleaning_and_maintenance | clothing_rental | colleges_universities | commercial_equipment | commercial_footwear | commercial_photography_art_and_graphics | commuter_transport_and_ferries | computer_network_services | computer_programming | computer_repair | computer_software_stores | computers_peripherals_and_software | concrete_work_services | construction_materials | consulting_public_relations | correspondence_schools | cosmetic_stores | counseling_services | country_clubs | courier_services | court_costs | credit_reporting_agencies | cruise_lines | dairy_products_stores | dance_hall_studios_schools | dating_escort_services | dentists_orthodontists | department_stores | detective_agencies | direct_marketing_catalog_merchant | direct_marketing_combination_catalog_and_retail_merchant | direct_marketing_inbound_telemarketing | direct_marketing_insurance_services | direct_marketing_other | direct_marketing_outbound_telemarketing | direct_marketing_subscription | direct_marketing_travel | discount_stores | doctors | door_to_door_sales | drapery_window_covering_and_upholstery_stores | drinking_places | drug_stores_and_pharmacies | drugs_drug_proprietaries_and_druggist_sundries | dry_cleaners | durable_goods | duty_free_stores | eating_places_restaurants | educational_services | electric_razor_stores | electrical_parts_and_equipment | electrical_services | electronics_repair_shops | electronics_stores | elementary_secondary_schools | employment_temp_agencies | equipment_rental | exterminating_services | family_clothing_stores | fast_food_restaurants | financial_institutions | fines_government_administrative_entities | fireplace_fireplace_screens_and_accessories_stores | floor_covering_stores | florists | florists_supplies_nursery_stock_and_flowers | freezer_and_locker_meat_provisioners | fuel_dealers_non_automotive | funeral_services_crematories | furniture_home_furnishings_and_equipment_stores_except_appliances | furniture_repair_refinishing | furriers_and_fur_shops | general_services | gift_card_novelty_and_souvenir_shops | glass_paint_and_wallpaper_stores | glassware_crystal_stores | golf_courses_public | government_services | grocery_stores_supermarkets | hardware_equipment_and_supplies | hardware_stores | health_and_beauty_spas | hearing_aids_sales_and_supplies | heating_plumbing_a_c | hobby_toy_and_game_shops | home_supply_warehouse_stores | hospitals | hotels_motels_and_resorts | household_appliance_stores | industrial_supplies | information_retrieval_services | insurance_default | insurance_underwriting_premiums | intra_company_purchases | jewelry_stores_watches_clocks_and_silverware_stores | landscaping_services | laundries | laundry_cleaning_services | legal_services_attorneys | luggage_and_leather_goods_stores | lumber_building_materials_stores | manual_cash_disburse | marinas_service_and_supplies | masonry_stonework_and_plaster | massage_parlors | means_womens_clothing_stores | medical_and_dental_labs | medical_dental_ophthalmic_and_hospital_equipment_and_supplies | medical_services | membership_organizations | mens_and_boys_clothing_and_accessories_stores | metal_service_centers | miscellaneous | miscellaneous_apparel_and_accessory_shops | miscellaneous_auto_dealers | miscellaneous_business_services | miscellaneous_food_stores | miscellaneous_general_merchandise | miscellaneous_general_services | miscellaneous_home_furnishing_specialty_stores | miscellaneous_publishing_and_printing | miscellaneous_recreation_services | miscellaneous_repair_shops | miscellaneous_specialty_retail | mobile_home_dealers | motion_picture_theaters | motor_freight_carriers_and_trucking | motor_homes_dealers | motor_vehicle_supplies_and_new_parts | motorcycle_shops_and_dealers | motorcycle_shops_dealers | music_stores_musical_instruments_pianos_and_sheet_music | news_dealers_and_newsstands | non_fi_money_orders | non_fi_stored_value_card_purchase_load | nondurable_goods | nurseries_lawn_and_garden_supply_stores | nursing_personal_care | office_and_commercial_furniture | opticians_eyeglasses | optometrists_ophthalmologist | orthopedic_goods_prosthetic_devices | osteopaths | package_stores_beer_wine_and_liquor | paints_varnishes_and_supplies | parking_lots_garages | passenger_railways | pawn_shops | pet_shops_pet_food_and_supplies | petroleum_and_petroleum_products | photo_developing | photographic_photocopy_microfilm_equipment_and_supplies | photographic_studios | picture_video_production | piece_goods_notions_and_other_dry_goods | plumbing_heating_equipment_and_supplies | political_organizations | postal_services_government_only | precious_stones_and_metals_watches_and_jewelry | professional_services | public_warehousing_and_storage | quick_copy_repro_and_blueprint | railroads | real_estate_agents_and_managers_rentals | record_stores | recreational_vehicle_rentals | religious_goods_stores | religious_organizations | roofing_siding_sheet_metal | secretarial_support_services | security_brokers_dealers | service_stations | sewing_needlework_fabric_and_piece_goods_stores | shoe_repair_hat_cleaning | shoe_stores | small_appliance_repair | snowmobile_dealers | special_trade_services | specialty_cleaning | sporting_goods_stores | sporting_recreation_camps | sports_and_riding_apparel_stores | sports_clubs_fields | stamp_and_coin_stores | stationary_office_supplies_printing_and_writing_paper | stationery_stores_office_and_school_supply_stores | swimming_pools_sales | t_ui_travel_germany | tailors_alterations | tax_payments_government_agencies | tax_preparation_services | taxicabs_limousines | telecommunication_equipment_and_telephone_sales | telecommunication_services | telegraph_services | tent_and_awning_shops | testing_laboratories | theatrical_ticket_agencies | timeshares | tire_retreading_and_repair | tolls_bridge_fees | tourist_attractions_and_exhibits | towing_services | trailer_parks_campgrounds | transportation_services | travel_agencies_tour_operators | truck_stop_iteration | truck_utility_trailer_rentals | typesetting_plate_making_and_related_services | typewriter_stores | u_s_federal_government_agencies_or_departments | uniforms_commercial_clothing | used_merchandise_and_secondhand_stores | utilities | variety_stores | veterinary_services | video_amusement_game_supplies | video_game_arcades | video_tape_rental_stores | vocational_trade_schools | watch_jewelry_repair | welding_repair | wholesale_clubs | wig_and_toupee_stores | wires_money_orders | womens_accessory_and_specialty_shops | womens_ready_to_wear_stores | wrecking_and_salvage_yards" ],
    "blocked_categories" : [ "string. Possible values: ac_refrigeration_repair | accounting_bookkeeping_services | advertising_services | agricultural_cooperative | airlines_air_carriers | airports_flying_fields | ambulance_services | amusement_parks_carnivals | antique_reproductions | antique_shops | aquariums | architectural_surveying_services | art_dealers_and_galleries | artists_supply_and_craft_shops | auto_and_home_supply_stores | auto_body_repair_shops | auto_paint_shops | auto_service_shops | automated_cash_disburse | automated_fuel_dispensers | automobile_associations | automotive_parts_and_accessories_stores | automotive_tire_stores | bail_and_bond_payments | bakeries | bands_orchestras | barber_and_beauty_shops | betting_casino_gambling | bicycle_shops | billiard_pool_establishments | boat_dealers | boat_rentals_and_leases | book_stores | books_periodicals_and_newspapers | bowling_alleys | bus_lines | business_secretarial_schools | buying_shopping_services | cable_satellite_and_other_pay_television_and_radio | camera_and_photographic_supply_stores | candy_nut_and_confectionery_stores | car_and_truck_dealers_new_used | car_and_truck_dealers_used_only | car_rental_agencies | car_washes | carpentry_services | carpet_upholstery_cleaning | caterers | charitable_and_social_service_organizations_fundraising | chemicals_and_allied_products | chidrens_and_infants_wear_stores | child_care_services | chiropodists_podiatrists | chiropractors | cigar_stores_and_stands | civic_social_fraternal_associations | cleaning_and_maintenance | clothing_rental | colleges_universities | commercial_equipment | commercial_footwear | commercial_photography_art_and_graphics | commuter_transport_and_ferries | computer_network_services | computer_programming | computer_repair | computer_software_stores | computers_peripherals_and_software | concrete_work_services | construction_materials | consulting_public_relations | correspondence_schools | cosmetic_stores | counseling_services | country_clubs | courier_services | court_costs | credit_reporting_agencies | cruise_lines | dairy_products_stores | dance_hall_studios_schools | dating_escort_services | dentists_orthodontists | department_stores | detective_agencies | direct_marketing_catalog_merchant | direct_marketing_combination_catalog_and_retail_merchant | direct_marketing_inbound_telemarketing | direct_marketing_insurance_services | direct_marketing_other | direct_marketing_outbound_telemarketing | direct_marketing_subscription | direct_marketing_travel | discount_stores | doctors | door_to_door_sales | drapery_window_covering_and_upholstery_stores | drinking_places | drug_stores_and_pharmacies | drugs_drug_proprietaries_and_druggist_sundries | dry_cleaners | durable_goods | duty_free_stores | eating_places_restaurants | educational_services | electric_razor_stores | electrical_parts_and_equipment | electrical_services | electronics_repair_shops | electronics_stores | elementary_secondary_schools | employment_temp_agencies | equipment_rental | exterminating_services | family_clothing_stores | fast_food_restaurants | financial_institutions | fines_government_administrative_entities | fireplace_fireplace_screens_and_accessories_stores | floor_covering_stores | florists | florists_supplies_nursery_stock_and_flowers | freezer_and_locker_meat_provisioners | fuel_dealers_non_automotive | funeral_services_crematories | furniture_home_furnishings_and_equipment_stores_except_appliances | furniture_repair_refinishing | furriers_and_fur_shops | general_services | gift_card_novelty_and_souvenir_shops | glass_paint_and_wallpaper_stores | glassware_crystal_stores | golf_courses_public | government_services | grocery_stores_supermarkets | hardware_equipment_and_supplies | hardware_stores | health_and_beauty_spas | hearing_aids_sales_and_supplies | heating_plumbing_a_c | hobby_toy_and_game_shops | home_supply_warehouse_stores | hospitals | hotels_motels_and_resorts | household_appliance_stores | industrial_supplies | information_retrieval_services | insurance_default | insurance_underwriting_premiums | intra_company_purchases | jewelry_stores_watches_clocks_and_silverware_stores | landscaping_services | laundries | laundry_cleaning_services | legal_services_attorneys | luggage_and_leather_goods_stores | lumber_building_materials_stores | manual_cash_disburse | marinas_service_and_supplies | masonry_stonework_and_plaster | massage_parlors | means_womens_clothing_stores | medical_and_dental_labs | medical_dental_ophthalmic_and_hospital_equipment_and_supplies | medical_services | membership_organizations | mens_and_boys_clothing_and_accessories_stores | metal_service_centers | miscellaneous | miscellaneous_apparel_and_accessory_shops | miscellaneous_auto_dealers | miscellaneous_business_services | miscellaneous_food_stores | miscellaneous_general_merchandise | miscellaneous_general_services | miscellaneous_home_furnishing_specialty_stores | miscellaneous_publishing_and_printing | miscellaneous_recreation_services | miscellaneous_repair_shops | miscellaneous_specialty_retail | mobile_home_dealers | motion_picture_theaters | motor_freight_carriers_and_trucking | motor_homes_dealers | motor_vehicle_supplies_and_new_parts | motorcycle_shops_and_dealers | motorcycle_shops_dealers | music_stores_musical_instruments_pianos_and_sheet_music | news_dealers_and_newsstands | non_fi_money_orders | non_fi_stored_value_card_purchase_load | nondurable_goods | nurseries_lawn_and_garden_supply_stores | nursing_personal_care | office_and_commercial_furniture | opticians_eyeglasses | optometrists_ophthalmologist | orthopedic_goods_prosthetic_devices | osteopaths | package_stores_beer_wine_and_liquor | paints_varnishes_and_supplies | parking_lots_garages | passenger_railways | pawn_shops | pet_shops_pet_food_and_supplies | petroleum_and_petroleum_products | photo_developing | photographic_photocopy_microfilm_equipment_and_supplies | photographic_studios | picture_video_production | piece_goods_notions_and_other_dry_goods | plumbing_heating_equipment_and_supplies | political_organizations | postal_services_government_only | precious_stones_and_metals_watches_and_jewelry | professional_services | public_warehousing_and_storage | quick_copy_repro_and_blueprint | railroads | real_estate_agents_and_managers_rentals | record_stores | recreational_vehicle_rentals | religious_goods_stores | religious_organizations | roofing_siding_sheet_metal | secretarial_support_services | security_brokers_dealers | service_stations | sewing_needlework_fabric_and_piece_goods_stores | shoe_repair_hat_cleaning | shoe_stores | small_appliance_repair | snowmobile_dealers | special_trade_services | specialty_cleaning | sporting_goods_stores | sporting_recreation_camps | sports_and_riding_apparel_stores | sports_clubs_fields | stamp_and_coin_stores | stationary_office_supplies_printing_and_writing_paper | stationery_stores_office_and_school_supply_stores | swimming_pools_sales | t_ui_travel_germany | tailors_alterations | tax_payments_government_agencies | tax_preparation_services | taxicabs_limousines | telecommunication_equipment_and_telephone_sales | telecommunication_services | telegraph_services | tent_and_awning_shops | testing_laboratories | theatrical_ticket_agencies | timeshares | tire_retreading_and_repair | tolls_bridge_fees | tourist_attractions_and_exhibits | towing_services | trailer_parks_campgrounds | transportation_services | travel_agencies_tour_operators | truck_stop_iteration | truck_utility_trailer_rentals | typesetting_plate_making_and_related_services | typewriter_stores | u_s_federal_government_agencies_or_departments | uniforms_commercial_clothing | used_merchandise_and_secondhand_stores | utilities | variety_stores | veterinary_services | video_amusement_game_supplies | video_game_arcades | video_tape_rental_stores | vocational_trade_schools | watch_jewelry_repair | welding_repair | wholesale_clubs | wig_and_toupee_stores | wires_money_orders | womens_accessory_and_specialty_shops | womens_ready_to_wear_stores | wrecking_and_salvage_yards" ],
    "max_amount" : "integer"
  },
  "status" : "Specifies whether to permit authorizations on this card. Possible values are `active` or `inactive`."
}
```

</details>

## create_issuing_cardholder

Creates a new Issuing Cardholder object that can be issued cards.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "name" : "The cardholder's name. This will be printed on cards issued to them.",
  "phone_number" : "The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already.",
  "type" : "The type of cardholder. Possible values are `individual` or `business_entity`.",
  "email" : "The cardholder's email address.",
  "billing" : {
    "address" : {
      "country" : "Required string",
      "city" : "Required string",
      "state" : "string",
      "postal_code" : "Required string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "name" : "string"
  },
  "status" : "Specifies whether to permit authorizations on this cardholder's cards. Possible values are `active` or `inactive`."
}
```

</details>

## create_issuing_dispute

Creates an Issuing Dispute object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "reason" : "The reason for the dispute, which can be chosen out of a set of valid values.",
  "amount" : "Amount to dispute, defaults to full value, given in the currency the transaction was made in.",
  "expand" : [ "string" ],
  "metadata" : { },
  "evidence" : {
    "other" : {
      "dispute_explanation" : "Required string",
      "uncategorized_file" : "string"
    },
    "fraudulent" : {
      "dispute_explanation" : "Required string",
      "uncategorized_file" : "string"
    }
  },
  "disputed_transaction" : "The ID of the issuing transaction to create a dispute for."
}
```

</details>

## create_login_link

Creates a single-use login link for an Express account to access their Stripe dashboard.
You may only create login links for Express accounts connected to your platform.

<details><summary>Parameters</summary>

### account (required)

The identifier of the account to create a login link for.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "redirect_url" : "Where to redirect the user after they log out of their dashboard."
}
```

</details>

## create_order

Creates a new Order object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "coupon" : "A coupon code that represents a discount to be applied to this order. Must be one-time duration and in same currency as the order.",
  "shipping" : {
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string"
  },
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "items" : [ {
    "parent" : "string",
    "amount" : "integer",
    "quantity" : "integer",
    "description" : "string",
    "currency" : "string",
    "type" : "string. Possible values: discount | shipping | sku | tax"
  } ],
  "email" : "The email address of the customer placing the order.",
  "customer" : "The ID of an existing customer to use for this order. If provided, the customer email and shipping address will be used to create the order. Subsequently, the customer will also be charged to pay the order. If `email` or `shipping` are also provided, they will override the values retrieved from the customer object."
}
```

</details>

## create_order_return

Return all or part of an order. The order must have a status of paid or fulfilled before it can be returned. Once all items have been returned, the order will become canceled or returned depending on which status the order started in.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "items" : [ {
    "parent" : "string",
    "amount" : "integer",
    "quantity" : "integer",
    "description" : "string",
    "type" : "string. Possible values: discount | shipping | sku | tax"
  } ]
}
```

</details>

## create_payment



<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "metadata" : { },
  "destination" : {
    "amount" : "integer",
    "account" : "Required string"
  },
  "description" : "string",
  "external_id" : "string",
  "source" : "string",
  "invoice_source" : "string",
  "statement_descriptor" : "string",
  "shipping" : {
    "carrier" : "string",
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string",
    "tracking_number" : "string"
  },
  "alternate_statement_descriptors" : {
    "kanji" : "string",
    "kana" : "string"
  },
  "idempotency_key" : "string",
  "currency" : "Required string",
  "payment_method" : "string",
  "user_agent" : "string",
  "order" : "string",
  "include" : [ "string" ],
  "amount" : "Required integer",
  "payment_user_agent" : "string",
  "transfer_group" : "string",
  "device_id" : "string",
  "exchange_rate" : "number",
  "on_behalf_of" : "string",
  "recurring" : "boolean",
  "ip" : "string",
  "cross_border_classification" : "string. Possible values: export",
  "capture" : "boolean",
  "referrer" : "string",
  "expand" : [ "string" ],
  "application" : "string",
  "receipt_email" : "string",
  "statement_address" : {
    "city" : "Required string",
    "state" : "Required string",
    "postal_code" : "Required string",
    "line2" : "string",
    "line1" : "Required string"
  },
  "uncaptured" : "boolean",
  "application_fee" : "integer",
  "invoice" : "string",
  "card_program" : "string",
  "level3" : {
    "shipping_amount" : "integer",
    "merchant_reference" : "Required string",
    "customer_reference" : "string",
    "shipping_address_zip" : "string",
    "line_items" : [ {
      "tax_amount" : "integer",
      "quantity" : "integer",
      "discount_amount" : "integer",
      "unit_cost" : "integer",
      "product_code" : "Required string",
      "product_description" : "Required string"
    } ],
    "shipping_from_zip" : "string"
  },
  "customer" : "string"
}
```

</details>

## create_payment_intent

Creates a PaymentIntent object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "capture_method" : "Capture method of this PaymentIntent, one of `automatic` or `manual`.",
  "amount" : "Amount intended to be collected by this PaymentIntent",
  "metadata" : { },
  "transfer_group" : "A string that identifies the resulting payment as part of a group. See the [Connect documentation](/docs/connect/charges-transfers#grouping-transactions) for details.",
  "allowed_source_types" : [ "string" ],
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users.",
  "source" : "ID of the Source object to attach to this PaymentIntent.",
  "statement_descriptor" : "Extra information about a PaymentIntent. This will appear on your customer's statement when this PaymentIntent succeeds in creating a charge.",
  "transfer_data" : {
    "amount" : "integer",
    "destination" : "Required string"
  },
  "expand" : [ "string" ],
  "shipping" : {
    "carrier" : "string",
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string",
    "tracking_number" : "string"
  },
  "receipt_email" : "Email address that the receipt for the resulting payment will be sent to.",
  "return_url" : "The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "save_source_to_customer" : "`true` to save this PaymentIntent's Source to the associated Customer, if the Source is not already attached.",
  "attempt_confirmation" : "Attempt to confirm this PaymentIntent on source attachment.",
  "application_fee_amount" : "The amount of the application fee (if any) that will be applied to the payment and transferred to theapplication owner's Stripe account. To use an application fee, therequest must be made on behalf of another account, using the`Stripe-Account` header or an OAuth key. For more information, see[Collecting applicationfees](/docs/connect/direct-charges#collecting-fees).",
  "customer" : "ID of the customer this PaymentIntent is for if one exists."
}
```

</details>

## create_payout

To send funds to your own bank account, you create a new payout object. Your Stripe balance must be able to cover the payout amount, or you’ll receive an “Insufficient Funds” error.
If your API key is in test mode, money won’t actually be sent, though everything else will occur as if in live mode.
If you are creating a manual payout on a Stripe account that uses multiple payment source types, you’ll need to specify the source type balance that the payout should draw from. The balance object details available and pending amounts by source type.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "statement_descriptor" : "A string to be displayed on the recipient's bank or card statement. This may be at most 22 characters. Attempting to use a `statement_descriptor` longer than 22 characters will return an error. Note: Most banks will truncate this information and/or display it inconsistently. Some may not display it at all.",
  "amount" : "A positive integer in cents representing how much to payout.",
  "expand" : [ "string" ],
  "metadata" : { },
  "method" : "The method used to send this payout, which can be `standard` or `instant`. `instant` is only supported for payouts to debit cards. (See [Instant payouts for marketplaces for more information](https://stripe.com/blog/instant-payouts-for-marketplaces).)",
  "destination" : "The ID of a bank account or a card to send the payout to. If no destination is supplied, the default external account for the specified currency will be used.",
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "source_type" : "The source balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the balances API. Valid options are: **alipay_account**, **bank_account**, and **card**."
}
```

</details>

## create_plan

You can create plans using the API, or in the Stripe Dashboard.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "interval_count" : "The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).",
  "amount" : "A positive integer in %s (or 0 for a free plan) representing how much to charge on a recurring basis.",
  "metadata" : { },
  "product" : {
    "statement_descriptor" : "string",
    "metadata" : { },
    "name" : "Required string",
    "active" : "boolean",
    "id" : "string",
    "unit_label" : "string"
  },
  "tiers" : [ {
    "up_to" : { },
    "unit_amount" : "integer"
  } ],
  "transform_usage" : {
    "round" : "Required string. Possible values: down | up",
    "divide_by" : "Required integer"
  },
  "active" : "Whether the plan is currently available for new subscriptions. Defaults to `true`.",
  "aggregate_usage" : "Specifies a usage aggregation strategy for plans of `usage_type=metered`. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for picking the last usage record reported within a period, `last_ever` for picking the last usage record ever (across period bounds) or `max` which picks the usage record with the maximum reported usage during a period. Defaults to `sum`.",
  "billing_scheme" : "Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.",
  "trial_period_days" : "Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](/docs/api#create_subscription-trial_from_plan).",
  "statement_descriptor" : "An arbitrary string to be displayed on your customer's credit card statement. This may be up to 22 characters. The statement description may not include &lt;&gt;\"' characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all. It must contain at least one letter.",
  "tiers_mode" : "Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.",
  "expand" : [ "string" ],
  "usage_type" : "Configures how the quantity per period should be determined, can be either `metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`.",
  "name" : "The plan name. Customers may see this value on Stripe-generated invoices and receipts.",
  "nickname" : "A brief description of the plan, hidden from customers.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "interval" : "Specifies billing frequency. Either `day`, `week`, `month` or `year`.",
  "id" : "An identifier randomly generated by Stripe. Used to identify this plan when subscribing a customer. You can optionally override this ID, but the ID must be unique across all plans in your Stripe account. You can, however, use the same plan ID in both live and test modes."
}
```

</details>

## create_platform_earning_refund

Refunds an application fee that has previously been collected but not yet refunded.Funds will be refunded to the Stripe account from which the fee was originally collected.
You can optionally refund only part of an application fee.You can do so multiple times, until the entire fee has been refunded.
Once entirely refunded, an application fee can’t be refunded again.This method will raise an error when called on an already-refunded application fee,or when trying to refund more money than is left on an application fee.

<details><summary>Parameters</summary>

### id (required)

The identifier of the application fee to be refunded.

**Type:** string

### $body

**Type:** object

```json
{
  "amount" : "A positive integer, in _%s_, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.",
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## create_point_of_sale_connection_token

To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "operator_account" : "If the request is being made from the platform account but the reader is being operated by a connected account, indicate the operating account."
}
```

</details>

## create_point_of_sale_location

Creates a new Location object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "address" : {
    "country" : "Required string",
    "city" : "Required string",
    "state" : "string",
    "postal_code" : "Required string",
    "line2" : "string",
    "line1" : "Required string"
  },
  "display_name" : "A name for the location.",
  "operator_account" : "If the request is being made from the platform account but the reader is being operated by a connected account, indicate the operating account."
}
```

</details>

## create_point_of_sale_reader

Creates a new Reader object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "registration_code" : "A code generated by the reader used for registering to an account.",
  "location" : "The location to assign the reader to. If no location is specified, the reader will be assigned to the account's default location.",
  "label" : "Custom label given to the reader for easier identification. If no label is specified, the registration code will be used.",
  "operator_account" : "If the request is being made from the platform account but the reader is being operated by a connected account, indicate the operating account."
}
```

</details>

## create_product

Creates a new product object. To create a product for use with subscriptions, see Subscriptions Products.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "deactivate_on" : [ "string" ],
  "images" : [ "string" ],
  "metadata" : { },
  "active" : "Whether the product is currently available for purchase. Defaults to `true`.",
  "caption" : "A short one-line description of the product, meant to be displayable to the customer. May only be set if type=`good`.",
  "description" : "The product's description, meant to be displayable to the customer. May only be set if type=`good`.",
  "type" : "The type of the product. The product is either of type `service`, which is eligible for use with Subscriptions and Plans or `good`, which is eligible for use with Orders and SKUs.",
  "url" : "A URL of a publicly-accessible webpage for this product. May only be set if type=`good`.",
  "package_dimensions" : {
    "length" : "Required number",
    "width" : "Required number",
    "weight" : "Required number",
    "height" : "Required number"
  },
  "statement_descriptor" : "An arbitrary string to be displayed on your customer's credit card statement. This may be up to 22 characters. The statement description may not include &lt;&gt;\"' characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all. It must contain at least one letter. May only be set if type=`service`.",
  "expand" : [ "string" ],
  "shippable" : "Whether this product is shipped (i.e., physical goods). Defaults to `true`. May only be set if type=`good`.",
  "name" : "The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types.",
  "attributes" : [ "string" ],
  "id" : "An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account. Applicable to both `service` and `good` types.",
  "unit_label" : "A label that represents units of this product, such as seat(s), in Stripe and on customers’ receipts and invoices. Only available on products of type=`service`."
}
```

</details>

## create_refund



<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "reason" : "string. Possible values: duplicate | fraudulent | requested_by_customer",
  "amount" : "integer",
  "expand" : [ "string" ],
  "metadata" : { },
  "charge" : "string",
  "refund_application_fee" : "boolean",
  "description" : "string",
  "reverse_transfer" : "boolean",
  "directive" : { }
}
```

</details>

## create_sku

Creates a new SKU associated with a product.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "package_dimensions" : {
    "length" : "Required number",
    "width" : "Required number",
    "weight" : "Required number",
    "height" : "Required number"
  },
  "image" : "The URL of an image for this SKU, meant to be displayable to the customer.",
  "expand" : [ "string" ],
  "metadata" : { },
  "product" : "The ID of the product this SKU is associated with. Must be a product with type `good`.",
  "price" : "The cost of the item as a nonnegative integer in the smallest currency unit (that is, 100 cents to charge $1.00, or 100 to charge ¥100, Japanese Yen being a zero-decimal currency).",
  "active" : "Whether the SKU is available for purchase. Default to `true`.",
  "attributes" : "A dictionary of attributes and values for the attributes defined by the product. If, for example, a product's attributes are `[\"size\", \"gender\"]`, a valid SKU has the following dictionary of attributes: `{\"size\": \"Medium\", \"gender\": \"Unisex\"}`.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "id" : "The identifier for the SKU. Must be unique. If not provided, an identifier will be randomly generated.",
  "inventory" : {
    "quantity" : "integer",
    "type" : "string. Possible values: bucket | finite | infinite",
    "value" : "string. Possible values:  | in_stock | limited | out_of_stock"
  }
}
```

</details>

## create_source

Creates a new source object.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "owner" : {
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "phone" : "string",
    "name" : "string",
    "email" : "string"
  },
  "redirect" : {
    "return_url" : "Required string"
  },
  "amount" : "Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources.",
  "mandate" : {
    "notification_method" : "string. Possible values: email | manual | none",
    "acceptance" : {
      "date" : "Required integer",
      "ip" : "Required string",
      "user_agent" : "Required string",
      "status" : "Required string. Possible values: accepted | pending | refused | revoked"
    }
  },
  "metadata" : { },
  "receiver" : {
    "refund_attributes_method" : "string. Possible values: email | manual | none"
  },
  "usage" : "string. Possible values: reusable | single_use",
  "type" : "The `type` of the source to create. Required unless `customer` and `original_source` are specified (see the [Shared card Sources](/docs/sources/connect#shared-card-sources) guide)",
  "original_source" : "The source to share.",
  "token" : "An optional token used to create the source. When passed, token properties will override source parameters.",
  "statement_descriptor" : "An arbitrary string to be displayed on your customer's statement. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket.` While many payment types will display this information, some may not display it at all.",
  "expand" : [ "string" ],
  "currency" : "Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready.",
  "flow" : "The authentication `flow` of the source to create. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. It is generally inferred unless a type supports multiple flows.",
  "customer" : "The `Customer` to whom the original source is attached to. Must be set when the original source is not a `Source` (e.g., `Card`)."
}
```

</details>

## create_subscription

Creates a new subscription on an existing customer.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "metadata" : { },
  "cancel_at_period_end" : "Boolean indicating whether this subscription should cancel at the end of the current period.",
  "coupon" : "The code of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription.",
  "days_until_due" : "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `billing` is set to `send_invoice`.",
  "trial_end" : "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately.",
  "trial_period_days" : "Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan.",
  "application_fee_percent" : "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account. The request must be made with an OAuth key in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).",
  "billing_cycle_anchor" : "A future timestamp to anchor the subscription's [billing cycle](/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.",
  "billing" : "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions. Defaults to `charge_automatically`.",
  "tax_percent" : "A non-negative decimal (with at most four decimal places) between 0 and 100. This represents the percentage of the subscription invoice subtotal that will be calculated and added as tax to the final amount in each billing period. For example, a plan which charges $10/month with a `tax_percent` of `20.0` will charge $12 per invoice. To unset a previously-set value, pass an empty string.",
  "expand" : [ "string" ],
  "trial_from_plan" : "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed.",
  "items" : [ {
    "quantity" : "integer",
    "plan" : "Required string"
  } ],
  "prorate" : "Boolean (defaults to `true`) telling us whether to [credit for unused time](/docs/subscriptions/billing-cycle#prorations) when the billing cycle changes (e.g. when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial). If `false`, the anchor period will be free (similar to a trial) and no proration adjustments will be created.",
  "customer" : "The identifier of the customer to subscribe."
}
```

</details>

## create_subscription_item

Adds a new item to an existing subscription. No existing items will be changed or replaced.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "quantity" : "The quantity you'd like to apply to the subscription item you're creating.",
  "subscription" : "The identifier of the subscription to modify.",
  "plan" : "The identifier of the plan to add to the subscription.",
  "prorate" : "Flag indicating whether to [prorate](/docs/subscriptions/upgrading-downgrading#understanding-proration) switching plans during a billing cycle.",
  "proration_date" : "If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](#retrieve_customer_invoice) endpoint."
}
```

</details>

## create_topup

Top up the balance of an account

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "statement_descriptor" : "Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters.",
  "amount" : "A positive integer in %s representing how much to transfer.",
  "expand" : [ "string" ],
  "metadata" : { },
  "transfer_group" : "A string that identifies this top-up as part of a group.",
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "source" : "The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](/docs/connect/testing#testing-top-ups))."
}
```

</details>

## create_transfer

To send funds from your Stripe account to a connected account, you create a new transfer object. Your Stripe balance must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "amount" : "A positive integer in %s representing how much to transfer.",
  "expand" : [ "string" ],
  "metadata" : { },
  "transfer_group" : "A string that identifies this transaction as part of a group. See the [Connect documentation](/docs/connect/charges-transfers#grouping-transactions) for details.",
  "destination" : "The ID of a connected Stripe account. See the Connect documentation for details.",
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users.",
  "source_transaction" : "You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](/docs/connect/charges-transfers#transfer-availability) for details.",
  "currency" : "3-letter [ISO code for currency](/docs/payouts)."
}
```

</details>

## create_transfer_recipient

Creates a new Recipient object and verifies the recipient’s identity.Also verifies the recipient’s bank account information or debit card, if either is provided.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "name" : "The recipient's full, legal name. For type `individual`, should be in the format `First Last`, `First Middle Last`, or `First M Last` (no prefixes or suffixes). For `corporation`, the full, incorporated name.",
  "description" : "An arbitrary string which you can attach to a `Recipient` object. It is displayed alongside the recipient in the web interface.",
  "type" : "Type of the recipient: either `individual` or `corporation`.",
  "card" : { },
  "email" : "The recipient's email address. It is displayed alongside the recipient in the web interface, and can be useful for searching and tracking.",
  "tax_id" : "The recipient's tax ID, as a string. For type `individual`, the full SSN; for type `corporation`, the full EIN.",
  "bank_account" : { }
}
```

</details>

## create_transfer_reversal

When you create a new reversal, you must specify a transfer to create it on.
When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.
Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.

<details><summary>Parameters</summary>

### id (required)

The ID of the transfer to be reversed.

**Type:** string

### $body

**Type:** object

```json
{
  "amount" : "A positive integer in %s representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.",
  "expand" : [ "string" ],
  "metadata" : { },
  "refund_application_fee" : "Boolean indicating whether the application fee should be refunded when reversing this transfer. If a full transfer reversal is given, the full application fee will be refunded. Otherwise, the application fee will be refunded with an amount proportional to the amount of the transfer reversed.",
  "description" : "An arbitrary string which you can attach to a reversal object. It is displayed alongside the reversal in the Dashboard. This will be unset if you POST an empty value."
}
```

</details>

## create_usage_record

Creates a usage record for a specified subscription item and date, and fills it with a quantity.

<details><summary>Parameters</summary>

### subscription_item (required)

The ID of the subscription item for this usage record.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "quantity" : "The usage quantity for the specified timestamp.",
  "action" : "Valid values are `increment` (default) or `set`. When using `increment` the specified `quantity` will be added to the usage at the specified timestamp. The `set` action will overwrite the usage quantity at that timestamp.",
  "timestamp" : "The timestamp for the usage event. This timestamp must be within the current billing period of the subscription of the provided `subscription_item`."
}
```

</details>

## decline_issuing_authorization

Declines a pending Issuing Authorization object.

<details><summary>Parameters</summary>

### authorization (required)

The identifier of the issuing authorization to decline.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ]
}
```

</details>

## delete_account

With Connect, you may delete Custom accounts you manage.
Custom accounts created using test-mode keys can be deleted at any time. Custom accounts created using live-mode keys may only be deleted once all balances are zero.
If you are looking to close your own account, use the data tab in your account settings instead.

<details><summary>Parameters</summary>

### account (required)

The identifier of the account to be deleted. If none is provided, will default to the account of the API key.

**Type:** string

</details>

## delete_bank_account



<details><summary>Parameters</summary>

### account (required)

**Type:** string

### id (required)

The ID of the external account to be deleted.

**Type:** string

</details>

## delete_coupon

You can delete coupons via the coupon management page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.

<details><summary>Parameters</summary>

### coupon (required)

The identifier of the coupon to be deleted.

**Type:** string

</details>

## delete_customer

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

<details><summary>Parameters</summary>

### customer (required)

The identifier of the customer to be deleted.

**Type:** string

</details>

## delete_customer_discount

Removes the currently applied discount on a customer.

<details><summary>Parameters</summary>

### customer (required)

**Type:** string

</details>

## delete_customer_source



<details><summary>Parameters</summary>

### customer (required)

**Type:** string

### id (required)

The ID of the source to be deleted.

**Type:** string

</details>

## delete_invoice_item

Removes an invoice item from the upcoming invoice. Removing an invoice item is only possible before the invoice it’s attached to is closed.

<details><summary>Parameters</summary>

### invoiceitem (required)

The identifier of the invoice item to be deleted.

**Type:** string

</details>

## delete_plan

Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.

<details><summary>Parameters</summary>

### plan (required)

The identifier of the plan to be deleted.

**Type:** string

</details>

## delete_product

Delete a product. Deleting a product with type=good is only possible if it has no SKUs associated with it. Deleting a product with type=service is only possible if it has no plans associated with it.

<details><summary>Parameters</summary>

### id (required)

The ID of the product to delete.

**Type:** string

</details>

## delete_sku

Delete a SKU. Deleting a SKU is only possible until it has been used in an order.

<details><summary>Parameters</summary>

### id (required)

The identifier of the SKU to be deleted.

**Type:** string

</details>

## delete_subscription

Cancels a customer’s subscription immediately. The customer will not be charged again for the subscription.
Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually deleted. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.
By default, upon subscription cancellation, Stripe will close all unpaid invoices for the customer. This is designed to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can reopen the invoices manually after subscription cancellation to have us proceed with payment collection. Or, you could even re-attempt payment yourself on all unpaid invoices before allowing the customer to cancel the subscription at all.

<details><summary>Parameters</summary>

### subscription_exposed_id (required)

**Type:** string

</details>

## delete_subscription_discount

Removes the currently applied discount on a subscription.

<details><summary>Parameters</summary>

### subscription_exposed_id (required)

**Type:** string

</details>

## delete_subscription_item

Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.

<details><summary>Parameters</summary>

### item (required)

The identifier of the subscription item to delete.

**Type:** string

</details>

## delete_transfer_recipient

Permanently deletes a recipient. It cannot be undone.

<details><summary>Parameters</summary>

### id (required)

The identifier of the recipient to be deleted.

**Type:** string

</details>

## get_account

Retrieves the details of the account.

<details><summary>Parameters</summary>

### account (required)

The identifier of the account to retrieve. If none is provided, the account associated with the API key is returned.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_accounts

Returns a list of accounts connected to your platform via Connect. If you’re not a platform, the list is empty.

<details><summary>Parameters</summary>

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_balance_transactions

Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.

<details><summary>Parameters</summary>

### available_on

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### currency

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### payout

For automatic Stripe payouts only, only returns transactions that were payed out on the specified payout ID.

**Type:** string

### source

Only returns the original transaction.

**Type:** string

### type

Only returns transactions of the given type. One of: `charge`, `refund`, `adjustment`, `application_fee`, `application_fee_refund`, `transfer`, `payment`, `payout`, `payout_failure`, `stripe_fee`, or `network_cost`.

**Type:** string

</details>

## get_all_charges

Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### customer

Only return charges for the customer specified by this customer ID.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### source

A filter on the list, based on the source of the charge. The value can be a dictionary with the following options:

**Type:** object

```json
{
  "object" : "string"
}
```

### transfer_group

Only return charges for this transfer group.

**Type:** string

</details>

## get_all_country_specs

Lists all Country Spec objects available in the API.

<details><summary>Parameters</summary>

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_coupons

Returns a list of your coupons.

<details><summary>Parameters</summary>

### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_customer_sources



<details><summary>Parameters</summary>

### customer (required)

The ID of the customer whose sources will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### object

Filter sources according to a particular object type.

**Type:** string

### type

**Type:** string

</details>

## get_all_customer_subscriptions

You can see a list of the customer’s active subscriptions. Note that the 10 most recent active subscriptions are always available by default on the customer object. If you need more than those 10, you can use the limit and starting_after parameters to page through additional subscriptions.

<details><summary>Parameters</summary>

### customer (required)

The ID of the customer whose subscriptions will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_customers

Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### email

A filter on the list based on the customer's `email` field. The value must be a string.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_disputes

Returns a list of your disputes.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_external_accounts



<details><summary>Parameters</summary>

### account (required)

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_file_links

Returns a list of file links.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### expired

Filter links by their expiration status. By default, all links are returned.

**Type:** boolean

### file

Only return links for the given file.

**Type:** string

</details>

## get_all_files

Returns a list of the files that your account has access to. The files are returned sorted by creation date, with the most recently created files appearing first.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### purpose

The file purpose to filter queries by. If none is provided, files will not be filtered by purpose.

**Type:** string

**Potential values:** additional_verification, bootstrap_pilot_user_report, business_logo, customer_signature, dispute_evidence, finance_report_run, founders_stock_document, identity_document, incorporation_article, incorporation_document, india_export_payment_advice, invoice_statement, paper_check_image, payment_provider_transfer, pci_document, product_feed, sigma_scheduled_query, support_attachment, tandem_accepted, tandem_requested, tandem_voidance, tax_document, tax_document_user_upload, works_with_image

</details>

## get_all_invoice_items

Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### customer

The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### invoice

Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.

**Type:** string

</details>

## get_all_invoice_lines

When retrieving an invoice, you’ll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

<details><summary>Parameters</summary>

### invoice (required)

The ID of the invoice containing the lines to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_invoices

You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.

<details><summary>Parameters</summary>

### billing

The billing mode of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.

**Type:** string

**Potential values:** charge_automatically, send_invoice

### customer

Only return invoices for the customer specified by this customer ID.

**Type:** string

### date

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### due_date

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### subscription

Only return invoices for the subscription specified by this subscription ID.

**Type:** string

</details>

## get_all_issuing_authorizations

Returns a list of Issuing Authorization objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

<details><summary>Parameters</summary>

### card

Only return issuing transactions that belong to the given card.

**Type:** string

### cardholder

Only return authorizations belonging to the given cardholder.

**Type:** string

### created

Only return authorizations that were created during the given date interval.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### status

Only return authorizations with the given status. One of pending, closed, or reversed.

**Type:** string

**Potential values:** closed, pending, reversed

</details>

## get_all_issuing_cardholders

Returns a list of Issuing Cardholder objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

<details><summary>Parameters</summary>

### created

Only return cardholders that were created during the given date interval.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### email

Only return cardholders that have the given email address.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### phone_number

Only return cardholders that have the given phone number.

**Type:** string

### status

Only return cardholders that have the given status. One of `active` or `inactive`.

**Type:** string

**Potential values:** active, inactive

### type

Only return cardholders that have the given type. One of One of `individual` or `business_entity`.

**Type:** string

**Potential values:** business_entity, individual

</details>

## get_all_issuing_cards

Returns a list of Issuing Card objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

<details><summary>Parameters</summary>

### cardholder

Only return cards belonging to the Cardholder with the provided ID.

**Type:** string

### created

Only return cards that were issued during the given date interval.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### exp_month

Only return cards that have the given expiration month.

**Type:** integer

### exp_year

Only return cards that have the given expiration year.

**Type:** integer

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### last4

Only return cards that have the given last four digits.

**Type:** string

### name

Only return cards that have the given name.

**Type:** string

### source

Only return cards whose full card number matches that of this card source ID.

**Type:** string

### status

Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.

**Type:** string

**Potential values:** active, canceled, inactive, lost, pending_compliance, stolen

### type

Only return cards that have the given type. One of `virtual` or `physical`.

**Type:** string

**Potential values:** physical, virtual

</details>

## get_all_issuing_disputes

Returns a list of Issuing Dispute objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

<details><summary>Parameters</summary>

### created

Only return issuing disputes that were created during the given date interval.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### disputed_transaction

Only return issuing disputes for the given transaction.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_issuing_transactions

Returns a list of Issuing Transaction objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

<details><summary>Parameters</summary>

### card

Only return issuing transactions that belong to the given card.

**Type:** string

### cardholder

Only return authorizations belonging to the given cardholder.

**Type:** string

### created

Only return transactions that were created during the given date interval.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_notification_events

List events, going back up to 30 days.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### delivery_success

Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned.

**Type:** boolean

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### type

A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property.

**Type:** string

### types

An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_order_returns

Returns a list of your order returns. The returns are returned sorted by creation date, with the most recently created return appearing first.

<details><summary>Parameters</summary>

### created

Date this return was created.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### order

The order to retrieve returns for.

**Type:** string

</details>

## get_all_orders

Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.

<details><summary>Parameters</summary>

### created

Date this order was created.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### customer

Only return orders for the given customer.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### ids

Only return orders with the given IDs.

**Type:** array

```json
[ "string" ]
```

### status

Only return orders that have the given status. One of `created`, `paid`, `fulfilled`, or `refunded`.

**Type:** string

### status_transitions

Filter orders based on when they were paid, fulfilled, canceled, or returned.

**Type:** object

```json
{
  "canceled" : {
    "lt" : "integer",
    "gte" : "integer",
    "lte" : "integer",
    "gt" : "integer"
  },
  "fulfilled" : {
    "lt" : "integer",
    "gte" : "integer",
    "lte" : "integer",
    "gt" : "integer"
  },
  "paid" : {
    "lt" : "integer",
    "gte" : "integer",
    "lte" : "integer",
    "gt" : "integer"
  },
  "returned" : {
    "lt" : "integer",
    "gte" : "integer",
    "lte" : "integer",
    "gt" : "integer"
  }
}
```

### upstream_ids

Only return orders with the given upstream order IDs.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_payment_flows_payment_intent

Returns a list of PaymentIntents.

<details><summary>Parameters</summary>

### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_payout

Returns a list of existing payouts sent to third-party bank accounts or that Stripe has sent you. The payouts are returned in sorted order, with the most recently created payouts appearing first.

<details><summary>Parameters</summary>

### arrival_date

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### destination

The ID of an external account - only return payouts sent to this external account.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### status

Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`.

**Type:** string

</details>

## get_all_plans

Returns a list of your plans.

<details><summary>Parameters</summary>

### active

Only return plans that are active or inactive (e.g., pass `false` to list all inactive products).

**Type:** boolean

### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### product

Only return plans for the given product.

**Type:** string

</details>

## get_all_platform_earnings

Returns a list of application fees you’ve previously collected. The application fees are returned in sorted order, with the most recent fees appearing first.

<details><summary>Parameters</summary>

### charge

Only return application fees for the charge specified by this charge ID.

**Type:** string

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_platform_earnings_refunds

You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional refunds.

<details><summary>Parameters</summary>

### id (required)

The ID of the application fee whose refunds will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_point_of_sale_locations

Returns a list of Location objects.

<details><summary>Parameters</summary>

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### operator_account

The identifier of the account associated with this location.

**Type:** string

</details>

## get_all_point_of_sale_readers

Returns a list of Reader objects.

<details><summary>Parameters</summary>

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### location

A location id to filter the response list to only readers at the specific location

**Type:** string

### operator_account

The identifier of the account associated with this reader.

**Type:** string

### status

A status filter to filter readers to only offline or online readers

**Type:** string

</details>

## get_all_products

Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.

<details><summary>Parameters</summary>

### active

Only return products that are active or inactive (e.g., pass `false` to list all inactive products).

**Type:** boolean

### created

Only return products that were created during the given date interval.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### ids

Only return products with the given IDs.

**Type:** array

```json
[ "string" ]
```

### shippable

Only return products that can be shipped (i.e., physical, not digital products).

**Type:** boolean

### type

Only return products of this type.

**Type:** string

**Potential values:** good, service

### url

Only return products with the given url.

**Type:** string

</details>

## get_all_refunds

Returns a list of all refunds you’ve previously created. The refunds are returned in sorted order, with the most recent refunds appearing first. For convenience, the 10 most recent refunds are always available by default on the charge object.

<details><summary>Parameters</summary>

### charge

Only return refunds for the charge specified by this charge ID.

**Type:** string

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_scheduled_query_runs

Returns a list of scheduled query runs.

<details><summary>Parameters</summary>

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_skus

Returns a list of your SKUs. The SKUs are returned sorted by creation date, with the most recently created SKUs appearing first.

<details><summary>Parameters</summary>

### active

Only return SKUs that are active or inactive (e.g., pass `false` to list all inactive products).

**Type:** boolean

### attributes

Only return SKUs that have the specified key/value pairs in this partially constructed dictionary. Can be specified only if `product` is also supplied. For instance, if the associated product has attributes `["color", "size"]`, passing in `attributes[color]=red` returns all the SKUs for this product that have `color` set to `red`.

**Type:** object

```json
{
  "<string>" : "string"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### ids

Only return SKUs with the given IDs.

**Type:** array

```json
[ "string" ]
```

### in_stock

Only return SKUs that are either in stock or out of stock (e.g., pass `false` to list all SKUs that are out of stock). If no value is provided, all SKUs are returned.

**Type:** boolean

### product

The ID of the product whose SKUs will be retrieved. Must be a product with type `good`.

**Type:** string

</details>

## get_all_subscription_item_period_summaries

Returns a list of subscription item period summaries sorted in reverse-chronological order (newest first). The first entry represents the current period of usage; its ID is NOT stable until the period ends.

<details><summary>Parameters</summary>

### subscription_item (required)

Only summary items for the given subscription item.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_subscription_items

Returns a list of your subscription items for a given subscription.

<details><summary>Parameters</summary>

### subscription (required)

The ID of the subscription whose items will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_subscriptions

By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify status=canceled.

<details><summary>Parameters</summary>

### billing

The billing mode of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.

**Type:** string

**Potential values:** charge_automatically, send_invoice

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### customer

The ID of the customer whose subscriptions will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### plan

The ID of the plan whose subscriptions will be retrieved.

**Type:** string

### status

The status of the subscriptions to retrieve. One of: `trialing`, `active`, `past_due`, `unpaid`, `canceled`, or `all`. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Passing in a value of `all` will return subscriptions of all statuses.

**Type:** string

**Potential values:** active, all, canceled, past_due, trialing, unpaid

</details>

## get_all_topups

Returns a list of top-ups.

<details><summary>Parameters</summary>

### amount

A positive integer in %s representing how much to transfer.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### status

Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`.

**Type:** string

**Potential values:** canceled, failed, pending, succeeded

</details>

## get_all_transfer_recipients

Returns a list of your recipients. The recipients are returned sorted by creation date, with the most recently created recipients appearing first.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### type

**Type:** string

**Potential values:** corporation, individual

### verified

Only return recipients that are verified or unverified.

**Type:** boolean

</details>

## get_all_transfer_reversals

You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional reversals.

<details><summary>Parameters</summary>

### id (required)

The ID of the transfer whose reversals will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_all_transfers

Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.

<details><summary>Parameters</summary>

### created

**Type:** object

```json
{
  "lt" : "integer",
  "gte" : "integer",
  "lte" : "integer",
  "gt" : "integer"
}
```

### destination

Only return transfers for the destination specified by this account ID.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### transfer_group

Only return transfers with the specified transfer group.

**Type:** string

</details>

## get_all_upcoming_invoice_lines

When retrieving an upcoming invoice, you’ll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

<details><summary>Parameters</summary>

### customer (required)

The customer of the upcoming invoice is required. In other cases it is ignored.

**Type:** string

### coupon

The code of the coupon to apply. If `subscription` or `subscription_items` is provided, the invoice returned will preview updating or creating a subscription with that coupon. Otherwise, it will preview applying that coupon to the customer for the next upcoming invoice from among the customer's subscriptions. The invoice can be previewed without a coupon by passing this value as an empty string.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### subscription

The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.

**Type:** string

### subscription_billing_cycle_anchor

For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.For existing subscriptions, the value can only be set to `now` or `unchanged`.

**Type:** object

```json
{ }
```

### subscription_cancel_at_period_end

Boolean indicating whether this subscription should cancel at the end of the current period.

**Type:** boolean

### subscription_items

Preview updating the subscription with this list of items. Otherwise this parameter is ignored.

**Type:** array

```json
[ {
  "metadata" : { },
  "deleted" : "boolean",
  "quantity" : "integer",
  "clear_usage" : "boolean",
  "id" : "string",
  "plan" : "string"
} ]
```

### subscription_prorate

If previewing an update to a subscription, this decides whether the preview will show the result of applying prorations or not. If set, one of `subscription_items` or `subscription`, and one of `subscription_items` or `subscription_trial_end` are required.

**Type:** boolean

### subscription_proration_date

If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period, and cannot be before the subscription was on its current plan. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration` cannot be set to false.

**Type:** integer

### subscription_tax_percent

If provided, the invoice returned will preview updating or creating a subscription with that tax percent. If set, one of `subscription_items` or `subscription` is required.

**Type:** number

### subscription_trial_end

If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required.

**Type:** object

```json
{ }
```

### subscription_trial_from_plan

Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed.

**Type:** boolean

</details>

## get_application_fee_refund

By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

<details><summary>Parameters</summary>

### fee (required)

ID of the application fee refunded.

**Type:** string

### id (required)

ID of refund to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_balance

Retrieves the current account balance, based on the authentication that was used to make the request.

<details><summary>Parameters</summary>

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_balance_transaction

Retrieves the balance transaction with the given ID.

<details><summary>Parameters</summary>

### id (required)

The ID of the desired balance transaction, as found on any API object that affects the balance (e.g., a charge or transfer).

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_charge

Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

<details><summary>Parameters</summary>

### charge (required)

The identifier of the charge to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_country_spec

Returns a Country Spec for a given Country code.

<details><summary>Parameters</summary>

### country (required)

An ISO 3166-1 alpha-2 country code. Available country codes can be listed with the [List Country Specs](/docs/api#list_country_specs) endpoint.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_coupon

Retrieves the coupon with the given ID.

<details><summary>Parameters</summary>

### coupon (required)

The ID of the desired coupon.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_customer

Retrieves the details of an existing customer. You need only supply the unique customer identifier that was returned upon customer creation.

<details><summary>Parameters</summary>

### customer (required)

The identifier of the customer to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_customer_discount



<details><summary>Parameters</summary>

### customer (required)

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_customer_source



<details><summary>Parameters</summary>

### customer (required)

**Type:** string

### id (required)

The ID of the source to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_dispute

Retrieves the dispute with the given ID.

<details><summary>Parameters</summary>

### dispute (required)

ID of dispute to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_external_account



<details><summary>Parameters</summary>

### account (required)

**Type:** string

### id (required)

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_file

Retrieves the details of an existing file object. Supply the unique file ID from a file, and Stripe will return the corresponding file object.

<details><summary>Parameters</summary>

### file (required)

The identifier of the file to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_file_link

Retrieves the file link with the given ID.

<details><summary>Parameters</summary>

### link (required)

The identifier of the file link to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_invoice

Retrieves the invoice with the given ID.

<details><summary>Parameters</summary>

### invoice (required)

The identifier of the desired invoice.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_invoice_item

Retrieves the invoice item with the given ID.

<details><summary>Parameters</summary>

### invoiceitem (required)

The ID of the desired invoice item.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_issuing_authorization

Retrieves an Issuing Authorization object.

<details><summary>Parameters</summary>

### authorization (required)

The ID of the authorization to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_issuing_card

Retrieves an Issuing Card object.

<details><summary>Parameters</summary>

### card (required)

The identifier of the card to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_issuing_card_details

For virtual cards only. Retrieves an Issuing Card_details object that contains the sensitive details of a virtual card.

<details><summary>Parameters</summary>

### card (required)

The identifier of the virtual card to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_issuing_cardholder

Retrieves an Issuing Cardholder object.

<details><summary>Parameters</summary>

### cardholder (required)

The identifier of the cardholder to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_issuing_dispute

Retrieves an Issuing Dispute object.

<details><summary>Parameters</summary>

### dispute (required)

The ID of the dispute to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_issuing_transaction

Retrieves an Issuing Transaction object.

<details><summary>Parameters</summary>

### transaction (required)

The ID of the transaction to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_notification_event

Retrieves the details of an event. Supply the unique identifier of the event, which you might have received in a webhook.

<details><summary>Parameters</summary>

### id (required)

The identifier of the event to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_order

Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.

<details><summary>Parameters</summary>

### id (required)

The identifier of the order to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_order_return

Retrieves the details of an existing order return. Supply the unique order ID from either an order return creation request or the order return list, and Stripe will return the corresponding order information.

<details><summary>Parameters</summary>

### id (required)

The identifier of the order return to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_payment



<details><summary>Parameters</summary>

### payment (required)

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_payment_intent

Retrieves the details of a PaymentIntent that has previously been created. 
Client-side retrieval using a publishable key is allowed when the client_secret is provided in the query string. 
When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the payment intent object reference for more details.

<details><summary>Parameters</summary>

### intent (required)

**Type:** string

### client_secret

The client secret of the PaymentIntent. Required if a publishable key is used to retrieve the source.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_payout

Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list, and Stripe will return the corresponding payout information.

<details><summary>Parameters</summary>

### payout (required)

The identifier of the payout to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_plan

Retrieves the plan with the given ID.

<details><summary>Parameters</summary>

### plan (required)

The ID of the desired plan.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_platform_earning

Retrieves the details of an application fee that your account has collected. The same information is returned when refunding the application fee.

<details><summary>Parameters</summary>

### id (required)

The identifier of the fee to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_point_of_sale_location

Retrieves a Location object.

<details><summary>Parameters</summary>

### location (required)

The identifier of the location to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### operator_account

The identifier of the account associated with this location.

**Type:** string

</details>

## get_point_of_sale_reader

Retrieves a Reader object.

<details><summary>Parameters</summary>

### reader (required)

The identifier of the reader to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### operator_account

The identifier of the account associated with this reader.

**Type:** string

</details>

## get_product

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.

<details><summary>Parameters</summary>

### id (required)

The identifier of the product to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_refund

Retrieves the details of an existing refund.

<details><summary>Parameters</summary>

### refund (required)

ID of refund to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_scheduled_query_run

Retrieves the details of an scheduled query run.

<details><summary>Parameters</summary>

### scheduled_query_run (required)

Unique identifier for the object.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_sku

Retrieves the details of an existing SKU. Supply the unique SKU identifier from either a SKU creation request or from the product, and Stripe will return the corresponding SKU information.

<details><summary>Parameters</summary>

### id (required)

The identifier of the SKU to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_source

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

<details><summary>Parameters</summary>

### source (required)

The identifier of the source to be retrieved.

**Type:** string

### client_secret

The client secret of the source. Required if a publishable key is used to retrieve the source.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_source_transaction

Retrieve an existing source transaction object. Supply the unique source ID from a source creation request and the source transaction ID and Stripe will return the corresponding up-to-date source object information.

<details><summary>Parameters</summary>

### source (required)

The ID of the source whose source transaction will be retrieved.

**Type:** string

### source_transaction (required)

The ID of the source transaction that will be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_subscription

Retrieves the subscription with the given ID.

<details><summary>Parameters</summary>

### subscription_exposed_id (required)

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_subscription_item

Retrieves the invoice item with the given ID.

<details><summary>Parameters</summary>

### item (required)

The identifier of the subscription item to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_token

Retrieves the token with the given ID.

<details><summary>Parameters</summary>

### token (required)

The ID of the desired token.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_topup

Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.

<details><summary>Parameters</summary>

### topup (required)

The ID of the top-up to retrieve.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_transfer

Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.

<details><summary>Parameters</summary>

### transfer (required)

The identifier of the transfer to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_transfer_recipient

Retrieves the details of an existing recipient. You need only supply the unique recipient identifier that was returned upon recipient creation.

<details><summary>Parameters</summary>

### id (required)

The identifier of the recipient to be retrieved.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_transfer_reversal

By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

<details><summary>Parameters</summary>

### id (required)

ID of reversal to retrieve.

**Type:** string

### transfer (required)

ID of the transfer reversed.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

</details>

## get_upcoming_invoice

At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discount that is applicable to the customer.
Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.
You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass a proration_date parameter when doing the actual subscription update. The value passed in should be the same as the subscription_proration_date returned on the upcoming invoice resource. The recommended way to get only the prorations being previewed is to consider only proration line items where period[start] is equal to the subscription_proration_date on the upcoming invoice resource.

<details><summary>Parameters</summary>

### customer (required)

The identifier of the customer whose upcoming invoice you'd like to retrieve.

**Type:** string

### coupon

The code of the coupon to apply. If `subscription` or `subscription_items` is provided, the invoice returned will preview updating or creating a subscription with that coupon. Otherwise, it will preview applying that coupon to the customer for the next upcoming invoice from among the customer's subscriptions. The invoice can be previewed without a coupon by passing this value as an empty string.

**Type:** string

### expand

Specifies which fields in the response should be expanded.

**Type:** array

```json
[ "string" ]
```

### invoice_items

List of invoice items to add or update in the upcoming invoice preview.

**Type:** array

```json
[ {
  "amount" : "integer",
  "metadata" : { },
  "invoiceitem" : "string",
  "description" : "string",
  "currency" : "string",
  "discountable" : "boolean"
} ]
```

### subscription

The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.

**Type:** string

### subscription_billing_cycle_anchor

For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.For existing subscriptions, the value can only be set to `now` or `unchanged`.

**Type:** object

```json
{ }
```

### subscription_cancel_at_period_end

Boolean indicating whether this subscription should cancel at the end of the current period.

**Type:** boolean

### subscription_items

List of subscription items, each with an attached plan.

**Type:** array

```json
[ {
  "metadata" : { },
  "deleted" : "boolean",
  "quantity" : "integer",
  "clear_usage" : "boolean",
  "id" : "string",
  "plan" : "string"
} ]
```

### subscription_prorate

If previewing an update to a subscription, this decides whether the preview will show the result of applying prorations or not. If set, one of `subscription_items` or `subscription`, and one of `subscription_items` or `subscription_trial_end` are required.

**Type:** boolean

### subscription_proration_date

If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period, and cannot be before the subscription was on its current plan. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration` cannot be set to false.

**Type:** integer

### subscription_tax_percent

If provided, the invoice returned will preview updating or creating a subscription with that tax percent. If set, one of `subscription_items` or `subscription` is required.

**Type:** number

### subscription_trial_end

If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required.

**Type:** object

```json
{ }
```

### subscription_trial_from_plan

Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed.

**Type:** boolean

</details>

## issuing_authorization_approve

Approves a pending Issuing Authorization object.

<details><summary>Parameters</summary>

### authorization (required)

The identifier of the authorization to approve.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "held_amount" : "If the authorization's `is_held_amount_controllable` property is `true`, you may provide this value to control how much to hold for the authorization."
}
```

</details>

## pay_invoice

Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your subscriptions settings. However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.

<details><summary>Parameters</summary>

### invoice (required)

ID of invoice to pay.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "forgive" : "Determines if invoice should be forgiven if source has insufficient funds to fully pay the invoice.",
  "source" : "A payment source to be charged. The source must be the ID of a source belonging to the customer associated with the invoice being paid."
}
```

</details>

## pay_order



<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "shipping_method" : "string",
  "application_fee" : "integer",
  "source" : { },
  "email" : "The email address of the customer placing the order. Required if not previously specified for the order.",
  "customer" : "The ID of an existing customer that will be charged for this order. If no customer was attached to the order at creation, either `source` or `customer` is required. Otherwise, the specified customer will be charged instead of the one attached to the order."
}
```

</details>

## payment_intent_capture

Capture the funds of an existing uncaptured PaymentIntent where required_action="requires_capture".
Uncaptured PaymentIntents will be canceled exactly seven days after they are created.

<details><summary>Parameters</summary>

### intent (required)

**Type:** string

### $body

**Type:** object

```json
{
  "transfer_data" : {
    "amount" : "integer"
  },
  "expand" : [ "string" ],
  "amount_to_capture" : "The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Any additional amount will be automatically refunded. Defaults to the full `amount_capturable` if not provided.",
  "application_fee_amount" : "The amount of the application fee (if any) that will be applied to the payment and transferred to theapplication owner's Stripe account. To use an application fee, therequest must be made on behalf of another account, using the`Stripe-Account` header or an OAuth key. For more information, see[Collecting applicationfees](/docs/connect/direct-charges#collecting-fees)."
}
```

</details>

## payment_intent_confirm

Confirm that your customer intends to pay with current or providedsource. Upon confirmation, the PaymentIntent will attempt to initiatea payment.
If the selected source requires additional authentication steps, thePaymentIntent will transition to the requires_source_action status andsuggest additional actions via next_source_action. If payment fails,the PaymentIntent will transition to the requires_source status. Ifpayment succeeds, the PaymentIntent will transition to the succeededstatus (or requires_capture, if capture_method is set to manual).
When using a publishable key, theclient_secret must be providedto confirm the PaymentIntent.

<details><summary>Parameters</summary>

### intent (required)

**Type:** string

### $body

**Type:** object

```json
{
  "invoice_charge_reason" : "string. Possible values: api | dunning_retry | invoice_payer | manual_admin | manual_mrch | payment_receiver | unsent_invoice | update_card | update_customer | update_invoice",
  "expand" : [ "string" ],
  "receipt_email" : "Email address that the receipt for the resulting payment will be sent to.",
  "return_url" : "The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.",
  "save_source_to_customer" : "`true` to save this PaymentIntent's Source to the associated Customer, if the Source is not already attached.",
  "client_secret" : "The client secret of the PaymentIntent.",
  "invoice" : "string",
  "source" : "ID of the Source object to attach to this PaymentIntent."
}
```

</details>

## reject_account

With Connect, you may flag accounts as suspicious.
Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.

<details><summary>Parameters</summary>

### account (required)

The identifier of the account to reject

**Type:** string

### $body

**Type:** object

```json
{
  "reason" : "The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.",
  "expand" : [ "string" ]
}
```

</details>

## retry_notification_event

Resend an event. This only works in testmode

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ]
}
```

</details>

## update_account

Updates a connected Express or Custom account by setting the values of the parameters passed. Any parameters not provided are left unchanged. Most parameters can be changed only for Custom accounts. (These are marked Custom Only below.) Parameters marked Custom and Express are supported by both account types.
To update your own account, use the Dashboard. Refer to our Connect documentation to learn more about updating accounts.

<details><summary>Parameters</summary>

### account (required)

**Type:** string

### $body

**Type:** object

```json
{
  "business_logo" : "(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for this account (at least 128px x 128px)",
  "debit_negative_balances" : "A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](/docs/connect/account-balances).",
  "tos_acceptance" : {
    "date" : "Required integer",
    "ip" : "Required string",
    "user_agent" : "string"
  },
  "business_name" : "The publicly sharable name for this account.",
  "metadata" : { },
  "payout_schedule" : {
    "weekly_anchor" : "string. Possible values: friday | monday | saturday | sunday | thursday | tuesday | wednesday",
    "interval" : "string. Possible values: daily | four_times_monthly | manual | monthly | weekly",
    "delay_days" : "integer",
    "monthly_anchor" : "integer"
  },
  "support_phone" : "A publicly shareable support phone number for the business.",
  "account_token" : "An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account.",
  "decline_charge_on" : {
    "avs_failure" : "boolean",
    "cvc_failure" : "boolean"
  },
  "statement_descriptor" : "The default text that appears on credit card statements when a charge is made [directly on the account](/docs/connect/direct-charges)",
  "expand" : [ "string" ],
  "support_email" : "A publicly shareable support email address for the business.",
  "support_url" : "A publicly shareable URL that provides support for this account.",
  "external_account" : { },
  "business_primary_color" : "A CSS hex color value representing the primary branding color for this account.",
  "legal_entity" : {
    "business_vat_id" : "string",
    "personal_address_kana" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "gender" : "string",
    "address_kana" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "type" : "string",
    "personal_address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "address_kanji" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "ssn_last_4" : "string",
    "first_name" : "string",
    "first_name_kana" : "string",
    "personal_id_number" : "string",
    "verification" : {
      "document" : "string"
    },
    "last_name_kanji" : "string",
    "personal_address_kanji" : {
      "country" : "string",
      "town" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "business_name" : "string",
    "maiden_name" : "string",
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "business_tax_id" : "string",
    "first_name_kanji" : "string",
    "last_name" : "string",
    "business_name_kana" : "string",
    "tax_id_registrar" : "string",
    "dob" : {
      "month" : "Required integer",
      "year" : "Required integer",
      "day" : "Required integer"
    },
    "additional_owners" : {
      "<string>" : {
        "maiden_name" : "string",
        "address" : {
          "country" : "string",
          "city" : "string",
          "state" : "string",
          "postal_code" : "string",
          "line2" : "string",
          "line1" : "string"
        },
        "dob" : {
          "month" : "Required integer",
          "year" : "Required integer",
          "day" : "Required integer"
        },
        "last_name" : "string",
        "first_name" : "string",
        "personal_id_number" : "string",
        "verification" : {
          "document" : "string"
        }
      }
    },
    "last_name_kana" : "string",
    "business_name_kanji" : "string",
    "phone_number" : "string"
  },
  "business_url" : "The URL that best shows the service or product provided by this account.",
  "default_currency" : "Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts).",
  "product_description" : "Internal-only description of the product sold by, or service provided by, the business. Used by Stripe for risk and underwriting purposes.",
  "email" : "Email address of the account representative. For Standard accounts, this is used to ask them to claim their Stripe account. For Custom accounts, this only makes the account easier to identify to platforms; Stripe does not email the account representative.",
  "payout_statement_descriptor" : "The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.",
  "bank_account" : { }
}
```

</details>

## update_bank_account

Updates the metadata, account holder name, and account holder type of a bank account belonging to a Custom account, and optionally sets it as the default for its currency. Other bank account details are not editable by design.
You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.

<details><summary>Parameters</summary>

### account (required)

**Type:** string

### id (required)

The ID of the external account to update

**Type:** string

### $body

**Type:** object

```json
{
  "metadata" : { },
  "account_holder_name" : "The name of the person or business that owns the bank account.",
  "address_country" : "Billing address country, if provided when creating card.",
  "address_state" : "State/County/Province/Region.",
  "exp_month" : "Two digit number representing the card’s expiration month.",
  "exp_year" : "Four digit number representing the card’s expiration year.",
  "address_city" : "City/District/Suburb/Town/Village.",
  "expand" : [ "string" ],
  "address_line2" : "Address line 2 (Apartment/Suite/Unit/Building).",
  "address_line1" : "Address line 1 (Street address/PO Box/Company name).",
  "account_holder_type" : "The type of entity that holds the account. This can be either `individual` or `company`.",
  "name" : "Cardholder name.",
  "address_zip" : "ZIP or postal code",
  "default_for_currency" : "When set to true, this becomes the default external account for its currency."
}
```

</details>

## update_charge

Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### charge (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "transfer_group" : "A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](/docs/connect/charges-transfers#grouping-transactions) for details.",
  "shipping" : {
    "carrier" : "string",
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string",
    "tracking_number" : "string"
  },
  "receipt_email" : "This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.",
  "description" : "An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.",
  "fraud_details" : {
    "user_report" : "Required string. Possible values: fraudulent | safe"
  },
  "customer" : "The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge."
}
```

</details>

## update_coupon

Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

<details><summary>Parameters</summary>

### coupon (required)

The identifier of the coupon to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "name" : "Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set."
}
```

</details>

## update_customer



<details><summary>Parameters</summary>

### customer (required)

The identifier of the customer to subscribe.

**Type:** string

### $body

**Type:** object

```json
{
  "metadata" : { },
  "account_balance" : "An integer amount in %s that represents the account balance for your customer. Account balances only affect invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.",
  "coupon" : "string",
  "default_source" : "ID of the source to make the customer's new default.",
  "invoice_prefix" : "The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.",
  "description" : "An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.",
  "trial_end" : "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately.",
  "source" : { },
  "expand" : [ "string" ],
  "default_alipay_account" : "ID of Alipay account to make the customer's new default for invoice payments.",
  "default_bank_account" : "ID of bank account to make the customer's new default for invoice payments.",
  "shipping" : {
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "phone" : "string",
    "name" : "Required string"
  },
  "tax_info" : {
    "type" : "Required string. Possible values: vat",
    "tax_id" : "Required string"
  },
  "default_card" : "ID of card to make the customer's new default for invoice payments.",
  "card" : { },
  "email" : "Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.",
  "bank_account" : { }
}
```

</details>

## update_customer_source



<details><summary>Parameters</summary>

### customer (required)

**Type:** string

### id (required)

The ID of the card to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "owner" : {
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "phone" : "string",
    "name" : "string",
    "email" : "string"
  },
  "metadata" : { },
  "account_holder_name" : "The name of the person or business that owns the bank account.",
  "address_country" : "Billing address country, if provided when creating card.",
  "address_state" : "State/County/Province/Region.",
  "exp_month" : "Two digit number representing the card’s expiration month.",
  "exp_year" : "Four digit number representing the card’s expiration year.",
  "address_city" : "City/District/Suburb/Town/Village.",
  "expand" : [ "string" ],
  "address_line2" : "Address line 2 (Apartment/Suite/Unit/Building).",
  "address_line1" : "Address line 1 (Street address/PO Box/Company name).",
  "account_holder_type" : "The type of entity that holds the account. This can be either `individual` or `company`.",
  "name" : "Cardholder name.",
  "address_zip" : "ZIP or postal code"
}
```

</details>

## update_dispute

When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your dashboard, but if you prefer, you can use the API to submit evidence programmatically.
Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our guide to dispute types.

<details><summary>Parameters</summary>

### dispute (required)

ID of the dispute to update.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "evidence" : {
    "refund_policy" : "string",
    "customer_communication" : "string",
    "shipping_date" : "string",
    "billing_address" : "string",
    "duplicate_charge_documentation" : "string",
    "refund_policy_disclosure" : "string",
    "shipping_carrier" : "string",
    "service_documentation" : "string",
    "uncategorized_text" : "string",
    "cancellation_policy_disclosure" : "string",
    "service_date" : "string",
    "duplicate_charge_id" : "string",
    "shipping_address" : "string",
    "product_description" : "string",
    "duplicate_charge_explanation" : "string",
    "customer_purchase_ip" : "string",
    "refund_refusal_explanation" : "string",
    "uncategorized_file" : "string",
    "shipping_documentation" : "string",
    "access_activity_log" : "string",
    "cancellation_rebuttal" : "string",
    "customer_signature" : "string",
    "cancellation_policy" : "string",
    "receipt" : "string",
    "customer_name" : "string",
    "customer_email_address" : "string",
    "shipping_tracking_number" : "string"
  },
  "submit" : "Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default)."
}
```

</details>

## update_file_link

Updates an existing file link object. Expired links can no longer be updated.

<details><summary>Parameters</summary>

### link (required)

The ID of the file link.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "expires_at" : { }
}
```

</details>

## update_invoice

Until an invoice is paid, it is marked as open (closed=false). If you’d like to stop Stripe from attempting to collect payment on an invoice or would simply like to close the invoice out as no longer owed by the customer, you can update the closed parameter.

<details><summary>Parameters</summary>

### invoice (required)

**Type:** string

### $body

**Type:** object

```json
{
  "statement_descriptor" : "Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`.",
  "tax_percent" : "The percent tax rate applied to the invoice, represented as a non-negative decimal number (with at most four decimal places) between 0 and 100. To unset a previously-set value, pass an empty string. The tax rate of an attempted, paid or forgiven invoice cannot be changed.",
  "expand" : [ "string" ],
  "metadata" : { },
  "forgiven" : "Boolean representing whether an invoice is forgiven or not. To forgive an invoice, pass true. Forgiving an invoice instructs us to update the subscription status as if the invoice were successfully paid. Once an invoice has been forgiven, it cannot be unforgiven or reopened.",
  "due_date" : "The date on which payment for this invoice is due. Only valid for invoices where `billing=send_invoice`.",
  "paid" : "Boolean representing whether an invoice is paid or not. To mark invoice as paid, pass true. Only applies to invoices where `billing=send_invoice`.",
  "closed" : "Boolean representing whether an invoice is closed or not. To close an invoice, pass true.",
  "days_until_due" : "The number of days from which the invoice is created until it is due. Only valid for invoices where `billing=send_invoice`.",
  "description" : "string",
  "application_fee" : "A fee in %s that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](/docs/connect/subscriptions#working-with-invoices)."
}
```

</details>

## update_invoice_item

Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.

<details><summary>Parameters</summary>

### invoiceitem (required)

**Type:** string

### $body

**Type:** object

```json
{
  "amount" : "The integer amount in **%s** of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.",
  "expand" : [ "string" ],
  "metadata" : { },
  "quantity" : "Non-negative integer. The quantity of units for the invoice item.",
  "description" : "An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.",
  "unit_amount" : "The integer unit amount in **%s** of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer's account, pass a negative unit_amount.",
  "discountable" : "Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations."
}
```

</details>

## update_issuing_authorization

Updates the specified Issuing Authorization object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### authorization (required)

The identifier of the authorization to update.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## update_issuing_card

Updates the specified Issuing Card object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### card (required)

The identifier of the issued card to update.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "cardholder" : "The [Cardholder](/docs/api#issuing_cardholder_object) to associate the card with.",
  "authorization_controls" : {
    "max_approvals" : "integer",
    "allowed_categories" : [ "string. Possible values: ac_refrigeration_repair | accounting_bookkeeping_services | advertising_services | agricultural_cooperative | airlines_air_carriers | airports_flying_fields | ambulance_services | amusement_parks_carnivals | antique_reproductions | antique_shops | aquariums | architectural_surveying_services | art_dealers_and_galleries | artists_supply_and_craft_shops | auto_and_home_supply_stores | auto_body_repair_shops | auto_paint_shops | auto_service_shops | automated_cash_disburse | automated_fuel_dispensers | automobile_associations | automotive_parts_and_accessories_stores | automotive_tire_stores | bail_and_bond_payments | bakeries | bands_orchestras | barber_and_beauty_shops | betting_casino_gambling | bicycle_shops | billiard_pool_establishments | boat_dealers | boat_rentals_and_leases | book_stores | books_periodicals_and_newspapers | bowling_alleys | bus_lines | business_secretarial_schools | buying_shopping_services | cable_satellite_and_other_pay_television_and_radio | camera_and_photographic_supply_stores | candy_nut_and_confectionery_stores | car_and_truck_dealers_new_used | car_and_truck_dealers_used_only | car_rental_agencies | car_washes | carpentry_services | carpet_upholstery_cleaning | caterers | charitable_and_social_service_organizations_fundraising | chemicals_and_allied_products | chidrens_and_infants_wear_stores | child_care_services | chiropodists_podiatrists | chiropractors | cigar_stores_and_stands | civic_social_fraternal_associations | cleaning_and_maintenance | clothing_rental | colleges_universities | commercial_equipment | commercial_footwear | commercial_photography_art_and_graphics | commuter_transport_and_ferries | computer_network_services | computer_programming | computer_repair | computer_software_stores | computers_peripherals_and_software | concrete_work_services | construction_materials | consulting_public_relations | correspondence_schools | cosmetic_stores | counseling_services | country_clubs | courier_services | court_costs | credit_reporting_agencies | cruise_lines | dairy_products_stores | dance_hall_studios_schools | dating_escort_services | dentists_orthodontists | department_stores | detective_agencies | direct_marketing_catalog_merchant | direct_marketing_combination_catalog_and_retail_merchant | direct_marketing_inbound_telemarketing | direct_marketing_insurance_services | direct_marketing_other | direct_marketing_outbound_telemarketing | direct_marketing_subscription | direct_marketing_travel | discount_stores | doctors | door_to_door_sales | drapery_window_covering_and_upholstery_stores | drinking_places | drug_stores_and_pharmacies | drugs_drug_proprietaries_and_druggist_sundries | dry_cleaners | durable_goods | duty_free_stores | eating_places_restaurants | educational_services | electric_razor_stores | electrical_parts_and_equipment | electrical_services | electronics_repair_shops | electronics_stores | elementary_secondary_schools | employment_temp_agencies | equipment_rental | exterminating_services | family_clothing_stores | fast_food_restaurants | financial_institutions | fines_government_administrative_entities | fireplace_fireplace_screens_and_accessories_stores | floor_covering_stores | florists | florists_supplies_nursery_stock_and_flowers | freezer_and_locker_meat_provisioners | fuel_dealers_non_automotive | funeral_services_crematories | furniture_home_furnishings_and_equipment_stores_except_appliances | furniture_repair_refinishing | furriers_and_fur_shops | general_services | gift_card_novelty_and_souvenir_shops | glass_paint_and_wallpaper_stores | glassware_crystal_stores | golf_courses_public | government_services | grocery_stores_supermarkets | hardware_equipment_and_supplies | hardware_stores | health_and_beauty_spas | hearing_aids_sales_and_supplies | heating_plumbing_a_c | hobby_toy_and_game_shops | home_supply_warehouse_stores | hospitals | hotels_motels_and_resorts | household_appliance_stores | industrial_supplies | information_retrieval_services | insurance_default | insurance_underwriting_premiums | intra_company_purchases | jewelry_stores_watches_clocks_and_silverware_stores | landscaping_services | laundries | laundry_cleaning_services | legal_services_attorneys | luggage_and_leather_goods_stores | lumber_building_materials_stores | manual_cash_disburse | marinas_service_and_supplies | masonry_stonework_and_plaster | massage_parlors | means_womens_clothing_stores | medical_and_dental_labs | medical_dental_ophthalmic_and_hospital_equipment_and_supplies | medical_services | membership_organizations | mens_and_boys_clothing_and_accessories_stores | metal_service_centers | miscellaneous | miscellaneous_apparel_and_accessory_shops | miscellaneous_auto_dealers | miscellaneous_business_services | miscellaneous_food_stores | miscellaneous_general_merchandise | miscellaneous_general_services | miscellaneous_home_furnishing_specialty_stores | miscellaneous_publishing_and_printing | miscellaneous_recreation_services | miscellaneous_repair_shops | miscellaneous_specialty_retail | mobile_home_dealers | motion_picture_theaters | motor_freight_carriers_and_trucking | motor_homes_dealers | motor_vehicle_supplies_and_new_parts | motorcycle_shops_and_dealers | motorcycle_shops_dealers | music_stores_musical_instruments_pianos_and_sheet_music | news_dealers_and_newsstands | non_fi_money_orders | non_fi_stored_value_card_purchase_load | nondurable_goods | nurseries_lawn_and_garden_supply_stores | nursing_personal_care | office_and_commercial_furniture | opticians_eyeglasses | optometrists_ophthalmologist | orthopedic_goods_prosthetic_devices | osteopaths | package_stores_beer_wine_and_liquor | paints_varnishes_and_supplies | parking_lots_garages | passenger_railways | pawn_shops | pet_shops_pet_food_and_supplies | petroleum_and_petroleum_products | photo_developing | photographic_photocopy_microfilm_equipment_and_supplies | photographic_studios | picture_video_production | piece_goods_notions_and_other_dry_goods | plumbing_heating_equipment_and_supplies | political_organizations | postal_services_government_only | precious_stones_and_metals_watches_and_jewelry | professional_services | public_warehousing_and_storage | quick_copy_repro_and_blueprint | railroads | real_estate_agents_and_managers_rentals | record_stores | recreational_vehicle_rentals | religious_goods_stores | religious_organizations | roofing_siding_sheet_metal | secretarial_support_services | security_brokers_dealers | service_stations | sewing_needlework_fabric_and_piece_goods_stores | shoe_repair_hat_cleaning | shoe_stores | small_appliance_repair | snowmobile_dealers | special_trade_services | specialty_cleaning | sporting_goods_stores | sporting_recreation_camps | sports_and_riding_apparel_stores | sports_clubs_fields | stamp_and_coin_stores | stationary_office_supplies_printing_and_writing_paper | stationery_stores_office_and_school_supply_stores | swimming_pools_sales | t_ui_travel_germany | tailors_alterations | tax_payments_government_agencies | tax_preparation_services | taxicabs_limousines | telecommunication_equipment_and_telephone_sales | telecommunication_services | telegraph_services | tent_and_awning_shops | testing_laboratories | theatrical_ticket_agencies | timeshares | tire_retreading_and_repair | tolls_bridge_fees | tourist_attractions_and_exhibits | towing_services | trailer_parks_campgrounds | transportation_services | travel_agencies_tour_operators | truck_stop_iteration | truck_utility_trailer_rentals | typesetting_plate_making_and_related_services | typewriter_stores | u_s_federal_government_agencies_or_departments | uniforms_commercial_clothing | used_merchandise_and_secondhand_stores | utilities | variety_stores | veterinary_services | video_amusement_game_supplies | video_game_arcades | video_tape_rental_stores | vocational_trade_schools | watch_jewelry_repair | welding_repair | wholesale_clubs | wig_and_toupee_stores | wires_money_orders | womens_accessory_and_specialty_shops | womens_ready_to_wear_stores | wrecking_and_salvage_yards" ],
    "blocked_categories" : [ "string. Possible values: ac_refrigeration_repair | accounting_bookkeeping_services | advertising_services | agricultural_cooperative | airlines_air_carriers | airports_flying_fields | ambulance_services | amusement_parks_carnivals | antique_reproductions | antique_shops | aquariums | architectural_surveying_services | art_dealers_and_galleries | artists_supply_and_craft_shops | auto_and_home_supply_stores | auto_body_repair_shops | auto_paint_shops | auto_service_shops | automated_cash_disburse | automated_fuel_dispensers | automobile_associations | automotive_parts_and_accessories_stores | automotive_tire_stores | bail_and_bond_payments | bakeries | bands_orchestras | barber_and_beauty_shops | betting_casino_gambling | bicycle_shops | billiard_pool_establishments | boat_dealers | boat_rentals_and_leases | book_stores | books_periodicals_and_newspapers | bowling_alleys | bus_lines | business_secretarial_schools | buying_shopping_services | cable_satellite_and_other_pay_television_and_radio | camera_and_photographic_supply_stores | candy_nut_and_confectionery_stores | car_and_truck_dealers_new_used | car_and_truck_dealers_used_only | car_rental_agencies | car_washes | carpentry_services | carpet_upholstery_cleaning | caterers | charitable_and_social_service_organizations_fundraising | chemicals_and_allied_products | chidrens_and_infants_wear_stores | child_care_services | chiropodists_podiatrists | chiropractors | cigar_stores_and_stands | civic_social_fraternal_associations | cleaning_and_maintenance | clothing_rental | colleges_universities | commercial_equipment | commercial_footwear | commercial_photography_art_and_graphics | commuter_transport_and_ferries | computer_network_services | computer_programming | computer_repair | computer_software_stores | computers_peripherals_and_software | concrete_work_services | construction_materials | consulting_public_relations | correspondence_schools | cosmetic_stores | counseling_services | country_clubs | courier_services | court_costs | credit_reporting_agencies | cruise_lines | dairy_products_stores | dance_hall_studios_schools | dating_escort_services | dentists_orthodontists | department_stores | detective_agencies | direct_marketing_catalog_merchant | direct_marketing_combination_catalog_and_retail_merchant | direct_marketing_inbound_telemarketing | direct_marketing_insurance_services | direct_marketing_other | direct_marketing_outbound_telemarketing | direct_marketing_subscription | direct_marketing_travel | discount_stores | doctors | door_to_door_sales | drapery_window_covering_and_upholstery_stores | drinking_places | drug_stores_and_pharmacies | drugs_drug_proprietaries_and_druggist_sundries | dry_cleaners | durable_goods | duty_free_stores | eating_places_restaurants | educational_services | electric_razor_stores | electrical_parts_and_equipment | electrical_services | electronics_repair_shops | electronics_stores | elementary_secondary_schools | employment_temp_agencies | equipment_rental | exterminating_services | family_clothing_stores | fast_food_restaurants | financial_institutions | fines_government_administrative_entities | fireplace_fireplace_screens_and_accessories_stores | floor_covering_stores | florists | florists_supplies_nursery_stock_and_flowers | freezer_and_locker_meat_provisioners | fuel_dealers_non_automotive | funeral_services_crematories | furniture_home_furnishings_and_equipment_stores_except_appliances | furniture_repair_refinishing | furriers_and_fur_shops | general_services | gift_card_novelty_and_souvenir_shops | glass_paint_and_wallpaper_stores | glassware_crystal_stores | golf_courses_public | government_services | grocery_stores_supermarkets | hardware_equipment_and_supplies | hardware_stores | health_and_beauty_spas | hearing_aids_sales_and_supplies | heating_plumbing_a_c | hobby_toy_and_game_shops | home_supply_warehouse_stores | hospitals | hotels_motels_and_resorts | household_appliance_stores | industrial_supplies | information_retrieval_services | insurance_default | insurance_underwriting_premiums | intra_company_purchases | jewelry_stores_watches_clocks_and_silverware_stores | landscaping_services | laundries | laundry_cleaning_services | legal_services_attorneys | luggage_and_leather_goods_stores | lumber_building_materials_stores | manual_cash_disburse | marinas_service_and_supplies | masonry_stonework_and_plaster | massage_parlors | means_womens_clothing_stores | medical_and_dental_labs | medical_dental_ophthalmic_and_hospital_equipment_and_supplies | medical_services | membership_organizations | mens_and_boys_clothing_and_accessories_stores | metal_service_centers | miscellaneous | miscellaneous_apparel_and_accessory_shops | miscellaneous_auto_dealers | miscellaneous_business_services | miscellaneous_food_stores | miscellaneous_general_merchandise | miscellaneous_general_services | miscellaneous_home_furnishing_specialty_stores | miscellaneous_publishing_and_printing | miscellaneous_recreation_services | miscellaneous_repair_shops | miscellaneous_specialty_retail | mobile_home_dealers | motion_picture_theaters | motor_freight_carriers_and_trucking | motor_homes_dealers | motor_vehicle_supplies_and_new_parts | motorcycle_shops_and_dealers | motorcycle_shops_dealers | music_stores_musical_instruments_pianos_and_sheet_music | news_dealers_and_newsstands | non_fi_money_orders | non_fi_stored_value_card_purchase_load | nondurable_goods | nurseries_lawn_and_garden_supply_stores | nursing_personal_care | office_and_commercial_furniture | opticians_eyeglasses | optometrists_ophthalmologist | orthopedic_goods_prosthetic_devices | osteopaths | package_stores_beer_wine_and_liquor | paints_varnishes_and_supplies | parking_lots_garages | passenger_railways | pawn_shops | pet_shops_pet_food_and_supplies | petroleum_and_petroleum_products | photo_developing | photographic_photocopy_microfilm_equipment_and_supplies | photographic_studios | picture_video_production | piece_goods_notions_and_other_dry_goods | plumbing_heating_equipment_and_supplies | political_organizations | postal_services_government_only | precious_stones_and_metals_watches_and_jewelry | professional_services | public_warehousing_and_storage | quick_copy_repro_and_blueprint | railroads | real_estate_agents_and_managers_rentals | record_stores | recreational_vehicle_rentals | religious_goods_stores | religious_organizations | roofing_siding_sheet_metal | secretarial_support_services | security_brokers_dealers | service_stations | sewing_needlework_fabric_and_piece_goods_stores | shoe_repair_hat_cleaning | shoe_stores | small_appliance_repair | snowmobile_dealers | special_trade_services | specialty_cleaning | sporting_goods_stores | sporting_recreation_camps | sports_and_riding_apparel_stores | sports_clubs_fields | stamp_and_coin_stores | stationary_office_supplies_printing_and_writing_paper | stationery_stores_office_and_school_supply_stores | swimming_pools_sales | t_ui_travel_germany | tailors_alterations | tax_payments_government_agencies | tax_preparation_services | taxicabs_limousines | telecommunication_equipment_and_telephone_sales | telecommunication_services | telegraph_services | tent_and_awning_shops | testing_laboratories | theatrical_ticket_agencies | timeshares | tire_retreading_and_repair | tolls_bridge_fees | tourist_attractions_and_exhibits | towing_services | trailer_parks_campgrounds | transportation_services | travel_agencies_tour_operators | truck_stop_iteration | truck_utility_trailer_rentals | typesetting_plate_making_and_related_services | typewriter_stores | u_s_federal_government_agencies_or_departments | uniforms_commercial_clothing | used_merchandise_and_secondhand_stores | utilities | variety_stores | veterinary_services | video_amusement_game_supplies | video_game_arcades | video_tape_rental_stores | vocational_trade_schools | watch_jewelry_repair | welding_repair | wholesale_clubs | wig_and_toupee_stores | wires_money_orders | womens_accessory_and_specialty_shops | womens_ready_to_wear_stores | wrecking_and_salvage_yards" ],
    "max_amount" : "integer"
  },
  "status" : "Specifies whether to permit authorizations on this card. Possible values are `active`, `inactive`, or `canceled`."
}
```

</details>

## update_issuing_cardholder

Updates the specified Issuing Cardholder object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### cardholder (required)

The ID of the cardholder to update.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "name" : "The name of the cardholder, printed on the card.",
  "phone_number" : "The cardholder's phone number.",
  "email" : "The cardholder's email address.",
  "billing" : {
    "address" : {
      "country" : "Required string",
      "city" : "Required string",
      "state" : "string",
      "postal_code" : "Required string",
      "line2" : "string",
      "line1" : "Required string"
    },
    "name" : "string"
  },
  "status" : "Specifies whether to permit authorizations on this cardholder's cards. Possible values are `active` or `inactive`."
}
```

</details>

## update_issuing_dispute

Updates the specified Issuing Dispute object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### dispute (required)

The ID of the dispute to update.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## update_issuing_transaction

Updates the specified Issuing Transaction object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### transaction (required)

The identifier of the transaction to update.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## update_order

Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "coupon" : "A coupon code that represents a discount to be applied to this order. Must be one-time duration and in same currency as the order.",
  "shipping" : {
    "carrier" : "Required string",
    "tracking_number" : "Required string"
  },
  "selected_shipping_method" : "The shipping method to select for fulfilling this order. If specified, must be one of the `id`s of a shipping method in the `shipping_methods` array. If specified, will overwrite the existing selected shipping method, updating `items` as necessary.",
  "status" : "Current order status. One of `created`, `paid`, `canceled`, `fulfilled`, or `returned`. More detail in the [Orders Guide](/docs/orders/guide#understanding-order-statuses)."
}
```

</details>

## update_payment_intent

Updates a PaymentIntent object.

<details><summary>Parameters</summary>

### intent (required)

**Type:** string

### $body

**Type:** object

```json
{
  "amount" : "Amount intended to be collected by this PaymentIntent",
  "metadata" : { },
  "transfer_group" : "A string that identifies the resulting payment as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](/docs/connect/charges-transfers#grouping-transactions) for details.",
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users.",
  "source" : "ID of the Source object to attach to this PaymentIntent.",
  "transfer_data" : {
    "amount" : "integer"
  },
  "expand" : [ "string" ],
  "receipt_email" : "Email address that the receipt for the resulting payment will be sent to.",
  "return_url" : "The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "save_source_to_customer" : "`true` to save this PaymentIntent's Source to the associated Customer, if the Source is not already attached.",
  "application_fee_amount" : "The amount of the application fee (if any) for the resulting payment. [See the Connect documentation](/docs/connect/direct-charges#collecting-fees) for details.",
  "customer" : "ID of the customer this PaymentIntent is for if one exists."
}
```

</details>

## update_payout

Updates the specified payout by setting the values of the parameters passed. Any parameters not provided will be left unchanged. This request accepts only the metadata as arguments.

<details><summary>Parameters</summary>

### payout (required)

The identifier of the payout to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## update_plan

Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.

<details><summary>Parameters</summary>

### plan (required)

The identifier of the plan to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "statement_descriptor" : "An arbitrary string to be displayed on your customer's credit card statement. This may be up to 22 characters. The statement description may not include &lt;&gt;\"' characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all. It must contain at least one letter.",
  "expand" : [ "string" ],
  "metadata" : { },
  "product" : "The product the plan belongs to. Note that after updating, statement descriptors and line items of the plan in active subscriptions will be affected.",
  "name" : "The plan name. Customers may see this value on Stripe-generated invoices and receipts.",
  "nickname" : "A brief description of the plan, hidden from customers.",
  "active" : "Whether the plan is currently available for new subscriptions.",
  "trial_period_days" : "Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](/docs/api#create_subscription-trial_from_plan)."
}
```

</details>

## update_platform_earning_refund

Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request only accepts metadata as an argument.

<details><summary>Parameters</summary>

### fee (required)

ID of the application fee refunded.

**Type:** string

### id (required)

ID of refund to retrieve.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## update_point_of_sale_location

Updates a Location object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### location (required)

The identifier of the location to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "address" : {
    "country" : "Required string",
    "city" : "Required string",
    "state" : "string",
    "postal_code" : "Required string",
    "line2" : "string",
    "line1" : "Required string"
  },
  "display_name" : "A name for the location.",
  "operator_account" : "The identifier of the new account associated with this location."
}
```

</details>

## update_point_of_sale_reader

Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

<details><summary>Parameters</summary>

### reader (required)

The identifier of the reader to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "label" : "The new label of the reader.",
  "operator_account" : "The identifier of the new account associated with this reader."
}
```

</details>

## update_product

Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
Note that a product’s attributes are not editable. Instead, you would need to deactivate the existing product and create a new one with the new attribute values.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "deactivate_on" : [ "string" ],
  "images" : [ "string" ],
  "metadata" : { },
  "active" : "Whether the product is available for purchase.",
  "caption" : "A short one-line description of the product, meant to be displayable to the customer.",
  "description" : "The product's description, meant to be displayable to the customer.",
  "url" : "A URL of a publicly-accessible webpage for this product.",
  "package_dimensions" : {
    "length" : "Required number",
    "width" : "Required number",
    "weight" : "Required number",
    "height" : "Required number"
  },
  "statement_descriptor" : "An arbitrary string to be displayed on your customer's credit card statement. This may be up to 22 characters. The statement description may not include &lt;&gt;\"' characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all. It must contain at least one letter. May only be set if type=`service`.",
  "expand" : [ "string" ],
  "shippable" : "Whether this product is shipped (i.e., physical goods). Defaults to `true`.",
  "name" : "The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types.",
  "attributes" : [ "string" ],
  "unit_label" : "A label that represents units of this product, such as seat(s), in Stripe and on customers’ receipts and invoices. Only available on products of type=`service`."
}
```

</details>

## update_refund

Updates the specified refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request only accepts metadata as an argument.

<details><summary>Parameters</summary>

### refund (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## update_sku

Updates the specific SKU by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
Note that a SKU’s attributes are not editable. Instead, you would need to deactivate the existing SKU and create a new one with the new attribute values.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "package_dimensions" : {
    "length" : "Required number",
    "width" : "Required number",
    "weight" : "Required number",
    "height" : "Required number"
  },
  "image" : "The URL of an image for this SKU, meant to be displayable to the customer.",
  "expand" : [ "string" ],
  "metadata" : { },
  "product" : "The ID of the product that this SKU should belong to. The product must exist, have the same set of attribute names as the SKU's current product, and be of type `good`.",
  "price" : "The cost of the item as a positive integer in the smallest currency unit (that is, 100 cents to charge $1.00, or 100 to charge ¥100, Japanese Yen being a zero-decimal currency).",
  "active" : "Whether this SKU is available for purchase.",
  "attributes" : "A dictionary of attributes and values for the attributes defined by the product. When specified, `attributes` will partially update the existing attributes dictionary on the product, with the postcondition that a value must be present for each attribute key on the product, and that all SKUs for the product must have unique sets of attributes.",
  "currency" : "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).",
  "inventory" : {
    "quantity" : "integer",
    "type" : "string. Possible values: bucket | finite | infinite",
    "value" : "string. Possible values:  | in_stock | limited | out_of_stock"
  }
}
```

</details>

## update_source

Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request accepts the metadata and owner as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our payment method guides for more detail.

<details><summary>Parameters</summary>

### source (required)

**Type:** string

### $body

**Type:** object

```json
{
  "owner" : {
    "address" : {
      "country" : "string",
      "city" : "string",
      "state" : "string",
      "postal_code" : "string",
      "line2" : "string",
      "line1" : "string"
    },
    "phone" : "string",
    "name" : "string",
    "email" : "string"
  },
  "expand" : [ "string" ],
  "mandate" : {
    "notification_method" : "string. Possible values: email | manual | none",
    "acceptance" : {
      "date" : "Required integer",
      "ip" : "Required string",
      "user_agent" : "Required string",
      "status" : "Required string. Possible values: accepted | pending | refused | revoked"
    }
  },
  "metadata" : { }
}
```

</details>

## update_subscription

Updates an existing subscription on a customer to match the specified parameters. When changing plans or quantities, we will optionally prorate the price we charge next month to make up for any price changes. To preview how the proration will be calculated, use the upcoming invoice endpoint.

<details><summary>Parameters</summary>

### subscription_exposed_id (required)

The identifier of the subscription to update.

**Type:** string

### $body

**Type:** object

```json
{
  "metadata" : { },
  "cancel_at_period_end" : "Boolean indicating whether this subscription should cancel at the end of the current period.",
  "coupon" : "The code of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription.",
  "days_until_due" : "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `billing` is set to `send_invoice`.",
  "trial_end" : "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately.",
  "application_fee_percent" : "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account. The request must be made with an OAuth key in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).",
  "billing_cycle_anchor" : "Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time. For more information, see the billing cycle [documentation](/docs/billing/subscriptions/billing-cycle).",
  "billing" : "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions. Defaults to `charge_automatically`.",
  "tax_percent" : "A non-negative decimal (with at most four decimal places) between 0 and 100. This represents the percentage of the subscription invoice subtotal that will be calculated and added as tax to the final amount in each billing period. For example, a plan which charges $10/month with a `tax_percent` of `20.0` will charge $12 per invoice. To unset a previously-set value, pass an empty string.",
  "expand" : [ "string" ],
  "trial_from_plan" : "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed.",
  "items" : [ {
    "metadata" : { },
    "deleted" : "boolean",
    "quantity" : "integer",
    "clear_usage" : "boolean",
    "id" : "string",
    "plan" : "string"
  } ],
  "prorate" : "Boolean (defaults to `true`) telling us whether to [credit for unused time](/docs/subscriptions/billing-cycle#prorations) when the billing cycle changes (e.g. when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial). If `false`, the anchor period will be free (similar to a trial) and no proration adjustments will be created.",
  "proration_date" : "If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](#retrieve_customer_invoice) endpoint. It can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations."
}
```

</details>

## update_subscription_item

Updates the plan or quantity of an item on a current subscription.

<details><summary>Parameters</summary>

### item (required)

The identifier of the subscription item to modify.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "quantity" : "The quantity you'd like to apply to the subscription item you're creating.",
  "plan" : "The identifier of the new plan for this subscription item.",
  "prorate" : "Flag indicating whether to [prorate](/docs/subscriptions/upgrading-downgrading#understanding-proration) switching plans during a billing cycle.",
  "proration_date" : "If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](#retrieve_customer_invoice) endpoint."
}
```

</details>

## update_topup

Updates the metadata of a top-up. Other top-up details are not editable by design.

<details><summary>Parameters</summary>

### topup (required)

The ID of the top-up to retrieve.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users."
}
```

</details>

## update_transfer

Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request accepts only metadata as an argument.

<details><summary>Parameters</summary>

### transfer (required)

The ID of the transfer to be updated.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "description" : "An arbitrary string attached to the object. Often useful for displaying to users."
}
```

</details>

## update_transfer_recipient

Updates the specified recipient by setting the values of the parameters passed.Any parameters not provided will be left unchanged.
If you update the name or tax ID, the identity verification will automatically be rerun.If you update the bank account, the bank account validation will automatically be rerun.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { },
  "default_card" : "ID of the card to set as the recipient's new default for payouts.",
  "name" : "The recipient's full, legal name. For type `individual`, should be in the format `First Last`, `First Middle Last`, or `First M Last` (no prefixes or suffixes). For `corporation`, the full, incorporated name.",
  "description" : "An arbitrary string which you can attach to a `Recipient` object. It is displayed alongside the recipient in the web interface.",
  "card" : { },
  "email" : "The recipient's email address. It is displayed alongside the recipient in the web interface, and can be useful for searching and tracking.",
  "tax_id" : "The recipient's tax ID, as a string. For type `individual`, the full SSN; for type `corporation`, the full EIN.",
  "bank_account" : { }
}
```

</details>

## update_transfer_reversal

Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
This request only accepts metadata and description as arguments.

<details><summary>Parameters</summary>

### id (required)

ID of reversal to retrieve.

**Type:** string

### transfer (required)

ID of the transfer reversed.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "metadata" : { }
}
```

</details>

## verify_customer_source



<details><summary>Parameters</summary>

### customer (required)

**Type:** string

### id (required)

The ID of the source to be verified.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "amounts" : [ "integer" ],
  "verification_method" : "string"
}
```

</details>

## verify_source



<details><summary>Parameters</summary>

### source (required)

The ID of the desired source.

**Type:** string

### $body

**Type:** object

```json
{
  "expand" : [ "string" ],
  "values" : [ "string" ]
}
```

</details>

