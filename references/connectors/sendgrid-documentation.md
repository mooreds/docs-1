---
id: sendgrid-documentation
title: SendGrid (version v3.*.*)
sidebar_label: SendGrid
layout: docs.mustache
---

## activate_version_of_template

**This endpoint allows you to activate a version of one of your templates.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.


For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string |  The ID of the template version |

<details><summary>Parameters</summary>

### template_id (required)

**Type:** string

### version_id (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

### on-behalf-of

**Type:** string

</details>

## add_authenticated_domain_to_subuser

**This endpoint allows you to associate a specific domain whitelabel with a subuser.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

Domain whitelabels can be associated with (i.e. assigned to) subusers from a parent account. This functionality allows subusers to send mail using their parent's whitelabels. To associate a whitelabel with a subuser, the parent account must first create the whitelabel and validate it. The the parent may then associate the whitelabel via the subuser management tools.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type   | Description  |
|---|---|---|
| domain_id | integer   | ID of the domain whitelabel to associate with the subuser. |

<details><summary>Parameters</summary>

### domain_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "username" : "Username to associate with the domain whitelabel."
}
```

### on-behalf-of

**Type:** string

</details>

## add_branded_link_to_subuser

**This endpoint allows you to associate a link whitelabel with a subuser account.**

Link whitelables can be associated with subusers from the parent account. This functionality allows
subusers to send mail using their parent's linke whitelabels. To associate a link whitelabel, the parent account
must first create a whitelabel and validate it. The parent may then associate that whitelabel with a subuser via the API or the Subuser Management page in the user interface.

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### link_id (required)

The id of the link whitelabel you want to associate.

**Type:** integer

### $body

**Type:** object

```json
{
  "username" : "The username of the subuser account that you want to associate the link whitelabel with."
}
```

### on-behalf-of

**Type:** string

</details>

## add_email_to_unsubscribe_group

**This endpoint allows you to add email addresses to an unsubscribe group.**

If you attempt to add suppressions to a group that has been deleted or does not exist, the suppressions will be added to the global suppressions list.

Suppressions are recipient email addresses that are added to [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html). Once a recipient's address is on the suppressions list for an unsubscribe group, they will not receive any emails that are tagged with that unsubscribe group.

<details><summary>Parameters</summary>

### group_id (required)

The id of the unsubscribe group that you are adding suppressions to.

**Type:** string

### $body

**Type:** object

```json
{
  "recipient_emails" : [ "string" ]
}
```

### on-behalf-of

**Type:** string

</details>

## add_emails_to_global_unsubscribe_group

**This endpoint allows you to add one or more email addresses to the global suppressions group.**

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "recipient_emails" : [ "string" ]
}
```

### on-behalf-of

**Type:** string

</details>

## add_ip_to_authenticated_domain

**This endpoint allows you to add an IP address to a domain whitelabel.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  |  Description  |
|---|---|---|
| id | integer  | ID of the domain to which you are adding an IP |

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "ip" : "IP to associate with the domain. Used for manually specifying IPs for custom SPF."
}
```

### on-behalf-of

**Type:** string

</details>

## add_ip_to_pool

**This endpoint allows you to add an IP address to an IP pool.**

You can add the same IP address to multiple pools. It may take up to 60 seconds for your IP address to be added to a pool after your request is made.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

<details><summary>Parameters</summary>

### pool_name (required)

The name of the IP pool that you want to add an IP address to.

**Type:** string

### $body

**Type:** object

```json
{
  "ip" : "The IP address that you want to add to an IP pool."
}
```

</details>

## add_ip_to_whitelist

**This endpoint allows you to add one or more IP addresses to your IP whitelist.**

When adding an IP to your whitelist, include the IP address in an array. You can whitelist one IP at a time, or you can whitelist multiple IPs at once.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ips" : [ {
    "ip" : "An IP address that you want to whitelist."
  } ]
}
```

### on-behalf-of

**Type:** string

</details>

## add_recipient_to_list

**This endpoint allows you to add a single recipient to a list.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

The ID of the list that you want to add the recipient to.

**Type:** integer

### recipient_id (required)

The ID of the recipient you are adding to the list.

**Type:** string

### $body

**Type:** object

```json
{ }
```

### on-behalf-of

**Type:** string

</details>

## add_recipients

**This endpoint allows you to add a Marketing Campaigns recipient.**

You can add custom field data as a parameter on this endpoint. We have provided an example using some of the default custom fields SendGrid provides.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### $body

**Type:** array

```json
[ {
  "last_name" : "The last name of the recipient.",
  "first_name" : "The first name of the recipient.",
  "age" : "integer",
  "email" : "The email address of the recipient."
} ]
```

### on-behalf-of

**Type:** string

</details>

## add_recipients_to_list

**This endpoint allows you to add multiple recipients to a list.**

Adds existing recipients to a list, passing in the recipient IDs to add. Recipient IDs should be passed exactly as they are returned from recipient endpoints.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

The id of the list of recipients you want to retrieve.

**Type:** integer

### $body

**Type:** array

```json
[ "string" ]
```

### on-behalf-of

**Type:** string

</details>

## approve_access_request

This endpoint allows you to approve an access attempt.

**Note:** Only teammate admins may approve another teammate’s access request.

<details><summary>Parameters</summary>

### request_id (required)

The ID of the request that you want to approve.

**Type:** string

</details>

## authenticate_domain

**This endpoint allows you to create a whitelabel for one of your domains.**

If you are creating a domain whitelabel that you would like a subuser to use, you have two options:
1. Use the "username" parameter. This allows you to create a whitelabel on behalf of your subuser. This means the subuser is able to see and modify the created whitelabel.
2. Use the Association workflow (see Associate Domain section). This allows you to assign a whitelabel created by the parent to a subuser. This means the subuser will default to the assigned whitelabel, but will not be able to see or modify that whitelabel. However, if the subuser creates their own whitelabel it will overwrite the assigned whitelabel.

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "default" : "Whether to use this whitelabel as the fallback if no domain whitelabels match the sender's domain.",
  "custom_spf" : "Specify whether to use a custom SPF or allow SendGrid to manage your SPF. This option is only available to domain whitelabels setup for manual security.",
  "automatic_security" : "Whether to allow SendGrid to manage your SPF records, DKIM keys, and DKIM key rotation.",
  "domain" : "Domain being whitelabeled.",
  "subdomain" : "The subdomain to use for this domain whitelabel.",
  "ips" : [ "string" ],
  "username" : "The username that this whitelabel will be associated with."
}
```

### on-behalf-of

**Type:** string

</details>

## create_alert

**This endpoint allows you to create a new alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. There are two types of alerts that can be created with this endpoint:

* `usage_limit` allows you to set the threshold at which an alert will be sent.
* `stats_notification` allows you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "email_to" : "The email address the alert will be sent to.\nExample: test@example.com",
  "percentage" : "Required for usage_alert. When this usage threshold is reached, the alert will be sent.\nExample: 90",
  "type" : "The type of alert you want to create. Can be either usage_limit or stats_notification.\nExample: usage_limit",
  "frequency" : "Required for stats_notification. How frequently the alert will be sent.\nExample: daily"
}
```

### Authorization

**Type:** string

### on-behalf-of

**Type:** string

</details>

## create_api_key

**This endpoint allows you to create a new random API Key for the user.**

A JSON request body containing a "name" property is required. If number of maximum keys is reached, HTTP 403 will be returned.

There is a limit of 100 API Keys on your account.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

See the [API Key Permissions List](https://sendgrid.com/docs/API_Reference/Web_API_v3/API_Keys/api_key_permissions_list.html) for a list of all available scopes.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "The name you will use to describe this API Key.",
  "scopes" : [ "string" ],
  "sample" : "string"
}
```

### on-behalf-of

**Type:** string

</details>

## create_batch

**This endpoint allows you to generate a new batch ID. This batch ID can be associated with scheduled sends via the mail/send endpoint.**

If you set the SMTPAPI header `batch_id`, it allows you to then associate multiple scheduled mail/send requests together with the same ID. Then at anytime up to 10 minutes before the schedule date, you can cancel all of the mail/send requests that have this batch ID by calling the Cancel Scheduled Send endpoint. 

More Information:

* [Scheduling Parameters &gt; Batch ID](https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_branded_link

**This endpoint allows you to create a new link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "default" : "Indicates if you want to use this link whitelabel as the fallback, or default, whitelabel.",
  "domain" : "The root domain for your subdomain that you are creating the whitelabel for. This should match your FROM email address.",
  "subdomain" : "The subdomain to create the link whitelabel for. Must be different from the subdomain you used for a domain whitelabel."
}
```

### limit

Number of domains to return.

**Type:** integer

### offset

Paging offset.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## create_campaign

**This endpoint allows you to create a campaign.**

Our Marketing Campaigns API lets you create, manage, send, and schedule campaigns.

Note: In order to send or schedule the campaign, you will be required to provide a subject, sender ID, content (we suggest both html and plain text), and at least one list or segment ID. This information is not required when you create a campaign.

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "html_content" : "The HTML of your marketing email.",
  "segment_ids" : [ "integer" ],
  "subject" : "The subject of your campaign that your recipients will see.",
  "suppression_group_id" : "The suppression group that this marketing email belongs to, allowing recipients to opt-out of emails of this type.",
  "ip_pool" : "The pool of IPs that you would like to send this email from.",
  "custom_unsubscribe_url" : "This is the url of the custom unsubscribe page that you provide for customers to unsubscribe from your suppression groups.",
  "categories" : [ "string" ],
  "title" : "The display title of your campaign. This will be viewable by you in the Marketing Campaigns UI.",
  "list_ids" : [ "integer" ],
  "plain_content" : "The plain text content of your emails.",
  "sender_id" : "The ID of the \"sender\" identity that you have created. Your recipients will see this as the \"from\" on your marketing emails."
}
```

</details>

## create_custom_field

**This endpoint allows you to create a custom field.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "string",
  "type" : "string"
}
```

### on-behalf-of

**Type:** string

</details>

## create_ip

This endpoint is for adding a(n) IP Address(es) to your account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "count" : "The amount of IPs to add to the account.",
  "subusers" : [ "string" ],
  "warmup" : "Whether or not to warmup the IPs being added."
}
```

</details>

## create_monitor_settings_for_subuser

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

<details><summary>Parameters</summary>

### subuser_name (required)

The name of the subuser for which to retrieve monitor settings.

**Type:** string

### $body

**Type:** object

```json
{
  "email" : "The email address to send emails at the frequency specified for monitoring.",
  "frequency" : "The frequency by which to send the emails. An email will be sent, every time your subuser sends this {frequency} emails."
}
```

</details>

## create_pool

**This endpoint allows you to create an IP pool.**

**Each user can create up to 10 different IP pools.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "The name of your new IP pool."
}
```

</details>

## create_recipient_list

**This endpoint allows you to create a list for your recipients.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "Required string"
}
```

### on-behalf-of

**Type:** string

</details>

## create_reverse_dns_record

**This endpoint allows you to create an IP whitelabel.**

When creating an IP whitelable, you should use the same subdomain that you used when you created a domain whitelabel.

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "domain" : "The root, or sending, domain that will be used to send message from the IP.",
  "ip" : "The IP address that you want to whitelabel.",
  "subdomain" : "The subdomain that will be used to send emails from the IP. Should be the same as the subdomain used for your domain whitelabel."
}
```

