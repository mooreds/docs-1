---
id: dark-sky-documentation
title: Dark Sky (version v2.*.*)
---

## get_forecast

returns the current weather forecast for the next week

<details><summary>Parameters</summary>

#### latitude (required)

The latitude of a location (in decimal degrees). Positive is north, negative is south.

**Type:** string

#### longitude (required)

The longitude of a location (in decimal degrees). Positive is east, negative is west.

**Type:** string

#### exclude

Exclude some number of data blocks from the API response. This is useful for reducing latency and saving cache space.

**Type:** array

#### extend

When present, return hour-by-hour data for the next 168 hours, instead of the next 48. When using this option, we strongly recommend enabling HTTP compression.

**Type:** string

**Potential values:** hourly

#### lang

Return summary properties in the desired language.

**Type:** string

#### units

Return weather conditions in the requested units.

**Type:** string

**Potential values:** auto, ca, uk2, us, si

</details>

## get_time_machine

returns the observed or forecast weather conditions for a date in the past or future

<details><summary>Parameters</summary>

#### latitude (required)

The latitude of a location (in decimal degrees). Positive is north, negative is south.

**Type:** string

#### longitude (required)

The longitude of a location (in decimal degrees). Positive is east, negative is west.

**Type:** string

#### time (required)

Either be a UNIX time (that is, seconds since midnight GMT on 1 Jan 1970) or a string formatted as  
[YYYY]-[MM]-[DD]T[HH]:[MM]:[SS][timezone]. timezone should either be omitted (to refer to local time for the location being requested), 
Z (referring to GMT time), or +[HH][MM] or -[HH][MM] for an offset from GMT in hours and minutes. 
The timezone is only used for determining the time of the request; the response will always be relative to the local time zone.


**Type:** string

#### exclude

Exclude some number of data blocks from the API response. This is useful for reducing latency and saving cache space.

**Type:** array

#### lang

Return summary properties in the desired language.

**Type:** string

#### units

Return weather conditions in the requested units.

**Type:** string

**Potential values:** auto, ca, uk2, us, si

</details>

