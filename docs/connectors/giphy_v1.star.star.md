---

id: giphy_documentation

title: Giphy

version: v1.*.*

---

## get_gif

Returns a GIF given that GIF's unique ID

<details><summary>Parameters</summary>

#### gif-id (required)

**Type:** string

</details>

## get_gifs

A multiget version of the get GIF by ID endpoint.

<details><summary>Parameters</summary>

#### ids

comma-separated string of ids

**Type:** string

</details>

## get_gifs_translate

The translate API draws on search, but uses the GIPHY special sauce to handle translating from one vocabulary to another. In this case, words and phrases to GIFs.

<details><summary>Parameters</summary>

#### s (required)

Search term

**Type:** string

</details>

## get_random_gif

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog.

<details><summary>Parameters</summary>

#### tag

**Type:** string

</details>

## get_random_stickers

Returns a random Sticker, limited by tag. Excluding the tag parameter will return a random Sticker from the GIPHY catalog.

*This operation has no parameters*

## get_stickers_translate

The translate API draws on search, but uses the GIPHY special sauce to handle translating from one vocabulary to another. In this case, words and phrases to GIFs.

<details><summary>Parameters</summary>

#### s (required)

search term

**Type:** string

</details>

## get_trending_gifs

Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team. The data returned mirrors the GIFs showcased on the GIPHY homepage

*This operation has no parameters*

## get_trending_stickers

Fetch Stickers currently trending online. Hand curated by the GIPHY editorial team.

*This operation has no parameters*

## search_gifs

Search all GIPHY GIFs for a word or phrase. Punctuation will be stripped and ignored. Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling or american+psycho

<details><summary>Parameters</summary>

#### q

**Type:** string

</details>

## search_stickers

Replicates the functionality and requirements of the classic GIPHY search, but returns animated stickers rather than GIFs.

<details><summary>Parameters</summary>

#### q

**Type:** string

</details>

