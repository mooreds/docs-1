---
id: terms
title: Terms & basics
layout: docs.mustache
---

## Applications

An application is the representation of a particular project; a container for functionality you want to build. Applications contain operations, data connections, keys to access data connections, and configurations for authentication and deployment.

## Data connections

Transposit creates a unified interface for interacting with various APIs. A data connection represents either external applications or other Transposit applications. OpenAPI or WSDL specifications are used to map external APIs to the Transposit ecosystem. Applications built within Transposit can be connected to each other without additional bindings.

The data connection encapsulates:

* [Authentication](/docs/references/connector-authentication) (OAuth, username/password, basic header auth, etc)
* API schema and delivery mechanism
* Pagination (supported by some operations)

## Operations

[Operations](/docs/building/operations) are callable units of work that can be written in [JavaScript](/docs/references/js-operations) or [SQL](/docs/references/sql-operations). Operations inside a Transposit application can be private (e.g. used only for development, or called by other operations within the application), [scheduled for periodic execution](/docs/building/scheduled-tasks), or deployed as [endpoints](/docs/building/endpoints).

## Authentication

Data connections used by your application may require access credentials, referred to as _keys_ in Transposit to disambiguate from other related concepts. Keys may be supplied by you as the developer, or by your users, if your application so specifies.

Separately, there is the "front door" to your application, which can have its own authentication requirements, entirely unrelated to data connection keys—your application may require users to register and log in, for example.

Transposit provides powerful tools to centrally manage these types of authentication and user management issues, making apps easier to build and faster to deploy.

## Hosted apps

To speed up the flow of application development and deploying, Transposit provides basic facilities for hosting a web page for use as access point to your application's front end. Use of this hosting is entirely optional. See also: [Hosted Apps](/docs/building/hosted-apps).

## Users

In the Transposit platform, there are two types of users:

  * The Transposit user; the developer an application
  * The application user; the consumer of the application

This distinction is important in that depending on the configuration of your application, credentials (keys) for accessing data connections may be supplied by you as the developer or by your end users. See also: [Managed authentication](/docs/building/managed-authentication).

