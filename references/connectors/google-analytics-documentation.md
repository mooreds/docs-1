---
id: google-analytics-documentation
title: Google Analytics (version v2.*.*)
sidebar_label: Google Analytics
layout: docs.mustache
---

## add_user_to_account

Adds a new user to the given account.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

```json
{
  "userRef" : {
    "kind" : "string",
    "id" : "User ID.",
    "email" : "Email ID of this user."
  },
  "kind" : "Resource type for entity user link.",
  "permissions" : {
    "effective" : [ "string" ],
    "local" : [ "string" ]
  },
  "id" : "Entity user link ID",
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    },
    "accountRef" : {
      "kind" : "Analytics account reference.",
      "name" : "Account name.",
      "href" : "Link for this account.",
      "id" : "Account ID."
    },
    "profileRef" : {
      "accountId" : "Account ID to which this view (profile) belongs.",
      "kind" : "Analytics view (profile) reference.",
      "name" : "Name of this view (profile).",
      "href" : "Link for this view (profile).",
      "id" : "View (Profile) ID.",
      "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
      "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
    }
  },
  "selfLink" : "Self link for this resource."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_account_ticket

Creates an account ticket.

<details><summary>Parameters</summary>

### $body

JSON template for an Analytics account ticket. The account ticket consists of the ticket ID and the basic information for the account, property and profile.

**Type:** object

```json
{
  "redirectUri" : "Redirect URI where the user will be sent after accepting Terms of Service. Must be configured in APIs console as a callback URL.",
  "webproperty" : {
    "profileCount" : "View (Profile) count for this web property.",
    "dataRetentionResetOnNewActivity" : "Set to true to reset the retention period of the user identifier with each new event from that user (thus setting the expiration date to current time plus retention period).\nSet to false to delete data associated with the user identifer automatically after the rentention period.\nThis property cannot be set on insert.",
    "parentLink" : {
      "href" : "Link to the account for this web property.",
      "type" : "Type of the parent link. Its value is \"analytics#account\"."
    },
    "dataRetentionTtl" : "The length of time for which user and event data is retained.\nThis property cannot be set on insert.",
    "defaultProfileId" : "Default view (profile) ID.",
    "level" : "Level for this web property. Possible values are STANDARD or PREMIUM.",
    "childLink" : {
      "href" : "Link to the list of views (profiles) for this web property.",
      "type" : "Type of the parent link. Its value is \"analytics#profiles\"."
    },
    "created" : "Time this web property was created.",
    "industryVertical" : "The industry vertical/category selected for this web property.",
    "kind" : "Resource type for Analytics WebProperty.",
    "selfLink" : "Link for this web property.",
    "accountId" : "Account ID to which this web property belongs.",
    "starred" : "Indicates whether this web property is starred or not.",
    "websiteUrl" : "Website url for this web property.",
    "permissions" : {
      "effective" : [ "string" ]
    },
    "name" : "Name of this web property.",
    "id" : "Web property ID of the form UA-XXXXX-YY.",
    "updated" : "Time this web property was last modified.",
    "internalWebPropertyId" : "Internal ID for this web property."
  },
  "kind" : "Resource type for account ticket.",
  "profile" : {
    "eCommerceTracking" : "Indicates whether ecommerce tracking is enabled for this view (profile).",
    "excludeQueryParameters" : "The query parameters that are excluded from this view (profile).",
    "siteSearchCategoryParameters" : "Site search category parameters for this view (profile).",
    "defaultPage" : "Default page for this view (profile).",
    "botFilteringEnabled" : "Indicates whether bot filtering is enabled for this view (profile).",
    "timezone" : "Time zone for which this view (profile) has been configured. Time zones are identified by strings from the TZ database.",
    "type" : "View (Profile) type. Supported types: WEB or APP.",
    "starred" : "Indicates whether this view (profile) is starred or not.",
    "websiteUrl" : "Website URL for this view (profile).",
    "permissions" : {
      "effective" : [ "string" ]
    },
    "siteSearchQueryParameters" : "The site search query parameters for this view (profile).",
    "currency" : "The currency type associated with this view (profile), defaults to USD. The supported values are:\nUSD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD, HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL, ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD, SAR, SGD, VEF, LVL",
    "id" : "View (Profile) ID.",
    "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
    "parentLink" : {
      "href" : "Link to the web property to which this view (profile) belongs.",
      "type" : "Value is \"analytics#webproperty\"."
    },
    "stripSiteSearchCategoryParameters" : "Whether or not Analytics will strip search category parameters from the URLs in your reports.",
    "childLink" : {
      "href" : "Link to the list of goals for this view (profile).",
      "type" : "Value is \"analytics#goals\"."
    },
    "created" : "Time this view (profile) was created.",
    "kind" : "Resource type for Analytics view (profile).",
    "enhancedECommerceTracking" : "Indicates whether enhanced ecommerce tracking is enabled for this view (profile). This property can only be enabled if ecommerce tracking is enabled.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs.",
    "selfLink" : "Link for this view (profile).",
    "accountId" : "Account ID to which this view (profile) belongs.",
    "stripSiteSearchQueryParameters" : "Whether or not Analytics will strip search query parameters from the URLs in your reports.",
    "name" : "Name of this view (profile).",
    "updated" : "Time this view (profile) was last modified."
  },
  "id" : "Account ticket ID used to access the account ticket.",
  "account" : {
    "starred" : "Indicates whether this account is starred or not.",
    "childLink" : {
      "href" : "Link to the list of web properties for this account.",
      "type" : "Type of the child link. Its value is \"analytics#webproperties\"."
    },
    "created" : "Time the account was created.",
    "kind" : "Resource type for Analytics account.",
    "permissions" : {
      "effective" : [ "string" ]
    },
    "name" : "Account name.",
    "id" : "Account ID.",
    "updated" : "Time the account was last modified.",
    "selfLink" : "Link for this account."
  }
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_custom_dimension

Create a new custom dimension.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Custom Dimension.

**Type:** object

```json
{
  "accountId" : "Account ID.",
  "parentLink" : {
    "href" : "Link to the property to which the custom dimension belongs.",
    "type" : "Type of the parent link. Set to \"analytics#webproperty\"."
  },
  "created" : "Time the custom dimension was created.",
  "kind" : "Kind value for a custom dimension. Set to \"analytics#customDimension\". It is a read-only field.",
  "scope" : "Scope of the custom dimension: HIT, SESSION, USER or PRODUCT.",
  "name" : "Name of the custom dimension.",
  "active" : "Boolean indicating whether the custom dimension is active.",
  "index" : "Index of the custom dimension.",
  "id" : "Custom dimension ID.",
  "updated" : "Time the custom dimension was last modified.",
  "webPropertyId" : "Property ID.",
  "selfLink" : "Link for the custom dimension"
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_custom_metric

Create a new custom metric.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Custom Metric.

**Type:** object

```json
{
  "parentLink" : {
    "href" : "Link to the property to which the custom metric belongs.",
    "type" : "Type of the parent link. Set to \"analytics#webproperty\"."
  },
  "created" : "Time the custom metric was created.",
  "kind" : "Kind value for a custom metric. Set to \"analytics#customMetric\". It is a read-only field.",
  "active" : "Boolean indicating whether the custom metric is active.",
  "index" : "Index of the custom metric.",
  "type" : "Data type of custom metric.",
  "webPropertyId" : "Property ID.",
  "selfLink" : "Link for the custom metric",
  "accountId" : "Account ID.",
  "min_value" : "Min value of custom metric.",
  "scope" : "Scope of the custom metric: HIT or PRODUCT.",
  "name" : "Name of the custom metric.",
  "id" : "Custom metric ID.",
  "updated" : "Time the custom metric was last modified.",
  "max_value" : "Max value of custom metric."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_experiment

Create a new experiment.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics experiment resource.

**Type:** object

```json
{
  "snippet" : "The snippet of code to include on the control page(s). This field is read-only.",
  "winnerFound" : "Boolean specifying whether a winner has been found for this experiment. This field is read-only.",
  "description" : "Notes about this experiment.",
  "minimumExperimentLengthInDays" : "An integer number in [3, 90]. Specifies the minimum length of the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED.",
  "variations" : [ {
    "won" : "True if the experiment has ended and this variation performed (statistically) significantly better than the original. This field is read-only.",
    "name" : "The name of the variation. This field is required when creating an experiment. This field may not be changed for an experiment whose status is ENDED.",
    "weight" : "Weight that this variation should receive. Only present if the experiment is running. This field is read-only.",
    "url" : "The URL of the variation. This field may not be changed for an experiment whose status is RUNNING or ENDED.",
    "status" : "Status of the variation. Possible values: \"ACTIVE\", \"INACTIVE\". INACTIVE variations are not served. This field may not be changed for an experiment whose status is ENDED."
  } ],
  "startTime" : "The starting time of the experiment (the time the status changed from READY_TO_RUN to RUNNING). This field is present only if the experiment has started. This field is read-only.",
  "id" : "Experiment ID. Required for patch and update. Disallowed for create.",
  "editableInGaUi" : "If true, the end user will be able to edit the experiment via the Google Analytics user interface.",
  "internalWebPropertyId" : "Internal ID for the web property to which this experiment belongs. This field is read-only.",
  "winnerConfidenceLevel" : "A floating-point number in (0, 1). Specifies the necessary confidence level to choose a winner. This field may not be changed for an experiments whose status is ENDED.",
  "parentLink" : {
    "href" : "Link to the view (profile) to which this experiment belongs. This field is read-only.",
    "type" : "Value is \"analytics#profile\". This field is read-only."
  },
  "created" : "Time the experiment was created. This field is read-only.",
  "kind" : "Resource type for an Analytics experiment. This field is read-only.",
  "webPropertyId" : "Web property ID to which this experiment belongs. The web property ID is of the form UA-XXXXX-YY. This field is read-only.",
  "reasonExperimentEnded" : "Why the experiment ended. Possible values: \"STOPPED_BY_USER\", \"WINNER_FOUND\", \"EXPERIMENT_EXPIRED\", \"ENDED_WITH_NO_WINNER\", \"GOAL_OBJECTIVE_CHANGED\". \"ENDED_WITH_NO_WINNER\" means that the experiment didn't expire but no winner was projected to be found. If the experiment status is changed via the API to ENDED this field is set to STOPPED_BY_USER. This field is read-only.",
  "selfLink" : "Link for this experiment. This field is read-only.",
  "trafficCoverage" : "A floating-point number in (0, 1]. Specifies the fraction of the traffic that participates in the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED.",
  "accountId" : "Account ID to which this experiment belongs. This field is read-only.",
  "equalWeighting" : "Boolean specifying whether to distribute traffic evenly across all variations. If the value is False, content experiments follows the default behavior of adjusting traffic dynamically based on variation performance. Optional -- defaults to False. This field may not be changed for an experiment whose status is ENDED.",
  "rewriteVariationUrlsAsOriginal" : "Boolean specifying whether variations URLS are rewritten to match those of the original. This field may not be changed for an experiments whose status is ENDED.",
  "profileId" : "View (Profile) ID to which this experiment belongs. This field is read-only.",
  "optimizationType" : "Whether the objectiveMetric should be minimized or maximized. Possible values: \"MAXIMUM\", \"MINIMUM\". Optional--defaults to \"MAXIMUM\". Cannot be specified without objectiveMetric. Cannot be modified when status is \"RUNNING\" or \"ENDED\".",
  "name" : "Experiment name. This field may not be changed for an experiment whose status is ENDED. This field is required when creating an experiment.",
  "endTime" : "The ending time of the experiment (the time the status changed from RUNNING to ENDED). This field is present only if the experiment has ended. This field is read-only.",
  "servingFramework" : "The framework used to serve the experiment variations and evaluate the results. One of:  \n- REDIRECT: Google Analytics redirects traffic to different variation pages, reports the chosen variation and evaluates the results.\n- API: Google Analytics chooses and reports the variation to serve and evaluates the results; the caller is responsible for serving the selected variation.\n- EXTERNAL: The variations will be served externally and the chosen variation reported to Google Analytics. The caller is responsible for serving the selected variation and evaluating the results.",
  "updated" : "Time the experiment was last modified. This field is read-only.",
  "objectiveMetric" : "The metric that the experiment is optimizing. Valid values: \"ga:goal(n)Completions\", \"ga:adsenseAdsClicks\", \"ga:adsenseAdsViewed\", \"ga:adsenseRevenue\", \"ga:bounces\", \"ga:pageviews\", \"ga:sessionDuration\", \"ga:transactions\", \"ga:transactionRevenue\". This field is required if status is \"RUNNING\" and servingFramework is one of \"REDIRECT\" or \"API\".",
  "status" : "Experiment status. Possible values: \"DRAFT\", \"READY_TO_RUN\", \"RUNNING\", \"ENDED\". Experiments can be created in the \"DRAFT\", \"READY_TO_RUN\" or \"RUNNING\" state. This field is required when creating an experiment."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_filter

Create a new filter.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### $body

JSON template for an Analytics account filter.

**Type:** object

```json
{
  "parentLink" : {
    "href" : "Link to the account to which this filter belongs.",
    "type" : "Value is \"analytics#account\"."
  },
  "searchAndReplaceDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "searchString" : "Term to search.",
    "field" : "Field to use in the filter.",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "replaceString" : "Term to replace the search term with."
  },
  "created" : "Time this filter was created.",
  "excludeDetails" : {
    "expressionValue" : "Filter expression value",
    "fieldIndex" : "The Index of the custom dimension. Set only if the field is a is CUSTOM_DIMENSION.",
    "field" : "Field to filter. Possible values:  \n- Content and Traffic  \n- PAGE_REQUEST_URI, \n- PAGE_HOSTNAME, \n- PAGE_TITLE, \n- REFERRAL, \n- COST_DATA_URI (Campaign target URL), \n- HIT_TYPE, \n- INTERNAL_SEARCH_TERM, \n- INTERNAL_SEARCH_TYPE, \n- SOURCE_PROPERTY_TRACKING_ID,   \n- Campaign or AdGroup  \n- CAMPAIGN_SOURCE, \n- CAMPAIGN_MEDIUM, \n- CAMPAIGN_NAME, \n- CAMPAIGN_AD_GROUP, \n- CAMPAIGN_TERM, \n- CAMPAIGN_CONTENT, \n- CAMPAIGN_CODE, \n- CAMPAIGN_REFERRAL_PATH,   \n- E-Commerce  \n- TRANSACTION_COUNTRY, \n- TRANSACTION_REGION, \n- TRANSACTION_CITY, \n- TRANSACTION_AFFILIATION (Store or order location), \n- ITEM_NAME, \n- ITEM_CODE, \n- ITEM_VARIATION, \n- TRANSACTION_ID, \n- TRANSACTION_CURRENCY_CODE, \n- PRODUCT_ACTION_TYPE,   \n- Audience/Users  \n- BROWSER, \n- BROWSER_VERSION, \n- BROWSER_SIZE, \n- PLATFORM, \n- PLATFORM_VERSION, \n- LANGUAGE, \n- SCREEN_RESOLUTION, \n- SCREEN_COLORS, \n- JAVA_ENABLED (Boolean Field), \n- FLASH_VERSION, \n- GEO_SPEED (Connection speed), \n- VISITOR_TYPE, \n- GEO_ORGANIZATION (ISP organization), \n- GEO_DOMAIN, \n- GEO_IP_ADDRESS, \n- GEO_IP_VERSION,   \n- Location  \n- GEO_COUNTRY, \n- GEO_REGION, \n- GEO_CITY,   \n- Event  \n- EVENT_CATEGORY, \n- EVENT_ACTION, \n- EVENT_LABEL,   \n- Other  \n- CUSTOM_FIELD_1, \n- CUSTOM_FIELD_2, \n- USER_DEFINED_VALUE,   \n- Application  \n- APP_ID, \n- APP_INSTALLER_ID, \n- APP_NAME, \n- APP_VERSION, \n- SCREEN, \n- IS_APP (Boolean Field), \n- IS_FATAL_EXCEPTION (Boolean Field), \n- EXCEPTION_DESCRIPTION,   \n- Mobile device  \n- IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile), \n- IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet), \n- DEVICE_CATEGORY, \n- MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field), \n- MOBILE_HAS_NFC_SUPPORT (Boolean Field), \n- MOBILE_HAS_CELLULAR_RADIO (Boolean Field), \n- MOBILE_HAS_WIFI_SUPPORT (Boolean Field), \n- MOBILE_BRAND_NAME, \n- MOBILE_MODEL_NAME, \n- MOBILE_MARKETING_NAME, \n- MOBILE_POINTING_METHOD,   \n- Social  \n- SOCIAL_NETWORK, \n- SOCIAL_ACTION, \n- SOCIAL_ACTION_TARGET,   \n- Custom dimension  \n- CUSTOM_DIMENSION (See accompanying field index),",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "kind" : "Kind value for filter expression",
    "matchType" : "Match type for this filter. Possible values are BEGINS_WITH, EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS, PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other filters must use MATCHES."
  },
  "kind" : "Resource type for Analytics filter.",
  "lowercaseDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "field" : "Field to use in the filter."
  },
  "type" : "Type of this filter. Possible values are INCLUDE, EXCLUDE, LOWERCASE, UPPERCASE, SEARCH_AND_REPLACE and ADVANCED.",
  "advancedDetails" : {
    "fieldA" : "Field A.",
    "fieldAIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "caseSensitive" : "Indicates if the filter expressions are case sensitive.",
    "overrideOutputField" : "Indicates if the existing value of the output field, if any, should be overridden by the output expression.",
    "extractA" : "Expression to extract from field A.",
    "extractB" : "Expression to extract from field B.",
    "fieldBRequired" : "Indicates if field B is required to match.",
    "fieldB" : "Field B.",
    "outputToField" : "Output field.",
    "fieldBIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "fieldARequired" : "Indicates if field A is required to match.",
    "outputToFieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "outputConstructor" : "Expression used to construct the output value."
  },
  "selfLink" : "Link for this filter.",
  "accountId" : "Account ID to which this filter belongs.",
  "name" : "Name of this filter.",
  "uppercaseDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "field" : "Field to use in the filter."
  },
  "id" : "Filter ID.",
  "includeDetails" : {
    "expressionValue" : "Filter expression value",
    "fieldIndex" : "The Index of the custom dimension. Set only if the field is a is CUSTOM_DIMENSION.",
    "field" : "Field to filter. Possible values:  \n- Content and Traffic  \n- PAGE_REQUEST_URI, \n- PAGE_HOSTNAME, \n- PAGE_TITLE, \n- REFERRAL, \n- COST_DATA_URI (Campaign target URL), \n- HIT_TYPE, \n- INTERNAL_SEARCH_TERM, \n- INTERNAL_SEARCH_TYPE, \n- SOURCE_PROPERTY_TRACKING_ID,   \n- Campaign or AdGroup  \n- CAMPAIGN_SOURCE, \n- CAMPAIGN_MEDIUM, \n- CAMPAIGN_NAME, \n- CAMPAIGN_AD_GROUP, \n- CAMPAIGN_TERM, \n- CAMPAIGN_CONTENT, \n- CAMPAIGN_CODE, \n- CAMPAIGN_REFERRAL_PATH,   \n- E-Commerce  \n- TRANSACTION_COUNTRY, \n- TRANSACTION_REGION, \n- TRANSACTION_CITY, \n- TRANSACTION_AFFILIATION (Store or order location), \n- ITEM_NAME, \n- ITEM_CODE, \n- ITEM_VARIATION, \n- TRANSACTION_ID, \n- TRANSACTION_CURRENCY_CODE, \n- PRODUCT_ACTION_TYPE,   \n- Audience/Users  \n- BROWSER, \n- BROWSER_VERSION, \n- BROWSER_SIZE, \n- PLATFORM, \n- PLATFORM_VERSION, \n- LANGUAGE, \n- SCREEN_RESOLUTION, \n- SCREEN_COLORS, \n- JAVA_ENABLED (Boolean Field), \n- FLASH_VERSION, \n- GEO_SPEED (Connection speed), \n- VISITOR_TYPE, \n- GEO_ORGANIZATION (ISP organization), \n- GEO_DOMAIN, \n- GEO_IP_ADDRESS, \n- GEO_IP_VERSION,   \n- Location  \n- GEO_COUNTRY, \n- GEO_REGION, \n- GEO_CITY,   \n- Event  \n- EVENT_CATEGORY, \n- EVENT_ACTION, \n- EVENT_LABEL,   \n- Other  \n- CUSTOM_FIELD_1, \n- CUSTOM_FIELD_2, \n- USER_DEFINED_VALUE,   \n- Application  \n- APP_ID, \n- APP_INSTALLER_ID, \n- APP_NAME, \n- APP_VERSION, \n- SCREEN, \n- IS_APP (Boolean Field), \n- IS_FATAL_EXCEPTION (Boolean Field), \n- EXCEPTION_DESCRIPTION,   \n- Mobile device  \n- IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile), \n- IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet), \n- DEVICE_CATEGORY, \n- MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field), \n- MOBILE_HAS_NFC_SUPPORT (Boolean Field), \n- MOBILE_HAS_CELLULAR_RADIO (Boolean Field), \n- MOBILE_HAS_WIFI_SUPPORT (Boolean Field), \n- MOBILE_BRAND_NAME, \n- MOBILE_MODEL_NAME, \n- MOBILE_MARKETING_NAME, \n- MOBILE_POINTING_METHOD,   \n- Social  \n- SOCIAL_NETWORK, \n- SOCIAL_ACTION, \n- SOCIAL_ACTION_TARGET,   \n- Custom dimension  \n- CUSTOM_DIMENSION (See accompanying field index),",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "kind" : "Kind value for filter expression",
    "matchType" : "Match type for this filter. Possible values are BEGINS_WITH, EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS, PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other filters must use MATCHES."
  },
  "updated" : "Time this filter was last modified."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_goal

