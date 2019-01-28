---

id: yelp_documentation

title: Yelp

version: v1.*.*

---

## get_autocomplete

This endpoint returns autocomplete suggestions for search keywords, businesses and categories, based on the input text.

<details><summary>Parameters</summary>

#### text (required)

Text to return autocomplete suggestions for.

**Type:** string

#### latitude

Required if location is not provided. Latitude of the location you want to search nearby.

**Type:** number

#### locale

List of supported locales https://www.yelp.com/developers/documentation/v3/supported_locales. Defaults to en_US.

**Type:** string

#### longitude

Required if location is not provided. Longitude of the location you want to search nearby.

**Type:** number

</details>

## get_business

This endpoint returns detailed business content. Normally, you would get the Business ID from /businesses/search, /businesses/search/phone, /transactions/{transaction_type}/search or /autocomplete. To retrieve review excerpts for a business, please refer to our Reviews endpoint (/businesses/{id}/reviews) Note: at this time, the API does not return businesses without any reviews.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### locale

List of supported locales https://www.yelp.com/developers/documentation/v3/supported_locales. Defaults to en_US.

**Type:** string

</details>

## get_business_reviews

This endpoint returns up to three review excerpts for a given business ordered by Yelp's default sort order. Note: at this time, the API does not return businesses without any reviews.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### locale

List of supported locales https://www.yelp.com/developers/documentation/v3/supported_locales. Defaults to en_US.

**Type:** string

</details>

## get_businesses_matches

This endpoint lets you match business data from other sources against businesses on Yelp, based on provided business information. For example, if you know a business's exact address and name, and you want to find that business and only that business on Yelp.

<details><summary>Parameters</summary>

#### address1 (required)

The first line of the business’s address. Maximum length is 64; only digits, letters, spaces, and ­’/#&,.: are allowed. The empty string '' is allowed; this will specifically match certain service businesses that have no street address.

**Type:** string

#### city (required)

The city of the business. Maximum length is 64; only digits, letters, spaces, and ­’.() are allowed.

**Type:** string

#### country (required)

The ISO 3166-1 alpha-2 country code of this business. Maximum length is 2.

**Type:** string

#### name (required)

The name of the business. Maximum length is 64; only digits, letters, spaces, and !#$%&+,­./:?@'are allowed.

**Type:** string

#### state (required)

The ISO 3166-2 (with a few exceptions) state code of this business. Maximum length is 3.

**Type:** string

#### address2

The second line of the business’s address. Maximum length is 64; only digits, letters, spaces, and ­’/#&,.: are allowed

**Type:** string

#### address3

The third line of the business’s address. Maximum length is 64; only digits, letters, spaces, and ­’/#&,.: are allowed

**Type:** string

#### latitude

Required if location is not provided. Latitude of the location you want to search nearby.

**Type:** number

#### limit

Maximum number of business results to return. By default, it will return 3. Maximum is 10.

**Type:** integer

#### longitude

Required if location is not provided. Longitude of the location you want to search nearby.

**Type:** number

#### match_threshold

Specifies whether a match quality threshold should be applied to the matched businesses. Must be either 'default' or 'none'. default: Apply a match quality threshold such that only very closely matching businesses will be returned. none: Do not apply any match quality threshold; all potential business matches will be returned. If this param is not included in a request, 'default' will be used.

**Type:** string

#### phone

The phone number of the business which can be submitted as (a) locally ­formatted with digits only (e.g., 016703080) or (b) internationally­ formatted with a leading + sign and digits only after (+35316703080). Maximum length is 32.

**Type:** string

#### yelp_business_id

Unique Yelp identifier of the business if available. Used as a hint when finding a matching business.

**Type:** string

#### zip_code

The Zip code of this business.

**Type:** string

</details>

## get_businesses_search

