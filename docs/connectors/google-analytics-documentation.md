---
id: google-analytics-documentation
title: Google Analytics (version v2.*.*)
sidebar_label: Google Analytics
---

## add_user_to_account

Adds a new user to the given account.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

</details>

## create_account_ticket

Creates an account ticket.

<details><summary>Parameters</summary>

#### $body

JSON template for an Analytics account ticket. The account ticket consists of the ticket ID and the basic information for the account, property and profile.

**Type:** object

</details>

## create_custom_dimension

Create a new custom dimension.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Custom Dimension.

**Type:** object

</details>

## create_custom_metric

Create a new custom metric.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Custom Metric.

**Type:** object

</details>

## create_experiment

Create a new experiment.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics experiment resource.

**Type:** object

</details>

## create_filter

Create a new filter.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### $body

JSON template for an Analytics account filter.

**Type:** object

</details>

## create_goal

Create a new goal.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics goal resource.

**Type:** object

</details>

## create_profile

Create a new view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics view (profile).

**Type:** object

</details>

## create_profile_filter_link

Create a new profile filter link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics profile filter link.

**Type:** object

</details>

## create_profile_user_link

Adds a new user to the given view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

</details>

## create_remarketing_audience

Creates a new remarketing audience.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics remarketing audience.

**Type:** object

</details>

## create_unsampled_report

Create a new unsampled report.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics unsampled report resource.

**Type:** object

</details>

## create_web_property

Create a new property if the account has fewer than 20 properties. Web properties are visible in the Google Analytics interface only if they have at least one profile.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### $body

JSON template for an Analytics web property.

**Type:** object

</details>

## create_web_property_adwords_link

Creates a webProperty-Google Ads link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Entity Google Ads Link.

**Type:** object

</details>

## create_web_property_user_link

Adds a new user to the given web property.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

</details>

## delete_data_for_upload

Delete data associated with a previous upload.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDataSourceId (required)

Custom data source ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

Request template for the delete upload data request.

**Type:** object

</details>

## delete_experiment

Delete an experiment.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### experimentId (required)

ID of the experiment.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_filter

Delete a filter.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### filterId (required)

Filter ID.

**Type:** string

</details>

## delete_profile

Deletes a view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_profile_filter_link

Delete a profile filter link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_profile_user_link

Removes a user from the given view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_remarketing_audience

Delete a remarketing audience.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_unsampled_report

Deletes an unsampled report.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### unsampledReportId (required)

ID of the unsampled report.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_user_from_account

Removes a user from the given account.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

</details>

## delete_web_property_adwords_link

Deletes a web property-Google Ads link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## delete_web_property_user_link

Removes a user from the given web property.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_custom_dimension

Get a custom dimension to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDimensionId (required)

The ID of the custom dimension.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_custom_metric

Get a custom metric to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customMetricId (required)

The ID of the custom metric.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_data_for_view

Returns Analytics data for a view (profile).

<details><summary>Parameters</summary>

#### end-date (required)

End date for fetching Analytics data. Request can should specify an end date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is yesterday.

**Type:** string

#### ids (required)

Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**Type:** string

#### metrics (required)

A comma-separated list of Analytics metrics. E.g., 'ga:sessions,ga:pageviews'. At least one metric must be specified.

**Type:** string

#### start-date (required)

Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**Type:** string

#### dimensions

A comma-separated list of Analytics dimensions. E.g., 'ga:browser,ga:city'.

**Type:** string

#### filters

A comma-separated list of dimension or metric filters to be applied to Analytics data.

**Type:** string

#### include-empty-rows

The response will include empty rows if this parameter is set to true, the default is true

**Type:** boolean

#### output

The selected format for the response. Default format is JSON.

**Type:** string

**Potential values:** dataTable, json

#### samplingLevel

The desired sampling level.

**Type:** string

**Potential values:** DEFAULT, FASTER, HIGHER_PRECISION

#### segment

An Analytics segment to be applied to data.

