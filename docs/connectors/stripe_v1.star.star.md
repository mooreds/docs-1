---
id: stripe-documentation
title: Stripe (version v1.*.*)
---

## cancel_payment_intent

<p>A PaymentIntent object can be canceled when it is in one of these statues: <code>requires_source</code>, <code>requires_capture</code>, <code>requires_confirmation</code>, or <code>requires_source_action</code>. </p><p>Once canceled, no additional charges will be made by the PaymentIntent and any operations on the PaymentIntent will fail with an error. For PaymentIntents with <code>status='requires_capture'</code>, the remaining <code>amount_capturable</code> will automatically be refunded.</p>

<details><summary>Parameters</summary>

#### intent (required)

**Type:** string

#### $body

**Type:** object

</details>

## cancel_payout

<p>A previously created payout can be canceled if it has not yet been paid out. Funds will be refunded to your available balance. You may not cancel automatic Stripe payouts.</p>

<details><summary>Parameters</summary>

#### payout (required)

The identifier of the payout to be canceled.

**Type:** string

#### $body

**Type:** object

</details>

## cancel_topup

<p>Cancels a top-up. Only pending top-ups can be canceled.</p>

<details><summary>Parameters</summary>

#### topup (required)

The ID of the top-up to cancel.

**Type:** string

#### $body

**Type:** object

</details>

## charge_capture

<p>Capture the payment of an existing, uncaptured, charge. This is the second half of the two-step payment flow, where first you <a href="#create_charge">created a charge</a> with the capture option set to false.</p><p>Uncaptured payments expire exactly seven days after they are created. If they are not captured by that point in time, they will be marked as refunded and will no longer be capturable.</p>

<details><summary>Parameters</summary>

#### charge (required)

**Type:** string

#### $body

**Type:** object

</details>

## close_dispute

<p>Closing the dispute for a charge indicates that you do not have any evidence to submit and are essentially dismissing the dispute, acknowledging it as lost.</p><p>The status of the dispute will change from <code>needs_response</code> to <code>lost</code>. <em>Closing a dispute is irreversible</em>.</p>

<details><summary>Parameters</summary>

#### dispute (required)

ID of the dispute to close.

**Type:** string

#### $body

**Type:** object

</details>

## create_account

<p>With <a href="/docs/connect">Connect</a>, you can create Stripe accounts for your users.To do this, you’ll first need to <a href="https://dashboard.stripe.com/account/applications/settings">register your platform</a>.</p><p>For Standard accounts, parameters other than <code>country</code>, <code>email</code>, and <code>type</code>are used to prefill the account application that we ask the account holder to complete.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_bank_account



<details><summary>Parameters</summary>

#### account (required)

**Type:** string

#### $body

**Type:** object

</details>

## create_card_token

<p>Creates a single-use token that represents a bank account’s details.This token can be used in place of a bank account dictionary with any API method.These tokens can be used only once: by attaching them to a <a href="#create_recipient">recipient</a> or <a href="#account">Custom account</a>.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_charge

<p>To charge a credit card or other payment source, you create a <code>Charge</code> object. If your API key is in test mode, the supplied payment source (e.g., card) won’t actually be charged, although everything else will occur as if in live mode. (Stripe assumes that the charge would have completed successfully).</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_coupon

<p>You can create coupons easily via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.</p><p>A coupon has either a <code>percent_off</code> or an <code>amount_off</code> and <code>currency</code>. If you set an <code>amount_off</code>, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of <currency>100</currency> will have a final total of <currency>0</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it and an invoice with a subtotal of <currency>300</currency> will have a final total of <currency>100</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_customer

<p>Creates a new customer object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_customer_source

<p>When you create a new credit card, you must specify a customer or recipient on which to create it.</p><p>If the card’s owner has no default card, then the new card will become the default.However, if the owner already has a default, then it will not change.To change the default, you should either <a href="/docs/api#update_customer">update the customer</a> to have a new <code>default_source</code>,or <a href="/docs/api#update_recipient">update the recipient</a> to have a new <code>default_card</code>.</p>

<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

#### $body

**Type:** object

</details>

## create_customer_subscription

<p>Creates a new subscription on an existing customer.</p>

<details><summary>Parameters</summary>

#### customer (required)

The identifier of the customer to subscribe.

**Type:** string

#### $body

**Type:** object

</details>

## create_file_link

<p>Creates a new file link object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_invoice

<p>If you need to invoice your customer outside the regular billing cycle, you can create an invoice that pulls in all pending invoice items, including prorations. The customer’s billing cycle and regular subscription won’t be affected.</p><p>Once you create the invoice, Stripe will attempt to collect payment according to your <a href="https://dashboard.stripe.com/account/recurring">subscriptions settings</a>, though you can choose to <a href="#pay_invoice">pay it right</a> away.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_invoice_item

<p>Adds an arbitrary charge or credit to the customer’s upcoming invoice.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_issuing_card

<p>Creates an Issuing <code>Card</code> object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_issuing_cardholder

<p>Creates a new Issuing <code>Cardholder</code> object that can be issued cards.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_issuing_dispute

<p>Creates an Issuing <code>Dispute</code> object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_login_link

<p>Creates a single-use login link for an Express account to access their Stripe dashboard.</p><p><strong>You may only create login links for <a href="/docs/connect/express-accounts">Express accounts</a> connected to your platform</strong>.</p>

<details><summary>Parameters</summary>

#### account (required)

The identifier of the account to create a login link for.

**Type:** string

#### $body

**Type:** object

</details>

## create_order

<p>Creates a new <code>Order</code> object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_order_return

<p>Return all or part of an order. The order must have a status of <code>paid</code> or <code>fulfilled</code> before it can be returned. Once all items have been returned, the order will become <code>canceled</code> or <code>returned</code> depending on which status the order started in.</p>

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## create_payment



