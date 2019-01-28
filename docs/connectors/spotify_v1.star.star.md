---

id: spotify_documentation

title: Spotify

version: v1.*.*

---

## add_track_to_playlist

[Add Tracks to a Playlist](https://developer.spotify.com/web-api/add-tracks-to-playlist/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### uris (required)

A comma-separated list of Spotify track URIs to add. A maximum of 100 tracks can be added in one request.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### position

The position to insert the tracks, a zero-based index

**Type:** integer

</details>

## browse_featured_playlists

[Get a List of Featured Playlists](https://developer.spotify.com/web-api/get-list-featured-playlists/)


<details><summary>Parameters</summary>

#### country

The country (an ISO 3166-1 alpha-2 country code)

**Type:** string

#### locale

The desired language, consisting of an ISO 639 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)".


**Type:** string

#### timestamp

A timestamp in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss) with the user's local time to get results tailored to a specific date and time in the day. If not provided, it defaults to the current UTC time. Example: "2014-10-23T09:00:00" for a user whose local time is 9AM.


**Type:** string

</details>

## browse_new_releases

[Get a List of New Releases](https://developer.spotify.com/web-api/get-list-new-releases/)


<details><summary>Parameters</summary>

#### country

The country (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## check_if_i_am_following

[Check if Current User Follows Artists or Users](https://developer.spotify.com/web-api/check-current-user-follows/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated string of the artists or users ids.

**Type:** string

#### type (required)

The type to follow.

**Type:** string

**Potential values:** artist, user

</details>

## check_my_saved_tracks

[Check Current User's Saved Tracks](https://developer.spotify.com/web-api/check-users-saved-tracks/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of IDs

**Type:** string

</details>

## check_playlist_followers

[Check if Users Follow a Playlist](https://developer.spotify.com/web-api/check-user-following-playlist/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of users ids

**Type:** string

#### owner_id (required)

The playlist owner's Spotify ID

**Type:** string

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

</details>

## create_playlist

[Create a Playlist](https://developer.spotify.com/web-api/create-playlist/)


<details><summary>Parameters</summary>

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### $body

**Type:** object

</details>

## delete_my_track

[Remove Tracks for Current User](https://developer.spotify.com/web-api/remove-tracks-user/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of IDs

**Type:** string

</details>

## edit_playlist_details

[Change a Playlist's Details](https://developer.spotify.com/web-api/change-playlist-details/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### $body

**Type:** object

</details>

## follow

[Follow Artists or Users](https://developer.spotify.com/web-api/follow-artists-users/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of the artists or users ids

**Type:** string

#### type (required)

The type to follow.

**Type:** string

**Potential values:** artist, user

</details>

## follow_playlist

[Follow a Playlist](https://developer.spotify.com/web-api/follow-playlist/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### $body

**Type:** object

</details>

## get_album

[Get an Album](https://developer.spotify.com/web-api/get-album/)


<details><summary>Parameters</summary>

#### id (required)

The Spotify ID for the album

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_album_tracks

[Get an Album's Tracks](https://developer.spotify.com/web-api/get-albums-tracks/)


<details><summary>Parameters</summary>

#### id (required)

The Spotify ID for the album

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_albums

[Get Several Albums](https://developer.spotify.com/web-api/get-several-albums/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of IDs

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_artist

[Get an Artist](https://developer.spotify.com/web-api/get-artist/)


<details><summary>Parameters</summary>

#### id (required)

The Spotify ID for the artist

**Type:** string

</details>

## get_artist_albums

[Get an Artist's Albums](https://developer.spotify.com/web-api/get-artists-albums/)


<details><summary>Parameters</summary>

#### id (required)

The Spotify ID for the artist

**Type:** string

#### album_type

Filter by album types

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_artist_top_tracks

[Get an Artist's Top Tracks](https://developer.spotify.com/web-api/get-artists-top-tracks/)


<details><summary>Parameters</summary>

#### country (required)

The country (an ISO 3166-1 alpha-2 country code)

**Type:** string

#### id (required)

The Spotify ID for the artist

**Type:** string

</details>

## get_artists

[Get Several Artists](https://developer.spotify.com/web-api/get-several-artists/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of IDs

**Type:** string

</details>

## get_artists_i_am_following

[Get User's Followed Artists](https://developer.spotify.com/web-api/get-followed-artists/)


<details><summary>Parameters</summary>

#### type (required)

The ID type, currently only artist is supported.

**Type:** string

**Potential values:** artist

</details>

## get_browse_categories

[Get a List of Browse Categories](https://developer.spotify.com/web-api/get-list-categories/)


<details><summary>Parameters</summary>

#### country

The country (an ISO 3166-1 alpha-2 country code)

**Type:** string

#### locale

The desired language, consisting of an ISO 639 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)".


**Type:** string

</details>

## get_browse_category

[Get a Single Browse Category](https://developer.spotify.com/web-api/get-category/)


<details><summary>Parameters</summary>

#### category_id (required)

The Spotify ID of the category you wish to fetch.

**Type:** string

#### country

The country (an ISO 3166-1 alpha-2 country code)

**Type:** string

#### locale

The desired language, consisting of an ISO 639 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore. For example: es_MX, meaning "Spanish (Mexico)".


**Type:** string

</details>

## get_category_playlists

[Get a Category's playlists](https://developer.spotify.com/web-api/get-categorys-playlists/)


<details><summary>Parameters</summary>

#### category_id (required)

The Spotify ID of the category you wish to fetch.

**Type:** string

#### country

The country (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_my_profile



*This operation has no parameters*

## get_my_saved_tracks

[Get Current User's Saved Tracks](https://developer.spotify.com/web-api/get-users-saved-tracks/)


<details><summary>Parameters</summary>

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_playlist

[Get a Playlist](https://developer.spotify.com/web-api/get-playlist/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### fields

A comma-separated list of fields to filter query

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_playlist_tracks

[Get a Playlist's Tracks](https://developer.spotify.com/web-api/get-playlists-tracks/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### fields

A comma-separated list of fields to filter query

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_related_artists

[Get an Artist's Related Artists](https://developer.spotify.com/web-api/get-related-artists/)


<details><summary>Parameters</summary>

#### id (required)

The Spotify ID for the artist

**Type:** string

</details>

## get_track

[Get a Track](https://developer.spotify.com/web-api/get-track/)


<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_tracks

[Get Several Tracks](https://developer.spotify.com/web-api/get-several-tracks/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of IDs

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code)

**Type:** string

</details>

## get_user

[Get a User's Profile](https://developer.spotify.com/web-api/get-users-profile/)


<details><summary>Parameters</summary>

#### user_id (required)

The user's Spotify user ID.

**Type:** string

</details>

## get_user_playlists

[Get a List of a User's Playlists](https://developer.spotify.com/web-api/get-list-users-playlists/)


<details><summary>Parameters</summary>

#### user_id (required)

The user's Spotify user ID.

**Type:** string

</details>

## reorder_playlist_tracks

[Reorder or replace a Playlist's Tracks](https://developer.spotify.com/web-api/reorder-playlists-tracks/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

#### $body

**Type:** object

</details>

## save_track

[Save Tracks for Current User](https://developer.spotify.com/web-api/save-tracks-user/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of IDs

**Type:** string

</details>

## search

[Search for an Item](https://developer.spotify.com/web-api/search-item/)


<details><summary>Parameters</summary>

#### q (required)

The search query's keywords (and optional field filters). The search is not case-sensitive: 'roadhouse' will match 'Roadhouse', 'roadHouse', etc. Keywords will be matched in any order unless surrounded by quotes, thus q=roadhouse&20blues will match both 'Blues Roadhouse' and 'Roadhouse of the Blues'. Quotation marks can be used to limit the match to a phrase: q=roadhouse&20blues will match 'My Roadhouse Blues' but not 'Roadhouse of the Blues'. By default, results are returned when a match is found in any field of the target object type. Searches can be made more specific by specifying an album, artist or track field filter. For example q=album:gold%20artist:abba&type=album will search for albums with the text 'gold' in the album name and the text 'abba' in an artist name. Other possible field filters, depending on object types being searched, include year, genre, upc, and isrc. For example, q=damian%20genre:reggae-pop&type=artist. The asterisk (*) character can, with some limitations, be used as a wildcard (maximum: 2 per query). It will match a variable number of non-white-space characters. It cannot be used in a quoted phrase, in a field filter, or as the first character of the keyword string. Searching for playlists will return results matching the playlist's name and/or description.

**Type:** string

#### type (required)

A comma-separated list of item types to search across. Search results will include hits from all the specified item types; for example q=name:abacab&type=album,track will return both albums and tracks with "abacab" in their name.

**Type:** string

#### market

The market (an ISO 3166-1 alpha-2 country code).  If given, only items with content playable in that market will be returned.

**Type:** string

</details>

## unfollow

[Unfollow Artists or Users](https://developer.spotify.com/web-api/unfollow-artists-users/)


<details><summary>Parameters</summary>

#### ids (required)

A comma-separated list of the artists or users ids

**Type:** string

#### type (required)

The type to unfollow.

**Type:** string

**Potential values:** artist, user

</details>

## unfollow_playlist

[Unfollow a Playlist](https://developer.spotify.com/web-api/unfollow-playlist/)


<details><summary>Parameters</summary>

#### playlist_id (required)

The Spotify playlist ID.

**Type:** string

#### user_id (required)

The user's Spotify user ID.

**Type:** string

</details>