**Type:** string

#### sort

A comma-separated list of dimensions or metrics that determine the sort order for Analytics data.

**Type:** string

</details>

## get_experiment

Returns an experiment to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### experimentId (required)

ID of the experiment.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_filter

Returns a filters to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### filterId (required)

Filter ID.

**Type:** string

</details>

## get_goal

Gets a goal to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### goalId (required)

Goal ID to retrieve the goal for.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_multichannel_funnels_data_for_view

Returns Analytics Multi-Channel Funnels data for a view (profile).

<details><summary>Parameters</summary>

#### end-date (required)

End date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**Type:** string

#### ids (required)

Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**Type:** string

#### metrics (required)

A comma-separated list of Multi-Channel Funnels metrics. E.g., 'mcf:totalConversions,mcf:totalConversionValue'. At least one metric must be specified.

**Type:** string

#### start-date (required)

Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**Type:** string

#### dimensions

A comma-separated list of Multi-Channel Funnels dimensions. E.g., 'mcf:source,mcf:medium'.

**Type:** string

#### filters

A comma-separated list of dimension or metric filters to be applied to the Analytics data.

**Type:** string

#### samplingLevel

The desired sampling level.

**Type:** string

**Potential values:** DEFAULT, FASTER, HIGHER_PRECISION

#### sort

A comma-separated list of dimensions or metrics that determine the sort order for the Analytics data.

**Type:** string

</details>

## get_profile

Gets a view (profile) to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_profile_filter_link

Returns a single profile filter link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_realtime_data_for_view

Returns real time data for a view (profile).

<details><summary>Parameters</summary>

#### ids (required)

Unique table ID for retrieving real time data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**Type:** string

#### metrics (required)

A comma-separated list of real time metrics. E.g., 'rt:activeUsers'. At least one metric must be specified.

**Type:** string

#### dimensions

A comma-separated list of real time dimensions. E.g., 'rt:medium,rt:city'.

**Type:** string

#### filters

A comma-separated list of dimension or metric filters to be applied to real time data.

**Type:** string

#### sort

A comma-separated list of dimensions or metrics that determine the sort order for real time data.

**Type:** string

</details>

## get_remarketing_audience

Gets a remarketing audience to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_unsampled_report

Returns a single unsampled report.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### unsampledReportId (required)

ID of the unsampled report.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_upload

List uploads to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDataSourceId (required)

Custom data source ID.

**Type:** string

#### uploadId (required)

Upload ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_web_property

Gets a web property to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## get_web_property_adwords_link

Returns a web property-Google Ads link to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## hash_client_id

Hashes the given Client ID.

<details><summary>Parameters</summary>

#### $body

JSON template for a hash Client Id request resource.

**Type:** object

</details>

## list_account_summaries

Lists account summaries (lightweight tree comprised of accounts/properties/profiles) to which the user has access.

*This operation has no parameters*

## list_account_user_links

Lists account-user links for a given account.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

</details>

## list_accounts

Lists all accounts to which the user has access.

*This operation has no parameters*

## list_columns_for_report_type

Lists all columns for a report type

<details><summary>Parameters</summary>

#### reportType (required)

Report type. Allowed Values: 'ga'. Where 'ga' corresponds to the Core Reporting API

**Type:** string

</details>

## list_custom_data_sources

List custom data sources to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_custom_dimensions

Lists custom dimensions to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_custom_metrics

Lists custom metrics to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_experiments

Lists experiments to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_filters

Lists all filters for an account

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

</details>

## list_goals

Lists goals to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_profile_filter_links

Lists all profile filter links for a profile.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_profile_user_links

Lists profile-user links for a given view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_profiles

Lists views (profiles) to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_remarketing_audiences

Lists remarketing audiences to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### type

**Type:** string

</details>

## list_segments

Lists segments to which the user has access.

*This operation has no parameters*

## list_unsampled_reports

Lists unsampled reports to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_uploads

List uploads to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDataSourceId (required)

Custom data source ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_web_properties

