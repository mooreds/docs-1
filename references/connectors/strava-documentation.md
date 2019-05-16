---
id: strava-documentation
title: Strava (version v1.*.*)
sidebar_label: Strava
layout: docs.mustache
---

## create_activity

Creates a manual activity for an athlete. Requires write permissions, as requested during the authorization process.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## explore_segments

Returns the top 10 segments matching a specified query.

<details><summary>Parameters</summary>

#### bounds (required)

The latitude and longitude for two points describing a rectangular boundary for the search: [southwest corner latitutde, southwest corner longitude, northeast corner latitude, northeast corner longitude]

**Type:** array

#### activity_type

Desired activity type.

**Type:** string

**Potential values:** running, riding

#### max_cat

The maximum climbing category.

**Type:** integer

#### min_cat

The minimum climbing category.

**Type:** integer

</details>

## get_activity_by_id

Returns the given activity that is owned by the authenticated athlete.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

#### include_all_efforts

To include all segments efforts.

**Type:** boolean

</details>

## get_activity_streams

Returns the given activity's streams.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

#### key_by_type (required)

Must be true.

**Type:** boolean

#### keys (required)

Desired stream types.

**Type:** array

</details>

## get_club_activities_by_id

Retrieve recent activities from members of a specific club. The authenticated athlete must belong to the requested club in order to hit this endpoint. Pagination is supported. Enhanced Privacy Mode is respected for all activities.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the club.

**Type:** integer

</details>

## get_club_admins_by_id

Returns a list of the administrators of a given club.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the club.

**Type:** integer

</details>

## get_club_by_id

Returns a given club using its identifier.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the club.

**Type:** integer

</details>

## get_club_members_by_id

Returns a list of the athletes who are members of a given club.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the club.

**Type:** integer

</details>

## get_comments_by_activity_id

Returns the comments on the given activity.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

</details>

## get_efforts_by_segment_id

Returns a set of the authenticated athlete's segment efforts for a given segment.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the segment.

**Type:** integer

</details>

## get_gear_by_id

Returns an equipment using its identifier.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the gear.

**Type:** integer

</details>

## get_kudoers_by_activity_id

Returns the athletes who kudoed an activity identified by an identifier.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

</details>

## get_laps_by_activity_id

Returns the laps of an activity identified by an identifier.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

</details>

## get_leaderboard_by_segment_id

Returns the specified segment leaderboard.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the segment leaderboard.

**Type:** integer

#### age_group

Premium Feature. Filter by age group.

**Type:** string

**Potential values:** 0_19, 20_24, 25_34, 35_44, 45_54, 55_64, 65_69, 70_74, 75_plus

#### club_id

Filter by club.

**Type:** integer

#### context_entries

**Type:** integer

#### date_range

Filter by date range.

**Type:** string

**Potential values:** this_year, this_month, this_week, today

#### following

Filter by friends of the authenticated athlete.

**Type:** boolean

#### gender

Filter by gender.

**Type:** string

**Potential values:** M, F

#### weight_class

Premium Feature. Filter by weight class.

**Type:** string

**Potential values:** 0_124, 125_149, 150_164, 165_179, 180_199, 200_224, 225_249, 250_plus, 0_54, 55_64, 65_74, 75_84, 85_94, 95_104, 105_114, 115_plus

</details>

## get_logged_in_athlete



*This operation has no parameters*

## get_logged_in_athlete_activities

Returns the activities of an athlete for a specific identifier.

<details><summary>Parameters</summary>

#### after

An epoch timestamp to use for filtering activities that have taken place after a certain time.

**Type:** integer

#### before

An epoch timestamp to use for filtering activities that have taken place before a certain time.

**Type:** integer

</details>

## get_logged_in_athlete_clubs

Returns a list of the clubs whose membership includes the authenticated athlete.

*This operation has no parameters*

## get_logged_in_athlete_starred_segments

List of the authenticated athlete's starred segments.

*This operation has no parameters*

## get_logged_in_athlete_zones



*This operation has no parameters*

## get_route_as_gpx

Returns a GPX file of the route.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the route.

**Type:** integer

</details>

## get_route_as_tcx

Returns a TCX file of the route.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the route.

**Type:** integer

</details>

## get_route_by_id

Returns a route using its identifier.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the route.

**Type:** integer

</details>

## get_routes_by_athlete_id

Returns a list of the routes created by the authenticated athlete using their athlete ID.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the athlete.

**Type:** integer

</details>

## get_running_race_by_id

Returns a running race for a given identifier.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the running race.

**Type:** integer

</details>

## get_running_races

Returns a list running races based on a set of search criteria.

<details><summary>Parameters</summary>

#### year

Filters the list by a given year.

**Type:** integer

</details>

## get_segment_by_id

Returns the specified segment.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the segment.

**Type:** integer

</details>

## get_segment_effort_by_id

Returns a segment effort from an activity that is owned by the authenticated athlete.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the segment effort.

**Type:** integer

</details>

## get_segment_effort_streams

Returns a set of streams for a segment effort completed by the authenticated athlete.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the segment effort.

**Type:** integer

#### key_by_type (required)

Must be true.

**Type:** boolean

#### keys (required)

The types of streams to return.

**Type:** array

</details>

## get_segment_streams

Returns the given segment's streams.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the segment.

**Type:** integer

#### key_by_type (required)

Must be true.

**Type:** boolean

#### keys (required)

The types of streams to return.

**Type:** array

</details>

## get_stats

Returns the activity stats of an athlete.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the athlete. Must match the authenticated athlete.

**Type:** integer

</details>

## get_upload_by_id

Returns an upload for a given identifier.

<details><summary>Parameters</summary>

#### uploadId (required)

The identifier of the upload.

**Type:** integer

</details>

## get_zones_by_activity_id

Premium Feature. Returns the zones of a given activity.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

</details>

## update_activity_by_id

Updates the given activity that is owned by the authenticated athlete.

<details><summary>Parameters</summary>

#### id (required)

The identifier of the activity.

**Type:** integer

#### $body

**Type:** object

</details>

## update_logged_in_athlete

Update the currently authenticated athlete.

<details><summary>Parameters</summary>

#### $body

AthleteDescription.

**Type:** object

</details>

