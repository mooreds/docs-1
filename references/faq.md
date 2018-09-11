# FAQ

Itemized FAQ + answers. For more technical stuff; a place to add "support" items we can link to users.

## When should I use SQL and when should I use JavaScript?

## What applications should use Transposit?

* Anything that connects with multiple data sources and APIs
* Bots and utilities for interacting with/integrating multiple applications
* Automating custom workflows as applications
  * Not just event-based -- on-demand \(calling out to other sources of data\)
  * standalone
* Applications that require access management \(eg, to business data\)
  * Useful in big organizations
  * Sharing data with customers or partners
  * With security concerns
* Aggregating data from multiple sources into a custom interfaces that also allow you to modify data in the source applications.

## How is Transposit different from Zapier/IFTTT/Workato/etc.?

* Applications, not workflows
* No wiki required
* Error-proof, share, and customize your presentation

## Rate limits

* To make sure you don't accidentally run through your API rate limits for your data connections, we limit the number of API fetches to 25 per operation per request.

