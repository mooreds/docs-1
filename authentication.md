# Authentication

## Keys and Keychains

### Keys

Transposit supports several authorization mechanisms including oauth, auth via headers, username and password, and a few less common options such as wsdl auth and oauth v1. When you enter your credentials (or complete an oauth flow), Transposit securely stores your credentials as a key for future use. Each Transposit application has its own keys that are not shared across applications, contexts, or organizations (unless using keychains, see below).

When first adding a data connection to your application, Transposit will ask you to authorize the connection. After adding a data connection, keys for that dependency can be added or removed from the Keys section of the Transposit operations console.

#### Production keys

Transposit keeps separate sets of development and production keys. The keys shown in the Transposit operation console are for development. Adding or removing production keys is done via Authentication &gt; Production keys.

From Authentication &gt; Production keys, you can also require the user to provide the credentials for a data connection.

#### Scheduled task keys

Keys used when running scheduled tasks are kept separate from development and production keys. You can add keys to a selected task via Deploy &gt; Scheduled tasks

### Keychains

Keychains are sets of keys that you can enable in development, production, or other contexts. You can also share keychains within an organization. Keychains are managed in Transposit via Authentication &gt; Keychains.

In order to share keychains within an organization, create the keychain with the organization as the owner. Any keys put in that organization-owned keychain will be usable by others in the organization.

## User Login

User login is deployed on a per endpoint basis. Currently available login mechanisms include Google login. Domains and usernames can be whitelisted for login. Configuration via google clientId and secret are under Authentication &gt; Login. You can manage your logged in users' information via Authentication &gt; Registered Users.

