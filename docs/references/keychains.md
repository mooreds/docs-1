---
id: keychains
title: Keys and Keychains
sidebar_label: Keys
---

Here you can find details around Transposit's options for authentication, including keys and keychains, API keys, hosted app authentication, and endpoint deploy settings. For a high-level explanation, read about how we've designed [managed authentication in Transposit](../building/managed-authentication.md).

## Keys

Transposit supports several authorization mechanisms including OAuth, auth via headers, username/password, and a few less common options such as WSDL auth and OAuth v1. When you [enter credentials or complete an OAuth flow](../references/connector-authentication.md), Transposit securely stores them for future use as a key. Each Transposit application has its own keys that are not shared across applications, contexts, or organizations (unless using keychains; see below).

When first adding a data connection to your application, Transposit will ask you to authorize the connection. After adding a data connection, keys for that dependency can be added or removed from the Keys section of the Transposit operations console.

### Production keys

Transposit keeps separate sets of development and production keys. The keys shown in the Transposit operation console are for development. Adding or removing production keys is done via **Authentication > Production keys**.

From **Authentication > Production keys**, you can also require the user to provide the credentials for a data connection.

### Scheduled task keys

Keys used when running scheduled tasks are kept separate from development and production keys. You can add keys to a selected task via **Deploy > Scheduled tasks**.

## Keychains

Keychains are sets of keys that you can enable in development, production, or other contexts. You can also share keychains within an organization. Keychains are managed in Transposit via **Authentication > Keychains**.

In order to share keychains within an organization, create the keychain with the organization as the owner. Any keys put in that organization-owned keychain will be usable by others in the organization.