<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_payment_intent

<p>Creates a PaymentIntent object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_payout

<p>To send funds to your own bank account, you create a new payout object. Your <a href="#balance">Stripe balance</a> must be able to cover the payout amount, or you’ll receive an “Insufficient Funds” error.</p><p>If your API key is in test mode, money won’t actually be sent, though everything else will occur as if in live mode.</p><p>If you are creating a manual payout on a Stripe account that uses multiple payment source types, you’ll need to specify the source type balance that the payout should draw from. The <a href="#balance_object">balance object</a> details available and pending amounts by source type.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_plan

<p>You can create plans using the API, or in the Stripe <a href="https://dashboard.stripe.com/subscriptions/products">Dashboard</a>.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_platform_earning_refund

<p>Refunds an application fee that has previously been collected but not yet refunded.Funds will be refunded to the Stripe account from which the fee was originally collected.</p><p>You can optionally refund only part of an application fee.You can do so multiple times, until the entire fee has been refunded.</p><p>Once entirely refunded, an application fee can’t be refunded again.This method will raise an error when called on an already-refunded application fee,or when trying to refund more money than is left on an application fee.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the application fee to be refunded.

**Type:** string

#### $body

**Type:** object

</details>

## create_point_of_sale_connection_token

<p>To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_point_of_sale_location

<p>Creates a new <code>Location</code> object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_point_of_sale_reader

<p>Creates a new <code>Reader</code> object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_product

<p>Creates a new product object. To create a product for use with subscriptions, see <a href="#create_service_product">Subscriptions Products</a>.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_refund



<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_sku

<p>Creates a new SKU associated with a product.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_source

<p>Creates a new source object.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_subscription

<p>Creates a new subscription on an existing customer.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_subscription_item

<p>Adds a new item to an existing subscription. No existing items will be changed or replaced.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_tax_rate_template



*This operation has no parameters*

## create_topup

<p>Top up the balance of an account</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_transfer

<p>To send funds from your Stripe account to a connected account, you create a new transfer object. Your <a href="#balance">Stripe balance</a> must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_transfer_recipient

<p>Creates a new <code>Recipient</code> object and verifies the recipient’s identity.Also verifies the recipient’s bank account information or debit card, if either is provided.</p>

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_transfer_reversal

<p>When you create a new reversal, you must specify a transfer to create it on.</p><p>When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.</p><p>Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.</p>

<details><summary>Parameters</summary>

#### id (required)

The ID of the transfer to be reversed.

**Type:** string

#### $body

**Type:** object

</details>

## create_usage_record

<p>Creates a usage record for a specified subscription item and date, and fills it with a quantity.</p>

<details><summary>Parameters</summary>

#### subscription_item (required)

The ID of the subscription item for this usage record.

**Type:** string

#### $body

**Type:** object

</details>

## decline_issuing_authorization

<p>Declines a pending Issuing <code>Authorization</code> object.</p>

<details><summary>Parameters</summary>

#### authorization (required)

The identifier of the issuing authorization to decline.

**Type:** string

#### $body

**Type:** object

</details>

## delete_account

<p>With <a href="/docs/connect">Connect</a>, you may delete Custom accounts you manage.</p><p>Custom accounts created using test-mode keys can be deleted at any time. Custom accounts created using live-mode keys may only be deleted once all balances are zero.</p><p>If you are looking to close your own account, use the <a href="https://dashboard.stripe.com/account/data">data tab in your account settings</a> instead.</p>

<details><summary>Parameters</summary>

#### account (required)

The identifier of the account to be deleted. If none is provided, will default to the account of the API key.

**Type:** string

</details>

## delete_bank_account



<details><summary>Parameters</summary>

#### account (required)

**Type:** string

#### id (required)

The ID of the external account to be deleted.

**Type:** string

</details>

## delete_coupon

<p>You can delete coupons via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.</p>

<details><summary>Parameters</summary>

#### coupon (required)

The identifier of the coupon to be deleted.

**Type:** string

</details>

## delete_customer

<p>Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.</p>

<details><summary>Parameters</summary>

#### customer (required)

The identifier of the customer to be deleted.

**Type:** string

</details>

## delete_customer_discount

<p>Removes the currently applied discount on a customer.</p>

<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

</details>

## delete_customer_source



<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

#### id (required)

The ID of the source to be deleted.

**Type:** string

</details>

## delete_invoice_item

<p>Removes an invoice item from the upcoming invoice. Removing an invoice item is only possible before the invoice it’s attached to is closed.</p>

<details><summary>Parameters</summary>

#### invoiceitem (required)

The identifier of the invoice item to be deleted.

**Type:** string

</details>

## delete_plan

<p>Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.</p>

<details><summary>Parameters</summary>

#### plan (required)

The identifier of the plan to be deleted.

**Type:** string

</details>

## delete_product

<p>Delete a product. Deleting a product with type=<code>good</code> is only possible if it has no SKUs associated with it. Deleting a product with type=<code>service</code> is only possible if it has no plans associated with it.</p>

<details><summary>Parameters</summary>

#### id (required)

The ID of the product to delete.

**Type:** string

</details>

## delete_sku

<p>Delete a SKU. Deleting a SKU is only possible until it has been used in an order.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the SKU to be deleted.

**Type:** string

</details>

## delete_subscription

<p>Cancels a customer’s subscription immediately. The customer will not be charged again for the subscription.</p><p>Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.</p><p>By default, upon subscription cancellation, Stripe will close all unpaid invoices for the customer. This is designed to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can reopen the invoices manually after subscription cancellation to have us proceed with payment collection. Or, you could even re-attempt payment yourself on all unpaid invoices before allowing the customer to cancel the subscription at all.</p>

