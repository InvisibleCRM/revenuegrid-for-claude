# Action items

## Review

- Always pass a filter. Add `IsResolved eq false` for open work, since the default includes resolved
  items.
- For "my" items, filter `ResponsibleId eq '<user CRM ID>'`.
- For a deal, filter on both the deal and its account link, because RAP usually links AI items to
  the account: `crm_links/any(l: (l/CrmType eq '<deal>' and l/CrmId eq '<id>') or (l/CrmType eq '<account>' and l/CrmId eq '<id>'))`.
- Sort ascending by due date to see overdue items first. Many due dates are RAP's default of 14 days,
  so call an item overdue only when the date is clearly past.

## Create

Create an item only when the user asks for new work to track. Pass clear content, the related CRM objects, and resolution
criteria. RAP records the user as the responsible for this item. Pass a due date only when the user gives one. Otherwise it defaults to 14 days from now.

## Resolve

Resolve an item only when the user says the work is done or no longer needed. Pass the item ID and a
short reason. RAP records the user as the resolver.
