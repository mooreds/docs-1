---
id: google-distance-documentation
title: Google Distance (version v1.*.*)
sidebar_label: Google Distance
layout: docs.mustache
---

## get_direction_matrix



<details><summary>Parameters</summary>

#### destinations (required)

One or more locations to use as the finishing point for calculating travel distance and time. The options for the destinations parameter are the same as for the origins parameter, described above.

**Type:** string

#### origins (required)

The starting point for calculating travel distance and time.You can supply one or more locations separated by the pipe character (|), in the form of an address, latitude/longitude coordinates, or a place ID.

**Type:** string

#### outputFormat (required)

desired output format. json or xml

**Type:** string

#### arrival_time

Specifies the desired time of arrival for transit requests, in seconds since midnight, January 1, 1970 UTC.

**Type:** string

#### avoid

Introduces restrictions to the route.

**Type:** string

#### departure_time

The desired time of departure.

**Type:** string

#### language

The language in which to return results.

**Type:** string

#### mode

defaults to driving. driving, walking, bicycling, or transit

**Type:** string

#### region

The region code, specified as a ccTLD (country code top-level domain) two-character value

**Type:** string

#### traffic_model

defaults to best_guess. choose from best_guess, pessimistic or optimistic

**Type:** string

#### transit_mode

Specifies one or more preferred modes of transit. choose from bus, subway, train, tram, or rail. eg transit_mode=train|tram|subway

**Type:** string

#### transit_routing_preference

Specifies preferences for transit requests. choose from less_walking or fewer_transfers

**Type:** string

#### units

Specifies the unit system to use when expressing distance as text.

**Type:** string

</details>