<details><summary>Parameters</summary>

#### subscription_exposed_id (required)

**Type:** string

</details>

## delete_subscription_discount

<p>Removes the currently applied discount on a subscription.</p>

<details><summary>Parameters</summary>

#### subscription_exposed_id (required)

**Type:** string

</details>

## delete_subscription_item

<p>Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.</p>

<details><summary>Parameters</summary>

#### item (required)

The identifier of the subscription item to delete.

**Type:** string

#### $body

**Type:** object

</details>

## delete_tax_rate_template



*This operation has no parameters*

## delete_transfer_recipient

<p>Permanently deletes a recipient. It cannot be undone.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the recipient to be deleted.

**Type:** string

</details>

## get_account

<p>Retrieves the details of the account.</p>

<details><summary>Parameters</summary>

#### account (required)

The identifier of the account to retrieve. If none is provided, the account associated with the API key is returned.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_accounts

<p>Returns a list of accounts connected to your platform via <a href="/docs/connect">Connect</a>. If you’re not a platform, the list is empty.</p>

<details><summary>Parameters</summary>

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_balance_transactions

<p>Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.</p>

<details><summary>Parameters</summary>

#### available_on

**Type:** object

#### created

**Type:** object

#### currency

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### payout

For automatic Stripe payouts only, only returns transactions that were payed out on the specified payout ID.

**Type:** string

#### source

Only returns the original transaction.

**Type:** string

#### type

Only returns transactions of the given type. One of: `charge`, `refund`, `adjustment`, `application_fee`, `application_fee_refund`, `transfer`, `payment`, `payout`, `payout_failure`, `stripe_fee`, or `network_cost`.

**Type:** string

</details>

## get_all_charges

<p>Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### customer

Only return charges for the customer specified by this customer ID.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### source

A filter on the list, based on the source of the charge. The value can be a dictionary with the following options:

**Type:** object

#### transfer_group

Only return charges for this transfer group.

**Type:** string

</details>

## get_all_country_specs

<p>Lists all Country Spec objects available in the API.</p>

<details><summary>Parameters</summary>

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_coupons

<p>Returns a list of your coupons.</p>

<details><summary>Parameters</summary>

#### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_customer_sources



<details><summary>Parameters</summary>

#### customer (required)

The ID of the customer whose sources will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### object

Filter sources according to a particular object type.

**Type:** string

#### type

**Type:** string

</details>

## get_all_customer_subscriptions

<p>You can see a list of the customer’s active subscriptions. Note that the 10 most recent active subscriptions are always available by default on the customer object. If you need more than those 10, you can use the limit and starting_after parameters to page through additional subscriptions.</p>

<details><summary>Parameters</summary>

#### customer (required)

The ID of the customer whose subscriptions will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_customers

<p>Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### email

A filter on the list based on the customer's `email` field. The value must be a string.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_disputes

<p>Returns a list of your disputes.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_external_accounts



<details><summary>Parameters</summary>

#### account (required)

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_file_links

<p>Returns a list of file links.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### expired

Filter links by their expiration status. By default, all links are returned.

**Type:** boolean

#### file

Only return links for the given file.

**Type:** string

</details>

## get_all_files

<p>Returns a list of the files that your account has access to. The files are returned sorted by creation date, with the most recently created files appearing first.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### purpose

The file purpose to filter queries by. If none is provided, files will not be filtered by purpose.

**Type:** string

**Potential values:** additional_verification, bootstrap_pilot_user_report, business_logo, customer_signature, dispute_evidence, finance_report_run, founders_stock_document, identity_document, incorporation_article, incorporation_document, india_export_payment_advice, invoice_statement, paper_check_image, payment_provider_transfer, pci_document, product_feed, sigma_scheduled_query, support_attachment, tandem_accepted, tandem_requested, tandem_voidance, tax_document, tax_document_user_upload, works_with_image

</details>

## get_all_invoice_items

<p>Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### customer

The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### invoice

Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.

**Type:** string

</details>

## get_all_invoice_lines

<p>When retrieving an invoice, you’ll get a <strong>lines</strong> property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

<details><summary>Parameters</summary>

#### invoice (required)

The ID of the invoice containing the lines to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_invoices

<p>You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.</p>

<details><summary>Parameters</summary>

#### billing

The billing mode of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.

**Type:** string

**Potential values:** charge_automatically, send_invoice

#### customer

Only return invoices for the customer specified by this customer ID.

**Type:** string

#### date

**Type:** object

#### due_date

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### subscription

Only return invoices for the subscription specified by this subscription ID.

**Type:** string

</details>

## get_all_issuing_authorizations

<p>Returns a list of Issuing <code>Authorization</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

<details><summary>Parameters</summary>

#### card

Only return issuing transactions that belong to the given card.

**Type:** string

#### cardholder

Only return authorizations belonging to the given cardholder.

**Type:** string

#### created

Only return authorizations that were created during the given date interval.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### status

Only return authorizations with the given status. One of pending, closed, or reversed.

**Type:** string

**Potential values:** closed, pending, reversed

</details>

## get_all_issuing_cardholders

<p>Returns a list of Issuing <code>Cardholder</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

<details><summary>Parameters</summary>

#### created

Only return cardholders that were created during the given date interval.

**Type:** object

#### email

Only return cardholders that have the given email address.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### phone_number

Only return cardholders that have the given phone number.

**Type:** string

#### status

Only return cardholders that have the given status. One of `active` or `inactive`.

**Type:** string

**Potential values:** active, inactive

#### type

Only return cardholders that have the given type. One of One of `individual` or `business_entity`.

**Type:** string

**Potential values:** business_entity, individual

</details>

## get_all_issuing_cards

<p>Returns a list of Issuing <code>Card</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

<details><summary>Parameters</summary>

#### cardholder