### on-behalf-of

**Type:** string

</details>

## create_segment

**This endpoint allows you to create a segment.**

All recipients in your contactdb will be added or removed automatically depending on whether they match the criteria for this segment.

List Id:

* Send this to segment from an existing list
* Don't send this in order to segment from your entire contactdb.

Valid operators for create and update depend on the type of the field you are segmenting: 

* **Dates:** "eq", "ne", "lt" (before), "gt" (after) 
* **Text:** "contains", "eq" (is - matches the full field), "ne" (is not - matches any field where the entire field is not the condition value) 
* **Numbers:** "eq", "lt", "gt" 
* **Email Clicks and Opens:** "eq" (opened), "ne" (not opened) 

Segment conditions using "eq" or "ne" for email clicks and opens should provide a "field" of either *clicks.campaign_identifier* or *opens.campaign_identifier*. The condition value should be a string containing the id of a completed campaign. 

Segments may contain multiple condtions, joined by an "and" or "or" in the "and_or" field. The first condition in the conditions list must have an empty "and_or", and subsequent conditions must all specify an "and_or".

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "list_id" : "The list id from which to make this segment. Not including this ID will mean your segment is created from the main contactdb rather than a list.",
  "name" : "The name of this segment.",
  "recipient_count" : "The count of recipients in this list. This is not included on creation of segments.",
  "conditions" : [ {
    "field" : "Required string",
    "and_or" : "string. Possible values: and | or | ",
    "value" : "Required string",
    "operator" : "Required string. Possible values: eq | ne | lt | gt | contains"
  } ]
}
```

### on-behalf-of

**Type:** string

</details>

## create_sender

**This endpoint allows you to create a new sender identity.**

*You may create up to 100 unique sender identities.*

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "zip" : "The zipcode of the sender identity.",
  "country" : "The country of the sender identity.",
  "address" : "The physical address of the sender identity.",
  "reply_to" : {
    "name" : "This is the name appended to the reply to email field. IE - Your name or company name.",
    "email" : "This is the email that your recipient will reply to."
  },
  "city" : "The city of the sender identity.",
  "address_2" : "Additional sender identity address information.",
  "nickname" : "A nickname for the sender identity. Not used for sending.",
  "from" : {
    "name" : "This is the name appended to the from email field. IE - Your name or company name.",
    "email" : "This is where the email will appear to originate from for your recipient"
  },
  "state" : "The state of the sender identity."
}
```

### on-behalf-of

**Type:** string

</details>

## create_subuser

This endpoint allows you to retrieve a list of all of your subusers. You can choose to retrieve specific subusers as well as limit the results that come back from the API.

For more information about Subusers:

* [User Guide &gt; Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom &gt; How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "password" : "The password this subuser will use when logging into SendGrid.",
  "ips" : [ "ipv4" ],
  "email" : "The email address of the subuser.",
  "username" : "The username for this subuser."
}
```

</details>

## create_template

**This endpoint allows you to create a transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "The name for the new transactional template."
}
```

### on-behalf-of

**Type:** string

</details>

## create_unsubscribe_group

**This endpoint allows you to create a new suppression group.**

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "The name that you would like to use for your new suppression group.",
  "description" : "A brief description of your new suppression group.",
  "is_default" : "Indicates if you would like this to be your default suppression group."
}
```

### on-behalf-of

**Type:** string

</details>

## create_user_scheduled_sends

**This endpoint allows you to cancel or pause an email that has been scheduled to be sent.**

If the maximum number of cancellations/pauses are added, HTTP 400 will
be returned.

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header. Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "batch_id" : "The batch ID is the identifier that your scheduled mail sends share.",
  "status" : "The status of the send you would like to implement. This can be pause or cancel. To delete a pause or cancel status see DELETE /v3/user/scheduled_sends/{batch_id}"
}
```

</details>

## create_version_of_template

**This endpoint allows you to create a new version of a template.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

<details><summary>Parameters</summary>

### template_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "html_content" : "The HTML content of the new version. Must include &lt;%body%&gt; tag. Maximum of 1048576 bytes allowed for plain content.",
  "subject" : "Subject of the new transactional template version. Must include &lt;%subject%&gt; tag.",
  "name" : "Name of the new transactional template version.",
  "active" : "Set the new version as the active version associated with the template. Only one version of a template can be active. The first version created for a template will automatically be set to Active.",
  "template_id" : "The name of the original transactional template.",
  "plain_content" : "Text/plain content of the new transactional template version. Must include &lt;%body%&gt; tag. Maximum of 1048576 bytes allowed for plain content."
}
```

### on-behalf-of

**Type:** string

</details>

## create_webhooks_parse_setting

**This endpoint allows you to create a new inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the content, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "hostname" : "A specific and unique domain or subdomain that you have created to use exclusively to parse your incoming email. For example, parse.yourdomain.com.",
  "spam_check" : "Indicates if you would like SendGrid to check the content parsed from your emails for spam before POSTing them to your domain.",
  "send_raw" : "Indicates if you would like SendGrid to post the original MIME-type content of your parsed email. When this parameter is set to \"false\", SendGrid will send a JSON payload of the content of your email.",
  "url" : "The public URL where you would like SendGrid to POST the data parsed from your email. Any emails sent with the given hostname provided (whose MX records have been updated to point to SendGrid) will be parsed and POSTed to this URL."
}
```

### on-behalf-of

**Type:** string

</details>

## delete_alert

**This endpoint allows you to delete an alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

<details><summary>Parameters</summary>

### alert_id (required)

The ID of the alert you would like to retrieve.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## delete_all_blocked_emails

**This endpoint allows you to delete all email addresses on your blocks list.**

There are two options for deleting blocked emails: 

1. You can delete all blocked emails by setting `delete_all` to true in the request body. 
2. You can delete some blocked emails by specifying the email addresses in an array in the request body.

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_all_bounces

**This endpoint allows you to delete all of your bounces. You can also use this endpoint to remove a specific email address from your bounce list.**

A bounced email is when the message is undeliverable and then returned to the server that sent it.

For more information see: 

* [User Guide &gt; Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary &gt; Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)
* [Classroom &gt; List Scrubbing Guide](https://sendgrid.com/docs/Classroom/Deliver/list_scrubbing.html)

Note: the `delete_all` and `emails` parameters should be used independently of each other as they have different purposes.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_api_key

**This endpoint allows you to revoke an existing API Key**

Authentications using this API Key will fail after this request is made, with some small propogation delay.If the API Key ID does not exist an HTTP 404 will be returned.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

## URI Parameters

| URI Parameter   | Type  | Required?  | Description  |
|---|---|---|---|
|api_key_id |string | required | The ID of the API Key you are deleting.|

<details><summary>Parameters</summary>

### api_key_id (required)

The ID of the API Key for which you are requesting information.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_authenticated_domain

**This endpoint allows you to delete a domain whitelabel.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

<details><summary>Parameters</summary>

### domain_id (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_authenticated_domain_from_subuser

**This endpoint allows you to disassociate a specific whitelabel from a subuser.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

Domain whitelabels can be associated with (i.e. assigned to) subusers from a parent account. This functionality allows subusers to send mail using their parent's whitelabels. To associate a whitelabel with a subuser, the parent account must first create the whitelabel and validate it. The the parent may then associate the whitelabel via the subuser management tools.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  | Required?  | Description  |
|---|---|---|---|
| username | string  | required  | Username for the subuser to find associated whitelabels for. |

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_branded_link

**This endpoint allows you to delete a link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### id (required)

The id of the link whitelabel you want to retrieve.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## delete_campaign

**This endpoint allows you to delete a specific campaign.**

Our Marketing Campaigns API lets you create, manage, send, and schedule campaigns.

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

The id of the campaign you would like to retrieve.

**Type:** integer

</details>

## delete_custom_field

**This endpoint allows you to delete a custom field by ID.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### custom_field_id (required)

The ID of the custom field that you want to retrieve.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## delete_email_from_bounces

**This endpoint allows you to remove an email address from your bounce list.**

A bounced email is when the message is undeliverable and then returned to the server that sent it. This endpoint allows you to delete a single email addresses from your bounce list. 

For more information see: 

* [User Guide &gt; Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary &gt; Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)
* [Classroom &gt; List Scrubbing Guide](https://sendgrid.com/docs/Classroom/Deliver/list_scrubbing.html)

<details><summary>Parameters</summary>

### email (required)

**Type:** string

### email_address (required)

The email address you would like to remove from the bounce list.

**Type:** email

### on-behalf-of

**Type:** string

</details>

## delete_email_from_global_unsubscribe_group

**This endpoint allows you to remove an email address from the global suppressions group.**

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

<details><summary>Parameters</summary>

### email (required)

The email address of the global suppression you want to retrieve. Or, if you want to check if an email address is on the global suppressions list, enter that email address here.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_email_from_unsubscribe_group

**This endpoint allows you to remove a suppressed email address from the given suppression group.**

Suppressions are recipient email addresses that are added to [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html). Once a recipient's address is on the suppressions list for an unsubscribe group, they will not receive any emails that are tagged with that unsubscribe group.

<details><summary>Parameters</summary>

### email (required)

The email address that you want to remove from the suppression group.

**Type:** string

### group_id (required)

The id of the suppression group that you are removing an email address from.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_invalid_email

**This endpoint allows you to remove a specific email address from the invalid email address list.**

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipient’s mail server.

Examples include addresses without the “@” sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### email (required)

The specific email address of the invalid email entry that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_invalid_emails

**This endpoint allows you to remove email addresses from your invalid email address list.**

There are two options for deleting invalid email addresses: 

1) You can delete all invalid email addresses by setting `delete_all` to true in the request body.
2) You can delete some invalid email addresses by specifying certain addresses in an array in the request body.

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipient’s mail server.

Examples include addresses without the “@” sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_ip_from_authenticated_domain

**This endpoint allows you to remove a domain's IP address from that domain's whitelabel.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  | Description  |
|---|---|---|
| id | integer  | ID of the domain whitelabel to delete the IP from. |
| ip | string | IP to remove from the domain whitelabel. |

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### ip (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_ip_from_pool

**This endpoint allows you to remove an IP address from an IP pool.**

The same IP address can be added to multiple IP pools.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

<details><summary>Parameters</summary>

### ip (required)

The IP address that you are removing.

**Type:** string

### pool_name (required)

The name of the IP pool that you are removing the IP address from.

**Type:** string

</details>

## delete_ip_from_whitelist

**This endpoint allows you to remove a specific IP address from your IP whitelist.**

When removing a specific IP address from your whitelist, you must include the ID in your call.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

<details><summary>Parameters</summary>

### rule_id (required)

The ID of the whitelisted IP address that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_ips_from_whitelist

**This endpoint allows you to remove one or more IPs from your IP whitelist.**

You can remove one IP at a time, or you can remove multiple IP addresses.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_monitor_settings_for_subuser

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### subuser_name (required)

The name of the subuser for which to retrieve monitor settings.

**Type:** string

</details>

## delete_pool

**This endpoint allows you to delete an IP pool.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

