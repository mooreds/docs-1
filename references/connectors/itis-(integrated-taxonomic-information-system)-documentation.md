---
id: itis-(integrated-taxonomic-information-system)-documentation
title: ITIS (Integrated Taxonomic Information System) (version v1.*.*)
sidebar_label: ITIS (Integrated Taxonomic Information System)
layout: docs.mustache
---

## get_accepted_names_from_tsn

Returns a list of accepted names for the TSN. This can return more than one result if the TSN is for a synonym.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_any_match_count

Returns a count of the matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## get_comment_detail_from_tsn

Returns the list of comments for the TSN. This can return more than result if multiple comments are entered.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_common_names_from_tsn

Returns a list of common names for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_core_metadata_from_tsn

Returns the set of core metadata for the TSN. This contains credibility rating, taxonomic usage, unacceptability reason, coverage, and currency data

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_coverage_from_tsn

Returns the taxon coverage information for the TSN. This information is available for Genus and above (rank_id &gt; 190) only.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_credibility_rating_from_tsn

Returns the credibility rating for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_credibility_ratings



*This operation has no parameters*

## get_currency_from_tsn

Returns the taxon currency information for the TSN. This information is available for Genus and above (rank_id &gt; 190) only.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_date_data_from_tsn

Returns the initial time stamp and last update date for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_description



*This operation has no parameters*

## get_experts_from_tsn

Returns a list of the expert information for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_full_hierarchy_from_tsn

Returns the Taxonomic Hierarchy from the kingdom to the requested scientific name, and the immediate children of the scientific name.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_full_record_from_lsid

Returns the full ITIS record for the TSN in the LSID, found by comparing the TSN in the search key to the TSN field. Returns an empty result set if there is no match or the TSN is invalid. Note: Because this API must do multiple database lookups, this can be a time-comsuming operation and may take several seconds to return information.

<details><summary>Parameters</summary>

### lsid

A string containing the LSID.

**Type:** string

</details>

## get_full_record_from_tsn

Returns the full ITIS record for a TSN found by comparing the search key to the TSN field, or an empty result set if there is no match. Note: Because this API must do multiple database lookups, this can be a time-comsuming operation and may take several seconds to return information.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_geographic_divisions_from_tsn

Returns a list of the geographic divisions for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_geographic_values



*This operation has no parameters*

## get_global_species_completeness_from_tsn

Retruns the taxon completeness rating for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_hierarchy_down_from_tsn

Returns a list of all the valid/accepted scientific names contained within a particular valid/accepted scientific name and their TSNs, limited to immediate children only. The result set will be found by comparing the search key to the parent TSN field. Note: There is the possibility that this could return a sizable set of data. For example, if searching with the TSN for Animalia (TSN 202423), the returned group would be all records in the Animalia tree. Because of this, this function will only return the immediate children of the search key (i.e. searching for Animalia's TSN would return the phyla directly linked to it, and the names of any other rank directly linked to it).

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_hierarchy_up_from_tsn

Returns the parent of the TSN (i.e. the parent of the current scientific name in the taxonomic hierarchy) found by comparing the search key to the ITIS TSN field.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_itis_terms

Gets a list of ITIS Terms as used by the Resource Catalog Input Tool from a common or scientific name match, or an empty result set if there is no match.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## get_itis_terms_from_common_name

Gets a list of ITIS Terms as used by the Resource Catalog Input Tool from a common name match, or an empty result set if there is no match.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## get_itis_terms_from_scientific_name

Gets a list of ITIS Terms as used by the Resource Catalog Input Tool from a scientific name match, or an empty result set if there is no match.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## get_jurisdiction_values



*This operation has no parameters*

## get_jurisdictional_origin_from_tsn

Rerurns a list of the jurisdiction and origin values for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_jurisdictional_origin_values



*This operation has no parameters*

## get_kingdom_name_from_tsn

Returns the kingdom name for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_kingdom_names



*This operation has no parameters*

## get_last_change_date



*This operation has no parameters*

## get_lsid_from_tsn

Gets the unique LSID for the TSN, or an empty result if there is no match.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_other_sources_from_tsn

Returns a list of the other sources used for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_parent_tsn_from_tsn

Returns the parent TSN for the entered TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_publications_from_tsn

Returns a list of the pulications used for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_rank_names



*This operation has no parameters*

## get_record_from_lsid

Gets the partial ITIS record for the TSN in the LSID, found by comparing the TSN in the search key to the TSN field. Returns an empty result set if there is no match or the TSN is invalid. Note: This record is a subset of the full ITIS record and will match the return record from the LSID server.

<details><summary>Parameters</summary>

### lsid

A string containing the LSID.

**Type:** string

</details>

## get_review_year_from_tsn

Returns the review year for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_scientific_name_from_tsn

Returns the scientific name for the TSN. Also returns the component parts (names and indicators) of the scientific name.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_synonym_names_from_tsn

Returns a list of the synonyms (if any) for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_taxon_authorship_from_tsn

Returns the author information for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_taxonomic_rank_name_from_tsn

Returns the kingdom and rank information for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_taxonomic_usage_from_tsn

Returns the usage information for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_tsn_by_vernacular_language

Provide a listing of TSNs with vernaculars entered in the requested language. Currently language is only specified in the ITIS database for vernaculars.

<details><summary>Parameters</summary>

### language

Vernacular language

**Type:** string

</details>

## get_tsn_from_lsid

Gets the TSN corresponding to the LSID, or an empty result if there is no match.

<details><summary>Parameters</summary>

### lsid

A string containing the LSID.

**Type:** string

</details>

## get_unacceptability_reason_from_tsn

Returns the unacceptability reason, if any, for the TSN.

<details><summary>Parameters</summary>

### tsn

A string containing the ITIS TSN.

**Type:** string

</details>

## get_vernacular_languages



*This operation has no parameters*

## search_by_common_name

Returns matches found by comparing the search key to the ITIS common names.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## search_by_common_name_begins_with

Return matches found by comparing the search key to the beginning of the ITIS common names.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## search_by_common_name_ends_with

Return matches found by comparing the search key to the end of the ITIS common names.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## search_by_scientific_name

Returns matches found by comparing the search key to the ITIS full Scientific Names, both with and without the indicator fields.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

## search_for_any_match

Returns matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.

<details><summary>Parameters</summary>

### srchKey

A string containing the search key.

**Type:** string

</details>