Only return cards belonging to the Cardholder with the provided ID.

**Type:** string

#### created

Only return cards that were issued during the given date interval.

**Type:** object

#### exp_month

Only return cards that have the given expiration month.

**Type:** integer

#### exp_year

Only return cards that have the given expiration year.

**Type:** integer

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### last4

Only return cards that have the given last four digits.

**Type:** string

#### name

Only return cards that have the given name.

**Type:** string

#### source

Only return cards whose full card number matches that of this card source ID.

**Type:** string

#### status

Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.

**Type:** string

**Potential values:** active, canceled, inactive, lost, pending_compliance, stolen

#### type

Only return cards that have the given type. One of `virtual` or `physical`.

**Type:** string

**Potential values:** physical, virtual

</details>

## get_all_issuing_disputes

<p>Returns a list of Issuing <code>Dispute</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

<details><summary>Parameters</summary>

#### created

Only return issuing disputes that were created during the given date interval.

**Type:** object

#### disputed_transaction

Only return issuing disputes for the given transaction.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_issuing_transactions

<p>Returns a list of Issuing <code>Transaction</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

<details><summary>Parameters</summary>

#### card

Only return issuing transactions that belong to the given card.

**Type:** string

#### cardholder

Only return authorizations belonging to the given cardholder.

**Type:** string

#### created

Only return transactions that were created during the given date interval.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_notification_events

<p>List events, going back up to 30 days.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### delivery_success

Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned.

**Type:** boolean

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### type

A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property.

**Type:** string

#### types

An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both.

**Type:** array

</details>

## get_all_order_returns

<p>Returns a list of your order returns. The returns are returned sorted by creation date, with the most recently created return appearing first.</p>

<details><summary>Parameters</summary>

#### created

Date this return was created.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### order

The order to retrieve returns for.

**Type:** string

</details>

## get_all_orders

<p>Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.</p>

<details><summary>Parameters</summary>

#### created

Date this order was created.

**Type:** object

#### customer

Only return orders for the given customer.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### ids

Only return orders with the given IDs.

**Type:** array

#### status

Only return orders that have the given status. One of `created`, `paid`, `fulfilled`, or `refunded`.

**Type:** string

#### status_transitions

Filter orders based on when they were paid, fulfilled, canceled, or returned.

**Type:** object

#### upstream_ids

Only return orders with the given upstream order IDs.

**Type:** array

</details>

## get_all_payment_flows_payment_intent

<p>Returns a list of PaymentIntents.</p>

<details><summary>Parameters</summary>

#### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_payout

<p>Returns a list of existing payouts sent to third-party bank accounts or that Stripe has sent you. The payouts are returned in sorted order, with the most recently created payouts appearing first.</p>

<details><summary>Parameters</summary>

#### arrival_date

**Type:** object

#### created

**Type:** object

#### destination

The ID of an external account - only return payouts sent to this external account.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### status

Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`.

**Type:** string

</details>

## get_all_plans

<p>Returns a list of your plans.</p>

<details><summary>Parameters</summary>

#### active

Only return plans that are active or inactive (e.g., pass `false` to list all inactive products).

**Type:** boolean

#### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### product

Only return plans for the given product.

**Type:** string

</details>

## get_all_platform_earnings

<p>Returns a list of application fees you’ve previously collected. The application fees are returned in sorted order, with the most recent fees appearing first.</p>

<details><summary>Parameters</summary>

#### charge

Only return application fees for the charge specified by this charge ID.

**Type:** string

#### created

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_platform_earnings_refunds

<p>You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional refunds.</p>

<details><summary>Parameters</summary>

#### id (required)

The ID of the application fee whose refunds will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_point_of_sale_locations

<p>Returns a list of <code>Location</code> objects.</p>

<details><summary>Parameters</summary>

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### operator_account

The identifier of the account associated with this location.

**Type:** string

</details>

## get_all_point_of_sale_readers

<p>Returns a list of <code>Reader</code> objects.</p>

<details><summary>Parameters</summary>

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### location

A location id to filter the response list to only readers at the specific location

**Type:** string

#### operator_account

The identifier of the account associated with this reader.

**Type:** string

#### status

A status filter to filter readers to only offline or online readers

**Type:** string

</details>

## get_all_products

<p>Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.</p>

<details><summary>Parameters</summary>

#### active

Only return products that are active or inactive (e.g., pass `false` to list all inactive products).

**Type:** boolean

#### created

Only return products that were created during the given date interval.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### ids

Only return products with the given IDs.

**Type:** array

#### shippable

Only return products that can be shipped (i.e., physical, not digital products).

**Type:** boolean

#### type

Only return products of this type.

**Type:** string

**Potential values:** good, service

#### url

Only return products with the given url.

**Type:** string

</details>

## get_all_refunds

<p>Returns a list of all refunds you’ve previously created. The refunds are returned in sorted order, with the most recent refunds appearing first. For convenience, the 10 most recent refunds are always available by default on the charge object.</p>

<details><summary>Parameters</summary>

#### charge

Only return refunds for the charge specified by this charge ID.

**Type:** string

#### created

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_scheduled_query_runs

<p>Returns a list of scheduled query runs.</p>

<details><summary>Parameters</summary>

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_skus

<p>Returns a list of your SKUs. The SKUs are returned sorted by creation date, with the most recently created SKUs appearing first.</p>

<details><summary>Parameters</summary>

#### active

Only return SKUs that are active or inactive (e.g., pass `false` to list all inactive products).

**Type:** boolean

#### attributes

Only return SKUs that have the specified key/value pairs in this partially constructed dictionary. Can be specified only if `product` is also supplied. For instance, if the associated product has attributes `["color", "size"]`, passing in `attributes[color]=red` returns all the SKUs for this product that have `color` set to `red`.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### ids

Only return SKUs with the given IDs.

**Type:** array

#### in_stock

Only return SKUs that are either in stock or out of stock (e.g., pass `false` to list all SKUs that are out of stock). If no value is provided, all SKUs are returned.

**Type:** boolean

#### product

The ID of the product whose SKUs will be retrieved. Must be a product with type `good`.

**Type:** string

</details>

## get_all_subscription_item_period_summaries

<p>Returns a list of subscription item period summaries sorted in reverse-chronological order (newest first). The first entry represents the current period of usage; its ID is NOT stable until the period ends.</p>

<details><summary>Parameters</summary>

#### subscription_item (required)

Only summary items for the given subscription item.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_subscription_items

<p>Returns a list of your subscription items for a given subscription.</p>

<details><summary>Parameters</summary>

#### subscription (required)

The ID of the subscription whose items will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_subscriptions

<p>By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify <code>status=canceled</code>.</p>

<details><summary>Parameters</summary>

#### billing

The billing mode of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.

**Type:** string

**Potential values:** charge_automatically, send_invoice

#### created

**Type:** object

#### customer

The ID of the customer whose subscriptions will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### plan

The ID of the plan whose subscriptions will be retrieved.

**Type:** string

#### status

The status of the subscriptions to retrieve. One of: `trialing`, `active`, `past_due`, `unpaid`, `canceled`, or `all`. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Passing in a value of `all` will return subscriptions of all statuses.

**Type:** string

**Potential values:** active, all, canceled, past_due, trialing, unpaid

</details>

## get_all_topups

<p>Returns a list of top-ups.</p>

<details><summary>Parameters</summary>

#### amount

A positive integer in %s representing how much to transfer.

**Type:** object

#### created

A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### status

Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`.