<details><summary>Parameters</summary>

### pool_name (required)

The name of the IP pool that you want to retrieve the IP addresses from.

**Type:** string

</details>

## delete_recipient

**This endpoint allows you to delete a single recipient with the given ID from your contact database.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### recipient_id (required)

The ID of the recipient that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_recipient_from_list

**This endpoint allows you to delete a single recipient from a list.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

The ID of the list that you want to add the recipient to.

**Type:** integer

### recipient_id (required)

The ID of the recipient you are adding to the list.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_recipient_list

**This endpoint allows you to delete a specific recipient list with the given ID.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

**Type:** string

### delete_contacts

Adds the ability to delete all contacts on the list in addition to deleting the list.

**Type:** boolean

**Potential values:** true, false

### on-behalf-of

**Type:** string

</details>

## delete_recipient_lists

**This endpoint allows you to delete multiple recipient lists.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_recipients

**This endpoint allows you to deletes one or more recipients.**

The body of an API call to this endpoint must include an array of recipient IDs of the recipients you want to delete.

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_reverse_dns_record

**This endpoint allows you to delete an IP whitelabel.**

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

<details><summary>Parameters</summary>

### id (required)

The id of the IP whitelabel that you would like to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_segment

**This endpoint allows you to delete a segment from your recipients database.**

You also have the option to delete all the contacts from your Marketing Campaigns recipient database who were in this segment.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

<details><summary>Parameters</summary>

### segment_id (required)

**Type:** string

### delete_contacts

True to delete all contacts matching the segment in addition to deleting the segment

**Type:** boolean

### on-behalf-of

**Type:** string

</details>

## delete_sender

**This endoint allows you to delete one of your sender identities.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

<details><summary>Parameters</summary>

### sender_id (required)

The ID of the sender identity that you want to update.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## delete_spam_report

**This endpoint allows you to delete a specific spam report.**

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

<details><summary>Parameters</summary>

### email (required)

The email address of a specific spam report that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_spam_reports

**This endpoint allows you to delete your spam reports.**

There are two options for deleting spam reports: 

1) You can delete all spam reports by setting "delete_all" to true in the request body. 
2) You can delete some spam reports by specifying the email addresses in an array in the request body.

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## delete_subuser

This endpoint allows you to delete a subuser. This is a permanent action, once deleted a subuser cannot be retrieved.

For more information about Subusers:

* [User Guide &gt; Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom &gt; How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

<details><summary>Parameters</summary>

### subuser_name (required)

**Type:** string

</details>

## delete_teammate

This endpoint allows you to delete a teammate.

**Only the parent user or an admin teammate can delete another teammate.**

<details><summary>Parameters</summary>

### username (required)

The username of the teammate that you want to retrieve.

**Type:** string

</details>

## delete_template

**This endpoint allows you to delete a transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

<details><summary>Parameters</summary>

### template_id (required)

The id of the transactional template you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_unsubscribe_group

**This endpoint allows you to delete a suppression group.**

You can only delete groups that have not been attached to sent mail in the last 60 days. If a recipient uses the "one-click unsubscribe" option on an email associated with a deleted group, that recipient will be added to the global suppression list.

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

<details><summary>Parameters</summary>

### group_id (required)

The ID of the suppression group you would like to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_user_scheduled_send

**This endpoint allows you to delete the cancellation/pause of a scheduled send.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header. Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

<details><summary>Parameters</summary>

### batch_id (required)

**Type:** string

</details>

## delete_version_of_template

**This endpoint allows you to delete one of your transactional template versions.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string | The ID of the template version |

<details><summary>Parameters</summary>

### template_id (required)

**Type:** string

### version_id (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## delete_webhooks_parse_setting

**This endpoint allows you to delete a specific inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

<details><summary>Parameters</summary>

### hostname (required)

The hostname associated with the inbound parse setting that you would like to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## deny_access_request

This endpoint allows you to deny an attempt to access your account.

**Note:** Only teammate admins may delete a teammate's access request.

<details><summary>Parameters</summary>

### request_id (required)

The ID of the request that you want to deny.

**Type:** string

</details>

## enable_disable_subuser

This endpoint allows you to enable or disable a subuser.

For more information about Subusers:

* [User Guide &gt; Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom &gt; How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

<details><summary>Parameters</summary>

### subuser_name (required)

**Type:** string

### $body

**Type:** object

```json
{
  "disabled" : "Whether or not this subuser is disabled. True means disabled, False means enabled."
}
```

</details>

## get_address_whitelist

**This endpoint allows you to retrieve your current email address whitelist settings.**

The address whitelist setting whitelists a specified email address or domain for which mail should never be suppressed. For example, you own the domain “example.com,” and one or more of your recipients use email@example.com addresses, by placing example.com in the address whitelist setting, all bounces, blocks, and unsubscribes logged for that domain will be ignored and sent as if under normal sending conditions.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_alert

**This endpoint allows you to retrieve a specific alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

<details><summary>Parameters</summary>

### alert_id (required)

The ID of the alert you would like to retrieve.

**Type:** integer

### Authorization

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_api_key

**This endpoint allows you to retrieve a single api key.**

If the API Key ID does not exist an HTTP 404 will be returned.

<details><summary>Parameters</summary>

### api_key_id (required)

The ID of the API Key for which you are requesting information.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_authenticated_domain

**This endpoint allows you to retrieve a specific domain whitelabel.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

<details><summary>Parameters</summary>

### domain_id (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_bcc_settings

**This endpoint allows you to retrieve your current BCC mail settings.**

When the BCC mail setting is enabled, SendGrid will automatically send a blind carbon copy (BCC) to an address for every email sent without adding that address to the header. Please note that only one email address may be entered in this field, if you wish to distribute BCCs to multiple addresses you will need to create a distribution group or use forwarding rules.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_billable_count_recipients

**This endpoint allows you to retrieve the number of Marketing Campaigns recipients that you will be billed for.**

You are billed for marketing campaigns based on the highest number of recipients you have had in your account at one time. This endpoint will allow you to know the current billable count value.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_bounce_for_email

**This endpoint allows you to retrieve a specific bounce for a given email address.**

A bounced email is when the message is undeliverable and then returned to the server that sent it.

For more information see: 

* [User Guide &gt; Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary &gt; Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)
* [Classroom &gt; List Scrubbing Guide](https://sendgrid.com/docs/Classroom/Deliver/list_scrubbing.html)

<details><summary>Parameters</summary>

### email (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_bounce_forward_settings

**This endpoint allows you to retrieve your current bounce forwarding mail settings.**

Activating this setting allows you to specify an email address to which bounce reports are forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_bounce_purge_settings

**This endpoint allows you to retrieve your current bounce purge settings.**

This setting allows you to set a schedule for SendGrid to automatically delete contacts from your soft and hard bounce suppression lists.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_branded_link

**This endpoint allows you to retrieve a specific link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### id (required)

The id of the link whitelabel you want to retrieve.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## get_campaign

**This endpoint allows you to retrieve a specific campaign.**

Our Marketing Campaigns API lets you create, manage, send, and schedule campaigns.

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

The id of the campaign you would like to retrieve.

**Type:** integer

</details>

## get_custom_field

**This endpoint allows you to retrieve a custom field by ID.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### custom_field_id (required)

The ID of the custom field that you want to retrieve.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## get_default_authenticated_domain

**This endpoint allows you to retrieve the default whitelabel for a domain.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type   | Description  |
|---|---|---|
| domain | string  |The domain to find a default domain whitelabel for. |

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_default_branded_link

**This endpoint allows you to retrieve the default link whitelabel.**

Default link whitelabel is the actual link whitelabel to be used when sending messages. If there are multiple link whitelabels, the default is determined by the following order:

  Validated link whitelabels marked as "default"
  Legacy link whitelabels (migrated from the whitelabel wizard)
  Default SendGrid link whitelabel (i.e. 100.ct.sendgrid.net)


Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### domain

The domain to match against when finding a corresponding link whitelabel.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_email_blocked_status

**This endpoint allows you to retrieve a specific email address from your blocks list.**

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

<details><summary>Parameters</summary>

### email (required)

The email address of the specific block.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_emails_in_unsubscribe_group

**This endpoint allows you to retrieve all suppressed email addresses belonging to the given group.**

Suppressions are recipient email addresses that are added to [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html). Once a recipient's address is on the suppressions list for an unsubscribe group, they will not receive any emails that are tagged with that unsubscribe group.

<details><summary>Parameters</summary>

### group_id (required)

The id of the unsubscribe group that you are adding suppressions to.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_footer_settings

**This endpoint allows you to retrieve your current Footer mail settings.**

The footer setting will insert a custom footer at the bottom of the text and HTML bodies. Use the embedded HTML editor and plain text entry fields to create the content of the footers to be inserted into your emails.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_invalid_email

**This endpoint allows you to retrieve a specific invalid email addresses.**

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipient’s mail server.

Examples include addresses without the “@” sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### email (required)

The specific email address of the invalid email entry that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_ip_from_whitelist

**This endpoint allows you to retreive a specific IP address that has been whitelisted.**

You must include the ID for the specific IP address you want to retrieve in your call.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

<details><summary>Parameters</summary>

### rule_id (required)

The ID of the whitelisted IP address that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_ips_assigned



*This operation has no parameters*

## get_ips_remaining



*This operation has no parameters*

## get_ips_warmup

**This endpoint allows you to retrieve all of your IP addresses that are currently warming up.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_lists_for_recipient

**This endpoint allows you to retrieve the lists that a given recipient belongs to.**

Each recipient can be on many lists. This endpoint gives you all of the lists that any one recipient has been added to.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### recipient_id (required)

The ID of the recipient for whom you are retrieving lists.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_monitor_settings_for_subuser

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

<details><summary>Parameters</summary>

### subuser_name (required)

The name of the subuser for which to retrieve monitor settings.

**Type:** string

</details>

## get_partner_settings

**This endpoint allows you to retrieve a list of all partner settings that you can enable.**

Our partner settings allow you to integrate your SendGrid account with our partners to increase your SendGrid experience and functionality. For more information about our partners, and how you can begin integrating with them, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/partners.html).

*This operation has no parameters*

## get_partner_settings_new_relic



*This operation has no parameters*

## get_plain_content_settings

**This endpoint allows you to retrieve your current Plain Content mail settings.**

The plain content setting will automatically convert any plain text emails that you send to HTML before sending.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_pool

**This endpoint allows you to list all of the IP addresses that are in a specific IP pool.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

<details><summary>Parameters</summary>

### pool_name (required)

The name of the IP pool that you want to retrieve the IP addresses from.

**Type:** string

</details>

## get_pools_for_ip

**This endpoint allows you to see which IP pools a particular IP address has been added to.**

The same IP address can be added to multiple IP pools.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

<details><summary>Parameters</summary>

### ip_address (required)

The IP address you are retrieving the IP pools for.

**Type:** string

</details>

## get_recipient

**This endpoint allows you to retrieve a single recipient by ID from your contact database.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### recipient_id (required)

The ID of the recipient that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_recipient_list

This endpoint allows you to retrieve a single recipient list.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_reputations_for_subusers

Subuser sender reputations give a good idea how well a sender is doing with regards to how recipients and recipient servers react to the mail that is being received. When a bounce, spam report, or other negative action happens on a sent email, it will effect your sender rating.

This endpoint allows you to request the reputations for your subusers.

<details><summary>Parameters</summary>

### usernames

**Type:** string

</details>

## get_reverse_dns_record

**This endpoint allows you to retrieve an IP whitelabel.**

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

<details><summary>Parameters</summary>

### id (required)

The id of the IP whitelabel that you would like to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_schedule_for_campaign

This endpoint allows you to retrieve the date and time that the given campaign has been scheduled to be sent.

<details><summary>Parameters</summary>

### campaign_id (required)

**Type:** integer

</details>

## get_segment

**This endpoint allows you to retrieve a single segment with the given ID.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

<details><summary>Parameters</summary>

### segment_id (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_sender

**This endpoint allows you to retrieve a specific sender identity.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

<details><summary>Parameters</summary>

### sender_id (required)

The ID of the sender identity that you want to update.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## get_spam_check_settings

**This endpoint allows you to retrieve your current Spam Checker mail settings.**

The spam checker filter notifies you when emails are detected that exceed a predefined spam threshold.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_spam_forward_settings

**This endpoint allows you to retrieve your current Forward Spam mail settings.**

Enabling the forward spam setting allows you to specify an email address to which spam reports will be forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_spam_report

**This endpoint allows you to retrieve a specific spam report.**

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

<details><summary>Parameters</summary>

### email (required)

The email address of a specific spam report that you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats

**This endpoint allows you to retrieve all of your global email statistics between a given date range.**

Parent accounts will see aggregated stats for their account and all subuser accounts. Subuser accounts will only see their own stats.

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_a_client_type

**This endpoint allows you to retrieve your email statistics segmented by a specific client type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

## Available Client Types
- phone
- tablet
- webmail
- desktop

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

<details><summary>Parameters</summary>

### client_type (required)

Specifies the type of client to retrieve stats for. Must be either "phone", "tablet", "webmail", or "desktop".

**Type:** string

**Potential values:** phone, tablet, webmail, desktop

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_browser

**This endpoint allows you to retrieve your email statistics segmented by browser type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the stats. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### browsers

The browsers to get statistics for. You can include up to 10 different browsers by including this parameter multiple times.

**Type:** string

### end_date

The end date of the statistics to retrieve. Defaults to today.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_category

**This endpoint allows you to retrieve all of your email statistics for each of your categories.**

If you do not define any query parameters, this endpoint will return a sum for each category in groups of 10.

Categories allow you to group your emails together according to broad topics that you define. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/categories.html).

<details><summary>Parameters</summary>

### categories (required)

The individual categories that you want to retrieve statistics for. You may include up to 10 different categories.

**Type:** string

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_client_type

**This endpoint allows you to retrieve your email statistics segmented by client type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_device_type

**This endpoint allows you to retrieve your email statistics segmented by the device type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

## Available Device Types
| **Device** | **Description** | **Example** |
|---|---|---|
| Desktop | Email software on desktop computer. | I.E., Outlook, Sparrow, or Apple Mail. |
| Webmail |	A web-based email client. | I.E., Yahoo, Google, AOL, or Outlook.com. |
| Phone | A smart phone. | iPhone, Android, Blackberry, etc.
| Tablet | A tablet computer. | iPad, android based tablet, etc. |
| Other | An unrecognized device. |

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve.

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

### end_date

The end date of the statistics to retrieve. Defaults to today.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_geo

**This endpoint allows you to retrieve your email statistics segmented by country and state/province.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### start_date (required)

The starting date of the statistics to retrieve. Must be in format YYYY-MM-DD

**Type:** string

### aggregated_by

How you would like the statistics to be grouped. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### country

The country you would like to see statistics for. Currently only supported for US and CA.

**Type:** string

**Potential values:** US, CA

### end_date

The end date of the statistics to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_by_mailbox_provider

**This endpoint allows you to retrieve your email statistics segmented by recipient mailbox provider.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the stats. Must be either "day", "wee", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### mailbox_providers

The mail box providers to get statistics for. You can include up to 10 by including this parameter multiple times.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_stats_for_a_subuser_monthly

**This endpoint allows you to retrive the monthly email statistics for a specific subuser.**

While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats for your subusers. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

When using the `sort_by_metric` to sort your stats by a specific metric, you can not sort by the following metrics:
`bounce_drops`, `deferred`, `invalid_emails`, `processed`, `spam_report_drops`, `spam_reports`, or `unsubscribe_drops`.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

<details><summary>Parameters</summary>

### date (required)

The date of the month to retrieve statistics for. Must be formatted YYYY-MM-DD

**Type:** string

### subuser_name (required)

**Type:** string

### sort_by_direction

The direction you want to sort.

**Type:** string

**Potential values:** desc, asc

### sort_by_metric

The metric that you want to sort by. Metrics that you can sort by are: `blocks`, `bounces`, `clicks`, `delivered`, `opens`, `requests`, `unique_clicks`, `unique_opens`, and `unsubscribes`.'

**Type:** string

</details>

## get_stats_for_subusers

**This endpoint allows you to retrieve the email statistics for the given subusers.**

You may retrieve statistics for up to 10 different subusers by including an additional _subusers_ parameter for each additional subuser.

While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### subusers (required)

The subuser you want to retrieve statistics for. You may include this parameter up to 10 times to retrieve statistics for multiple subusers.

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today.

**Type:** string

</details>

## get_stats_for_subusers_monthly

**This endpoint allows you to retrieve the monthly email statistics for all subusers over the given date range.**

While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats for your subusers. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

When using the `sort_by_metric` to sort your stats by a specific metric, you can not sort by the following metrics:
`bounce_drops`, `deferred`, `invalid_emails`, `processed`, `spam_report_drops`, `spam_reports`, or `unsubscribe_drops`.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

<details><summary>Parameters</summary>

### date (required)

The date of the month to retrieve statistics for. Must be formatted YYYY-MM-DD

**Type:** string

### sort_by_direction

The direction you want to sort.

**Type:** string

**Potential values:** desc, asc

### sort_by_metric

The metric that you want to sort by. Metrics that you can sort by are: `blocks`, `bounces`, `clicks`, `delivered`, `opens`, `requests`, `unique_clicks`, `unique_opens`, and `unsubscribes`.'

**Type:** string

### subuser

A substring search of your subusers.

**Type:** string

</details>

## get_stats_for_subusers_summed

**This endpoint allows you to retrieve the total sums of each email statistic metric for all subusers over the given date range.**


While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the statistics. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### sort_by_direction

The direction you want to sort.

**Type:** string

**Potential values:** desc, asc

### sort_by_metric

The metric that you want to sort by. Must be a single metric.

**Type:** string

</details>

## get_summed_stats_by_category

**This endpoint allows you to retrieve the total sum of each email statistic for every category over the given date range.**

If you do not define any query parameters, this endpoint will return a sum for each category in groups of 10.

Categories allow you to group your emails together according to broad topics that you define. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/categories.html).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics to retrieve. Must follow format YYYY-MM-DD.