Create a new goal.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics goal resource.

**Type:** object

```json
{
  "visitNumPagesDetails" : {
    "comparisonValue" : "Value used for this comparison.",
    "comparisonType" : "Type of comparison. Possible values are LESS_THAN, GREATER_THAN, or EQUAL."
  },
  "parentLink" : {
    "href" : "Link to the view (profile) to which this goal belongs.",
    "type" : "Value is \"analytics#profile\"."
  },
  "created" : "Time this goal was created.",
  "kind" : "Resource type for an Analytics goal.",
  "urlDestinationDetails" : {
    "caseSensitive" : "Determines if the goal URL must exactly match the capitalization of visited URLs.",
    "matchType" : "Match type for the goal URL. Possible values are HEAD, EXACT, or REGEX.",
    "firstStepRequired" : "Determines if the first step in this goal is required.",
    "steps" : [ {
      "number" : "Step number.",
      "name" : "Step name.",
      "url" : "URL for this step."
    } ],
    "url" : "URL for this goal."
  },
  "visitTimeOnSiteDetails" : {
    "comparisonValue" : "Value used for this comparison.",
    "comparisonType" : "Type of comparison. Possible values are LESS_THAN or GREATER_THAN."
  },
  "active" : "Determines whether this goal is active.",
  "type" : "Goal type. Possible values are URL_DESTINATION, VISIT_TIME_ON_SITE, VISIT_NUM_PAGES, AND EVENT.",
  "webPropertyId" : "Web property ID to which this goal belongs. The web property ID is of the form UA-XXXXX-YY.",
  "selfLink" : "Link for this goal.",
  "accountId" : "Account ID to which this goal belongs.",
  "eventDetails" : {
    "eventConditions" : [ {
      "expression" : "Expression used for this match.",
      "comparisonValue" : "Value used for this comparison.",
      "matchType" : "Type of the match to be performed. Possible values are REGEXP, BEGINS_WITH, or EXACT.",
      "comparisonType" : "Type of comparison. Possible values are LESS_THAN, GREATER_THAN or EQUAL.",
      "type" : "Type of this event condition. Possible values are CATEGORY, ACTION, LABEL, or VALUE."
    } ],
    "useEventValue" : "Determines if the event value should be used as the value for this goal."
  },
  "profileId" : "View (Profile) ID to which this goal belongs.",
  "name" : "Goal name.",
  "id" : "Goal ID.",
  "updated" : "Time this goal was last modified.",
  "value" : "Goal value.",
  "internalWebPropertyId" : "Internal ID for the web property to which this goal belongs."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_profile

Create a new view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics view (profile).

**Type:** object

```json
{
  "eCommerceTracking" : "Indicates whether ecommerce tracking is enabled for this view (profile).",
  "excludeQueryParameters" : "The query parameters that are excluded from this view (profile).",
  "siteSearchCategoryParameters" : "Site search category parameters for this view (profile).",
  "defaultPage" : "Default page for this view (profile).",
  "botFilteringEnabled" : "Indicates whether bot filtering is enabled for this view (profile).",
  "timezone" : "Time zone for which this view (profile) has been configured. Time zones are identified by strings from the TZ database.",
  "type" : "View (Profile) type. Supported types: WEB or APP.",
  "starred" : "Indicates whether this view (profile) is starred or not.",
  "websiteUrl" : "Website URL for this view (profile).",
  "permissions" : {
    "effective" : [ "string" ]
  },
  "siteSearchQueryParameters" : "The site search query parameters for this view (profile).",
  "currency" : "The currency type associated with this view (profile), defaults to USD. The supported values are:\nUSD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD, HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL, ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD, SAR, SGD, VEF, LVL",
  "id" : "View (Profile) ID.",
  "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
  "parentLink" : {
    "href" : "Link to the web property to which this view (profile) belongs.",
    "type" : "Value is \"analytics#webproperty\"."
  },
  "stripSiteSearchCategoryParameters" : "Whether or not Analytics will strip search category parameters from the URLs in your reports.",
  "childLink" : {
    "href" : "Link to the list of goals for this view (profile).",
    "type" : "Value is \"analytics#goals\"."
  },
  "created" : "Time this view (profile) was created.",
  "kind" : "Resource type for Analytics view (profile).",
  "enhancedECommerceTracking" : "Indicates whether enhanced ecommerce tracking is enabled for this view (profile). This property can only be enabled if ecommerce tracking is enabled.",
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs.",
  "selfLink" : "Link for this view (profile).",
  "accountId" : "Account ID to which this view (profile) belongs.",
  "stripSiteSearchQueryParameters" : "Whether or not Analytics will strip search query parameters from the URLs in your reports.",
  "name" : "Name of this view (profile).",
  "updated" : "Time this view (profile) was last modified."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_profile_filter_link

Create a new profile filter link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics profile filter link.

**Type:** object

```json
{
  "kind" : "Resource type for Analytics filter.",
  "rank" : "The rank of this profile filter link relative to the other filters linked to the same profile.\nFor readonly (i.e., list and get) operations, the rank always starts at 1.\nFor write (i.e., create, update, or delete) operations, you may specify a value between 0 and 255 inclusively, [0, 255]. In order to insert a link at the end of the list, either don't specify a rank or set a rank to a number greater than the largest rank in the list. In order to insert a link to the beginning of the list specify a rank that is less than or equal to 1. The new link will move all existing filters with the same or lower rank down the list. After the link is inserted/updated/deleted all profile filter links will be renumbered starting at 1.",
  "id" : "Profile filter link ID.",
  "filterRef" : {
    "accountId" : "Account ID to which this filter belongs.",
    "kind" : "Kind value for filter reference.",
    "name" : "Name of this filter.",
    "href" : "Link for this filter.",
    "id" : "Filter ID."
  },
  "profileRef" : {
    "accountId" : "Account ID to which this view (profile) belongs.",
    "kind" : "Analytics view (profile) reference.",
    "name" : "Name of this view (profile).",
    "href" : "Link for this view (profile).",
    "id" : "View (Profile) ID.",
    "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
  },
  "selfLink" : "Link for this profile filter link."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_profile_user_link

Adds a new user to the given view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

```json
{
  "userRef" : {
    "kind" : "string",
    "id" : "User ID.",
    "email" : "Email ID of this user."
  },
  "kind" : "Resource type for entity user link.",
  "permissions" : {
    "effective" : [ "string" ],
    "local" : [ "string" ]
  },
  "id" : "Entity user link ID",
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    },
    "accountRef" : {
      "kind" : "Analytics account reference.",
      "name" : "Account name.",
      "href" : "Link for this account.",
      "id" : "Account ID."
    },
    "profileRef" : {
      "accountId" : "Account ID to which this view (profile) belongs.",
      "kind" : "Analytics view (profile) reference.",
      "name" : "Name of this view (profile).",
      "href" : "Link for this view (profile).",
      "id" : "View (Profile) ID.",
      "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
      "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
    }
  },
  "selfLink" : "Self link for this resource."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_remarketing_audience

