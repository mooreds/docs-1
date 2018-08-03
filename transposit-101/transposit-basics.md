# Transposit Basics

## What is a user? 

TODO: Transposit user \(you the developer\), end user \(your applications’ users\)

## What is a connector?

Transposit creates a unified interface for interacting with various APIs. A data connector represents either external applications or other Transposit applications. OpenAPI or WSDL specifications are used to map external APIs to the Transposit ecosystem. Applications built within Transposit can be connected to each other without any additional bindings.

The data connector encapsulates:

* Authentication \(OAuth, username/password, basic header auth, etc\)
* API schema and delivery mechanism
* Pagination \(supported by some operations\)

## What is an operation?

Operations are a callable unit of work that can be written as either JavaScript or SQL. What makes connectors unique is that they have easy access to data from your application's data connections. For external data connectors, Transposit operations usually represent a single API endpoint. Operations inside a Transposit application can be private \(e.g. used only for development or called by other operations within the application\), scheduled for periodic execution, or deployed as an endpoint \(link to some deployment documentation\).

## **What’s a Hosted app?**

## How does authentication work in Transposit?

* How end users authenticate into Transposit
* How Transposit authenticates to your integrations  
* Google Login

For more info, go to Authentication