**Type:** string

### aggregated_by

How to group the statistics. Must be either "day", "week", or "month".

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics to retrieve. Defaults to today. Must follow format YYYY-MM-DD.

**Type:** string

### on-behalf-of

**Type:** string

### sort_by_direction

The direction you want to sort.

**Type:** string

**Potential values:** desc, asc

### sort_by_metric

The metric that you want to sort by. Must be a single metric.

**Type:** string

</details>

## get_teammate

This endpoint allows you to retrieve a specific teammate by username.

<details><summary>Parameters</summary>

### username (required)

The username of the teammate that you want to retrieve.

**Type:** string

</details>

## get_template

**This endpoint allows you to retrieve a single transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

<details><summary>Parameters</summary>

### template_id (required)

The id of the transactional template you want to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_template_settings

**This endpoint allows you to retrieve your current legacy email template settings.**

This setting refers to our original email templates. We currently support more fully featured [transactional templates](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html). 

The legacy email template setting wraps an HTML template around your email content. This can be useful for sending out marketing email and/or other HTML formatted messages.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_total_count_recipients

**This endpoint allows you to retrieve the total number of Marketing Campaigns recipients.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_tracking_settings_click

**This endpoint allows you to retrieve your current click tracking setting.**

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_tracking_settings_google_analytics

**This endpoint allows you to retrieve your current setting for Google Analytics.**