Creates a new remarketing audience.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics remarketing audience.

**Type:** object

```json
{
  "created" : "Time this remarketing audience was created.",
  "kind" : "Collection type.",
  "description" : "The description of this remarketing audience.",
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this remarketing audience belongs.",
  "audienceDefinition" : {
    "includeConditions" : {
      "daysToLookBack" : "The look-back window lets you specify a time frame for evaluating the behavior that qualifies users for your audience. For example, if your filters include users from Central Asia, and Transactions Greater than 2, and you set the look-back window to 14 days, then any user from Central Asia whose cumulative transactions exceed 2 during the last 14 days is added to the audience.",
      "kind" : "Resource type for include conditions.",
      "segment" : "The segment condition that will cause a user to be added to an audience.",
      "membershipDurationDays" : "Number of days (in the range 1 to 540) a user remains in the audience.",
      "isSmartList" : "Boolean indicating whether this segment is a smart list. https://support.google.com/analytics/answer/4628577"
    }
  },
  "stateBasedAudienceDefinition" : {
    "excludeConditions" : {
      "segment" : "The segment condition that will cause a user to be removed from an audience.",
      "exclusionDuration" : "Whether to make the exclusion TEMPORARY or PERMANENT."
    },
    "includeConditions" : {
      "daysToLookBack" : "The look-back window lets you specify a time frame for evaluating the behavior that qualifies users for your audience. For example, if your filters include users from Central Asia, and Transactions Greater than 2, and you set the look-back window to 14 days, then any user from Central Asia whose cumulative transactions exceed 2 during the last 14 days is added to the audience.",
      "kind" : "Resource type for include conditions.",
      "segment" : "The segment condition that will cause a user to be added to an audience.",
      "membershipDurationDays" : "Number of days (in the range 1 to 540) a user remains in the audience.",
      "isSmartList" : "Boolean indicating whether this segment is a smart list. https://support.google.com/analytics/answer/4628577"
    }
  },
  "accountId" : "Account ID to which this remarketing audience belongs.",
  "linkedViews" : [ "string" ],
  "name" : "The name of this remarketing audience.",
  "id" : "Remarketing Audience ID.",
  "audienceType" : "The type of audience, either SIMPLE or STATE_BASED.",
  "updated" : "Time this remarketing audience was last modified.",
  "internalWebPropertyId" : "Internal ID for the web property to which this remarketing audience belongs.",
  "linkedAdAccounts" : [ {
    "accountId" : "Account ID to which this linked foreign account belongs.",
    "eligibleForSearch" : "Boolean indicating whether this is eligible for search.",
    "remarketingAudienceId" : "Remarketing audience ID to which this linked foreign account belongs.",
    "linkedAccountId" : "The foreign account ID. For example the an Google Ads `linkedAccountId` has the following format XXX-XXX-XXXX.",
    "kind" : "Resource type for linked foreign account.",
    "id" : "Entity ad account link ID.",
    "type" : "The type of the foreign account. For example, `ADWORDS_LINKS`, `DBM_LINKS`, `MCC_LINKS` or `OPTIMIZE`.",
    "internalWebPropertyId" : "Internal ID for the web property to which this linked foreign account belongs.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this linked foreign account belongs.",
    "status" : "The status of this foreign account link."
  } ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_unsampled_report

Create a new unsampled report.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics unsampled report resource.

**Type:** object

```json
{
  "created" : "Time this unsampled report was created.",
  "kind" : "Resource type for an Analytics unsampled report.",
  "start-date" : "The start date for the unsampled report.",
  "filters" : "The filters for the unsampled report.",
  "title" : "Title of the unsampled report.",
  "driveDownloadDetails" : {
    "documentId" : "Id of the document/file containing the report data."
  },
  "webPropertyId" : "Web property ID to which this unsampled report belongs. The web property ID is of the form UA-XXXXX-YY.",
  "selfLink" : "Link for this unsampled report.",
  "accountId" : "Account ID to which this unsampled report belongs.",
  "end-date" : "The end date for the unsampled report.",
  "profileId" : "View (Profile) ID to which this unsampled report belongs.",
  "segment" : "The segment for the unsampled report.",
  "downloadType" : "The type of download you need to use for the report data file. Possible values include `GOOGLE_DRIVE` and `GOOGLE_CLOUD_STORAGE`. If the value is `GOOGLE_DRIVE`, see the `driveDownloadDetails` field. If the value is `GOOGLE_CLOUD_STORAGE`, see the `cloudStorageDownloadDetails` field.",
  "id" : "Unsampled report ID.",
  "metrics" : "The metrics for the unsampled report.",
  "updated" : "Time this unsampled report was last modified.",
  "cloudStorageDownloadDetails" : {
    "bucketId" : "Id of the bucket the file object is stored in.",
    "objectId" : "Id of the file object containing the report data."
  },
  "dimensions" : "The dimensions for the unsampled report.",
  "status" : "Status of this unsampled report. Possible values are PENDING, COMPLETED, or FAILED."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_web_property

Create a new property if the account has fewer than 20 properties. Web properties are visible in the Google Analytics interface only if they have at least one profile.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### $body

JSON template for an Analytics web property.

**Type:** object

```json
{
  "profileCount" : "View (Profile) count for this web property.",
  "dataRetentionResetOnNewActivity" : "Set to true to reset the retention period of the user identifier with each new event from that user (thus setting the expiration date to current time plus retention period).\nSet to false to delete data associated with the user identifer automatically after the rentention period.\nThis property cannot be set on insert.",
  "parentLink" : {
    "href" : "Link to the account for this web property.",
    "type" : "Type of the parent link. Its value is \"analytics#account\"."
  },
  "dataRetentionTtl" : "The length of time for which user and event data is retained.\nThis property cannot be set on insert.",
  "defaultProfileId" : "Default view (profile) ID.",
  "level" : "Level for this web property. Possible values are STANDARD or PREMIUM.",
  "childLink" : {
    "href" : "Link to the list of views (profiles) for this web property.",
    "type" : "Type of the parent link. Its value is \"analytics#profiles\"."
  },
  "created" : "Time this web property was created.",
  "industryVertical" : "The industry vertical/category selected for this web property.",
  "kind" : "Resource type for Analytics WebProperty.",
  "selfLink" : "Link for this web property.",
  "accountId" : "Account ID to which this web property belongs.",
  "starred" : "Indicates whether this web property is starred or not.",
  "websiteUrl" : "Website url for this web property.",
  "permissions" : {
    "effective" : [ "string" ]
  },
  "name" : "Name of this web property.",
  "id" : "Web property ID of the form UA-XXXXX-YY.",
  "updated" : "Time this web property was last modified.",
  "internalWebPropertyId" : "Internal ID for this web property."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_web_property_adwords_link

Creates a webProperty-Google Ads link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Entity Google Ads Link.

**Type:** object

```json
{
  "kind" : "Resource type for entity Google Ads link.",
  "name" : "Name of the link. This field is required when creating a Google Ads link.",
  "profileIds" : [ "string" ],
  "id" : "Entity Google Ads link ID",
  "adWordsAccounts" : [ {
    "kind" : "Resource type for Google Ads account.",
    "customerId" : "Customer ID. This field is required when creating a Google Ads link.",
    "autoTaggingEnabled" : "True if auto-tagging is enabled on the Google Ads account. Read-only after the insert operation."
  } ],
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    }
  },
  "selfLink" : "URL link for this Google Analytics - Google Ads link."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_web_property_user_link

Adds a new user to the given web property.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

