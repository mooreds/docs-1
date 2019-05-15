---
id: introduction
title: Introduction
layout: docs.mustache
---

Transposit is an end-to-end solution for building production-ready applications on top of APIs. With Transposit's relational engine, you can use SQL and JavaScript to join, filter and transform your data, wherever it lives, in an interactive interface. Transposit will handle for you the complexities of authentication, retries, caching, and optimized execution. Your client application can interact with Transposit through a JavaScript client or plain HTTP.

## Relational engine

Transposit provides the ability to write SQL queries \(or JavaScript\) to transform and explore your data, as if each data connection is a virtual table in a single relational database. It abstracts away the details of data representation allowing you to express your intent, while the relational engine translates that intent, optimizes it, and executes it.

To make this work, we’ve built Transposit to know how to securely communicate with APIs, optimize performance around network calls, and account for the unreliable nature of modern APIs.

## Powerful managed authentication

Transposit provides end-to-end tooling to centrally administer the authentication and user management required in a data-driven application. You can use Transposit to easily connect to data requiring developer authentication, build a login flows allowing users to connect their own data, and maintain the mapping of user records to their data connections.

## Modern developer tooling

Transposit also provides the features you'd expect of a first-class developer tool. We are developers, and we built Transposit with developers' needs in mind. That's why Transposit is:

* **Incrementally adoptable:** Transposit is a library, not an ecosystem. You can use Transposit to build a single endpoint, or as your entire backend.
* **Based on open standards:** Take advantage of the battle-tested tools and libraries you already know and love.
* **Backed by git:** Your application’s code is stored and versioned in a [git repository](references/repository.md), so you can edit in the cloud or clone it locally.
* **Equipped with modern tooling:** Build on a standard interface with smart treatments of APIs, pagination, serverless functions, caching, and basic application hosting.
* **Free to try:** You can start using Transposit without speaking to a single person. No need to pay until your applications or endpoints start to see a lot of traffic.

## How to use these docs

* [Getting started](get-started/quickstart) — Get acquainted with Transposit by following easy guides, learning product basics, and getting answers to common questions.

* [Building and deploying applications](building/operations) — Learn how to connect data sources, write operations to manipulate data, and deploy to real users.

* [References](references/keys-and-keychains) — Dive deep into our reference documentation for SQL and JavaScript, authentication and credentials, and answers for common technical scenarios.

## Get in touch

If you run into any issues or questions that aren't covered in our documentation, reach out to our team to get support. We'd also love to hear from you if you have feedback about our product or documentation, or have built something awesome you'd like to share. You can email us at [support@transposit.com](mailto:support@transposit.com).
