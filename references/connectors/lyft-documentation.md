---
id: lyft-documentation
title: Lyft (version v1.*.*)
sidebar_label: Lyft
layout: docs.mustache
---

## cancel_ride

Cancel a ongoing ride which was requested earlier by providing the ride id.


<details><summary>Parameters</summary>

#### id (required)

The ID of the ride

**Type:** string

#### $body

**Type:** object

</details>

## get_cost

Estimate the cost of taking a Lyft between two points.


<details><summary>Parameters</summary>

#### start_lat (required)

Latitude of the starting location

**Type:** number

#### start_lng (required)

Longitude of the starting location

**Type:** number

#### end_lat

Latitude of the ending location

**Type:** number

#### end_lng

Longitude of the ending location

**Type:** number

#### ride_type

ID of a ride type

**Type:** string

**Potential values:** lyft, lyft_line, lyft_plus, lyft_premier, lyft_lux, lyft_luxsuv

</details>

## get_eta

The ETA endpoint lets you know how quickly a Lyft driver can come get you


<details><summary>Parameters</summary>

#### lat (required)

Latitude of a location

**Type:** number

#### lng (required)

Longitude of a location

**Type:** number

#### destination_lat

Latitude of destination location

**Type:** number

#### destination_lng

Longitude of destination location

**Type:** number

#### ride_type

ID of a ride type

**Type:** string

**Potential values:** lyft, lyft_line, lyft_plus, lyft_premier, lyft_lux, lyft_luxsuv

</details>

## get_my_profile



*This operation has no parameters*

## get_my_rides

Get a list of past &amp; current rides for this passenger.


<details><summary>Parameters</summary>

#### start_time (required)

Restrict to rides starting after this point in time. The earliest supported date is 2015-01-01T00:00:00+00:00


**Type:** date-time

#### end_time

Restrict to rides starting before this point in time. The earliest supported date is 2015-01-01T00:00:00+00:00


**Type:** date-time

#### limit

The maximum number of rides to return. The default limit is 10 if not specified. The maximum allowed value is 50, an integer greater that 50 will return at most 50 results.


**Type:** integer

</details>

## get_nearby_drivers

The drivers endpoint returns a list of nearby drivers' lat and lng at a given location.


<details><summary>Parameters</summary>

#### lat (required)

Latitude of a location

**Type:** number

#### lng (required)

Longitude of a location

**Type:** number

</details>

## get_ride_information

Get the status of a ride along with information about the driver, vehicle and price of a given ride ID


<details><summary>Parameters</summary>

#### id (required)

The ID of the ride

**Type:** string

</details>

## get_ride_receipt

Get the receipt information of a processed ride by providing the ride id. Receipts will only be available to view once the payment has been processed. In the case of canceled ride, cancellation penalty is included if applicable.


<details><summary>Parameters</summary>

#### id (required)

The ID of the ride

**Type:** string

</details>

## get_ride_types

The ride types endpoint returns information about what kinds of Lyft rides you can request at a given location.


<details><summary>Parameters</summary>

#### lat (required)

Latitude of a location

**Type:** number

#### lng (required)

Longitude of a location

**Type:** number

#### ride_type

ID of a ride type

**Type:** string

**Potential values:** lyft, lyft_line, lyft_plus, lyft_premier, lyft_lux, lyft_luxsuv

</details>

## request_ride

Request a Lyft come pick you up at the given location.


<details><summary>Parameters</summary>

#### $body

Ride request information

**Type:** object

</details>

## set_ride_destination

Add or update the ride's destination. Note that the ride must still be active (not droppedOff or canceled), and that destinations on Lyft Line rides can not be changed.


<details><summary>Parameters</summary>

#### id (required)

The ID of the ride

**Type:** string

#### $body

The coordinates and optional address of the destination

**Type:** object

</details>

## set_ride_rating

Add the passenger's 1 to 5 star rating of the ride, optional written feedback, and optional tip amount in minor units and currency. The ride must already be dropped off, and ratings must be given within 24 hours of drop off. For purposes of display, 5 is considered the default rating. When this endpoint is successfully called, payment processing will begin.


<details><summary>Parameters</summary>

#### id (required)

The ID of the ride

**Type:** string

#### $body

The rating and optional feedback

**Type:** object

</details>