```json
{
  "userRef" : {
    "kind" : "string",
    "id" : "User ID.",
    "email" : "Email ID of this user."
  },
  "kind" : "Resource type for entity user link.",
  "permissions" : {
    "effective" : [ "string" ],
    "local" : [ "string" ]
  },
  "id" : "Entity user link ID",
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    },
    "accountRef" : {
      "kind" : "Analytics account reference.",
      "name" : "Account name.",
      "href" : "Link for this account.",
      "id" : "Account ID."
    },
    "profileRef" : {
      "accountId" : "Account ID to which this view (profile) belongs.",
      "kind" : "Analytics view (profile) reference.",
      "name" : "Name of this view (profile).",
      "href" : "Link for this view (profile).",
      "id" : "View (Profile) ID.",
      "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
      "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
    }
  },
  "selfLink" : "Self link for this resource."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_data_for_upload

Delete data associated with a previous upload.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDataSourceId (required)

Custom data source ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

Request template for the delete upload data request.

**Type:** object

```json
{
  "customDataImportUids" : [ "string" ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_experiment

Delete an experiment.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### experimentId (required)

ID of the experiment.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_filter

Delete a filter.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### filterId (required)

Filter ID.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_profile

Deletes a view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_profile_filter_link

Delete a profile filter link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_profile_user_link

Removes a user from the given view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_remarketing_audience

Delete a remarketing audience.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_unsampled_report

Deletes an unsampled report.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### unsampledReportId (required)

ID of the unsampled report.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_user_from_account

Removes a user from the given account.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_web_property_adwords_link

Deletes a web property-Google Ads link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_web_property_user_link

Removes a user from the given web property.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_custom_dimension

Get a custom dimension to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDimensionId (required)

The ID of the custom dimension.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_custom_metric

Get a custom metric to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customMetricId (required)

The ID of the custom metric.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_data_for_view

Returns Analytics data for a view (profile).

<details><summary>Parameters</summary>

### end-date (required)

End date for fetching Analytics data. Request can should specify an end date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is yesterday.

**Type:** string

### ids (required)

Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**Type:** string

### metrics (required)

A comma-separated list of Analytics metrics. E.g., 'ga:sessions,ga:pageviews'. At least one metric must be specified.

**Type:** string

### start-date (required)

Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### dimensions

A comma-separated list of Analytics dimensions. E.g., 'ga:browser,ga:city'.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### filters

A comma-separated list of dimension or metric filters to be applied to Analytics data.

**Type:** string

### include-empty-rows

The response will include empty rows if this parameter is set to true, the default is true

**Type:** boolean

### output

The selected format for the response. Default format is JSON.

**Type:** string

**Potential values:** dataTable, json

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### samplingLevel

The desired sampling level.

**Type:** string

**Potential values:** DEFAULT, FASTER, HIGHER_PRECISION

### segment

An Analytics segment to be applied to data.

**Type:** string

### sort

A comma-separated list of dimensions or metrics that determine the sort order for Analytics data.

**Type:** string

</details>

## get_experiment

Returns an experiment to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### experimentId (required)

ID of the experiment.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_filter

Returns a filters to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### filterId (required)

Filter ID.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_goal

Gets a goal to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### goalId (required)

Goal ID to retrieve the goal for.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_multichannel_funnels_data_for_view

Returns Analytics Multi-Channel Funnels data for a view (profile).

<details><summary>Parameters</summary>

### end-date (required)

End date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**Type:** string

### ids (required)

Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**Type:** string

### metrics (required)

A comma-separated list of Multi-Channel Funnels metrics. E.g., 'mcf:totalConversions,mcf:totalConversionValue'. At least one metric must be specified.

**Type:** string

### start-date (required)

Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### dimensions

A comma-separated list of Multi-Channel Funnels dimensions. E.g., 'mcf:source,mcf:medium'.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### filters

A comma-separated list of dimension or metric filters to be applied to the Analytics data.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### samplingLevel

The desired sampling level.

**Type:** string

**Potential values:** DEFAULT, FASTER, HIGHER_PRECISION

### sort

A comma-separated list of dimensions or metrics that determine the sort order for the Analytics data.

**Type:** string

</details>

## get_profile

Gets a view (profile) to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_profile_filter_link

Returns a single profile filter link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_realtime_data_for_view

Returns real time data for a view (profile).

<details><summary>Parameters</summary>

### ids (required)

Unique table ID for retrieving real time data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**Type:** string

### metrics (required)

A comma-separated list of real time metrics. E.g., 'rt:activeUsers'. At least one metric must be specified.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### dimensions

A comma-separated list of real time dimensions. E.g., 'rt:medium,rt:city'.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### filters

A comma-separated list of dimension or metric filters to be applied to real time data.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sort

A comma-separated list of dimensions or metrics that determine the sort order for real time data.

**Type:** string

</details>

## get_remarketing_audience

Gets a remarketing audience to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_unsampled_report

Returns a single unsampled report.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### unsampledReportId (required)

ID of the unsampled report.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_upload

List uploads to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDataSourceId (required)

Custom data source ID.

**Type:** string

### uploadId (required)

Upload ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_web_property

Gets a web property to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_web_property_adwords_link

Returns a web property-Google Ads link to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## hash_client_id

Hashes the given Client ID.

<details><summary>Parameters</summary>

### $body

JSON template for a hash Client Id request resource.

**Type:** object

```json
{
  "clientId" : "string",
  "kind" : "string",
  "webPropertyId" : "string"
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_account_summaries

Lists account summaries (lightweight tree comprised of accounts/properties/profiles) to which the user has access.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_account_user_links

Lists account-user links for a given account.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_accounts

Lists all accounts to which the user has access.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_columns_for_report_type

Lists all columns for a report type

<details><summary>Parameters</summary>

### reportType (required)

Report type. Allowed Values: 'ga'. Where 'ga' corresponds to the Core Reporting API

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_custom_data_sources

List custom data sources to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_custom_dimensions

Lists custom dimensions to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_custom_metrics

Lists custom metrics to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_experiments

Lists experiments to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_filters

Lists all filters for an account

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_goals

Lists goals to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_profile_filter_links

Lists all profile filter links for a profile.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_profile_user_links

Lists profile-user links for a given view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_profiles

Lists views (profiles) to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_remarketing_audiences

Lists remarketing audiences to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### type

**Type:** string

</details>

## list_segments

Lists segments to which the user has access.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_unsampled_reports

Lists unsampled reports to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_uploads

List uploads to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDataSourceId (required)

Custom data source ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_web_properties

Lists web properties to which the user has access.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_web_property_adwords_links

Lists webProperty-Google Ads links for a given web property.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_web_property_user_links

Lists webProperty-user links for a given web property.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_custom_dimension

Updates an existing custom dimension. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDimensionId (required)

The ID of the custom dimension.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Custom Dimension.

**Type:** object

```json
{
  "accountId" : "Account ID.",
  "parentLink" : {
    "href" : "Link to the property to which the custom dimension belongs.",
    "type" : "Type of the parent link. Set to \"analytics#webproperty\"."
  },
  "created" : "Time the custom dimension was created.",
  "kind" : "Kind value for a custom dimension. Set to \"analytics#customDimension\". It is a read-only field.",
  "scope" : "Scope of the custom dimension: HIT, SESSION, USER or PRODUCT.",
  "name" : "Name of the custom dimension.",
  "active" : "Boolean indicating whether the custom dimension is active.",
  "index" : "Index of the custom dimension.",
  "id" : "Custom dimension ID.",
  "updated" : "Time the custom dimension was last modified.",
  "webPropertyId" : "Property ID.",
  "selfLink" : "Link for the custom dimension"
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_custom_metric

Updates an existing custom metric. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customMetricId (required)

The ID of the custom metric.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Custom Metric.

**Type:** object

```json
{
  "parentLink" : {
    "href" : "Link to the property to which the custom metric belongs.",
    "type" : "Type of the parent link. Set to \"analytics#webproperty\"."
  },
  "created" : "Time the custom metric was created.",
  "kind" : "Kind value for a custom metric. Set to \"analytics#customMetric\". It is a read-only field.",
  "active" : "Boolean indicating whether the custom metric is active.",
  "index" : "Index of the custom metric.",
  "type" : "Data type of custom metric.",
  "webPropertyId" : "Property ID.",
  "selfLink" : "Link for the custom metric",
  "accountId" : "Account ID.",
  "min_value" : "Min value of custom metric.",
  "scope" : "Scope of the custom metric: HIT or PRODUCT.",
  "name" : "Name of the custom metric.",
  "id" : "Custom metric ID.",
  "updated" : "Time the custom metric was last modified.",
  "max_value" : "Max value of custom metric."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_experiment

Update an existing experiment. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### experimentId (required)

ID of the experiment.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics experiment resource.

**Type:** object

```json
{
  "snippet" : "The snippet of code to include on the control page(s). This field is read-only.",
  "winnerFound" : "Boolean specifying whether a winner has been found for this experiment. This field is read-only.",
  "description" : "Notes about this experiment.",
  "minimumExperimentLengthInDays" : "An integer number in [3, 90]. Specifies the minimum length of the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED.",
  "variations" : [ {
    "won" : "True if the experiment has ended and this variation performed (statistically) significantly better than the original. This field is read-only.",
    "name" : "The name of the variation. This field is required when creating an experiment. This field may not be changed for an experiment whose status is ENDED.",
    "weight" : "Weight that this variation should receive. Only present if the experiment is running. This field is read-only.",
    "url" : "The URL of the variation. This field may not be changed for an experiment whose status is RUNNING or ENDED.",
    "status" : "Status of the variation. Possible values: \"ACTIVE\", \"INACTIVE\". INACTIVE variations are not served. This field may not be changed for an experiment whose status is ENDED."
  } ],
  "startTime" : "The starting time of the experiment (the time the status changed from READY_TO_RUN to RUNNING). This field is present only if the experiment has started. This field is read-only.",
  "id" : "Experiment ID. Required for patch and update. Disallowed for create.",
  "editableInGaUi" : "If true, the end user will be able to edit the experiment via the Google Analytics user interface.",
  "internalWebPropertyId" : "Internal ID for the web property to which this experiment belongs. This field is read-only.",
  "winnerConfidenceLevel" : "A floating-point number in (0, 1). Specifies the necessary confidence level to choose a winner. This field may not be changed for an experiments whose status is ENDED.",
  "parentLink" : {
    "href" : "Link to the view (profile) to which this experiment belongs. This field is read-only.",
    "type" : "Value is \"analytics#profile\". This field is read-only."
  },
  "created" : "Time the experiment was created. This field is read-only.",
  "kind" : "Resource type for an Analytics experiment. This field is read-only.",
  "webPropertyId" : "Web property ID to which this experiment belongs. The web property ID is of the form UA-XXXXX-YY. This field is read-only.",
  "reasonExperimentEnded" : "Why the experiment ended. Possible values: \"STOPPED_BY_USER\", \"WINNER_FOUND\", \"EXPERIMENT_EXPIRED\", \"ENDED_WITH_NO_WINNER\", \"GOAL_OBJECTIVE_CHANGED\". \"ENDED_WITH_NO_WINNER\" means that the experiment didn't expire but no winner was projected to be found. If the experiment status is changed via the API to ENDED this field is set to STOPPED_BY_USER. This field is read-only.",
  "selfLink" : "Link for this experiment. This field is read-only.",
  "trafficCoverage" : "A floating-point number in (0, 1]. Specifies the fraction of the traffic that participates in the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED.",
  "accountId" : "Account ID to which this experiment belongs. This field is read-only.",
  "equalWeighting" : "Boolean specifying whether to distribute traffic evenly across all variations. If the value is False, content experiments follows the default behavior of adjusting traffic dynamically based on variation performance. Optional -- defaults to False. This field may not be changed for an experiment whose status is ENDED.",
  "rewriteVariationUrlsAsOriginal" : "Boolean specifying whether variations URLS are rewritten to match those of the original. This field may not be changed for an experiments whose status is ENDED.",
  "profileId" : "View (Profile) ID to which this experiment belongs. This field is read-only.",
  "optimizationType" : "Whether the objectiveMetric should be minimized or maximized. Possible values: \"MAXIMUM\", \"MINIMUM\". Optional--defaults to \"MAXIMUM\". Cannot be specified without objectiveMetric. Cannot be modified when status is \"RUNNING\" or \"ENDED\".",
  "name" : "Experiment name. This field may not be changed for an experiment whose status is ENDED. This field is required when creating an experiment.",
  "endTime" : "The ending time of the experiment (the time the status changed from RUNNING to ENDED). This field is present only if the experiment has ended. This field is read-only.",
  "servingFramework" : "The framework used to serve the experiment variations and evaluate the results. One of:  \n- REDIRECT: Google Analytics redirects traffic to different variation pages, reports the chosen variation and evaluates the results.\n- API: Google Analytics chooses and reports the variation to serve and evaluates the results; the caller is responsible for serving the selected variation.\n- EXTERNAL: The variations will be served externally and the chosen variation reported to Google Analytics. The caller is responsible for serving the selected variation and evaluating the results.",
  "updated" : "Time the experiment was last modified. This field is read-only.",
  "objectiveMetric" : "The metric that the experiment is optimizing. Valid values: \"ga:goal(n)Completions\", \"ga:adsenseAdsClicks\", \"ga:adsenseAdsViewed\", \"ga:adsenseRevenue\", \"ga:bounces\", \"ga:pageviews\", \"ga:sessionDuration\", \"ga:transactions\", \"ga:transactionRevenue\". This field is required if status is \"RUNNING\" and servingFramework is one of \"REDIRECT\" or \"API\".",
  "status" : "Experiment status. Possible values: \"DRAFT\", \"READY_TO_RUN\", \"RUNNING\", \"ENDED\". Experiments can be created in the \"DRAFT\", \"READY_TO_RUN\" or \"RUNNING\" state. This field is required when creating an experiment."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_filter

Updates an existing filter. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### filterId (required)

Filter ID.

**Type:** string

### $body

JSON template for an Analytics account filter.

**Type:** object

```json
{
  "parentLink" : {
    "href" : "Link to the account to which this filter belongs.",
    "type" : "Value is \"analytics#account\"."
  },
  "searchAndReplaceDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "searchString" : "Term to search.",
    "field" : "Field to use in the filter.",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "replaceString" : "Term to replace the search term with."
  },
  "created" : "Time this filter was created.",
  "excludeDetails" : {
    "expressionValue" : "Filter expression value",
    "fieldIndex" : "The Index of the custom dimension. Set only if the field is a is CUSTOM_DIMENSION.",
    "field" : "Field to filter. Possible values:  \n- Content and Traffic  \n- PAGE_REQUEST_URI, \n- PAGE_HOSTNAME, \n- PAGE_TITLE, \n- REFERRAL, \n- COST_DATA_URI (Campaign target URL), \n- HIT_TYPE, \n- INTERNAL_SEARCH_TERM, \n- INTERNAL_SEARCH_TYPE, \n- SOURCE_PROPERTY_TRACKING_ID,   \n- Campaign or AdGroup  \n- CAMPAIGN_SOURCE, \n- CAMPAIGN_MEDIUM, \n- CAMPAIGN_NAME, \n- CAMPAIGN_AD_GROUP, \n- CAMPAIGN_TERM, \n- CAMPAIGN_CONTENT, \n- CAMPAIGN_CODE, \n- CAMPAIGN_REFERRAL_PATH,   \n- E-Commerce  \n- TRANSACTION_COUNTRY, \n- TRANSACTION_REGION, \n- TRANSACTION_CITY, \n- TRANSACTION_AFFILIATION (Store or order location), \n- ITEM_NAME, \n- ITEM_CODE, \n- ITEM_VARIATION, \n- TRANSACTION_ID, \n- TRANSACTION_CURRENCY_CODE, \n- PRODUCT_ACTION_TYPE,   \n- Audience/Users  \n- BROWSER, \n- BROWSER_VERSION, \n- BROWSER_SIZE, \n- PLATFORM, \n- PLATFORM_VERSION, \n- LANGUAGE, \n- SCREEN_RESOLUTION, \n- SCREEN_COLORS, \n- JAVA_ENABLED (Boolean Field), \n- FLASH_VERSION, \n- GEO_SPEED (Connection speed), \n- VISITOR_TYPE, \n- GEO_ORGANIZATION (ISP organization), \n- GEO_DOMAIN, \n- GEO_IP_ADDRESS, \n- GEO_IP_VERSION,   \n- Location  \n- GEO_COUNTRY, \n- GEO_REGION, \n- GEO_CITY,   \n- Event  \n- EVENT_CATEGORY, \n- EVENT_ACTION, \n- EVENT_LABEL,   \n- Other  \n- CUSTOM_FIELD_1, \n- CUSTOM_FIELD_2, \n- USER_DEFINED_VALUE,   \n- Application  \n- APP_ID, \n- APP_INSTALLER_ID, \n- APP_NAME, \n- APP_VERSION, \n- SCREEN, \n- IS_APP (Boolean Field), \n- IS_FATAL_EXCEPTION (Boolean Field), \n- EXCEPTION_DESCRIPTION,   \n- Mobile device  \n- IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile), \n- IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet), \n- DEVICE_CATEGORY, \n- MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field), \n- MOBILE_HAS_NFC_SUPPORT (Boolean Field), \n- MOBILE_HAS_CELLULAR_RADIO (Boolean Field), \n- MOBILE_HAS_WIFI_SUPPORT (Boolean Field), \n- MOBILE_BRAND_NAME, \n- MOBILE_MODEL_NAME, \n- MOBILE_MARKETING_NAME, \n- MOBILE_POINTING_METHOD,   \n- Social  \n- SOCIAL_NETWORK, \n- SOCIAL_ACTION, \n- SOCIAL_ACTION_TARGET,   \n- Custom dimension  \n- CUSTOM_DIMENSION (See accompanying field index),",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "kind" : "Kind value for filter expression",
    "matchType" : "Match type for this filter. Possible values are BEGINS_WITH, EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS, PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other filters must use MATCHES."
  },
  "kind" : "Resource type for Analytics filter.",
  "lowercaseDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "field" : "Field to use in the filter."
  },
  "type" : "Type of this filter. Possible values are INCLUDE, EXCLUDE, LOWERCASE, UPPERCASE, SEARCH_AND_REPLACE and ADVANCED.",
  "advancedDetails" : {
    "fieldA" : "Field A.",
    "fieldAIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "caseSensitive" : "Indicates if the filter expressions are case sensitive.",
    "overrideOutputField" : "Indicates if the existing value of the output field, if any, should be overridden by the output expression.",
    "extractA" : "Expression to extract from field A.",
    "extractB" : "Expression to extract from field B.",
    "fieldBRequired" : "Indicates if field B is required to match.",
    "fieldB" : "Field B.",
    "outputToField" : "Output field.",
    "fieldBIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "fieldARequired" : "Indicates if field A is required to match.",
    "outputToFieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "outputConstructor" : "Expression used to construct the output value."
  },
  "selfLink" : "Link for this filter.",
  "accountId" : "Account ID to which this filter belongs.",
  "name" : "Name of this filter.",
  "uppercaseDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "field" : "Field to use in the filter."
  },
  "id" : "Filter ID.",
  "includeDetails" : {
    "expressionValue" : "Filter expression value",
    "fieldIndex" : "The Index of the custom dimension. Set only if the field is a is CUSTOM_DIMENSION.",
    "field" : "Field to filter. Possible values:  \n- Content and Traffic  \n- PAGE_REQUEST_URI, \n- PAGE_HOSTNAME, \n- PAGE_TITLE, \n- REFERRAL, \n- COST_DATA_URI (Campaign target URL), \n- HIT_TYPE, \n- INTERNAL_SEARCH_TERM, \n- INTERNAL_SEARCH_TYPE, \n- SOURCE_PROPERTY_TRACKING_ID,   \n- Campaign or AdGroup  \n- CAMPAIGN_SOURCE, \n- CAMPAIGN_MEDIUM, \n- CAMPAIGN_NAME, \n- CAMPAIGN_AD_GROUP, \n- CAMPAIGN_TERM, \n- CAMPAIGN_CONTENT, \n- CAMPAIGN_CODE, \n- CAMPAIGN_REFERRAL_PATH,   \n- E-Commerce  \n- TRANSACTION_COUNTRY, \n- TRANSACTION_REGION, \n- TRANSACTION_CITY, \n- TRANSACTION_AFFILIATION (Store or order location), \n- ITEM_NAME, \n- ITEM_CODE, \n- ITEM_VARIATION, \n- TRANSACTION_ID, \n- TRANSACTION_CURRENCY_CODE, \n- PRODUCT_ACTION_TYPE,   \n- Audience/Users  \n- BROWSER, \n- BROWSER_VERSION, \n- BROWSER_SIZE, \n- PLATFORM, \n- PLATFORM_VERSION, \n- LANGUAGE, \n- SCREEN_RESOLUTION, \n- SCREEN_COLORS, \n- JAVA_ENABLED (Boolean Field), \n- FLASH_VERSION, \n- GEO_SPEED (Connection speed), \n- VISITOR_TYPE, \n- GEO_ORGANIZATION (ISP organization), \n- GEO_DOMAIN, \n- GEO_IP_ADDRESS, \n- GEO_IP_VERSION,   \n- Location  \n- GEO_COUNTRY, \n- GEO_REGION, \n- GEO_CITY,   \n- Event  \n- EVENT_CATEGORY, \n- EVENT_ACTION, \n- EVENT_LABEL,   \n- Other  \n- CUSTOM_FIELD_1, \n- CUSTOM_FIELD_2, \n- USER_DEFINED_VALUE,   \n- Application  \n- APP_ID, \n- APP_INSTALLER_ID, \n- APP_NAME, \n- APP_VERSION, \n- SCREEN, \n- IS_APP (Boolean Field), \n- IS_FATAL_EXCEPTION (Boolean Field), \n- EXCEPTION_DESCRIPTION,   \n- Mobile device  \n- IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile), \n- IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet), \n- DEVICE_CATEGORY, \n- MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field), \n- MOBILE_HAS_NFC_SUPPORT (Boolean Field), \n- MOBILE_HAS_CELLULAR_RADIO (Boolean Field), \n- MOBILE_HAS_WIFI_SUPPORT (Boolean Field), \n- MOBILE_BRAND_NAME, \n- MOBILE_MODEL_NAME, \n- MOBILE_MARKETING_NAME, \n- MOBILE_POINTING_METHOD,   \n- Social  \n- SOCIAL_NETWORK, \n- SOCIAL_ACTION, \n- SOCIAL_ACTION_TARGET,   \n- Custom dimension  \n- CUSTOM_DIMENSION (See accompanying field index),",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "kind" : "Kind value for filter expression",
    "matchType" : "Match type for this filter. Possible values are BEGINS_WITH, EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS, PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other filters must use MATCHES."
  },
  "updated" : "Time this filter was last modified."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_goal

Updates an existing goal. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### goalId (required)

Goal ID to retrieve the goal for.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics goal resource.

**Type:** object

```json
{
  "visitNumPagesDetails" : {
    "comparisonValue" : "Value used for this comparison.",
    "comparisonType" : "Type of comparison. Possible values are LESS_THAN, GREATER_THAN, or EQUAL."
  },
  "parentLink" : {
    "href" : "Link to the view (profile) to which this goal belongs.",
    "type" : "Value is \"analytics#profile\"."
  },
  "created" : "Time this goal was created.",
  "kind" : "Resource type for an Analytics goal.",
  "urlDestinationDetails" : {
    "caseSensitive" : "Determines if the goal URL must exactly match the capitalization of visited URLs.",
    "matchType" : "Match type for the goal URL. Possible values are HEAD, EXACT, or REGEX.",
    "firstStepRequired" : "Determines if the first step in this goal is required.",
    "steps" : [ {
      "number" : "Step number.",
      "name" : "Step name.",
      "url" : "URL for this step."
    } ],
    "url" : "URL for this goal."
  },
  "visitTimeOnSiteDetails" : {
    "comparisonValue" : "Value used for this comparison.",
    "comparisonType" : "Type of comparison. Possible values are LESS_THAN or GREATER_THAN."
  },
  "active" : "Determines whether this goal is active.",
  "type" : "Goal type. Possible values are URL_DESTINATION, VISIT_TIME_ON_SITE, VISIT_NUM_PAGES, AND EVENT.",
  "webPropertyId" : "Web property ID to which this goal belongs. The web property ID is of the form UA-XXXXX-YY.",
  "selfLink" : "Link for this goal.",
  "accountId" : "Account ID to which this goal belongs.",
  "eventDetails" : {
    "eventConditions" : [ {
      "expression" : "Expression used for this match.",
      "comparisonValue" : "Value used for this comparison.",
      "matchType" : "Type of the match to be performed. Possible values are REGEXP, BEGINS_WITH, or EXACT.",
      "comparisonType" : "Type of comparison. Possible values are LESS_THAN, GREATER_THAN or EQUAL.",
      "type" : "Type of this event condition. Possible values are CATEGORY, ACTION, LABEL, or VALUE."
    } ],
    "useEventValue" : "Determines if the event value should be used as the value for this goal."
  },
  "profileId" : "View (Profile) ID to which this goal belongs.",
  "name" : "Goal name.",
  "id" : "Goal ID.",
  "updated" : "Time this goal was last modified.",
  "value" : "Goal value.",
  "internalWebPropertyId" : "Internal ID for the web property to which this goal belongs."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_profile

Updates an existing view (profile). This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics view (profile).

**Type:** object

```json
{
  "eCommerceTracking" : "Indicates whether ecommerce tracking is enabled for this view (profile).",
  "excludeQueryParameters" : "The query parameters that are excluded from this view (profile).",
  "siteSearchCategoryParameters" : "Site search category parameters for this view (profile).",
  "defaultPage" : "Default page for this view (profile).",
  "botFilteringEnabled" : "Indicates whether bot filtering is enabled for this view (profile).",
  "timezone" : "Time zone for which this view (profile) has been configured. Time zones are identified by strings from the TZ database.",
  "type" : "View (Profile) type. Supported types: WEB or APP.",
  "starred" : "Indicates whether this view (profile) is starred or not.",
  "websiteUrl" : "Website URL for this view (profile).",
  "permissions" : {
    "effective" : [ "string" ]
  },
  "siteSearchQueryParameters" : "The site search query parameters for this view (profile).",
  "currency" : "The currency type associated with this view (profile), defaults to USD. The supported values are:\nUSD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD, HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL, ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD, SAR, SGD, VEF, LVL",
  "id" : "View (Profile) ID.",
  "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
  "parentLink" : {
    "href" : "Link to the web property to which this view (profile) belongs.",
    "type" : "Value is \"analytics#webproperty\"."
  },
  "stripSiteSearchCategoryParameters" : "Whether or not Analytics will strip search category parameters from the URLs in your reports.",
  "childLink" : {
    "href" : "Link to the list of goals for this view (profile).",
    "type" : "Value is \"analytics#goals\"."
  },
  "created" : "Time this view (profile) was created.",
  "kind" : "Resource type for Analytics view (profile).",
  "enhancedECommerceTracking" : "Indicates whether enhanced ecommerce tracking is enabled for this view (profile). This property can only be enabled if ecommerce tracking is enabled.",
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs.",
  "selfLink" : "Link for this view (profile).",
  "accountId" : "Account ID to which this view (profile) belongs.",
  "stripSiteSearchQueryParameters" : "Whether or not Analytics will strip search query parameters from the URLs in your reports.",
  "name" : "Name of this view (profile).",
  "updated" : "Time this view (profile) was last modified."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_profile_filter_link

Update an existing profile filter link. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics profile filter link.

**Type:** object

```json
{
  "kind" : "Resource type for Analytics filter.",
  "rank" : "The rank of this profile filter link relative to the other filters linked to the same profile.\nFor readonly (i.e., list and get) operations, the rank always starts at 1.\nFor write (i.e., create, update, or delete) operations, you may specify a value between 0 and 255 inclusively, [0, 255]. In order to insert a link at the end of the list, either don't specify a rank or set a rank to a number greater than the largest rank in the list. In order to insert a link to the beginning of the list specify a rank that is less than or equal to 1. The new link will move all existing filters with the same or lower rank down the list. After the link is inserted/updated/deleted all profile filter links will be renumbered starting at 1.",
  "id" : "Profile filter link ID.",
  "filterRef" : {
    "accountId" : "Account ID to which this filter belongs.",
    "kind" : "Kind value for filter reference.",
    "name" : "Name of this filter.",
    "href" : "Link for this filter.",
    "id" : "Filter ID."
  },
  "profileRef" : {
    "accountId" : "Account ID to which this view (profile) belongs.",
    "kind" : "Analytics view (profile) reference.",
    "name" : "Name of this view (profile).",
    "href" : "Link for this view (profile).",
    "id" : "View (Profile) ID.",
    "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
  },
  "selfLink" : "Link for this profile filter link."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_remarketing_audience

Updates an existing remarketing audience. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics remarketing audience.

**Type:** object

```json
{
  "created" : "Time this remarketing audience was created.",
  "kind" : "Collection type.",
  "description" : "The description of this remarketing audience.",
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this remarketing audience belongs.",
  "audienceDefinition" : {
    "includeConditions" : {
      "daysToLookBack" : "The look-back window lets you specify a time frame for evaluating the behavior that qualifies users for your audience. For example, if your filters include users from Central Asia, and Transactions Greater than 2, and you set the look-back window to 14 days, then any user from Central Asia whose cumulative transactions exceed 2 during the last 14 days is added to the audience.",
      "kind" : "Resource type for include conditions.",
      "segment" : "The segment condition that will cause a user to be added to an audience.",
      "membershipDurationDays" : "Number of days (in the range 1 to 540) a user remains in the audience.",
      "isSmartList" : "Boolean indicating whether this segment is a smart list. https://support.google.com/analytics/answer/4628577"
    }
  },
  "stateBasedAudienceDefinition" : {
    "excludeConditions" : {
      "segment" : "The segment condition that will cause a user to be removed from an audience.",
      "exclusionDuration" : "Whether to make the exclusion TEMPORARY or PERMANENT."
    },
    "includeConditions" : {
      "daysToLookBack" : "The look-back window lets you specify a time frame for evaluating the behavior that qualifies users for your audience. For example, if your filters include users from Central Asia, and Transactions Greater than 2, and you set the look-back window to 14 days, then any user from Central Asia whose cumulative transactions exceed 2 during the last 14 days is added to the audience.",
      "kind" : "Resource type for include conditions.",
      "segment" : "The segment condition that will cause a user to be added to an audience.",
      "membershipDurationDays" : "Number of days (in the range 1 to 540) a user remains in the audience.",
      "isSmartList" : "Boolean indicating whether this segment is a smart list. https://support.google.com/analytics/answer/4628577"
    }
  },
  "accountId" : "Account ID to which this remarketing audience belongs.",
  "linkedViews" : [ "string" ],
  "name" : "The name of this remarketing audience.",
  "id" : "Remarketing Audience ID.",
  "audienceType" : "The type of audience, either SIMPLE or STATE_BASED.",
  "updated" : "Time this remarketing audience was last modified.",
  "internalWebPropertyId" : "Internal ID for the web property to which this remarketing audience belongs.",
  "linkedAdAccounts" : [ {
    "accountId" : "Account ID to which this linked foreign account belongs.",
    "eligibleForSearch" : "Boolean indicating whether this is eligible for search.",
    "remarketingAudienceId" : "Remarketing audience ID to which this linked foreign account belongs.",
    "linkedAccountId" : "The foreign account ID. For example the an Google Ads `linkedAccountId` has the following format XXX-XXX-XXXX.",
    "kind" : "Resource type for linked foreign account.",
    "id" : "Entity ad account link ID.",
    "type" : "The type of the foreign account. For example, `ADWORDS_LINKS`, `DBM_LINKS`, `MCC_LINKS` or `OPTIMIZE`.",
    "internalWebPropertyId" : "Internal ID for the web property to which this linked foreign account belongs.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this linked foreign account belongs.",
    "status" : "The status of this foreign account link."
  } ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_web_property

Updates an existing web property. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics web property.

**Type:** object

```json
{
  "profileCount" : "View (Profile) count for this web property.",
  "dataRetentionResetOnNewActivity" : "Set to true to reset the retention period of the user identifier with each new event from that user (thus setting the expiration date to current time plus retention period).\nSet to false to delete data associated with the user identifer automatically after the rentention period.\nThis property cannot be set on insert.",
  "parentLink" : {
    "href" : "Link to the account for this web property.",
    "type" : "Type of the parent link. Its value is \"analytics#account\"."
  },
  "dataRetentionTtl" : "The length of time for which user and event data is retained.\nThis property cannot be set on insert.",
  "defaultProfileId" : "Default view (profile) ID.",
  "level" : "Level for this web property. Possible values are STANDARD or PREMIUM.",
  "childLink" : {
    "href" : "Link to the list of views (profiles) for this web property.",
    "type" : "Type of the parent link. Its value is \"analytics#profiles\"."
  },
  "created" : "Time this web property was created.",
  "industryVertical" : "The industry vertical/category selected for this web property.",
  "kind" : "Resource type for Analytics WebProperty.",
  "selfLink" : "Link for this web property.",
  "accountId" : "Account ID to which this web property belongs.",
  "starred" : "Indicates whether this web property is starred or not.",
  "websiteUrl" : "Website url for this web property.",
  "permissions" : {
    "effective" : [ "string" ]
  },
  "name" : "Name of this web property.",
  "id" : "Web property ID of the form UA-XXXXX-YY.",
  "updated" : "Time this web property was last modified.",
  "internalWebPropertyId" : "Internal ID for this web property."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_web_property_adwords_link

Updates an existing webProperty-Google Ads link. This method supports patch semantics.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Entity Google Ads Link.

**Type:** object

```json
{
  "kind" : "Resource type for entity Google Ads link.",
  "name" : "Name of the link. This field is required when creating a Google Ads link.",
  "profileIds" : [ "string" ],
  "id" : "Entity Google Ads link ID",
  "adWordsAccounts" : [ {
    "kind" : "Resource type for Google Ads account.",
    "customerId" : "Customer ID. This field is required when creating a Google Ads link.",
    "autoTaggingEnabled" : "True if auto-tagging is enabled on the Google Ads account. Read-only after the insert operation."
  } ],
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    }
  },
  "selfLink" : "URL link for this Google Analytics - Google Ads link."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## provision_account

Provision account.

<details><summary>Parameters</summary>

### $body

JSON template for an Analytics account tree requests. The account tree request is used in the provisioning api to create an account, property, and view (profile). It contains the basic information required to make these fields.

**Type:** object

```json
{
  "profileName" : "string",
  "accountName" : "string",
  "websiteUrl" : "string",
  "kind" : "Resource type for account ticket.",
  "timezone" : "string",
  "webpropertyName" : "string"
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_custom_dimension

Updates an existing custom dimension.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDimensionId (required)

The ID of the custom dimension.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Custom Dimension.

**Type:** object

```json
{
  "accountId" : "Account ID.",
  "parentLink" : {
    "href" : "Link to the property to which the custom dimension belongs.",
    "type" : "Type of the parent link. Set to \"analytics#webproperty\"."
  },
  "created" : "Time the custom dimension was created.",
  "kind" : "Kind value for a custom dimension. Set to \"analytics#customDimension\". It is a read-only field.",
  "scope" : "Scope of the custom dimension: HIT, SESSION, USER or PRODUCT.",
  "name" : "Name of the custom dimension.",
  "active" : "Boolean indicating whether the custom dimension is active.",
  "index" : "Index of the custom dimension.",
  "id" : "Custom dimension ID.",
  "updated" : "Time the custom dimension was last modified.",
  "webPropertyId" : "Property ID.",
  "selfLink" : "Link for the custom dimension"
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_custom_metric

Updates an existing custom metric.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customMetricId (required)

The ID of the custom metric.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Custom Metric.

**Type:** object

```json
{
  "parentLink" : {
    "href" : "Link to the property to which the custom metric belongs.",
    "type" : "Type of the parent link. Set to \"analytics#webproperty\"."
  },
  "created" : "Time the custom metric was created.",
  "kind" : "Kind value for a custom metric. Set to \"analytics#customMetric\". It is a read-only field.",
  "active" : "Boolean indicating whether the custom metric is active.",
  "index" : "Index of the custom metric.",
  "type" : "Data type of custom metric.",
  "webPropertyId" : "Property ID.",
  "selfLink" : "Link for the custom metric",
  "accountId" : "Account ID.",
  "min_value" : "Min value of custom metric.",
  "scope" : "Scope of the custom metric: HIT or PRODUCT.",
  "name" : "Name of the custom metric.",
  "id" : "Custom metric ID.",
  "updated" : "Time the custom metric was last modified.",
  "max_value" : "Max value of custom metric."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### ignoreCustomDataSourceLinks

Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_experiment

Update an existing experiment.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### experimentId (required)

ID of the experiment.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics experiment resource.

**Type:** object

```json
{
  "snippet" : "The snippet of code to include on the control page(s). This field is read-only.",
  "winnerFound" : "Boolean specifying whether a winner has been found for this experiment. This field is read-only.",
  "description" : "Notes about this experiment.",
  "minimumExperimentLengthInDays" : "An integer number in [3, 90]. Specifies the minimum length of the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED.",
  "variations" : [ {
    "won" : "True if the experiment has ended and this variation performed (statistically) significantly better than the original. This field is read-only.",
    "name" : "The name of the variation. This field is required when creating an experiment. This field may not be changed for an experiment whose status is ENDED.",
    "weight" : "Weight that this variation should receive. Only present if the experiment is running. This field is read-only.",
    "url" : "The URL of the variation. This field may not be changed for an experiment whose status is RUNNING or ENDED.",
    "status" : "Status of the variation. Possible values: \"ACTIVE\", \"INACTIVE\". INACTIVE variations are not served. This field may not be changed for an experiment whose status is ENDED."
  } ],
  "startTime" : "The starting time of the experiment (the time the status changed from READY_TO_RUN to RUNNING). This field is present only if the experiment has started. This field is read-only.",
  "id" : "Experiment ID. Required for patch and update. Disallowed for create.",
  "editableInGaUi" : "If true, the end user will be able to edit the experiment via the Google Analytics user interface.",
  "internalWebPropertyId" : "Internal ID for the web property to which this experiment belongs. This field is read-only.",
  "winnerConfidenceLevel" : "A floating-point number in (0, 1). Specifies the necessary confidence level to choose a winner. This field may not be changed for an experiments whose status is ENDED.",
  "parentLink" : {
    "href" : "Link to the view (profile) to which this experiment belongs. This field is read-only.",
    "type" : "Value is \"analytics#profile\". This field is read-only."
  },
  "created" : "Time the experiment was created. This field is read-only.",
  "kind" : "Resource type for an Analytics experiment. This field is read-only.",
  "webPropertyId" : "Web property ID to which this experiment belongs. The web property ID is of the form UA-XXXXX-YY. This field is read-only.",
  "reasonExperimentEnded" : "Why the experiment ended. Possible values: \"STOPPED_BY_USER\", \"WINNER_FOUND\", \"EXPERIMENT_EXPIRED\", \"ENDED_WITH_NO_WINNER\", \"GOAL_OBJECTIVE_CHANGED\". \"ENDED_WITH_NO_WINNER\" means that the experiment didn't expire but no winner was projected to be found. If the experiment status is changed via the API to ENDED this field is set to STOPPED_BY_USER. This field is read-only.",
  "selfLink" : "Link for this experiment. This field is read-only.",
  "trafficCoverage" : "A floating-point number in (0, 1]. Specifies the fraction of the traffic that participates in the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED.",
  "accountId" : "Account ID to which this experiment belongs. This field is read-only.",
  "equalWeighting" : "Boolean specifying whether to distribute traffic evenly across all variations. If the value is False, content experiments follows the default behavior of adjusting traffic dynamically based on variation performance. Optional -- defaults to False. This field may not be changed for an experiment whose status is ENDED.",
  "rewriteVariationUrlsAsOriginal" : "Boolean specifying whether variations URLS are rewritten to match those of the original. This field may not be changed for an experiments whose status is ENDED.",
  "profileId" : "View (Profile) ID to which this experiment belongs. This field is read-only.",
  "optimizationType" : "Whether the objectiveMetric should be minimized or maximized. Possible values: \"MAXIMUM\", \"MINIMUM\". Optional--defaults to \"MAXIMUM\". Cannot be specified without objectiveMetric. Cannot be modified when status is \"RUNNING\" or \"ENDED\".",
  "name" : "Experiment name. This field may not be changed for an experiment whose status is ENDED. This field is required when creating an experiment.",
  "endTime" : "The ending time of the experiment (the time the status changed from RUNNING to ENDED). This field is present only if the experiment has ended. This field is read-only.",
  "servingFramework" : "The framework used to serve the experiment variations and evaluate the results. One of:  \n- REDIRECT: Google Analytics redirects traffic to different variation pages, reports the chosen variation and evaluates the results.\n- API: Google Analytics chooses and reports the variation to serve and evaluates the results; the caller is responsible for serving the selected variation.\n- EXTERNAL: The variations will be served externally and the chosen variation reported to Google Analytics. The caller is responsible for serving the selected variation and evaluating the results.",
  "updated" : "Time the experiment was last modified. This field is read-only.",
  "objectiveMetric" : "The metric that the experiment is optimizing. Valid values: \"ga:goal(n)Completions\", \"ga:adsenseAdsClicks\", \"ga:adsenseAdsViewed\", \"ga:adsenseRevenue\", \"ga:bounces\", \"ga:pageviews\", \"ga:sessionDuration\", \"ga:transactions\", \"ga:transactionRevenue\". This field is required if status is \"RUNNING\" and servingFramework is one of \"REDIRECT\" or \"API\".",
  "status" : "Experiment status. Possible values: \"DRAFT\", \"READY_TO_RUN\", \"RUNNING\", \"ENDED\". Experiments can be created in the \"DRAFT\", \"READY_TO_RUN\" or \"RUNNING\" state. This field is required when creating an experiment."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_filter

Updates an existing filter.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### filterId (required)

Filter ID.

**Type:** string

### $body

JSON template for an Analytics account filter.

**Type:** object

```json
{
  "parentLink" : {
    "href" : "Link to the account to which this filter belongs.",
    "type" : "Value is \"analytics#account\"."
  },
  "searchAndReplaceDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "searchString" : "Term to search.",
    "field" : "Field to use in the filter.",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "replaceString" : "Term to replace the search term with."
  },
  "created" : "Time this filter was created.",
  "excludeDetails" : {
    "expressionValue" : "Filter expression value",
    "fieldIndex" : "The Index of the custom dimension. Set only if the field is a is CUSTOM_DIMENSION.",
    "field" : "Field to filter. Possible values:  \n- Content and Traffic  \n- PAGE_REQUEST_URI, \n- PAGE_HOSTNAME, \n- PAGE_TITLE, \n- REFERRAL, \n- COST_DATA_URI (Campaign target URL), \n- HIT_TYPE, \n- INTERNAL_SEARCH_TERM, \n- INTERNAL_SEARCH_TYPE, \n- SOURCE_PROPERTY_TRACKING_ID,   \n- Campaign or AdGroup  \n- CAMPAIGN_SOURCE, \n- CAMPAIGN_MEDIUM, \n- CAMPAIGN_NAME, \n- CAMPAIGN_AD_GROUP, \n- CAMPAIGN_TERM, \n- CAMPAIGN_CONTENT, \n- CAMPAIGN_CODE, \n- CAMPAIGN_REFERRAL_PATH,   \n- E-Commerce  \n- TRANSACTION_COUNTRY, \n- TRANSACTION_REGION, \n- TRANSACTION_CITY, \n- TRANSACTION_AFFILIATION (Store or order location), \n- ITEM_NAME, \n- ITEM_CODE, \n- ITEM_VARIATION, \n- TRANSACTION_ID, \n- TRANSACTION_CURRENCY_CODE, \n- PRODUCT_ACTION_TYPE,   \n- Audience/Users  \n- BROWSER, \n- BROWSER_VERSION, \n- BROWSER_SIZE, \n- PLATFORM, \n- PLATFORM_VERSION, \n- LANGUAGE, \n- SCREEN_RESOLUTION, \n- SCREEN_COLORS, \n- JAVA_ENABLED (Boolean Field), \n- FLASH_VERSION, \n- GEO_SPEED (Connection speed), \n- VISITOR_TYPE, \n- GEO_ORGANIZATION (ISP organization), \n- GEO_DOMAIN, \n- GEO_IP_ADDRESS, \n- GEO_IP_VERSION,   \n- Location  \n- GEO_COUNTRY, \n- GEO_REGION, \n- GEO_CITY,   \n- Event  \n- EVENT_CATEGORY, \n- EVENT_ACTION, \n- EVENT_LABEL,   \n- Other  \n- CUSTOM_FIELD_1, \n- CUSTOM_FIELD_2, \n- USER_DEFINED_VALUE,   \n- Application  \n- APP_ID, \n- APP_INSTALLER_ID, \n- APP_NAME, \n- APP_VERSION, \n- SCREEN, \n- IS_APP (Boolean Field), \n- IS_FATAL_EXCEPTION (Boolean Field), \n- EXCEPTION_DESCRIPTION,   \n- Mobile device  \n- IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile), \n- IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet), \n- DEVICE_CATEGORY, \n- MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field), \n- MOBILE_HAS_NFC_SUPPORT (Boolean Field), \n- MOBILE_HAS_CELLULAR_RADIO (Boolean Field), \n- MOBILE_HAS_WIFI_SUPPORT (Boolean Field), \n- MOBILE_BRAND_NAME, \n- MOBILE_MODEL_NAME, \n- MOBILE_MARKETING_NAME, \n- MOBILE_POINTING_METHOD,   \n- Social  \n- SOCIAL_NETWORK, \n- SOCIAL_ACTION, \n- SOCIAL_ACTION_TARGET,   \n- Custom dimension  \n- CUSTOM_DIMENSION (See accompanying field index),",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "kind" : "Kind value for filter expression",
    "matchType" : "Match type for this filter. Possible values are BEGINS_WITH, EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS, PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other filters must use MATCHES."
  },
  "kind" : "Resource type for Analytics filter.",
  "lowercaseDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "field" : "Field to use in the filter."
  },
  "type" : "Type of this filter. Possible values are INCLUDE, EXCLUDE, LOWERCASE, UPPERCASE, SEARCH_AND_REPLACE and ADVANCED.",
  "advancedDetails" : {
    "fieldA" : "Field A.",
    "fieldAIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "caseSensitive" : "Indicates if the filter expressions are case sensitive.",
    "overrideOutputField" : "Indicates if the existing value of the output field, if any, should be overridden by the output expression.",
    "extractA" : "Expression to extract from field A.",
    "extractB" : "Expression to extract from field B.",
    "fieldBRequired" : "Indicates if field B is required to match.",
    "fieldB" : "Field B.",
    "outputToField" : "Output field.",
    "fieldBIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "fieldARequired" : "Indicates if field A is required to match.",
    "outputToFieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "outputConstructor" : "Expression used to construct the output value."
  },
  "selfLink" : "Link for this filter.",
  "accountId" : "Account ID to which this filter belongs.",
  "name" : "Name of this filter.",
  "uppercaseDetails" : {
    "fieldIndex" : "The Index of the custom dimension. Required if field is a CUSTOM_DIMENSION.",
    "field" : "Field to use in the filter."
  },
  "id" : "Filter ID.",
  "includeDetails" : {
    "expressionValue" : "Filter expression value",
    "fieldIndex" : "The Index of the custom dimension. Set only if the field is a is CUSTOM_DIMENSION.",
    "field" : "Field to filter. Possible values:  \n- Content and Traffic  \n- PAGE_REQUEST_URI, \n- PAGE_HOSTNAME, \n- PAGE_TITLE, \n- REFERRAL, \n- COST_DATA_URI (Campaign target URL), \n- HIT_TYPE, \n- INTERNAL_SEARCH_TERM, \n- INTERNAL_SEARCH_TYPE, \n- SOURCE_PROPERTY_TRACKING_ID,   \n- Campaign or AdGroup  \n- CAMPAIGN_SOURCE, \n- CAMPAIGN_MEDIUM, \n- CAMPAIGN_NAME, \n- CAMPAIGN_AD_GROUP, \n- CAMPAIGN_TERM, \n- CAMPAIGN_CONTENT, \n- CAMPAIGN_CODE, \n- CAMPAIGN_REFERRAL_PATH,   \n- E-Commerce  \n- TRANSACTION_COUNTRY, \n- TRANSACTION_REGION, \n- TRANSACTION_CITY, \n- TRANSACTION_AFFILIATION (Store or order location), \n- ITEM_NAME, \n- ITEM_CODE, \n- ITEM_VARIATION, \n- TRANSACTION_ID, \n- TRANSACTION_CURRENCY_CODE, \n- PRODUCT_ACTION_TYPE,   \n- Audience/Users  \n- BROWSER, \n- BROWSER_VERSION, \n- BROWSER_SIZE, \n- PLATFORM, \n- PLATFORM_VERSION, \n- LANGUAGE, \n- SCREEN_RESOLUTION, \n- SCREEN_COLORS, \n- JAVA_ENABLED (Boolean Field), \n- FLASH_VERSION, \n- GEO_SPEED (Connection speed), \n- VISITOR_TYPE, \n- GEO_ORGANIZATION (ISP organization), \n- GEO_DOMAIN, \n- GEO_IP_ADDRESS, \n- GEO_IP_VERSION,   \n- Location  \n- GEO_COUNTRY, \n- GEO_REGION, \n- GEO_CITY,   \n- Event  \n- EVENT_CATEGORY, \n- EVENT_ACTION, \n- EVENT_LABEL,   \n- Other  \n- CUSTOM_FIELD_1, \n- CUSTOM_FIELD_2, \n- USER_DEFINED_VALUE,   \n- Application  \n- APP_ID, \n- APP_INSTALLER_ID, \n- APP_NAME, \n- APP_VERSION, \n- SCREEN, \n- IS_APP (Boolean Field), \n- IS_FATAL_EXCEPTION (Boolean Field), \n- EXCEPTION_DESCRIPTION,   \n- Mobile device  \n- IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile), \n- IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet), \n- DEVICE_CATEGORY, \n- MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field), \n- MOBILE_HAS_NFC_SUPPORT (Boolean Field), \n- MOBILE_HAS_CELLULAR_RADIO (Boolean Field), \n- MOBILE_HAS_WIFI_SUPPORT (Boolean Field), \n- MOBILE_BRAND_NAME, \n- MOBILE_MODEL_NAME, \n- MOBILE_MARKETING_NAME, \n- MOBILE_POINTING_METHOD,   \n- Social  \n- SOCIAL_NETWORK, \n- SOCIAL_ACTION, \n- SOCIAL_ACTION_TARGET,   \n- Custom dimension  \n- CUSTOM_DIMENSION (See accompanying field index),",
    "caseSensitive" : "Determines if the filter is case sensitive.",
    "kind" : "Kind value for filter expression",
    "matchType" : "Match type for this filter. Possible values are BEGINS_WITH, EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS, PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other filters must use MATCHES."
  },
  "updated" : "Time this filter was last modified."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_goal

Updates an existing goal.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### goalId (required)

Goal ID to retrieve the goal for.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics goal resource.

**Type:** object

```json
{
  "visitNumPagesDetails" : {
    "comparisonValue" : "Value used for this comparison.",
    "comparisonType" : "Type of comparison. Possible values are LESS_THAN, GREATER_THAN, or EQUAL."
  },
  "parentLink" : {
    "href" : "Link to the view (profile) to which this goal belongs.",
    "type" : "Value is \"analytics#profile\"."
  },
  "created" : "Time this goal was created.",
  "kind" : "Resource type for an Analytics goal.",
  "urlDestinationDetails" : {
    "caseSensitive" : "Determines if the goal URL must exactly match the capitalization of visited URLs.",
    "matchType" : "Match type for the goal URL. Possible values are HEAD, EXACT, or REGEX.",
    "firstStepRequired" : "Determines if the first step in this goal is required.",
    "steps" : [ {
      "number" : "Step number.",
      "name" : "Step name.",
      "url" : "URL for this step."
    } ],
    "url" : "URL for this goal."
  },
  "visitTimeOnSiteDetails" : {
    "comparisonValue" : "Value used for this comparison.",
    "comparisonType" : "Type of comparison. Possible values are LESS_THAN or GREATER_THAN."
  },
  "active" : "Determines whether this goal is active.",
  "type" : "Goal type. Possible values are URL_DESTINATION, VISIT_TIME_ON_SITE, VISIT_NUM_PAGES, AND EVENT.",
  "webPropertyId" : "Web property ID to which this goal belongs. The web property ID is of the form UA-XXXXX-YY.",
  "selfLink" : "Link for this goal.",
  "accountId" : "Account ID to which this goal belongs.",
  "eventDetails" : {
    "eventConditions" : [ {
      "expression" : "Expression used for this match.",
      "comparisonValue" : "Value used for this comparison.",
      "matchType" : "Type of the match to be performed. Possible values are REGEXP, BEGINS_WITH, or EXACT.",
      "comparisonType" : "Type of comparison. Possible values are LESS_THAN, GREATER_THAN or EQUAL.",
      "type" : "Type of this event condition. Possible values are CATEGORY, ACTION, LABEL, or VALUE."
    } ],
    "useEventValue" : "Determines if the event value should be used as the value for this goal."
  },
  "profileId" : "View (Profile) ID to which this goal belongs.",
  "name" : "Goal name.",
  "id" : "Goal ID.",
  "updated" : "Time this goal was last modified.",
  "value" : "Goal value.",
  "internalWebPropertyId" : "Internal ID for the web property to which this goal belongs."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_or_create_user_deletion_request

Insert or update a user deletion requests.

<details><summary>Parameters</summary>

### $body

JSON template for a user deletion request resource.

**Type:** object

```json
{
  "kind" : "Value is \"analytics#userDeletionRequest\".",
  "id" : {
    "type" : "Type of user",
    "userId" : "The User's id"
  },
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY.",
  "deletionRequestTime" : "This marks the point in time for which all user data before should be deleted",
  "firebaseProjectId" : "Firebase Project Id"
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_permissions_for_user

Updates permissions for an existing user on the given account.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

```json
{
  "userRef" : {
    "kind" : "string",
    "id" : "User ID.",
    "email" : "Email ID of this user."
  },
  "kind" : "Resource type for entity user link.",
  "permissions" : {
    "effective" : [ "string" ],
    "local" : [ "string" ]
  },
  "id" : "Entity user link ID",
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    },
    "accountRef" : {
      "kind" : "Analytics account reference.",
      "name" : "Account name.",
      "href" : "Link for this account.",
      "id" : "Account ID."
    },
    "profileRef" : {
      "accountId" : "Account ID to which this view (profile) belongs.",
      "kind" : "Analytics view (profile) reference.",
      "name" : "Name of this view (profile).",
      "href" : "Link for this view (profile).",
      "id" : "View (Profile) ID.",
      "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
      "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
    }
  },
  "selfLink" : "Self link for this resource."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_profile

Updates an existing view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics view (profile).

**Type:** object

```json
{
  "eCommerceTracking" : "Indicates whether ecommerce tracking is enabled for this view (profile).",
  "excludeQueryParameters" : "The query parameters that are excluded from this view (profile).",
  "siteSearchCategoryParameters" : "Site search category parameters for this view (profile).",
  "defaultPage" : "Default page for this view (profile).",
  "botFilteringEnabled" : "Indicates whether bot filtering is enabled for this view (profile).",
  "timezone" : "Time zone for which this view (profile) has been configured. Time zones are identified by strings from the TZ database.",
  "type" : "View (Profile) type. Supported types: WEB or APP.",
  "starred" : "Indicates whether this view (profile) is starred or not.",
  "websiteUrl" : "Website URL for this view (profile).",
  "permissions" : {
    "effective" : [ "string" ]
  },
  "siteSearchQueryParameters" : "The site search query parameters for this view (profile).",
  "currency" : "The currency type associated with this view (profile), defaults to USD. The supported values are:\nUSD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD, HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL, ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD, SAR, SGD, VEF, LVL",
  "id" : "View (Profile) ID.",
  "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
  "parentLink" : {
    "href" : "Link to the web property to which this view (profile) belongs.",
    "type" : "Value is \"analytics#webproperty\"."
  },
  "stripSiteSearchCategoryParameters" : "Whether or not Analytics will strip search category parameters from the URLs in your reports.",
  "childLink" : {
    "href" : "Link to the list of goals for this view (profile).",
    "type" : "Value is \"analytics#goals\"."
  },
  "created" : "Time this view (profile) was created.",
  "kind" : "Resource type for Analytics view (profile).",
  "enhancedECommerceTracking" : "Indicates whether enhanced ecommerce tracking is enabled for this view (profile). This property can only be enabled if ecommerce tracking is enabled.",
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs.",
  "selfLink" : "Link for this view (profile).",
  "accountId" : "Account ID to which this view (profile) belongs.",
  "stripSiteSearchQueryParameters" : "Whether or not Analytics will strip search query parameters from the URLs in your reports.",
  "name" : "Name of this view (profile).",
  "updated" : "Time this view (profile) was last modified."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_profile_filter_link

Update an existing profile filter link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics profile filter link.

**Type:** object

```json
{
  "kind" : "Resource type for Analytics filter.",
  "rank" : "The rank of this profile filter link relative to the other filters linked to the same profile.\nFor readonly (i.e., list and get) operations, the rank always starts at 1.\nFor write (i.e., create, update, or delete) operations, you may specify a value between 0 and 255 inclusively, [0, 255]. In order to insert a link at the end of the list, either don't specify a rank or set a rank to a number greater than the largest rank in the list. In order to insert a link to the beginning of the list specify a rank that is less than or equal to 1. The new link will move all existing filters with the same or lower rank down the list. After the link is inserted/updated/deleted all profile filter links will be renumbered starting at 1.",
  "id" : "Profile filter link ID.",
  "filterRef" : {
    "accountId" : "Account ID to which this filter belongs.",
    "kind" : "Kind value for filter reference.",
    "name" : "Name of this filter.",
    "href" : "Link for this filter.",
    "id" : "Filter ID."
  },
  "profileRef" : {
    "accountId" : "Account ID to which this view (profile) belongs.",
    "kind" : "Analytics view (profile) reference.",
    "name" : "Name of this view (profile).",
    "href" : "Link for this view (profile).",
    "id" : "View (Profile) ID.",
    "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
  },
  "selfLink" : "Link for this profile filter link."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_profile_user_links

Updates permissions for an existing user on the given view (profile).

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### profileId (required)

ID of the view (profile). If possible, can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

```json
{
  "userRef" : {
    "kind" : "string",
    "id" : "User ID.",
    "email" : "Email ID of this user."
  },
  "kind" : "Resource type for entity user link.",
  "permissions" : {
    "effective" : [ "string" ],
    "local" : [ "string" ]
  },
  "id" : "Entity user link ID",
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    },
    "accountRef" : {
      "kind" : "Analytics account reference.",
      "name" : "Account name.",
      "href" : "Link for this account.",
      "id" : "Account ID."
    },
    "profileRef" : {
      "accountId" : "Account ID to which this view (profile) belongs.",
      "kind" : "Analytics view (profile) reference.",
      "name" : "Name of this view (profile).",
      "href" : "Link for this view (profile).",
      "id" : "View (Profile) ID.",
      "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
      "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
    }
  },
  "selfLink" : "Self link for this resource."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_remarketing_audience

Updates an existing remarketing audience.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### remarketingAudienceId (required)

The ID of the remarketing audience.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics remarketing audience.

**Type:** object

```json
{
  "created" : "Time this remarketing audience was created.",
  "kind" : "Collection type.",
  "description" : "The description of this remarketing audience.",
  "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this remarketing audience belongs.",
  "audienceDefinition" : {
    "includeConditions" : {
      "daysToLookBack" : "The look-back window lets you specify a time frame for evaluating the behavior that qualifies users for your audience. For example, if your filters include users from Central Asia, and Transactions Greater than 2, and you set the look-back window to 14 days, then any user from Central Asia whose cumulative transactions exceed 2 during the last 14 days is added to the audience.",
      "kind" : "Resource type for include conditions.",
      "segment" : "The segment condition that will cause a user to be added to an audience.",
      "membershipDurationDays" : "Number of days (in the range 1 to 540) a user remains in the audience.",
      "isSmartList" : "Boolean indicating whether this segment is a smart list. https://support.google.com/analytics/answer/4628577"
    }
  },
  "stateBasedAudienceDefinition" : {
    "excludeConditions" : {
      "segment" : "The segment condition that will cause a user to be removed from an audience.",
      "exclusionDuration" : "Whether to make the exclusion TEMPORARY or PERMANENT."
    },
    "includeConditions" : {
      "daysToLookBack" : "The look-back window lets you specify a time frame for evaluating the behavior that qualifies users for your audience. For example, if your filters include users from Central Asia, and Transactions Greater than 2, and you set the look-back window to 14 days, then any user from Central Asia whose cumulative transactions exceed 2 during the last 14 days is added to the audience.",
      "kind" : "Resource type for include conditions.",
      "segment" : "The segment condition that will cause a user to be added to an audience.",
      "membershipDurationDays" : "Number of days (in the range 1 to 540) a user remains in the audience.",
      "isSmartList" : "Boolean indicating whether this segment is a smart list. https://support.google.com/analytics/answer/4628577"
    }
  },
  "accountId" : "Account ID to which this remarketing audience belongs.",
  "linkedViews" : [ "string" ],
  "name" : "The name of this remarketing audience.",
  "id" : "Remarketing Audience ID.",
  "audienceType" : "The type of audience, either SIMPLE or STATE_BASED.",
  "updated" : "Time this remarketing audience was last modified.",
  "internalWebPropertyId" : "Internal ID for the web property to which this remarketing audience belongs.",
  "linkedAdAccounts" : [ {
    "accountId" : "Account ID to which this linked foreign account belongs.",
    "eligibleForSearch" : "Boolean indicating whether this is eligible for search.",
    "remarketingAudienceId" : "Remarketing audience ID to which this linked foreign account belongs.",
    "linkedAccountId" : "The foreign account ID. For example the an Google Ads `linkedAccountId` has the following format XXX-XXX-XXXX.",
    "kind" : "Resource type for linked foreign account.",
    "id" : "Entity ad account link ID.",
    "type" : "The type of the foreign account. For example, `ADWORDS_LINKS`, `DBM_LINKS`, `MCC_LINKS` or `OPTIMIZE`.",
    "internalWebPropertyId" : "Internal ID for the web property to which this linked foreign account belongs.",
    "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this linked foreign account belongs.",
    "status" : "The status of this foreign account link."
  } ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_web_property

Updates an existing web property.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics web property.

**Type:** object

```json
{
  "profileCount" : "View (Profile) count for this web property.",
  "dataRetentionResetOnNewActivity" : "Set to true to reset the retention period of the user identifier with each new event from that user (thus setting the expiration date to current time plus retention period).\nSet to false to delete data associated with the user identifer automatically after the rentention period.\nThis property cannot be set on insert.",
  "parentLink" : {
    "href" : "Link to the account for this web property.",
    "type" : "Type of the parent link. Its value is \"analytics#account\"."
  },
  "dataRetentionTtl" : "The length of time for which user and event data is retained.\nThis property cannot be set on insert.",
  "defaultProfileId" : "Default view (profile) ID.",
  "level" : "Level for this web property. Possible values are STANDARD or PREMIUM.",
  "childLink" : {
    "href" : "Link to the list of views (profiles) for this web property.",
    "type" : "Type of the parent link. Its value is \"analytics#profiles\"."
  },
  "created" : "Time this web property was created.",
  "industryVertical" : "The industry vertical/category selected for this web property.",
  "kind" : "Resource type for Analytics WebProperty.",
  "selfLink" : "Link for this web property.",
  "accountId" : "Account ID to which this web property belongs.",
  "starred" : "Indicates whether this web property is starred or not.",
  "websiteUrl" : "Website url for this web property.",
  "permissions" : {
    "effective" : [ "string" ]
  },
  "name" : "Name of this web property.",
  "id" : "Web property ID of the form UA-XXXXX-YY.",
  "updated" : "Time this web property was last modified.",
  "internalWebPropertyId" : "Internal ID for this web property."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_web_property_adwords_link

Updates an existing webProperty-Google Ads link.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### webPropertyAdWordsLinkId (required)

Web property Google Ads link ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for Analytics Entity Google Ads Link.

**Type:** object

```json
{
  "kind" : "Resource type for entity Google Ads link.",
  "name" : "Name of the link. This field is required when creating a Google Ads link.",
  "profileIds" : [ "string" ],
  "id" : "Entity Google Ads link ID",
  "adWordsAccounts" : [ {
    "kind" : "Resource type for Google Ads account.",
    "customerId" : "Customer ID. This field is required when creating a Google Ads link.",
    "autoTaggingEnabled" : "True if auto-tagging is enabled on the Google Ads account. Read-only after the insert operation."
  } ],
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    }
  },
  "selfLink" : "URL link for this Google Analytics - Google Ads link."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_web_property_user_link

Updates permissions for an existing user on the given web property.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### linkId (required)

Link ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### $body

JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

**Type:** object

```json
{
  "userRef" : {
    "kind" : "string",
    "id" : "User ID.",
    "email" : "Email ID of this user."
  },
  "kind" : "Resource type for entity user link.",
  "permissions" : {
    "effective" : [ "string" ],
    "local" : [ "string" ]
  },
  "id" : "Entity user link ID",
  "entity" : {
    "webPropertyRef" : {
      "accountId" : "Account ID to which this web property belongs.",
      "kind" : "Analytics web property reference.",
      "name" : "Name of this web property.",
      "href" : "Link for this web property.",
      "id" : "Web property ID of the form UA-XXXXX-YY.",
      "internalWebPropertyId" : "Internal ID for this web property."
    },
    "accountRef" : {
      "kind" : "Analytics account reference.",
      "name" : "Account name.",
      "href" : "Link for this account.",
      "id" : "Account ID."
    },
    "profileRef" : {
      "accountId" : "Account ID to which this view (profile) belongs.",
      "kind" : "Analytics view (profile) reference.",
      "name" : "Name of this view (profile).",
      "href" : "Link for this view (profile).",
      "id" : "View (Profile) ID.",
      "internalWebPropertyId" : "Internal ID for the web property to which this view (profile) belongs.",
      "webPropertyId" : "Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs."
    }
  },
  "selfLink" : "Self link for this resource."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## upload_custom_data_source

Upload data for a custom data source.

<details><summary>Parameters</summary>

### accountId (required)

Account ID. If possible, can either be a specific account ID or '~all', which refers to all the accounts that user has access to.

**Type:** string

### customDataSourceId (required)

Custom data source ID.

**Type:** string

### webPropertyId (required)

ID to retrieve the web property for. If possible, can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