For more information about using Google Analytics, please refer to [Google’s URL Builder](https://support.google.com/analytics/answer/1033867?hl=en) and their article on ["Best Practices for Campaign Building"](https://support.google.com/analytics/answer/1037445).

We default the settings to Google’s recommendations. For more information, see [Google Analytics Demystified](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/google_analytics_demystified_ga_statistics_vs_sg_statistics.html).

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_tracking_settings_open

**This endpoint allows you to retrieve your current settings for open tracking.**

Open Tracking adds an invisible image at the end of the email which can track email opens. If the email recipient has images enabled on their email client, a request to SendGrid’s server for the invisible image is executed and an open event is logged. These events are logged in the Statistics portal, Email Activity interface, and are reported by the Event Webhook.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_tracking_settings_subscription

**This endpoint allows you to retrieve your current settings for subscription tracking.**

Subscription tracking adds links to the bottom of your emails that allows your recipients to subscribe to, or unsubscribe from, your emails.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_unsubscribe_group

**This endpoint allows you to retrieve a single suppression group.**

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

<details><summary>Parameters</summary>

### group_id (required)

The ID of the suppression group you would like to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_unsubscribe_groups_for_email

**This endpoint returns the list of all groups that the given email address has been unsubscribed from.**

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

<details><summary>Parameters</summary>

### email (required)

The email address that you want to search suppression groups for.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_upload_status



<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_user_account

**This endpoint allows you to retrieve your user account details.**

Your user's account information includes the user's account type and reputation.

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_user_credits

**This endpoint allows you to retrieve the current credit balance for your account.**

Your monthly credit allotment limits the number of emails you may send before incurring overage charges. For more information about credits and billing, please visit our [Clssroom](https://sendgrid.com/docs/Classroom/Basics/Billing/billing_info_and_faqs.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_user_email

**This endpoint allows you to retrieve the email address currently on file for your account.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_user_profile

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_user_scheduled_send

**This endpoint allows you to retrieve the cancel/paused scheduled send information for a specific `batch_id`.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header. Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

<details><summary>Parameters</summary>

### batch_id (required)

**Type:** string

</details>

## get_user_settings_enforced_tls

**This endpoint allows you to retrieve your current Enforced TLS settings.**

The Enforced TLS settings specify whether or not the recipient is required to support TLS or have a valid certificate. See the [SMTP Ports User Guide](https://sendgrid.com/docs/Classroom/Basics/Email_Infrastructure/smtp_ports.html) for more information on opportunistic TLS.

**Note:** If either setting is enabled and the recipient does not support TLS or have a valid certificate, we drop the message and send a block event with “TLS required but not supported” as the description.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_username

**This endpoint allows you to retrieve your current account username.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_version_of_template

**This endpoint allows you to retrieve a specific version of a template.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string |  The ID of the template version |

<details><summary>Parameters</summary>

### template_id (required)

**Type:** string

### version_id (required)

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_warmup_status_for_ip

**This endpoint allows you to retrieve the warmup status for a specific IP address.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

<details><summary>Parameters</summary>

### ip_address (required)

The IP address that you want to retrieve the warmup status for.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_webhooks_events_settings

**This endpoint allows you to retrieve your current event webhook settings.**

If an event type is marked as `true`, then the event webhook will include information about that event.

SendGrid’s Event Webhook will notify a URL of your choice via HTTP POST with information about events that occur as SendGrid processes your email.

Common uses of this data are to remove unsubscribes, react to spam reports, determine unengaged recipients, identify bounced email addresses, or create advanced analytics of your email program.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## get_webhooks_parse_setting

**This endpoint allows you to retrieve a specific inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

<details><summary>Parameters</summary>

### hostname (required)

The hostname associated with the inbound parse setting that you would like to retrieve.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## get_webhooks_parse_stats

**This endpoint allows you to retrieve the statistics for your Parse Webhook usage.**

SendGrid's Inbound Parse Webhook allows you to parse the contents and attachments of incomming emails. The Parse API can then POST the parsed emails to a URL that you specify. The Inbound Parse Webhook cannot parse messages greater than 20MB in size, including all attachments.

There are a number of pre-made integrations for the SendGrid Parse Webhook which make processing events easy. You can find these integrations in the [Library Index](https://sendgrid.com/docs/Integrate/libraries.html#-Webhook-Libraries).

<details><summary>Parameters</summary>

### start_date (required)

The starting date of the statistics you want to retrieve. Must be in the format YYYY-MM-DD

**Type:** string

### aggregated_by

How you would like the statistics to by grouped.

**Type:** string

**Potential values:** day, week, month

### end_date

The end date of the statistics you want to retrieve. Must be in the format YYYY-MM-DD

**Type:** string

### on-behalf-of

**Type:** string

</details>

## invite_teammate

This endpoint allows you to send a teammate invitation via email with a predefined set of scopes, or permissions.

**Note:** A teammate invite will expire after 7 days, but you may resend the invite at any time to reset the expiration date.

Essentials, [Legacy Lite](https://sendgrid.com/docs/Classroom/Basics/Billing/legacy_lite_plan.html), and Free Trial users may create up to one teammate per account. There are no limits for how many teammates a Pro or higher account may create.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "is_admin" : "Set to true if teammate should be an admin user",
  "scopes" : [ "string" ],
  "email" : "New teammate's email"
}
```

</details>

## is_email_in_global_unsubscribe_group

**This endpoint allows you to retrieve a global suppression. You can also use this endpoint to confirm if an email address is already globally suppresed.**

If the email address you include in the URL path parameter `{email}` is alreayd globally suppressed, the response will include that email address. If the address you enter for `{email}` is not globally suppressed, an empty JSON object `{}` will be returned.

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

<details><summary>Parameters</summary>

### email (required)

The email address of the global suppression you want to retrieve. Or, if you want to check if an email address is on the global suppressions list, enter that email address here.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## list_access_requests_recent

This endpoint allows you to retrieve a list of all recent access requests.

**Note:** The Response Header's 'link' parameter will include pagination info. For example:

link: ```; rel="first"; title="1", ; rel="last"; title="2", ; rel="prev"; title="1"```

*This operation has no parameters*

## list_alerts

**This endpoint allows you to retieve all of your alerts.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

<details><summary>Parameters</summary>

### Authorization

**Type:** string

### on-behalf-of

**Type:** string

</details>

## list_all_unsubscribed

**This endpoint allows you to retrieve a list of all suppressions.**

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_api_keys

**This endpoint allows you to retrieve all API Keys that belong to the authenticated user.**

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_authenticated_domains

**This endpoint allows you to retrieve a list of all domain whitelabels you have created.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

<details><summary>Parameters</summary>

### domain

Search for domain whitelabels that match the given domain.

**Type:** string

### exclude_subusers

Exclude subuser domains from the result.

**Type:** boolean

### on-behalf-of

**Type:** string

### username

The username associated with a whitelabel.

**Type:** string

</details>

## list_authenticated_domains_for_subuser

**This endpoint allows you to retrieve all of the whitelabels that have been assigned to a specific subuser.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

Domain whitelabels can be associated with (i.e. assigned to) subusers from a parent account. This functionality allows subusers to send mail using their parent's whitelabels. To associate a whitelabel with a subuser, the parent account must first create the whitelabel and validate it. The the parent may then associate the whitelabel via the subuser management tools.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  | Description  |
|---|---|---|
| username | string  | Username of the subuser to find associated whitelabels for. |

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_blocked_emails

**This endpoint allows you to retrieve a list of all email addresses that are currently on your blocks list.**

There are several causes for [blocked](https://sendgrid.com/docs/Glossary/blocks.html) emails: for example, your mail server IP address is on an ISP blacklist, or blocked by an ISP, or if the receiving server flags the message content.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

<details><summary>Parameters</summary>

### end_time

Refers end of the time range in unix timestamp when a blocked email was created (inclusive).

**Type:** integer

### on-behalf-of

**Type:** string

### start_time

Refers start of the time range in unix timestamp when a blocked email was created (inclusive).

**Type:** integer

</details>

## list_bounces

**This endpoint allows you to retrieve all of your bounces.**

A bounced email is when the message is undeliverable and then returned to the server that sent it.  

For more information see: 

* [User Guide &gt; Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary &gt; Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)

<details><summary>Parameters</summary>

### Accept (required)

**Type:** string

### end_time

Refers end of the time range in unix timestamp when a bounce was created (inclusive).

**Type:** integer

### on-behalf-of

**Type:** string

### start_time

Refers start of the time range in unix timestamp when a bounce was created (inclusive).

**Type:** integer

</details>

## list_branded_links

**This endpoint allows you to retrieve all link whitelabels.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_branded_links_for_subuser

**This endpoint allows you to retrieve the associated link whitelabel for a subuser.**

Link whitelables can be associated with subusers from the parent account. This functionality allows
subusers to send mail using their parent's linke whitelabels. To associate a link whitelabel, the parent account
must first create a whitelabel and validate it. The parent may then associate that whitelabel with a subuser via the API or the Subuser Management page in the user interface.

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### username (required)

The username of the subuser to retrieve associated link whitelabels for.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## list_campaigns

**This endpoint allows you to retrieve a list of all of your campaigns.**

Returns campaigns in reverse order they were created (newest first).

Returns an empty array if no campaigns exist.

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

*This operation has no parameters*

## list_categories

**This endpoint allows you to retrieve a list of all of your categories.**

Categories can help organize your email analytics by enabling you to “tag” emails by type or broad topic. You can define your own custom categories. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/categories.html).

<details><summary>Parameters</summary>

### category

Allows you to perform a prefix search on this particular category.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## list_custom_fields

**This endpoint allows you to retrieve all custom fields.** 

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_global_unsubscribes

**This endpoint allows you to retrieve a list of all email address that are globally suppressed.**

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

<details><summary>Parameters</summary>

### end_time

Refers end of the time range in unix timestamp when an unsubscribe email was created (inclusive).

**Type:** integer

### on-behalf-of

**Type:** string

### start_time

Refers start of the time range in unix timestamp when an unsubscribe email was created (inclusive).

**Type:** integer

</details>

## list_invalid_emails

**This endpoint allows you to retrieve a list of all invalid email addresses.**

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipient’s mail server.

Examples include addresses without the “@” sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

<details><summary>Parameters</summary>

### end_time

Refers end of the time range in unix timestamp when an invalid email was created (inclusive).

**Type:** integer

### on-behalf-of

**Type:** string

### start_time

Refers start of the time range in unix timestamp when an invalid email was created (inclusive).

**Type:** integer

</details>

## list_ips

**This endpoint allows you to retrieve a list of all assigned and unassigned IPs.**

Response includes warm up status, pools, assigned subusers, and whitelabel info. The start_date field corresponds to when warmup started for that IP.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

<details><summary>Parameters</summary>

### exclude_whitelabels

Should we exclude whitelabels?

**Type:** boolean

### ip

The IP address to get

**Type:** string

### sort_by_direction

The direction to sort the results.

**Type:** string

**Potential values:** desc, asc

### subuser

The subuser you are requesting for.

**Type:** string

</details>

## list_ips_in_whitelist

**This endpoint allows you to retrieve a list of IP addresses that are currently whitelisted.**

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_ips_with_recent_activity

**This endpoint allows you to retrieve a list of all of the IP addresses that recently attempted to access your account either through the User Interface or the API.**

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_mail_settings

**This endpoint allows you to retrieve a list of all mail settings.**

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_pools



*This operation has no parameters*

## list_recipient_lists

**This endpoint allows you to retrieve all of your recipient lists. If you don't have any lists, an empty array will be returned.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_recipients

**This endpoint allows you to retrieve all of your Marketing Campaigns recipients.**

Batch deletion of a page makes it possible to receive an empty page of recipients before reaching the end of
the list of recipients. To avoid this issue; iterate over pages until a 404 is retrieved.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_recipients_for_list

**This endpoint allows you to retrieve all recipients on the list with the given ID.** 

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

The id of the list of recipients you want to retrieve.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## list_recipients_for_segment

**This endpoint allows you to retrieve all of the recipients in a segment with the given ID.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

<details><summary>Parameters</summary>

### segment_id (required)

The ID of the segment from which you want to retrieve recipients.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## list_reserved_fields

**This endpoint allows you to list all fields that are reserved and can't be used for custom field names.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_reverse_dns_records

**This endpoint allows you to retrieve all of the IP whitelabels that have been createdy by this account.**

You may include a search key by using the "ip" parameter. This enables you to perform a prefix search for a given IP segment (e.g. "192.").

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

<details><summary>Parameters</summary>

### ip

The IP segment that you would like to use in a prefix search.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## list_scopes

**This endpoint returns a list of all scopes that this user has access to.**

API Keys can be used to authenticate the use of [SendGrid’s v3 Web API](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html), or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html). API Keys may be assigned certain permissions, or scopes, that limit which API endpoints they are able to access. For a more detailed explanation of how you can use API Key permissios, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/api_keys.html#-API-Key-Permissions) or [Classroom](https://sendgrid.com/docs/Classroom/Basics/API/api_key_permissions.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_segments

**This endpoint allows you to retrieve all of your segments.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_senders

**This endpoint allows you to retrieve a list of all sender identities that have been created for your account.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_spam_reports

**This endpoint allows you to retrieve all spam reports.**

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

<details><summary>Parameters</summary>

### end_time

Refers end of the time range in unix timestamp when a spam report was created (inclusive).

**Type:** integer

### on-behalf-of

**Type:** string

### start_time

Refers start of the time range in unix timestamp when a spam report was created (inclusive).

**Type:** integer

</details>

## list_subusers

This endpoint allows you to retrieve a list of all of your subusers. You can choose to retrieve specific subusers as well as limit the results that come back from the API.

For more information about Subusers:

* [User Guide &gt; Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom &gt; How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

<details><summary>Parameters</summary>

### username

The username of this subuser.

**Type:** string

</details>

## list_teammates

This endpoint allows you to retrieve a list of all current teammates.

**Note:** The Response Header will include pagination info. For example:

link: ```; rel="first"; title="1", ; rel="last"; title="2", ; rel="prev"; title="1"```

*This operation has no parameters*

## list_teammates_pending



*This operation has no parameters*

## list_templates

**This endpoint allows you to retrieve all transactional templates.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_tracking_settings

**This endpoint allows you to retrieve a list of all tracking settings that you can enable on your account.**

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## list_unsubscribe_groups

**This endpoint allows you to retrieve information about multiple suppression groups.**

This endpoint will return information for each group ID that you include in your request. To add a group ID to your request, simply append `&amp;id=` followed by the group ID.

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

Suppression groups, or [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html), allow you to label a category of content that you regularly send. This gives your recipients the ability to opt out of a specific set of your email. For example, you might define a group for your transactional email, and one for your marketing email so that your users can continue recieving your transactional email witout having to receive your marketing content.

<details><summary>Parameters</summary>

### id

The ID of a suppression group that you want to retrieve information for.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## list_user_scheduled_sends



*This operation has no parameters*

## list_webhooks_parse_settings

**This endpoint allows you to retrieve all of your current inbound parse settings.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

</details>

## post_whitelabel_domains_id_validate

**This endpoint allows you to validate a domain whitelabel. If it fails, it will return an error message describing why the whitelabel could not be validated.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type   | Description  |
|---|---|---|
| id | integer  |ID of the domain whitelabel to validate. |

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

### on-behalf-of

**Type:** string

</details>

## remove_branded_link_from_subuser

**This endpoint allows you to disassociate a link whitelabel from a subuser.**

Link whitelables can be associated with subusers from the parent account. This functionality allows
subusers to send mail using their parent's linke whitelabels. To associate a link whitelabel, the parent account
must first create a whitelabel and validate it. The parent may then associate that whitelabel with a subuser via the API or the Subuser Management page in the user interface.

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### username (required)

The username of the subuser account that you want to disassociate a link whitelabel from.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## resend_sender_verification

**This enpdoint allows you to resend a sender identity verification email.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

<details><summary>Parameters</summary>

### sender_id (required)

The ID of the sender identity for which you would like to resend a verification email.

**Type:** integer

### on-behalf-of

**Type:** string

</details>

## resend_teammate_invite

This endpoint allows you to resend a teammate invite.

**Note:** Teammate invitations will expire after 7 days. Resending an invite will reset the expiration date.

<details><summary>Parameters</summary>

### token (required)

The token for the invite that you want to resend.

**Type:** string

</details>

## schedule_campaign

**This endpoint allows you to schedule a specific date and time for your campaign to be sent.**

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

**Type:** integer

### $body

**Type:** object

```json
{
  "send_at" : "The unix timestamp for the date and time you would like your campaign to be sent out."
}
```

</details>

## search_recipients

**This endpoint allows you to perform a search on all of your Marketing Campaigns recipients.**

field_name:

* is a variable that is substituted for your actual custom field name from your recipient.
* Text fields must be url-encoded. Date fields are searchable only by unix timestamp (e.g. 2/2/2015 becomes 1422835200)
* If field_name is a 'reserved' date field, such as created_at or updated_at, the system will internally convert
your epoch time to a date range encompassing the entire day. For example, an epoch time of 1422835600 converts to
Mon, 02 Feb 2015 00:06:40 GMT, but internally the system will search from Mon, 02 Feb 2015 00:00:00 GMT through
Mon, 02 Feb 2015 23:59:59 GMT.

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### on-behalf-of

**Type:** string

### {field_name}

**Type:** string

</details>

## search_unsubscribe_group

**This endpoint allows you to search a suppression group for multiple suppressions.**

When given a list of email addresses and a group ID, this endpoint will return only the email addresses that have been unsubscribed from the given group.

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

<details><summary>Parameters</summary>

### group_id (required)

The ID of the suppression group that you would like to search.

**Type:** string

### $body

**Type:** object

```json
{
  "recipient_emails" : [ "string" ]
}
```

### on-behalf-of

**Type:** string

</details>

## send_campaign_now

**This endpoint allows you to immediately send a campaign at the time you make the API call.**

Normally a POST would have a request body, but since this endpoint is telling us to send a resource that is already created, a request body is not needed.

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## send_campaign_test

**This endpoint allows you to send a test campaign.**

To send to multiple addresses, use an array for the JSON "to" value ["one@address","two@address"]

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

**Type:** integer

### $body

**Type:** object

```json
{
  "to" : "The email address that should receive the test campaign."
}
```

</details>

## send_mail

This endpoint allows you to send email over SendGrid’s v3 Web API, the most recent version of our API. If you are looking for documentation about the v2 Mail Send endpoint, please see our [v2 API Reference](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

* Top level parameters are referred to as "global".
* Individual fields within the personalizations array will override any other global, or “message level”, parameters that are defined outside of personalizations.
 
**SendGrid provides libraries to help you quickly and easily integrate with the v3 Web API in 7 different languages: [C#](https://github.com/sendgrid/sendgrid-csharp), [Go](https://github.com/sendgrid/sendgrid-go), [Java](https://github.com/sendgrid/sendgrid-java), [Node JS](https://github.com/sendgrid/sendgrid-nodejs), [PHP](https://github.com/sendgrid/sendgrid-php), [Python](https://github.com/sendgrid/sendgrid-python), and [Ruby](https://github.com/sendgrid/sendgrid-ruby).**


For more detailed information about how to use the v3 Mail Send endpoint, please visit our [Classroom](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "headers" : { },
  "mail_settings" : {
    "sandbox_mode" : {
      "enable" : "Indicates if this setting is enabled."
    },
    "bcc" : {
      "enable" : "Indicates if this setting is enabled.",
      "email" : "The email address that you would like to receive the BCC."
    },
    "footer" : {
      "enable" : "Indicates if this setting is enabled.",
      "html" : "The HTML content of your footer.",
      "text" : "The plain text content of your footer."
    },
    "spam_check" : {
      "enable" : "Indicates if this setting is enabled.",
      "threshold" : "The threshold used to determine if your content qualifies as spam on a scale from 1 to 10, with 10 being most strict, or most likely to be considered as spam.",
      "post_to_url" : "An Inbound Parse URL that you would like a copy of your email along with the spam report to be sent to."
    },
    "bypass_list_management" : {
      "enable" : "Indicates if this setting is enabled."
    }
  },
  "personalizations" : [ {
    "cc" : [ {
      "name" : "The name of the person to whom you are sending an email.",
      "email" : "Required email"
    } ],
    "headers" : { },
    "bcc" : [ {
      "name" : "The name of the person to whom you are sending an email.",
      "email" : "Required email"
    } ],
    "substitutions" : { },
    "subject" : "The subject of your email. Char length requirements, according to the RFC - http://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit#answer-1592310",
    "send_at" : "A unix timestamp allowing you to specify when you want your email to be delivered. Scheduling more than 72 hours in advance is forbidden.",
    "to" : [ {
      "name" : "The name of the person to whom you are sending an email.",
      "email" : "Required email"
    } ],
    "custom_args" : { }
  } ],
  "attachments" : [ {
    "disposition" : "The content-disposition of the attachment specifying how you would like the attachment to be displayed. For example, “inline” results in the attached file being displayed automatically within the message while “attachment” results in the attached file requiring some action to be taken before it is displayed (e.g. opening or downloading the file).",
    "filename" : "The filename of the attachment.",
    "content_id" : "The content id for the attachment. This is used when the disposition is set to “inline” and the attachment is an image, allowing the file to be displayed within the body of your email.",
    "type" : "The mime type of the content you are attaching. For example, “text/plain” or “text/html”.",
    "content" : "The Base64 encoded content of the attachment."
  } ],
  "tracking_settings" : {
    "click_tracking" : {
      "enable" : "Indicates if this setting is enabled.",
      "enable_text" : "Indicates if this setting should be included in the text/plain portion of your email."
    },
    "subscription_tracking" : {
      "enable" : "Indicates if this setting is enabled.",
      "html" : "HTML to be appended to the email, with the subscription tracking link. You may control where the link is by using the tag &lt;% %&gt;",
      "text" : "Text to be appended to the email, with the subscription tracking link. You may control where the link is by using the tag &lt;% %&gt;",
      "substitution_tag" : "A tag that will be replaced with the unsubscribe URL. for example: [unsubscribe_url]. If this parameter is used, it will override both the `text` and `html` parameters. The URL of the link will be placed at the substitution tag’s location, with no additional formatting."
    },
    "ganalytics" : {
      "utm_term" : "Used to identify any paid keywords.",
      "utm_campaign" : "The name of the campaign.",
      "enable" : "Indicates if this setting is enabled.",
      "utm_medium" : "Name of the marketing medium. (e.g. Email)",
      "utm_content" : "Used to differentiate your campaign from advertisements.",
      "utm_source" : "Name of the referrer source. (e.g. Google, SomeDomain.com, or Marketing Email)"
    },
    "open_tracking" : {
      "enable" : "Indicates if this setting is enabled.",
      "substitution_tag" : "Allows you to specify a substitution tag that you can insert in the body of your email at a location that you desire. This tag will be replaced by the open tracking pixel."
    }
  },
  "batch_id" : "This ID represents a batch of emails to be sent at the same time. Including a batch_id in your request allows you include this email in that batch, and also enables you to cancel or pause the delivery of that batch. For more information, see https://sendgrid.com/docs/API_Reference/Web_API_v3/cancel_schedule_send.html",
  "subject" : "The global, or “message level”, subject of your email. This may be overridden by personalizations[x].subject.",
  "send_at" : "A unix timestamp allowing you to specify when you want your email to be delivered. This may be overridden by the personalizations[x].send_at parameter. Scheduling more ta 72 hours in advance is forbidden.",
  "content" : [ {
    "type" : "The mime type of the content you are including in your email. For example, “text/plain” or “text/html”.",
    "value" : "The actual content of the specified mime type that you are including in your email."
  } ],
  "sections" : { },
  "custom_args" : { },
  "reply_to" : {
    "name" : "The name of the person to whom you are sending an email.",
    "email" : "Required email"
  },
  "asm" : {
    "group_id" : "The unsubscribe group to associate with this email.",
    "groups_to_display" : [ "integer" ]
  },
  "from" : {
    "name" : "The name of the person to whom you are sending an email.",
    "email" : "Required email"
  },
  "ip_pool_name" : "The IP Pool that you would like to send this email from.",
  "template_id" : "The id of a template that you would like to use. If you use a template that contains a subject and content (either text or html), you do not need to specify those at the personalizations nor message level.",
  "categories" : [ "string" ]
}
```

</details>

## stop_warmup_ip

**This endpoint allows you to remove an IP address from warmup mode.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

<details><summary>Parameters</summary>

### ip_address (required)

The IP address that you want to retrieve the warmup status for.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## test_webhook

**This endpoint allows you to test your event webhook by sending a fake event notification post to the provided URL.**

SendGrid’s Event Webhook will notify a URL of your choice via HTTP POST with information about events that occur as SendGrid processes your email.

Common uses of this data are to remove unsubscribes, react to spam reports, determine unengaged recipients, identify bounced email addresses, or create advanced analytics of your email program.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "url" : "The URL where you would like the test notification to be sent."
}
```

### on-behalf-of

**Type:** string

</details>

## unblock_email

**This endpoint allows you to delete a specific email address from your blocks list.**

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### email (required)

The email address of the specific block.

**Type:** string

### on-behalf-of

**Type:** string

</details>

## uninvite_teammate

This endpoint allows you to delete a pending teammate invite.

<details><summary>Parameters</summary>

### token (required)

The token for the invite you want to delete.

**Type:** string

</details>

## unschedule_campaign

**This endpoint allows you to unschedule a campaign that has already been scheduled to be sent.**

A successful unschedule will return a 204.
If the specified campaign is in the process of being sent, the only option is to cancel (a different method).

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

**Type:** integer

</details>

## update_address_whitelist

**This endpoint allows you to update your current email address whitelist settings.**

The address whitelist setting whitelists a specified email address or domain for which mail should never be suppressed. For example, you own the domain “example.com,” and one or more of your recipients use email@example.com addresses, by placing example.com in the address whitelist setting, all bounces, blocks, and unsubscribes logged for that domain will be ignored and sent as if under normal sending conditions.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "list" : [ "string" ],
  "enabled" : "Indicates if your email address whitelist is enabled."
}
```

### on-behalf-of

**Type:** string

</details>

## update_alert

**This endpoint allows you to update an alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

<details><summary>Parameters</summary>

### alert_id (required)

The ID of the alert you would like to retrieve.

**Type:** integer

### $body

**Type:** object

```json
{
  "email_to" : "The new email address you want your alert to be sent to.\nExample: test@example.com",
  "percentage" : "The new percentage threshold at which the usage_limit alert will be sent.\nExample: 90",
  "frequency" : "The new frequency at which to send the stats_notification alert.\nExample: monthly"
}
```

### on-behalf-of

**Type:** string

</details>

## update_api_key

**This endpoint allows you to update the name and scopes of a given API key.**

A JSON request body with a "name" property is required.
Most provide the list of all the scopes an api key should have.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

<details><summary>Parameters</summary>

### api_key_id (required)

The ID of the API Key for which you are requesting information.

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "string",
  "scopes" : [ "string" ]
}
```

### on-behalf-of

**Type:** string

</details>

## update_authenticated_domain

**This endpoint allows you to update the settings for a domain whitelabel.**

A domain whitelabel allows you to remove the “via” or “sent on behalf of” message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

<details><summary>Parameters</summary>

### domain_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "default" : "Indicates whether this domain whitelabel should be considered the default.",
  "custom_spf" : "Indicates whether to generate a custom SPF record for manual security."
}
```

### on-behalf-of

**Type:** string

</details>

## update_bcc_settings

**This endpoint allows you to update your current BCC mail settings.**

When the BCC mail setting is enabled, SendGrid will automatically send a blind carbon copy (BCC) to an address for every email sent without adding that address to the header. Please note that only one email address may be entered in this field, if you wish to distribute BCCs to multiple addresses you will need to create a distribution group or use forwarding rules.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "email" : "The email address of the recipient.",
  "enabled" : "Indicates if the mail setting is enabled."
}
```

### on-behalf-of

**Type:** string

</details>

## update_bounce_forward_settings

**This endpoint allows you to update your current bounce forwarding mail settings.**

Activating this setting allows you to specify an email address to which bounce reports are forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "email" : "The email address that you would like your bounce reports forwarded to.",
  "enabled" : "Indicates if the bounce forwarding mail setting is enabled."
}
```

### on-behalf-of

**Type:** string

</details>

## update_bounce_purge_settings

**This endpoint allows you to update your current bounce purge settings.**

This setting allows you to set a schedule for SendGrid to automatically delete contacts from your soft and hard bounce suppression lists.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "hard_bounces" : "The number of days, after which SendGrid will purge all contacts from your hard bounces suppression lists.",
  "soft_bounces" : "The number of days, after which SendGrid will purge all contacts from your soft bounces suppression lists.",
  "enabled" : "Indicates if the bounce purge mail setting is enabled."
}
```

### on-behalf-of

**Type:** string

</details>

## update_branded_link

**This endpoint allows you to update a specific link whitelabel. You can use this endpoint to change a link whitelabel's default status.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### id (required)

The id of the link whitelabel you want to retrieve.

**Type:** integer

### $body

**Type:** object

```json
{
  "default" : "Indicates if the link whitelabel is set as the default, or fallback, whitelabel."
}
```

### on-behalf-of

**Type:** string

</details>

## update_campaign

Update a campaign. This is especially useful if you only set up the campaign using POST /campaigns, but didn't set many of the parameters.

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

The id of the campaign you would like to retrieve.

**Type:** integer

### $body

**Type:** object

```json
{
  "html_content" : "The HTML content of this campaign.",
  "subject" : "The subject line for your campaign.",
  "categories" : [ "string" ],
  "title" : "The title of the campaign.",
  "plain_content" : "The plain content of this campaign."
}
```

</details>

## update_footer_settings

**This endpoint allows you to update your current Footer mail settings.**

The footer setting will insert a custom footer at the bottom of the text and HTML bodies. Use the embedded HTML editor and plain text entry fields to create the content of the footers to be inserted into your emails.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "html_content" : "The custom HTML content of your email footer.",
  "enabled" : "Indicates if the Footer mail setting is currently enabled.",
  "plain_content" : "The plain text content of your email footer."
}
```

