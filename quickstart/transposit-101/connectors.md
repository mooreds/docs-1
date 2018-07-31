# Data Connectors

Transposit creates a unified interface for interacting with various APIs. A data connector represents either external applications or other Transposit applications. We use OpenAPI or WSDL specifications to map external APIs to the Transposit ecosystem. Applications built within Transposit can be connected to each other without any additional bindings.

The data connector encapsulates:
- Authentication (OAuth, username/password, basic header auth, etc)
- API schema and delivery mechanism
- Pagination (supported by some operations)
