---
id: google-maps-documentation
title: Google Maps (version v1.*.*)
sidebar_label: Google Maps
layout: docs.mustache
---

## find_place



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### fields

a comma-separated list of place data types to return. Use a forward slash when specifying compound values.

**Type:** string

#### input

The text input specifying which place to search for (for example, a name, address, or phone number).

**Type:** string

#### inputtype

The type of input.

**Type:** string

**Potential values:** textquery, phonenumber

#### language

The language in which to return results.

**Type:** string

#### locationbias

Prefer results in a specified area, by specifying either a radius plus lat/lng, or two lat/lng pairs representing the points of a rectangle. If this parameter is not specified, the API uses IP address biasing by default. 
- A single lat/lng coordinate. Use the following format: point:lat,lng. 
- A string specifying radius in meters, plus lat/lng in decimal degrees. Use the following format: circle:radius@lat,lng. 
- A string specifying two lat/lng pairs in decimal degrees, representing the south/west and north/east points of a rectangle. Use the following format: rectangle:south,west|north,east. Note that east/west values are wrapped to the range -180, 180, and north/south values are clamped to the range -90, 90.

**Type:** string

</details>

## geocode



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### address

The street address that you want to geocode, in the format used by the national postal service of the country concerned. Additional address elements such as business names and unit, suite or floor numbers should be avoided.

**Type:** string

#### bounds

the viewport bounding box of the overview_polyline.

**Type:** object

#### components

A components filter with elements separated by a pipe (|). Each element in the components filter consists of a component:value pair, and fully restricts the results from the geocoder.

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### latlng

The latitude and longitude values specifying the location for which you wish to obtain the closest, human-readable address.

**Type:** object

#### location_type

A filter of one or more location types, separated by a pipe (|). If the parameter contains multiple location types, the API returns all addresses that match any of the types. A note about processing: The location_type parameter does not restrict the search to the specified location type(s). Rather, the location_type acts as a post-search filter: the API fetches all results for the specified latlng, then discards those results that do not match the specified location type(s).

**Type:** array

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### result_type

A filter of one or more address types, separated by a pipe (|). If the parameter contains multiple address types, the API returns all addresses that match any of the types. A note about processing: The result_type parameter does not restrict the search to the specified address type(s). Rather, the result_type acts as a post-search filter: the API fetches all results for the specified latlng, then discards those results that do not match the specified address type(s).

**Type:** array

</details>

## get_directions



<details><summary>Parameters</summary>

#### destination (required)

The starting point for calculating travel distance and time. You can supply the location in the form of an address, latitude/longitude coordinates, or a place ID.

**Type:** string

#### origin (required)

The starting point for calculating travel distance and time. You can supply the location in the form of an address, latitude/longitude coordinates, or a place ID.

**Type:** string

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### alternatives

If set to true, specifies that the Directions service may provide more than one route alternative in the response. Note that providing route alternatives may increase the response time from the server. This is only available for requests without intermediate waypoints.

**Type:** boolean

#### arrival_time

Specifies the desired time of arrival for transit requests, in seconds since midnight, January 1, 1970 UTC.

**Type:** integer

#### avoid

Introduces restrictions to the route.

**Type:** string

**Potential values:** tolls, highways, ferries, indoor

#### departure_time

The desired time of departure.

**Type:** integer

#### language

The language in which to return results.

**Type:** string

#### mode

Travel mode. Defaults to driving.

**Type:** string

**Potential values:** driving, walking, bicycling, transit

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### traffic_model

Specifies the assumptions to use when calculating time in traffic. This setting affects the value returned in the duration_in_traffic field in the response, which contains the predicted time in traffic based on historical averages. The traffic_model parameter may only be specified for requests where the travel mode is driving, and where the request includes a departure_time, and only if the request includes an API key or a Google Maps APIs Premium Plan client ID.

**Type:** string

**Potential values:** best_guess, optimistic, pessimistic

#### transit_mode

Specifies one or more preferred modes of transit. This parameter may only be specified for requests where the mode is transit.

**Type:** string

**Potential values:** bus, subway, train, tram, rail

#### transit_routing_preference

Specifies preferences for transit requests. Using this parameter, you can bias the options returned, rather than accepting the default best route chosen by the API. This parameter may only be specified for requests where the mode is transit.

**Type:** string

**Potential values:** less_walking, fewer_transfers

#### units

Specifies the unit system to use when expressing distance as text.

**Type:** string

**Potential values:** metric, imperial

#### waypoints

Specifies an array of intermediate locations to include along the route between the origin and destination points as pass through or stopover locations. Waypoints alter a route by directing it through the specified location(s). The API supports waypoints for driving, walking and bicycling; not transit. You can specify waypoints as either latitude/longitude coordinates, place ID, address, or encoded polyline.

**Type:** string

