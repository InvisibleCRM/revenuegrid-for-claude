# Record brief

For "what's going on with X", account or deal reviews, and context before a call about one record.

## Gather

1. Resolve the record and read only the CRM fields the answer needs, such as stage, amount, close
   date, owner, and, for a deal, its account lookup.
2. Fetch the current state and the recent activity in parallel:
   - `get_crm_summary_sections`
   - For a deal, `get_revenue_iq_suggestions` with the close date, stage, action priority, and next
     steps
   - For an account, `get_crm_health_artifacts` with health, action priority, and next steps
   - `list_action_items` with `IsResolved eq false`, filtered by the record's link and, for a deal,
     its account's link
   - `list_appointments` and `list_emails` filtered by the record's link over the last 90 days,
     newest first, about ten each, without bodies. Their headers give the last interaction, who is
     engaged, and how often.
3. If a deal has little linked activity, run the activity queries again on its account key and
   label those figures as account-wide.

If neither the record nor its account has linked activity or AI outputs, say so with the filters
you used, and do not run the remaining calls.

## Write

- Lead with the record's state and the one thing that most needs attention, with names and dates.
- Give the last interaction with its direction: who wrote or met last, and when. An outbound email
  after weeks without a customer reply is a finding in itself.
- Say how old an AI output is when its date is weeks before the latest activity.
- Separate what the data shows from your interpretation, and keep to what the user asked. A narrow
  question gets a narrow answer, not a full brief.
