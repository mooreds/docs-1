---
id: body-parameter
title: $body parameter
layout: docs.mustache
---

Many Transposit operations have a parameter named `$body` to represent the request body of the operation. The `$body` can be written as plain JSON in a JavaScript operation or a JSON-like object constructed through a `SELECT` statement in SQL.

For example, the following JS and SQL operations are equivalent:

```javascript
function run(params) {
  return api.run("spotify.create_playlist", 
  { 
    user_id: "12345", 
    $body: {public: true, name: "My New Playlist"}
  })
}
```

```sql
SELECT * FROM spotify.create_playlist
  WHERE user_id='12345'
  AND $body=(SELECT {
    'public' : true,
    'name' : 'My New Playlist'
  })
```

Note: the single quotes are optional for `public` and `name` in the SQL call, but string values, i.e `My New Playlist` should be single-quoted.

## Ability to extract from $body

The `$body` parameter supports nested object assignment, similar to a JSON object.

For example: the above SQL statement can also be written as

```sql
SELECT * FROM spotify.create_playlist
  WHERE user_id='12345'
  AND $body.public = true
  AND $body.name = 'My New Playlist'
``` 

> Duplicate variable assignments are not allowed.

Extracted `$body` parameters can also be objects. For example: 

```sql
SELECT * FROM stripe.create_charge
  WHERE $body.shipping = (SELECT {
    'carrier': 'USPS',
    'name': 'Transposit',
    'address': {
      'city': 'San Francisco',
      'state': 'CA',
      'postal_code': '94108',
      'line1': '49 Geary St'
    }
  })
  AND $body.shipping.address.country = 'USA'
  AND $body= (SELECT {
      'description' : 'Plants for the office',
      'source': 'tok_visa',
      'amount': 200,
      'currency': 'USD'
  })
```