### on-behalf-of

**Type:** string

</details>

## update_ips_for_subuser

Each subuser should be assigned to an IP address, from which all of this subuser's mail will be sent. Often, this is the same IP as the parent account, but each subuser can have their own, or multiple, IP addresses as well. 

More information:

* [How to request more IPs](https://sendgrid.com/docs/Classroom/Basics/Account/adding_an_additional_dedicated_ip_to_your_account.html)
* [IPs can be whitelabeled](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/ips.html)

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### subuser_name (required)

**Type:** string

### $body

The IP addresses you would like to assign to the subuser.

**Type:** array

```json
[ "ipv4" ]
```

</details>

## update_monitor_settings_for_subuser

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

<details><summary>Parameters</summary>

### subuser_name (required)

The name of the subuser for which to retrieve monitor settings.

**Type:** string

### $body

**Type:** object

```json
{
  "email" : "The email address to send emails at the frequency specified for monitoring.",
  "frequency" : "The frequency by which to send the emails. An email will be sent, every time your subuser sends this {frequency} emails."
}
```

</details>

## update_name_of_api_key

**This endpoint allows you to update the name of an existing API Key.**

A JSON request body with a "name" property is required.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

## URI Parameters

| URI Parameter   | Type  | Required?  | Description  |
|---|---|---|---|
|api_key_id |string | required | The ID of the API Key you are updating.|

<details><summary>Parameters</summary>

### api_key_id (required)

The ID of the API Key for which you are requesting information.

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "The new name of the API Key."
}
```

### on-behalf-of

**Type:** string

</details>

## update_name_of_pool

**This endpoint allows you to update the name of an IP pool.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

<details><summary>Parameters</summary>

### pool_name (required)

The name of the IP pool that you want to retrieve the IP addresses from.

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "The new name for your IP pool."
}
```

