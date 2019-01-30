---
id: opencage-documentation
title: OpenCage Geocoder (version v1.*.*)
sidebar_label: OpenCage Geocoder
---

geocoding api

## geocode

geocode a query

<details><summary>Parameters</summary>

#### format (required)

format of the response. One of 'json', 'xml' or 'map'. Note that only JSON is supported right now.

**Type:** string

**Potential values:** json

#### q (required)

string or lat,lng to be geocoded.

**Type:** string

#### abbrv

when true we attempt to abbreviate the formatted field in the response.

**Type:** boolean

#### add_request

if true the request is included in the response.

**Type:** boolean

#### bounds

four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat).

**Type:** string

#### countrycode

two letter code ISO 3166-1 Alpha 2 code to limit results to that country.

**Type:** string

#### language

an IETF format language code (ex: 'es' or 'pt-BR').

**Type:** string

#### limit

maximum number of results to return. Default is 10. Maximum is 100.

**Type:** integer

#### min_confidence

integer from 1-10. Only results with at least this confidence are returned.

**Type:** integer

#### no_annotations

when true annotations are not added to results.

**Type:** boolean

#### no_dedupe

when true results are not deduplicated.

**Type:** boolean

#### no_record

when true query content is not logged.

**Type:** boolean

</details>

