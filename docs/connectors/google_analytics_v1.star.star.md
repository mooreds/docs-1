---

id: google_analytics_documentation

title: Google Analytics

version: v1.*.*

---

## get_account_summaries



*This operation has no parameters*

## get_data



<details><summary>Parameters</summary>

#### end-date (required)

End date for fetching Analytics data. Request can specify an end date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or NdaysAgo where N is a positive integer). 

**Type:** string

#### ids (required)

The unique table ID of the form ga:XXXX, where XXXX is the Analytics view (profile) ID for which the query will retrieve the data. 

**Type:** string

#### metrics (required)

A list of comma-separated metrics, such as ga:sessions,ga:bounces. 

**Type:** string

#### start-date (required)

Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or NdaysAgo where N is a positive integer). 

**Type:** string

#### access_token

One possible way to provide an OAuth 2.0 token.

**Type:** string

#### callback

Name of the JavaScript callback function that handles the response. Used in JavaScript JSON-P requests.

**Type:** string

#### dimensions

A list of comma-separated dimensions for your Analytics data, such as ga:browser,ga:city. 

**Type:** string

#### fields

Selector specifying a subset of fields to include in the response. 

**Type:** string

#### filters

Dimension or metric filters that restrict the data returned for your request. 

**Type:** string

#### include-empty-rows

Defaults to true; if set to false, rows where all metric values are zero will be omitted from the response. 

**Type:** boolean

#### key

Used for OAuth 1.0a authorization to specify your application to get quota. For example: key=AldefliuhSFADSfasdfasdfASdf.

**Type:** string

#### output

The desired output type for the Analytics data returned in the response. Acceptable values are json and dataTable. Default: json. 

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks. Default false. 

**Type:** string

#### quotaUser

Alternative to userIp in cases when the user's IP address is unknown.

**Type:** string

#### samplingLevel

The desired sampling level. Allowed Values:  DEFAULT â Returns response with a sample size that balances speed and accuracy. FASTER â Returns a fast response with a smaller sample size. HIGHER_PRECISION â Returns a more accurate response using a large sample size, but this may result in the response being slower.  

**Type:** string

#### segment

Segments the data returned for your request. 

**Type:** string

#### sort

A list of comma-separated dimensions and metrics indicating the sorting order and sorting direction for the returned data. 

**Type:** string

#### userIp

Specifies IP address of the end user for whom the API call is being made. Used to cap usage per IP. 

**Type:** string

</details>