This endpoint returns up to 1000 businesses based on the provided search criteria. It has some basic information about the business. To get detailed information and reviews, please use the Business ID returned here and refer to /businesses/{id} and /businesses/{id}/reviews endpoints. Note: at this time, the API does not return businesses without any reviews.

<details><summary>Parameters</summary>

#### attributes

Try these additional filters to return specific search results! hot_and_new - popular businesses which recently joined Yelp. request_a_quote - businesses which actively reply to Request a Quote inquiries. reservation - businesses with Yelp Reservations bookings enabled on their profile page. waitlist_reservation - businesses with Yelp Waitlist bookings enabled on their profile screen (iOS/Android). cashback - businesses offering Yelp Cash Back to in-house customers. deals - businesses offering Yelp Deals on their profile page. gender_neutral_restrooms - businesses which provide gender neutral restrooms. You can combine multiple attributes by providing a comma separated like "attribute1,attribute2". If multiple attributes are used, only businesses that satisfy ALL attributes will be returned in search results. For example, the attributes "hot_and_new,cashback" will return businesses that are Hot and New AND offer Cash Back.

**Type:** string

#### categories

Categories to filter the search results with. https://www.yelp.com/developers/documentation/v3/all_category_list The category filter can be a list of comma delimited categories. For example, "bars,french" will filter by Bars OR French. The category identifier should be used (for example "discgolf", not "Disc Golf").

**Type:** string

#### latitude

Required if location is not provided. Latitude of the location you want to search nearby.

**Type:** number

#### locale

List of supported locales https://www.yelp.com/developers/documentation/v3/supported_locales. Defaults to en_US.

**Type:** string

#### location

Required if either latitude or longitude is not provided. Specifies the combination of "address, neighborhood, city, state or zip, optional country" to be used when searching for businesses.

**Type:** string

#### longitude

Required if location is not provided. Longitude of the location you want to search nearby.

**Type:** number

#### open_at

An integer represending the Unix time in the same timezone of the search location. If specified, it will return business open at the given time. Notice that open_at and open_now cannot be used together.

**Type:** integer

#### open_now

Default to false. When set to true, only return the businesses open now. Notice that open_at and open_now cannot be used together.

**Type:** boolean

#### price

Pricing levels to filter the search result with: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$. The price filter can be a list of comma delimited pricing levels. For example, "1, 2, 3" will filter the results to show the ones that are $, $$, or $$$.

**Type:** string

#### radius

Search radius in meters. If the value is too large, a AREA_TOO_LARGE error may be returned. The max value is 40000 meters (about 25 miles).

**Type:** number

#### sort_by

Sort the results by one of the these modes: best_match, rating, review_count or distance. By default it's best_match. The rating sort is not strictly sorted by the rating value, but by an adjusted rating value that takes into account the number of ratings, similar to a bayesian average. This is so a business with 1 rating of 5 stars doesn’t immediately jump to the top.

**Type:** string

#### term

Search term (e.g. "food", "restaurants"). If term isn’t included we search everything. The term keyword also accepts business names such as "Starbucks".

**Type:** string

</details>

## get_businesses_search_phone

This endpoint returns a list of businesses based on the provided phone number. It is possible for more than one business to have the same phone number (for example, chain stores with the same +1 800 phone number). Note: at this time, the API does not return businesses without any reviews.

<details><summary>Parameters</summary>

#### phone (required)

Phone number of the business you want to search for. It must start with + and include the country code, like +14159083801.

**Type:** number

</details>

## get_transactions_search

This endpoint returns a list of businesses which support food delivery transactions. Note: at this time, the API does not return businesses without any reviews.

<details><summary>Parameters</summary>

#### latitude

Required if location is not provided. Latitude of the location you want to search nearby.

**Type:** number

#### location

Required if either latitude or longitude is not provided. Specifies the combination of "address, neighborhood, city, state or zip, optional country" to be used when searching for businesses.

**Type:** string

#### longitude

Required if location is not provided. Longitude of the location you want to search nearby.

**Type:** number

</details>

