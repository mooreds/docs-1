---
id: medium-documentation
title: Medium (version v1.*.*)
sidebar_label: Medium
layout: docs.mustache
---

## create_post

Creates a post on the authenticated user’s profile.

<details><summary>Parameters</summary>

### authorId (required)

authorId is the user id of the authenticated user.

**Type:** string

### $body

Creates a post for user.

**Type:** object

```json
{
  "license" : "The license of the post. Valid values are `all-rights-reserved`, `cc-40-by`, `cc-40-by-sa`, `cc-40-by-nd`, `cc-40-by-nc`, `cc-40-by-nc-nd`, `cc-40-by-nc-sa`, `cc-40-zero`, `public-domain`. The default is `all-rights-reserved`.",
  "canonicalUrl" : "The original home of this content, if it was originally published elsewhere.",
  "contentFormat" : "The format of the \"content\" field. There are two valid values, \"html\", and \"markdown\"",
  "title" : "The title of the post. Note that this title is used for SEO and when rendering the post as a listing, but will not appear in the actual post—for that, the title must be specified in the content field as well. Titles longer than 100 characters will be ignored. In that case, a title will be synthesized from the first content in the post when it is published.",
  "content" : "The body of the post, in a valid, semantic, HTML fragment, or Markdown. Further markups may be supported in the future. For a full list of accepted HTML tags, see here. If you want your title to appear on the post page, you must also include it as part of the post content.",
  "publishStatus" : "The status of the post. Valid values are `public`, `draft`, or `unlisted`. The default is `public`.",
  "tags" : [ "string" ]
}
```

</details>

## create_publication_post

creating a post and associating it with a publication on Medium. The request also shows this association, considering posts a collection of resources under a publication

There are additional rules around publishing that each request to this API must respect:
  - If the authenticated user is an 'editor' for the publication, they can create posts with any publish status. Posts published as 'public' or 'unlisted' will appear in collection immediately, while posts created as 'draft' will remain in pending state under publication.
  - If the authenticated user is a 'writer' for the chosen publication, they can only create a post as a 'draft'. That post will remain in pending state under publication until an editor for the publication approves it.
  - If the authenticated user is neither a 'writer' nor an 'editor', they are not allowed to create any posts in a publication.


<details><summary>Parameters</summary>

### publicationId (required)

Here publicationId is the id of the publication the post is being created under. The publicationId can be acquired from the API for listing user’s publications.

**Type:** string

### $body

Creates a post for publication.

**Type:** object

```json
{
  "license" : "The license of the post. Valid values are `all-rights-reserved`, `cc-40-by`, `cc-40-by-sa`, `cc-40-by-nd`, `cc-40-by-nc`, `cc-40-by-nc-nd`, `cc-40-by-nc-sa`, `cc-40-zero`, `public-domain`. The default is `all-rights-reserved`.",
  "canonicalUrl" : "The original home of this content, if it was originally published elsewhere.",
  "contentFormat" : "The format of the \"content\" field. There are two valid values, \"html\", and \"markdown\"",
  "title" : "The title of the post. Note that this title is used for SEO and when rendering the post as a listing, but will not appear in the actual post—for that, the title must be specified in the content field as well. Titles longer than 100 characters will be ignored. In that case, a title will be synthesized from the first content in the post when it is published.",
  "content" : "The body of the post, in a valid, semantic, HTML fragment, or Markdown. Further markups may be supported in the future. For a full list of accepted HTML tags, see here. If you want your title to appear on the post page, you must also include it as part of the post content.",
  "publishStatus" : "The status of the post. Valid values are `public`, `draft`, or `unlisted`. The default is `public`.",
  "tags" : [ "string" ]
}
```

</details>

## get_my_profile



*This operation has no parameters*

## get_my_publications

Returns a full list of publications that the user is related to in some way. This includes all publications the user is subscribed to, writes to, or edits.

<details><summary>Parameters</summary>

### userId (required)

A unique identifier for the user.

**Type:** string

</details>

## get_publication_contributors

This endpoint returns a list of contributors for a given publication. In other words, a list of Medium users who are allowed to publish under a publication, as well as a description of their exact role in the publication (for now, either an editor or a writer).

<details><summary>Parameters</summary>

### publicationId (required)

A unique identifier for the publication.

**Type:** string

</details>