</details>

## get_distance_matrix



<details><summary>Parameters</summary>

#### destinations (required)

One or more locations to use as the finishing point for calculating travel distance and time. You can supply one or more locations separated by the pipe character (|), in the form of an address, latitude/longitude coordinates, or a place ID.

**Type:** string

#### origins (required)

The starting point for calculating travel distance and time. You can supply one or more locations separated by the pipe character (|), in the form of an address, latitude/longitude coordinates, or a place ID.

**Type:** string

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### arrival_time

Specifies the desired time of arrival for transit requests, in seconds since midnight, January 1, 1970 UTC.

**Type:** integer

#### avoid

Introduces restrictions to the route.

**Type:** string

**Potential values:** tolls, highways, ferries, indoor

#### departure_time

The desired time of departure.

**Type:** integer

#### language

The language in which to return results.

**Type:** string

#### mode

Travel mode. Defaults to driving.

**Type:** string

**Potential values:** driving, walking, bicycling, transit

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### traffic_model

Specifies the assumptions to use when calculating time in traffic. This setting affects the value returned in the duration_in_traffic field in the response, which contains the predicted time in traffic based on historical averages. The traffic_model parameter may only be specified for requests where the travel mode is driving, and where the request includes a departure_time, and only if the request includes an API key or a Google Maps APIs Premium Plan client ID.

**Type:** string

**Potential values:** best_guess, optimistic, pessimistic

#### transit_mode

Specifies one or more preferred modes of transit. This parameter may only be specified for requests where the mode is transit.

**Type:** string

**Potential values:** bus, subway, train, tram, rail

#### transit_routing_preference

Specifies preferences for transit requests. Using this parameter, you can bias the options returned, rather than accepting the default best route chosen by the API. This parameter may only be specified for requests where the mode is transit.

**Type:** string

**Potential values:** less_walking, fewer_transfers

#### units

Specifies the unit system to use when expressing distance as text.

**Type:** string

**Potential values:** metric, imperial

</details>

## get_elevation



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### locations

Either a single coordinate: locations=40.714728,-73.998672, an array of coordinates separated using the pipe ('|') character: locations=40.714728,-73.998672|-34.397,150.644, or a set of encoded coordinates using the Encoded Polyline Algorithm: locations=enc:gfo}EtohhU

**Type:** string

#### path

Either an array of coordinates separated using the pipe ('|') character: locations=40.714728,-73.998672|-34.397,150.644, or a set of encoded coordinates using the Encoded Polyline Algorithm: locations=enc:gfo}EtohhU

**Type:** string

#### samples

specifies the number of sample points along a path for which to return elevation data. The samples parameter divides the given path into an ordered set of equidistant points along the path.

**Type:** integer

</details>

## get_place_details



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### fields

a comma-separated list of place data types to return. Use a forward slash when specifying compound values.

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### place_id

a unique identifier that can be used with other Google APIs.

**Type:** string

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### sessiontoken

**Type:** string

</details>

## get_place_photo



<details><summary>Parameters</summary>

#### maxheight

Maximum height in pixels

**Type:** integer

#### maxwidth

Maximum width in pixels

**Type:** integer

#### photoreference

A string identifier that uniquely identifies a photo.

**Type:** string

</details>

## get_static_map



<details><summary>Parameters</summary>

#### center

defines the center of the map, equidistant from all edges of the map. This parameter takes a location as either a comma-separated {latitude,longitude} pair (e.g. "40.714728,-73.998672") or a string address (e.g. "city hall, new york, ny") identifying a unique location on the face of the earth.

**Type:** string

#### format

defines the format of the resulting image. By default, the Maps Static API creates PNG images. There are several possible formats including GIF, JPEG and PNG types. Which format you use depends on how you intend to present the image. JPEG typically provides greater compression, while GIF and PNG provide greater detail.

**Type:** string

**Potential values:** png, png8, png32, gif, jpg, jpg-baseline

#### language

The language in which to return results.

**Type:** string

#### maptype

defines the type of map to construct.

**Type:** string

**Potential values:** roadmap, satellite, terrain, hybrid

#### markers

defines a set of one or more markers (map pins) at a set of locations. Each marker defined within a single markers declaration must exhibit the same visual style; if you wish to display markers with different styles, you will need to supply multiple markers parameters with separate style information.

**Type:** array

#### path

Either an array of coordinates separated using the pipe ('|') character: locations=40.714728,-73.998672|-34.397,150.644, or a set of encoded coordinates using the Encoded Polyline Algorithm: locations=enc:gfo}EtohhU

**Type:** string

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### scale

