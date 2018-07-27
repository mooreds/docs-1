# Operations

Operations are a callable unit of work that can be written as either JavaScript or SQL. What makes them unique is that they have easy access to fetch data from your application's data connections. For external data connectors, Transposit operations usually represent a single API endpoint. Operations inside a Transposit application can be private (e.g. used only for development or called by other operations within the application), scheduled for periodic execution, or deployed as an endpoint (link to some deployment documentation).