**Type:** string

**Potential values:** canceled, failed, pending, succeeded

</details>

## get_all_transfer_recipients

<p>Returns a list of your recipients. The recipients are returned sorted by creation date, with the most recently created recipients appearing first.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### type

**Type:** string

**Potential values:** corporation, individual

#### verified

Only return recipients that are verified or unverified.

**Type:** boolean

</details>

## get_all_transfer_reversals

<p>You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional reversals.</p>

<details><summary>Parameters</summary>

#### id (required)

The ID of the transfer whose reversals will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_all_transfers

<p>Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.</p>

<details><summary>Parameters</summary>

#### created

**Type:** object

#### destination

Only return transfers for the destination specified by this account ID.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### transfer_group

Only return transfers with the specified transfer group.

**Type:** string

</details>

## get_all_upcoming_invoice_lines

<p>When retrieving an upcoming invoice, you’ll get a <strong>lines</strong> property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

<details><summary>Parameters</summary>

#### customer (required)

The customer of the upcoming invoice is required. In other cases it is ignored.

**Type:** string

#### coupon

The code of the coupon to apply. If `subscription` or `subscription_items` is provided, the invoice returned will preview updating or creating a subscription with that coupon. Otherwise, it will preview applying that coupon to the customer for the next upcoming invoice from among the customer's subscriptions. The invoice can be previewed without a coupon by passing this value as an empty string.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### subscription

The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.

**Type:** string

#### subscription_billing_cycle_anchor

For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.For existing subscriptions, the value can only be set to `now` or `unchanged`.

**Type:** object

#### subscription_cancel_at_period_end

Boolean indicating whether this subscription should cancel at the end of the current period.

**Type:** boolean

#### subscription_items

Preview updating the subscription with this list of items. Otherwise this parameter is ignored.

**Type:** array

#### subscription_prorate

If previewing an update to a subscription, this decides whether the preview will show the result of applying prorations or not. If set, one of `subscription_items` or `subscription`, and one of `subscription_items` or `subscription_trial_end` are required.

**Type:** boolean

#### subscription_proration_date