affects the number of pixels that are returned. scale=2 returns twice as many pixels as scale=1 while retaining the same coverage area and level of detail (i.e. the contents of the map don't change). This is useful when developing for high-resolution displays, or when generating a map for printing. The default value is 1. Accepted values are 2 and 4 (4 is only available to Google Maps APIs Premium Plan customers.)

**Type:** integer

#### signature

a digital signature used to verify that any site generating requests using your API key is authorized to do so.

**Type:** string

#### size

defines the rectangular dimensions of the map image. This parameter takes a string of the form {horizontal_value}x{vertical_value}. For example, 500x400 defines a map 500 pixels wide by 400 pixels high. Maps smaller than 180 pixels in width will display a reduced-size Google logo. This parameter is affected by the scale parameter, described below; the final output size is the product of the size and scale values.

**Type:** string

#### visible

specifies one or more locations that should remain visible on the map, though no markers or other indicators will be displayed. Use this parameter to ensure that certain features or map locations are shown on the Maps Static API.

**Type:** array

#### zoom

defines the zoom level of the map, which determines the magnification level of the map. This parameter takes a numerical value corresponding to the zoom level of the region desired.

**Type:** integer

</details>

## get_street_view



<details><summary>Parameters</summary>

#### fov

determines the horizontal field of view of the image. The field of view is expressed in degrees, with a maximum allowed value of 120. When dealing with a fixed-size viewport, as with a Street View image of a set size, field of view in essence represents zoom, with smaller numbers indicating a higher level of zoom.

**Type:** number

#### heading

indicates the compass heading of the camera. Accepted values are from 0 to 360 (both values indicating North, with 90 indicating East, and 180 South). If no heading is specified, a value will be calculated that directs the camera towards the specified location, from the point at which the closest photograph was taken.

**Type:** number

#### location

either a text string (such as Chagrin Falls, OH) or a lat/lng value (40.457375,-80.009353).

**Type:** string

#### pano

a specific panorama ID. These are generally stable.

**Type:** string

#### pitch

specifies the up or down angle of the camera relative to the Street View vehicle. This is often, but not always, flat horizontal. Positive values angle the camera up (with 90 degrees indicating straight up); negative values angle the camera down (with -90 indicating straight down).

**Type:** number

#### radius

a radius, specified in meters, in which to search for a panorama, centered on the given latitude and longitude. Valid values are non-negative integers.

**Type:** number

#### signature

a digital signature used to verify that any site generating requests using your API key is authorized to do so.

**Type:** string

#### size

defines the rectangular dimensions of the map image. This parameter takes a string of the form {horizontal_value}x{vertical_value}. For example, 500x400 defines a map 500 pixels wide by 400 pixels high. Maps smaller than 180 pixels in width will display a reduced-size Google logo. This parameter is affected by the scale parameter, described below; the final output size is the product of the size and scale values.

**Type:** string

#### source

limits Street View searches to selected sources.

**Type:** string

**Potential values:** default, outdoor

</details>

## get_timezone



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### language

The language in which to return results.

**Type:** string

#### location

a comma-separated lat,lng tuple (eg. location=-33.86,151.20), representing the location to look up.

**Type:** string

#### timestamp

the desired time as seconds since midnight, January 1, 1970 UTC. The Time Zone API uses the timestamp to determine whether or not Daylight Savings should be applied, based on the time zone of the location. Note that the API does not take historical time zones into account. That is, if you specify a past timestamp, the API does not take into account the possibility that the location was previously in a different time zone.

**Type:** number

</details>

## place_autocomplete



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### components

A components filter with elements separated by a pipe (|). Each element in the components filter consists of a component:value pair, and fully restricts the results from the geocoder. Currently, you can use components to filter by up to 5 countries. Countries must be passed as a two character, ISO 3166-1 Alpha-2 compatible country code. For example: components=country:fr would restrict your results to places within France.

**Type:** string

#### input

The text input specifying which place to search for (for example, a name, address, or phone number).

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### location

a comma-separated lat,lng tuple (eg. location=-33.86,151.20), representing the location to look up.

**Type:** string

#### offset

The position, in the input term, of the last character that the service uses to match predictions. For example, if the input is 'Google' and the offset is 3, the service will match on 'Goo'. The string determined by the offset is matched against the first word in the input term only. For example, if the input term is 'Google abc' and the offset is 3, the service will attempt to match against 'Goo abc'. If no offset is supplied, the service will use the whole term. The offset should generally be set to the position of the text caret.

**Type:** integer

#### sessiontoken

**Type:** string

#### strictbounds

Returns only those places that are strictly within the region defined by location and radius. This is a restriction, rather than a bias, meaning that results outside this region will not be returned even if they match the user input.

**Type:** boolean

#### types

The types of place results to return. If no type is specified, all types will be returned.

**Type:** string

**Potential values:** geocode, address, establishment, (regions), (cities)

</details>

## query_autocomplete



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### input

The text input specifying which place to search for (for example, a name, address, or phone number).

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### location

a comma-separated lat,lng tuple (eg. location=-33.86,151.20), representing the location to look up.

**Type:** string

#### offset

The position, in the input term, of the last character that the service uses to match predictions. For example, if the input is 'Google' and the offset is 3, the service will match on 'Goo'. The string determined by the offset is matched against the first word in the input term only. For example, if the input term is 'Google abc' and the offset is 3, the service will attempt to match against 'Goo abc'. If no offset is supplied, the service will use the whole term. The offset should generally be set to the position of the text caret.

**Type:** integer

#### radius

the distance (in meters) within which to return place results.

**Type:** number

</details>

## reverse_geocode



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### address

The street address that you want to geocode, in the format used by the national postal service of the country concerned. Additional address elements such as business names and unit, suite or floor numbers should be avoided.

**Type:** string

#### bounds

the viewport bounding box of the overview_polyline.

**Type:** object

#### components

A components filter with elements separated by a pipe (|). Each element in the components filter consists of a component:value pair, and fully restricts the results from the geocoder.

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### latlng

The latitude and longitude values specifying the location for which you wish to obtain the closest, human-readable address.

**Type:** object

#### location_type

A filter of one or more location types, separated by a pipe (|). If the parameter contains multiple location types, the API returns all addresses that match any of the types. A note about processing: The location_type parameter does not restrict the search to the specified location type(s). Rather, the location_type acts as a post-search filter: the API fetches all results for the specified latlng, then discards those results that do not match the specified location type(s).

**Type:** array

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### result_type

A filter of one or more address types, separated by a pipe (|). If the parameter contains multiple address types, the API returns all addresses that match any of the types. A note about processing: The result_type parameter does not restrict the search to the specified address type(s). Rather, the result_type acts as a post-search filter: the API fetches all results for the specified latlng, then discards those results that do not match the specified address type(s).

**Type:** array

</details>

## search_nearby



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### keyword

A term to be matched against all content that Google has indexed for this place, including but not limited to name, type, and address, as well as customer reviews and other third-party content.

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### location

a comma-separated lat,lng tuple (eg. location=-33.86,151.20), representing the location to look up.

**Type:** string

#### maxprice

The price level of the place, on a scale of 0 to 4. The exact amount indicated by a specific value will vary from region to region.

**Type:** integer

#### minprice

The price level of the place, on a scale of 0 to 4. The exact amount indicated by a specific value will vary from region to region.

**Type:** integer

#### name

**Type:** string

#### opennow

**Type:** boolean

#### radius

the distance (in meters) within which to return place results.

**Type:** number

#### rankby

the order in which results are listed. Note that rankby must not be included if radius is specified.

**Type:** string

**Potential values:** prominence, distance

#### type

the address type of the geocoding result used for calculating directions.

**Type:** string

**Potential values:** street_address, route, intersection, political, country, administrative_area_level_1, administrative_area_level_2, administrative_area_level_3, administrative_area_level_4, administrative_area_level_5, colloquial_area, locality, sublocality, sublocality_level_1, sublocality_level_2, sublocality_level_3, sublocality_level_4, sublocality_level_5, neighborhood, premise, subpremise, postal_code, natural_feature, airport, park, point_of_interest, floor, establishment, parking, post_box, postal_town, room, street_number, bus_station, train_station, transit_station, geocode

</details>

## text_search



<details><summary>Parameters</summary>

#### outputFormat (required)

Desired output format.

**Type:** string

**Potential values:** json, xml

#### language

The language in which to return results.

**Type:** string

#### location

a comma-separated lat,lng tuple (eg. location=-33.86,151.20), representing the location to look up.

**Type:** string

#### maxprice

The price level of the place, on a scale of 0 to 4. The exact amount indicated by a specific value will vary from region to region.

**Type:** integer

#### minprice

The price level of the place, on a scale of 0 to 4. The exact amount indicated by a specific value will vary from region to region.

**Type:** integer

#### opennow

**Type:** boolean

#### query

The text string on which to search, for example: "restaurant" or "123 Main Street". The Google Places service will return candidate matches based on this string and order the results based on their perceived relevance.

**Type:** string

#### radius

the distance (in meters) within which to return place results.

**Type:** number

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### type

the address type of the geocoding result used for calculating directions.

**Type:** string

**Potential values:** street_address, route, intersection, political, country, administrative_area_level_1, administrative_area_level_2, administrative_area_level_3, administrative_area_level_4, administrative_area_level_5, colloquial_area, locality, sublocality, sublocality_level_1, sublocality_level_2, sublocality_level_3, sublocality_level_4, sublocality_level_5, neighborhood, premise, subpremise, postal_code, natural_feature, airport, park, point_of_interest, floor, establishment, parking, post_box, postal_town, room, street_number, bus_station, train_station, transit_station, geocode

</details>

