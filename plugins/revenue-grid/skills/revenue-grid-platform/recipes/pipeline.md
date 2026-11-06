# Pipeline and team

For lists of deals, forecasts, win rates, at-risk reviews, and a manager's view of the team.

## Scope

- "My" deals are those whose owner field holds the user's CRM ID.
- For "my team", call `get_user_reports`. It returns direct reports by default. Use
  `relation="all"` when the user means everyone below them. Reports come from the CRM role
  hierarchy. If it returns nobody, ask whom to include. Say how many people the answer covers.
- For a named rep, find the user with `contains(tolower(Name), '<name>')` on the CRM user type.

## Query

- Fetch all owners' deals in one `query_crm_data` call, such as
  `(OwnerId eq '<id1>' or OwnerId eq '<id2>') and IsClosed eq false`. Do not query each rep separately.
- Find open, won, and lost deals with the boolean closed and won fields when metadata has them, such
  as `IsClosed` and `IsWon`. Otherwise use the stage picklist values from metadata. Never assume
  stage names. Records with an empty boolean match neither `eq true` nor `eq false`.
- For a period, filter on the close date. Read up to 50 rows per call and page while `skip` is below
  `total_items`.
- For counts and win rates, use `take=1` calls and read `total_items`.
  Below ten deals, give counts rather than percentages.
- Use `calculator` for sums, averages, and medians over more than a few numbers.

## Numbers

- Use the amount field the user means. Default to the standard amount field and name the field you
  used, since tenants often also have ARR or ACV fields with different values.
- Each record can have its own currency set for amount fields.
  Before you add amounts in different currencies, convert them with the rates in `rap://crm/currencies` and say so.
- Report the CRM's probability and forecast category as recorded. Do not invent weightings or move
  deals between forecast categories. If the evidence disagrees with the CRM, show your view
  separately and explain it.

## At-risk review

1. Shortlist from CRM fields: open deals with a past close date, large amounts, or a close date in
   the period. A close date in the past on an open deal is a fact worth stating.
2. For the shortlist, call `get_revenue_iq_suggestions` per deal with the close date and action
   priority, without reasoning, in parallel.
3. Find each shortlisted deal's last interaction with `list_emails` and `list_appointments`,
   `take=1`, newest first, one call per deal in parallel. A combined call returns the busiest deals
   and can miss the quiet ones.
4. Read deeper only on the few deals the user will act on.

For more than about ten deals, shortlist before calling per-deal tools.