If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period, and cannot be before the subscription was on its current plan. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration` cannot be set to false.

**Type:** integer

#### subscription_tax_percent

If provided, the invoice returned will preview updating or creating a subscription with that tax percent. If set, one of `subscription_items` or `subscription` is required.

**Type:** number

#### subscription_trial_end

If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required.

**Type:** object

#### subscription_trial_from_plan

Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed.

**Type:** boolean

</details>

## get_application_fee_refund

<p>By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.</p>

<details><summary>Parameters</summary>

#### fee (required)

ID of the application fee refunded.

**Type:** string

#### id (required)

ID of refund to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_balance

<p>Retrieves the current account balance, based on the authentication that was used to make the request.</p>

<details><summary>Parameters</summary>

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_balance_transaction

<p>Retrieves the balance transaction with the given ID.</p>

<details><summary>Parameters</summary>

#### id (required)

The ID of the desired balance transaction, as found on any API object that affects the balance (e.g., a charge or transfer).

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_charge

<p>Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.</p>

<details><summary>Parameters</summary>

#### charge (required)

The identifier of the charge to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_country_spec

<p>Returns a Country Spec for a given Country code.</p>

<details><summary>Parameters</summary>

#### country (required)

An ISO 3166-1 alpha-2 country code. Available country codes can be listed with the [List Country Specs](/docs/api#list_country_specs) endpoint.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_coupon

<p>Retrieves the coupon with the given ID.</p>

<details><summary>Parameters</summary>

#### coupon (required)

The ID of the desired coupon.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_customer

<p>Retrieves the details of an existing customer. You need only supply the unique customer identifier that was returned upon customer creation.</p>

<details><summary>Parameters</summary>

#### customer (required)

The identifier of the customer to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_customer_discount



<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_customer_source



<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

#### id (required)

The ID of the source to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_dispute

<p>Retrieves the dispute with the given ID.</p>

<details><summary>Parameters</summary>

#### dispute (required)

ID of dispute to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_external_account



<details><summary>Parameters</summary>

#### account (required)

**Type:** string

#### id (required)

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_file

<p>Retrieves the details of an existing file object. Supply the unique file ID from a file, and Stripe will return the corresponding file object.</p>

<details><summary>Parameters</summary>

#### file (required)

The identifier of the file to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_file_link

<p>Retrieves the file link with the given ID.</p>

<details><summary>Parameters</summary>

#### link (required)

The identifier of the file link to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_invoice

<p>Retrieves the invoice with the given ID.</p>

<details><summary>Parameters</summary>

#### invoice (required)

The identifier of the desired invoice.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_invoice_item

<p>Retrieves the invoice item with the given ID.</p>

<details><summary>Parameters</summary>

#### invoiceitem (required)

The ID of the desired invoice item.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_issuing_authorization

<p>Retrieves an Issuing <code>Authorization</code> object.</p>

<details><summary>Parameters</summary>

#### authorization (required)

The ID of the authorization to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_issuing_card

<p>Retrieves an Issuing <code>Card</code> object.</p>

<details><summary>Parameters</summary>

#### card (required)

The identifier of the card to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_issuing_card_details

<p>For virtual cards only. Retrieves an Issuing <code>Card_details</code> object that contains <a href="/docs/issuing/cards/management#virtual-card-info">the sensitive details</a> of a virtual card.</p>

<details><summary>Parameters</summary>

#### card (required)

The identifier of the virtual card to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_issuing_cardholder

<p>Retrieves an Issuing <code>Cardholder</code> object.</p>

<details><summary>Parameters</summary>

#### cardholder (required)

The identifier of the cardholder to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_issuing_dispute

<p>Retrieves an Issuing <code>Dispute</code> object.</p>

<details><summary>Parameters</summary>

#### dispute (required)

The ID of the dispute to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_issuing_transaction

<p>Retrieves an Issuing <code>Transaction</code> object.</p>

<details><summary>Parameters</summary>

#### transaction (required)

The ID of the transaction to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_notification_event

<p>Retrieves the details of an event. Supply the unique identifier of the event, which you might have received in a webhook.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the event to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_order

<p>Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the order to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_order_return

<p>Retrieves the details of an existing order return. Supply the unique order ID from either an order return creation request or the order return list, and Stripe will return the corresponding order information.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the order return to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_payment



<details><summary>Parameters</summary>

#### payment (required)

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_payment_intent

<p>Retrieves the details of a PaymentIntent that has previously been created. </p><p>Client-side retrieval using a publishable key is allowed when the <code>client_secret</code> is provided in the query string. </p><p>When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the <a href="#payment_intent_object">payment intent</a> object reference for more details.</p>

<details><summary>Parameters</summary>

#### intent (required)

**Type:** string

#### client_secret

The client secret of the PaymentIntent. Required if a publishable key is used to retrieve the source.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_payout

<p>Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list, and Stripe will return the corresponding payout information.</p>

<details><summary>Parameters</summary>

#### payout (required)

The identifier of the payout to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_plan

<p>Retrieves the plan with the given ID.</p>

<details><summary>Parameters</summary>

#### plan (required)

The ID of the desired plan.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_platform_earning

<p>Retrieves the details of an application fee that your account has collected. The same information is returned when refunding the application fee.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the fee to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_point_of_sale_location

<p>Retrieves a <code>Location</code> object.</p>

<details><summary>Parameters</summary>

#### location (required)

The identifier of the location to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### operator_account

The identifier of the account associated with this location.

**Type:** string

</details>

## get_point_of_sale_reader

<p>Retrieves a <code>Reader</code> object.</p>

<details><summary>Parameters</summary>

#### reader (required)

The identifier of the reader to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### operator_account

The identifier of the account associated with this reader.

**Type:** string

</details>

## get_product

<p>Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the product to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_refund

<p>Retrieves the details of an existing refund.</p>

<details><summary>Parameters</summary>

#### refund (required)

ID of refund to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_scheduled_query_run

<p>Retrieves the details of an scheduled query run.</p>

<details><summary>Parameters</summary>

#### scheduled_query_run (required)

Unique identifier for the object.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_sku

<p>Retrieves the details of an existing SKU. Supply the unique SKU identifier from either a SKU creation request or from the product, and Stripe will return the corresponding SKU information.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the SKU to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_source

<p>Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.</p>

<details><summary>Parameters</summary>

#### source (required)

The identifier of the source to be retrieved.

**Type:** string

#### client_secret

The client secret of the source. Required if a publishable key is used to retrieve the source.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_source_transaction

<p>Retrieve an existing source transaction object. Supply the unique source ID from a source creation request and the source transaction ID and Stripe will return the corresponding up-to-date source object information.</p>

<details><summary>Parameters</summary>

#### source (required)

The ID of the source whose source transaction will be retrieved.

**Type:** string

#### source_transaction (required)

The ID of the source transaction that will be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_subscription

<p>Retrieves the subscription with the given ID.</p>

<details><summary>Parameters</summary>

#### subscription_exposed_id (required)

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_subscription_item

<p>Retrieves the invoice item with the given ID.</p>

<details><summary>Parameters</summary>

#### item (required)

The identifier of the subscription item to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_tax_rate_template



*This operation has no parameters*

## get_token

<p>Retrieves the token with the given ID.</p>

<details><summary>Parameters</summary>

#### token (required)

The ID of the desired token.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_topup

<p>Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.</p>

<details><summary>Parameters</summary>

#### topup (required)

The ID of the top-up to retrieve.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_transfer

<p>Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.</p>

<details><summary>Parameters</summary>

#### transfer (required)

The identifier of the transfer to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_transfer_recipient

<p>Retrieves the details of an existing recipient. You need only supply the unique recipient identifier that was returned upon recipient creation.</p>

<details><summary>Parameters</summary>

#### id (required)

The identifier of the recipient to be retrieved.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_transfer_reversal

<p>By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.</p>

<details><summary>Parameters</summary>

#### id (required)

ID of reversal to retrieve.

**Type:** string

#### transfer (required)

ID of the transfer reversed.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

</details>

## get_upcoming_invoice

<p>At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discount that is applicable to the customer.</p><p>Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.</p><p>You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass a <code>proration_date</code> parameter when doing the actual subscription update. The value passed in should be the same as the <code>subscription_proration_date</code> returned on the upcoming invoice resource. The recommended way to get only the prorations being previewed is to consider only proration line items where <code>period[start]</code> is equal to the <code>subscription_proration_date</code> on the upcoming invoice resource.</p>

<details><summary>Parameters</summary>

#### customer (required)

The identifier of the customer whose upcoming invoice you'd like to retrieve.

**Type:** string

#### coupon

The code of the coupon to apply. If `subscription` or `subscription_items` is provided, the invoice returned will preview updating or creating a subscription with that coupon. Otherwise, it will preview applying that coupon to the customer for the next upcoming invoice from among the customer's subscriptions. The invoice can be previewed without a coupon by passing this value as an empty string.

**Type:** string

#### expand

Specifies which fields in the response should be expanded.

**Type:** array

#### invoice_items

List of invoice items to add or update in the upcoming invoice preview.

**Type:** array

#### subscription

The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.

**Type:** string

#### subscription_billing_cycle_anchor

For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.For existing subscriptions, the value can only be set to `now` or `unchanged`.

**Type:** object

#### subscription_cancel_at_period_end

Boolean indicating whether this subscription should cancel at the end of the current period.

**Type:** boolean

#### subscription_items

List of subscription items, each with an attached plan.

**Type:** array

#### subscription_prorate

If previewing an update to a subscription, this decides whether the preview will show the result of applying prorations or not. If set, one of `subscription_items` or `subscription`, and one of `subscription_items` or `subscription_trial_end` are required.

**Type:** boolean

#### subscription_proration_date

If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period, and cannot be before the subscription was on its current plan. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration` cannot be set to false.

