# Safe CRM Update

Use for confirmed CRM changes only.

## Flow

1. Resolve the record and object type.
2. Read object-specific CRM metadata first.
3. Resolve user-facing field labels to real field names through metadata.
4. Fetch the latest values for the fields you might change.
5. If the request is missing a field or value, or uses a relative value such as "next Friday", emit one clarifying question before proceeding.
6. Show a short `current -> proposed` diff.
7. If the proposed value already matches the current value, say so and do not write unless the user still confirms.
8. Get a separate explicit confirmation reply.
9. Execute the update.
10. Report the returned status exactly.

## Good Inputs

- `get_crm_metadata`
- `query_crm_data`
- `update_crm_record`

## Notes

- Do not guess field names or types.
- Do not write while values are still ambiguous.
- Do not reuse a value from previous tasks unless the user says `same as before`.
- Use `None` to clear nullable fields. Use `False` to clear boolean fields.