</details>

## update_partner_settings_new_relic

**This endpoint allows you to update or change your New Relic partner settings.**

Our partner settings allow you to integrate your SendGrid account with our partners to increase your SendGrid experience and functionality. For more information about our partners, and how you can begin integrating with them, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/partners.html).

By integrating with New Relic, you can send your SendGrid email statistics to your New Relic Dashboard. If you enable this setting, your stats will be sent to New Relic every 5 minutes. You will need your New Relic License Key to enable this setting. For more information, please see our [Classroom](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/new_relic.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "enable_subuser_statistics" : "Indicates if your subuser statistics will be sent to your New Relic Dashboard.",
  "enabled" : "Indicates if this partner setting is enabled.",
  "license_key" : "The license key for your New Relic account."
}
```

</details>

## update_plain_content_settings

**This endpoint allows you to update your current Plain Content mail settings.**

The plain content setting will automatically convert any plain text emails that you send to HTML before sending.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "enabled" : "The new setting you would like to use for your Plain Content mail setting."
}
```

### on-behalf-of

**Type:** string

</details>

## update_recipient_list

**This endpoint allows you to update the name of one of your recipient lists.**


The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

<details><summary>Parameters</summary>

### list_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "The new name for your list."
}
```

### on-behalf-of

**Type:** string

</details>

## update_recipients

**This endpoint allows you to update one or more recipients.**

The body of an API call to this endpoint must include an array of one or more recipient objects.

It is of note that you can add custom field data as parameters on recipient objects. We have provided an example using some of the default custom fields SendGrid provides.

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** array

```json
[ {
  "last_name" : "The last name of the recipient. This is one of the default custom fields.",
  "first_name" : "The first name of the recipient. This is one of the default custom fields.",
  "email" : "Required email"
} ]
```

### on-behalf-of

**Type:** string

</details>

## update_schedule_for_campaign

**This endpoint allows to you change the scheduled time and date for a campaign to be sent.**

For more information:

* [User Guide &gt; Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

<details><summary>Parameters</summary>

### campaign_id (required)

**Type:** integer

### $body

**Type:** object

```json
{
  "send_at" : "Required integer"
}
```

</details>

## update_segment

**This endpoint allows you to update a segment.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

<details><summary>Parameters</summary>

### segment_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "list_id" : "The list ID you would like this segment to be built from.",
  "name" : "Required string",
  "conditions" : [ {
    "field" : "Required string",
    "and_or" : "string. Possible values: and | or | ",
    "value" : "Required string",
    "operator" : "Required string. Possible values: eq | ne | lt | gt | contains"
  } ]
}
```

### on-behalf-of

**Type:** string

</details>

## update_sender

**This endpoint allows you to update a sender identity.**

Updates to `from.email` require re-verification. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

Partial updates are allowed, but fields that are marked as "required" in the POST (create) endpoint must not be nil if that field is included in the PATCH request.

<details><summary>Parameters</summary>

### sender_id (required)

The ID of the sender identity that you want to update.

**Type:** integer

### $body

**Type:** object

```json
{
  "zip" : "The zipcode of the sender identity.",
  "country" : "The country of the sender identity.",
  "address" : "The physical address of the sender identity.",
  "reply_to" : {
    "name" : "This is the name appended to the reply to email field. IE - Your name or company name.",
    "email" : "This is the email that your recipient will reply to."
  },
  "city" : "The city of the sender identity.",
  "address_2" : "Additional sender identity address information.",
  "nickname" : "A nickname for the sender identity. Not used for sending.",
  "from" : {
    "name" : "This is the name appended to the from email field. IE - Your name or company name.",
    "email" : "This is where the email will appear to originate from for your recipient"
  },
  "state" : "The state of the sender identity."
}
```

### on-behalf-of

**Type:** string

</details>

## update_spam_check_settings

**This endpoint allows you to update your current spam checker mail settings.**

The spam checker filter notifies you when emails are detected that exceed a predefined spam threshold.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "max_score" : "The new max score, or spam threshold that you would like to set for the spam checker.",
  "enabled" : "Indicates if you want the spam check mail setting to be enabled or not.",
  "url" : "The Inbound Parse URL where you would like your spam reports to be sent to."
}
```

### on-behalf-of

**Type:** string

</details>

## update_spam_forward_settings

**This endpoint allows you to update your current Forward Spam mail settings.**

Enabling the forward spam setting allows you to specify an email address to which spam reports will be forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "email" : "The email address where you would like the spam reports to be forwarded.",
  "enabled" : "Indicates if the Forward Spam setting is enabled."
}
```