**Type:** integer

#### subscription_tax_percent

If provided, the invoice returned will preview updating or creating a subscription with that tax percent. If set, one of `subscription_items` or `subscription` is required.

**Type:** number

#### subscription_trial_end

If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required.

**Type:** object

#### subscription_trial_from_plan

Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed.

**Type:** boolean

</details>

## issuing_authorization_approve

<p>Approves a pending Issuing <code>Authorization</code> object.</p>

<details><summary>Parameters</summary>

#### authorization (required)

The identifier of the authorization to approve.

**Type:** string

#### $body

**Type:** object

</details>

## pay_invoice

<p>Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your <a href="https://dashboard.stripe.com/account/recurring">subscriptions settings</a>. However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.</p>

<details><summary>Parameters</summary>

#### invoice (required)

ID of invoice to pay.

**Type:** string

#### $body

**Type:** object

</details>

## pay_order



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## payment_intent_capture

<p>Capture the funds of an existing uncaptured PaymentIntent where <code>required_action="requires_capture"</code>.</p><p>Uncaptured PaymentIntents will be canceled exactly seven days after they are created.</p>

<details><summary>Parameters</summary>

#### intent (required)

**Type:** string

#### $body

**Type:** object

</details>

## payment_intent_confirm

<p>Confirm that your customer intends to pay with current or provided<code>source</code>. Upon confirmation, the PaymentIntent will attempt to initiatea payment.</p><p>If the selected <code>source</code> requires additional authentication steps, thePaymentIntent will transition to the <code>requires_source_action</code> status andsuggest additional actions via <code>next_source_action</code>. If payment fails,the PaymentIntent will transition to the <code>requires_source</code> status. Ifpayment succeeds, the PaymentIntent will transition to the <code>succeeded</code>status (or <code>requires_capture</code>, if <code>capture_method</code> is set to <code>manual</code>).</p><p>When using a publishable key, the<a href="#payment_intent_object-client_secret">client_secret</a> must be providedto confirm the PaymentIntent.</p>

<details><summary>Parameters</summary>

#### intent (required)

**Type:** string

#### $body

**Type:** object

</details>

## reject_account

<p>With <a href="/docs/connect">Connect</a>, you may flag accounts as suspicious.</p><p>Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.</p>

<details><summary>Parameters</summary>

#### account (required)

The identifier of the account to reject

**Type:** string

#### $body

**Type:** object

</details>

## retry_notification_event

<p>Resend an event. This only works in testmode</p>

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_account

<p>Updates a connected <a href="/docs/connect/accounts">Express or Custom account</a> by setting the values of the parameters passed. Any parameters not provided are left unchanged. Most parameters can be changed only for Custom accounts. (These are marked <strong>Custom Only</strong> below.) Parameters marked <strong>Custom and Express</strong> are supported by both account types.</p><p>To update your own account, use the <a href="https://dashboard.stripe.com/account">Dashboard</a>. Refer to our <a href="/docs/connect/updating-accounts">Connect</a> documentation to learn more about updating accounts.</p>

<details><summary>Parameters</summary>

#### account (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_bank_account

<p>Updates the metadata, account holder name, and account holder type of a bank account belonging to a <a href="/docs/connect/custom-accounts">Custom account</a>, and optionally sets it as the default for its currency. Other bank account details are not editable by design.</p><p>You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.</p>

<details><summary>Parameters</summary>

#### account (required)

**Type:** string

#### id (required)

The ID of the external account to update

**Type:** string

#### $body

**Type:** object

</details>

## update_charge

<p>Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### charge (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_coupon

<p>Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.</p>