Lists web properties to which the user has access.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

</details>

## list_web_property_adwords_links

Lists webProperty-Google Ads links for a given web property.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## list_web_property_user_links

Lists webProperty-user links for a given web property.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

## patch_custom_dimension

Updates an existing custom dimension. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDimensionId (required)

The ID of the custom dimension.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Custom Dimension.

**Type:** object

#### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

**Type:** boolean

</details>

## patch_custom_metric

Updates an existing custom metric. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customMetricId (required)

The ID of the custom metric.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Custom Metric.

**Type:** object

#### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

**Type:** boolean

</details>

## patch_experiment

Update an existing experiment. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### experimentId (required)

ID of the experiment.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics experiment resource.

**Type:** object

</details>

## patch_filter

Updates an existing filter. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### filterId (required)

Filter ID.

**Type:** string

#### $body

JSON template for an Analytics account filter.

**Type:** object

</details>

## patch_goal

Updates an existing goal. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### goalId (required)

Goal ID to retrieve the goal for.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics goal resource.

**Type:** object

</details>

## patch_profile

Updates an existing view (profile). This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics view (profile).

**Type:** object

</details>

## patch_profile_filter_link

Update an existing profile filter link. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics profile filter link.

**Type:** object

</details>

## patch_remarketing_audience

Updates an existing remarketing audience. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics remarketing audience.

**Type:** object

</details>

## patch_web_property

Updates an existing web property. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics web property.

**Type:** object

</details>

## patch_web_property_adwords_link

Updates an existing webProperty-Google Ads link. This method supports patch semantics.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Entity Google Ads Link.

**Type:** object

</details>

## provision_account

Provision account.

<details><summary>Parameters</summary>

#### $body

JSON template for an Analytics account tree requests. The account tree request is used in the provisioning api to create an account, property, and view (profile). It contains the basic information required to make these fields.

**Type:** object

</details>

## update_custom_dimension

Updates an existing custom dimension.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDimensionId (required)

The ID of the custom dimension.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Custom Dimension.

**Type:** object

#### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

**Type:** boolean

</details>

## update_custom_metric

Updates an existing custom metric.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customMetricId (required)

The ID of the custom metric.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Custom Metric.

**Type:** object

#### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

**Type:** boolean

</details>

## update_experiment

Update an existing experiment.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### experimentId (required)

ID of the experiment.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics experiment resource.

**Type:** object

</details>

## update_filter

Updates an existing filter.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### filterId (required)

Filter ID.

**Type:** string

#### $body

JSON template for an Analytics account filter.

**Type:** object

</details>

## update_goal

Updates an existing goal.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### goalId (required)

Goal ID to retrieve the goal for.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics goal resource.

**Type:** object

</details>

## update_or_create_user_deletion_request

Insert or update a user deletion requests.

<details><summary>Parameters</summary>

#### $body

JSON template for a user deletion request resource.

**Type:** object

</details>

## update_permissions_for_user

Updates permissions for an existing user on the given account.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

</details>

## update_profile

Updates an existing view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics view (profile).

**Type:** object

</details>

## update_profile_filter_link

Update an existing profile filter link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics profile filter link.

**Type:** object

</details>

## update_profile_user_links

Updates permissions for an existing user on the given view (profile).

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

</details>

## update_remarketing_audience

Updates an existing remarketing audience.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics remarketing audience.

**Type:** object

</details>

## update_web_property

Updates an existing web property.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics web property.

**Type:** object

</details>

## update_web_property_adwords_link

Updates an existing webProperty-Google Ads link.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for Analytics Entity Google Ads Link.

**Type:** object

</details>

## update_web_property_user_link

Updates permissions for an existing user on the given web property.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### linkId (required)

Link ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

#### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

</details>

## upload_custom_data_source

Upload data for a custom data source.

<details><summary>Parameters</summary>

#### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

#### customDataSourceId (required)

Custom data source ID.

**Type:** string

#### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

</details>