### on-behalf-of

**Type:** string

</details>

## update_teammate

This endpoint allows you to update a teammate’s permissions.

To turn a teammate into an admin, the request body should contain an `is_admin` set to `true`. Otherwise, set `is_admin` to `false` and pass in all the scopes that a teammate should have.

**Only the parent user or other admin teammates can update another teammate’s permissions.**

**Admin users can only update permissions.**

<details><summary>Parameters</summary>

### username (required)

The username of the teammate that you want to retrieve.

**Type:** string

### $body

**Type:** object

```json
{
  "is_admin" : "Set to True if this teammate should be promoted to an admin user. If True, scopes should be an empty array.",
  "scopes" : [ "string" ]
}
```

</details>

## update_template

**This endpoint allows you to edit a transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

<details><summary>Parameters</summary>

### template_id (required)

The id of the transactional template you want to retrieve.

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "The name of the transactional template."
}
```

### on-behalf-of

**Type:** string

</details>

## update_template_settings

**This endpoint allows you to update your current legacy email template settings.**

This setting refers to our original email templates. We currently support more fully featured [transactional templates](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html). 

The legacy email template setting wraps an HTML template around your email content. This can be useful for sending out marketing email and/or other HTML formatted messages.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrid’s [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "html_content" : "The new HTML content for your legacy email template.",
  "enabled" : "Indicates if you want to enable the legacy email template mail setting."
}
```

### on-behalf-of

**Type:** string

</details>

## update_tracking_settings_click

**This endpoint allows you to change your current click tracking setting. You can enable, or disable, click tracking using this endpoint.**

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "enabled" : "The setting you want to use for click tracking."
}
```

### on-behalf-of

**Type:** string

</details>

## update_tracking_settings_google_analytics

**This endpoint allows you to update your current setting for Google Analytics.**

For more information about using Google Analytics, please refer to [Google’s URL Builder](https://support.google.com/analytics/answer/1033867?hl=en) and their article on ["Best Practices for Campaign Building"](https://support.google.com/analytics/answer/1037445).

We default the settings to Google’s recommendations. For more information, see [Google Analytics Demystified](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/google_analytics_demystified_ga_statistics_vs_sg_statistics.html).

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "utm_term" : "Any paid keywords.",
  "utm_campaign" : "The name of the campaign.",
  "utm_medium" : "Name of the marketing medium (e.g. \"Email\").",
  "enabled" : "Indicates if Google Analytics is enabled.",
  "utm_content" : "Used to differentiate ads",
  "utm_source" : "Name of the referrer source."
}
```

### on-behalf-of

**Type:** string

</details>

## update_tracking_settings_open

**This endpoint allows you to update your current settings for open tracking.**

Open Tracking adds an invisible image at the end of the email which can track email opens. If the email recipient has images enabled on their email client, a request to SendGrid’s server for the invisible image is executed and an open event is logged. These events are logged in the Statistics portal, Email Activity interface, and are reported by the Event Webhook.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "enabled" : "The new status that you want to set for open tracking."
}
```

### on-behalf-of

**Type:** string

</details>

## update_tracking_settings_subscription

**This endpoint allows you to update your current settings for subscription tracking.**

Subscription tracking adds links to the bottom of your emails that allows your recipients to subscribe to, or unsubscribe from, your emails.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "html_content" : "The information and HTML for your unsubscribe link.",
  "landing" : "The HTML that will be displayed on the page that your customers will see after clicking unsubscribe, hosted on SendGrid’s server.",
  "replace" : "Your custom defined replacement tag for your templates. Use this tag to place your unsubscribe content anywhere in your emailtemplate.",
  "enabled" : "Indicates if subscription tracking is enabled.",
  "plain_content" : "The information in plain text for your unsubscribe link. You should have the “&lt;% %&gt;” tag in your content, otherwise the user will have no URL for unsubscribing.",
  "url" : "The URL where you would like your users sent to unsubscribe."
}
```

### on-behalf-of

**Type:** string

</details>

## update_unsubscribe_group

**This endpoint allows you to update or change a suppression group.**

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

<details><summary>Parameters</summary>

### Authorization (required)

**Type:** string

### group_id (required)

The ID of the suppression group you would like to retrieve.

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "The name of the suppression group. Each group created by a user must have a unique name.",
  "description" : "The description of the suppression group.",
  "id" : "The id of the suppression group.",
  "is_default" : "Indicates if the suppression group is set as the default group."
}
```

### on-behalf-of

**Type:** string

</details>

## update_user_email

**This endpoint allows you to update the email address currently on file for your account.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "email" : "The new email address that you would like to use for your account."
}
```

### on-behalf-of

**Type:** string

</details>

## update_user_password

**This endpoint allows you to update your password.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "old_password" : "The old password for your account.",
  "new_password" : "The new password you would like to use for your account."
}
```

### on-behalf-of

**Type:** string

</details>

## update_user_profile

**This endpoint allows you to update your current profile details.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

It should be noted that any one or more of the parameters can be updated via the PATCH /user/profile endpoint. The only requirement is that you include at least one when you PATCH.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "zip" : "The zip code for this user.",
  "country" : "Th country of this user profile.",
  "website" : "The website associated with this user.",
  "address" : "The street address for this user profile.",
  "address2" : "An optional second line for the street address of this user profile.",
  "city" : "The city for the user profile.",
  "phone" : "The phone number for the user.",
  "last_name" : "The last name of the user.",
  "company" : "That company that this user profile is associated with.",
  "state" : "The state for this user.",
  "first_name" : "The first name of the user."
}
```

### on-behalf-of

**Type:** string

</details>

## update_user_scheduled_send

**This endpoint allows you to update the status of a scheduled send for the given `batch_id`.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header. Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

<details><summary>Parameters</summary>

### batch_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "status" : "The status you would like the scheduled send to have."
}
```

</details>

## update_user_settings_enforced_tls

**This endpoint allows you to update your current Enforced TLS settings.**

The Enforced TLS settings specify whether or not the recipient is required to support TLS or have a valid certificate. See the [SMTP Ports User Guide](https://sendgrid.com/docs/Classroom/Basics/Email_Infrastructure/smtp_ports.html) for more information on opportunistic TLS.

**Note:** If either setting is enabled and the recipient does not support TLS or have a valid certificate, we drop the message and send a block event with “TLS required but not supported” as the description.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "require_tls" : "Indicates if you want to require your recipients to support TLS.",
  "require_valid_cert" : "Indicates if you want to require your recipients to have a valid certificate."
}
```

### on-behalf-of

**Type:** string

</details>

## update_username

**This endpoint allows you to update the username for your account.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "username" : "The new username you would like to use for your account."
}
```

### on-behalf-of

**Type:** string

</details>

## update_version_of_template

**This endpoint allows you to edit a version of one of your transactional templates.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string | The ID of the template version |

<details><summary>Parameters</summary>

### template_id (required)

**Type:** string

### version_id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "html_content" : "The HTML content of the template version.",
  "subject" : "The subject of the template version.",
  "name" : "The name of the template version.",
  "active" : "Indicates if the template version is active.",
  "plain_content" : "The text/plain content of the template version."
}
```

### on-behalf-of

**Type:** string

</details>

## update_webhooks_events_settings

**This endpoint allows you to update your current event webhook settings.**

If an event type is marked as `true`, then the event webhook will include information about that event.

SendGrid’s Event Webhook will notify a URL of your choice via HTTP POST with information about events that occur as SendGrid processes your email.

Common uses of this data are to remove unsubscribes, react to spam reports, determine unengaged recipients, identify bounced email addresses, or create advanced analytics of your email program.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "deferred" : "Recipient's email server temporarily rejected message.",
  "group_unsubscribe" : "Recipient unsubscribe from specific group, by either direct link or updating preferences. You need to enable Subscription Tracking for getting this type of event.",
  "spam_report" : "Recipient marked a message as spam.",
  "bounce" : "Receiving server could not or would not accept message.",
  "dropped" : "You may see the following drop reasons: Invalid SMTPAPI header, Spam Content (if spam checker app enabled), Unsubscribed Address, Bounced Address, Spam Reporting Address, Invalid, Recipient List over Package Quota",
  "delivered" : "Message has been successfully delivered to the receiving server.",
  "click" : "Recipient clicked on a link within the message. You need to enable Click Tracking for getting this type of event.",
  "enabled" : "Indicates if the event webhook is enabled.",
  "url" : "The URL that you want the event webhook to POST to.",
  "processed" : "Message has been received and is ready to be delivered.",
  "unsubscribe" : "Recipient clicked on message's subscription management link. You need to enable Subscription Tracking for getting this type of event.",
  "group_resubscribe" : "Recipient resubscribes to specific group by updating preferences. You need to enable Subscription Tracking for getting this type of event.",
  "open" : "Recipient has opened the HTML message. You need to enable Open Tracking for getting this type of event."
}
```

### on-behalf-of

**Type:** string

</details>

## update_webhooks_parse_setting

**This endpoint allows you to update a specific inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

<details><summary>Parameters</summary>

### hostname (required)

The hostname associated with the inbound parse setting that you would like to retrieve.

**Type:** string

### $body

**Type:** object

```json
{
  "hostname" : "A specific and unique domain or subdomain that you have created to use exclusively to parse your incoming email. For example, parse.yourdomain.com.",
  "spam_check" : "Indicates if you would like SendGrid to check the content parsed from your emails for spam before POSTing them to your domain.",
  "send_raw" : "Indicates if you would like SendGrid to post the original MIME-type content of your parsed email. When this parameter is set to \"false\", SendGrid will send a JSON payload of the content of your email.",
  "url" : "The public URL where you would like SendGrid to POST the data parsed from your email. Any emails sent with the given hostname provided (whose MX records have been updated to point to SendGrid) will be parsed and POSTed to this URL."
}
```

### on-behalf-of

**Type:** string

</details>

## validate_batch

**This endpoint allows you to validate a batch ID.**

If you set the SMTPAPI header `batch_id`, it allows you to then associate multiple scheduled mail/send requests together with the same ID. Then at anytime up to 10 minutes before the schedule date, you can cancel all of the mail/send requests that have this batch ID by calling the Cancel Scheduled Send endpoint. 

More Information:

* [Scheduling Parameters &gt; Batch ID](https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html)

<details><summary>Parameters</summary>

### batch_id (required)

**Type:** string

</details>

## validate_branded_link

**This endpoint allows you to validate a link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

<details><summary>Parameters</summary>

### id (required)

The id of the link whitelabel that you want to validate.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### on-behalf-of

**Type:** string

</details>

## validate_reverse_dns_record

**This endpoint allows you to validate an IP whitelabel.**

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### on-behalf-of

**Type:** string

</details>

## warmup_ip

**This endpoint allows you to enter an IP address into warmup mode.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ip" : "The IP address that you want to begin warming up."
}
```

### on-behalf-of

**Type:** string

</details>