<details><summary>Parameters</summary>

#### coupon (required)

The identifier of the coupon to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_customer



<details><summary>Parameters</summary>

#### customer (required)

The identifier of the customer to subscribe.

**Type:** string

#### $body

**Type:** object

</details>

## update_customer_source



<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

#### id (required)

The ID of the card to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_dispute

<p>When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your <a href="https://dashboard.stripe.com/disputes">dashboard</a>, but if you prefer, you can use the API to submit evidence programmatically.</p><p>Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our <a href="/docs/disputes/categories">guide to dispute types</a>.</p>

<details><summary>Parameters</summary>

#### dispute (required)

ID of the dispute to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_file_link

<p>Updates an existing file link object. Expired links can no longer be updated.</p>

<details><summary>Parameters</summary>

#### link (required)

The ID of the file link.

**Type:** string

#### $body

**Type:** object

</details>

## update_invoice

<p>Until an invoice is paid, it is marked as open (<code>closed=false</code>). If you’d like to stop Stripe from attempting to collect payment on an invoice or would simply like to close the invoice out as no longer owed by the customer, you can update the closed parameter.</p>

<details><summary>Parameters</summary>

#### invoice (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_invoice_item

<p>Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.</p>

<details><summary>Parameters</summary>

#### invoiceitem (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_issuing_authorization

<p>Updates the specified Issuing <code>Authorization</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### authorization (required)

The identifier of the authorization to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_issuing_card

<p>Updates the specified Issuing <code>Card</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### card (required)

The identifier of the issued card to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_issuing_cardholder

<p>Updates the specified Issuing <code>Cardholder</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### cardholder (required)

The ID of the cardholder to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_issuing_dispute

<p>Updates the specified Issuing <code>Dispute</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### dispute (required)

The ID of the dispute to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_issuing_transaction

<p>Updates the specified Issuing <code>Transaction</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### transaction (required)

The identifier of the transaction to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_order

<p>Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_payment_intent

<p>Updates a PaymentIntent object.</p>

<details><summary>Parameters</summary>

#### intent (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_payout

<p>Updates the specified payout by setting the values of the parameters passed. Any parameters not provided will be left unchanged. This request accepts only the metadata as arguments.</p>

<details><summary>Parameters</summary>

#### payout (required)

The identifier of the payout to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_plan

<p>Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.</p>

<details><summary>Parameters</summary>

#### plan (required)

The identifier of the plan to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_platform_earning_refund

<p>Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>This request only accepts metadata as an argument.</p>

<details><summary>Parameters</summary>

#### fee (required)

ID of the application fee refunded.

**Type:** string

#### id (required)

ID of refund to retrieve.

**Type:** string

#### $body

**Type:** object

</details>

## update_point_of_sale_location

<p>Updates a <code>Location</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### location (required)

The identifier of the location to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_point_of_sale_reader

<p>Updates a <code>Reader</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<details><summary>Parameters</summary>

#### reader (required)

The identifier of the reader to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_product

<p>Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>Note that a product’s <code>attributes</code> are not editable. Instead, you would need to deactivate the existing product and create a new one with the new attribute values.</p>

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_refund

<p>Updates the specified refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>This request only accepts <code>metadata</code> as an argument.</p>

<details><summary>Parameters</summary>

#### refund (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_sku

<p>Updates the specific SKU by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>Note that a SKU’s <code>attributes</code> are not editable. Instead, you would need to deactivate the existing SKU and create a new one with the new attribute values.</p>

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_source

<p>Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>This request accepts the <code>metadata</code> and <code>owner</code> as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our <a href="/docs/sources">payment method guides</a> for more detail.</p>

<details><summary>Parameters</summary>

#### source (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_subscription

<p>Updates an existing subscription on a customer to match the specified parameters. When changing plans or quantities, we will optionally prorate the price we charge next month to make up for any price changes. To preview how the proration will be calculated, use the <a href="#upcoming_invoice">upcoming invoice</a> endpoint.</p>

<details><summary>Parameters</summary>

#### subscription_exposed_id (required)

The identifier of the subscription to update.

**Type:** string

#### $body

**Type:** object

</details>

## update_subscription_item

<p>Updates the plan or quantity of an item on a current subscription.</p>

<details><summary>Parameters</summary>

#### item (required)

The identifier of the subscription item to modify.

**Type:** string

#### $body

**Type:** object

</details>

## update_topup

<p>Updates the metadata of a top-up. Other top-up details are not editable by design.</p>

<details><summary>Parameters</summary>

#### topup (required)

The ID of the top-up to retrieve.

**Type:** string

#### $body

**Type:** object

</details>

## update_transfer

<p>Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>This request accepts only metadata as an argument.</p>

<details><summary>Parameters</summary>

#### transfer (required)

The ID of the transfer to be updated.

**Type:** string

#### $body

**Type:** object

</details>

## update_transfer_recipient

<p>Updates the specified recipient by setting the values of the parameters passed.Any parameters not provided will be left unchanged.</p><p>If you update the name or tax ID, the identity verification will automatically be rerun.If you update the bank account, the bank account validation will automatically be rerun.</p>

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_transfer_reversal

<p>Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p><p>This request only accepts metadata and description as arguments.</p>

<details><summary>Parameters</summary>

#### id (required)

ID of reversal to retrieve.

**Type:** string

#### transfer (required)

ID of the transfer reversed.

**Type:** string

#### $body

**Type:** object

</details>

## verify_customer_source



<details><summary>Parameters</summary>

#### customer (required)

**Type:** string

#### id (required)

The ID of the source to be verified.

**Type:** string

#### $body

**Type:** object

</details>

## verify_source



<details><summary>Parameters</summary>

#### source (required)

The ID of the desired source.

**Type:** string

#### $body

**Type:** object

</details>

