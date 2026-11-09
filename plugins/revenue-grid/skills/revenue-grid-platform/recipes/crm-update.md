# CRM update

`update_crm_record` writes to the underlying CRM with the user's own permissions. It replaces each field
value you pass. It does not append or merge.

1. Identify the record and read the type's metadata.
2. Map the user's wording to field names, picklist API values, and value types from metadata.
   Read-only fields cannot be changed.
3. Read the current values of every field you will change with `query_crm_data`.
4. Build each final value. For a long text field, ask whether to replace, append, or prepend the new
   text, but only if the user's request leaves it unclear. Whichever they choose, pass the full new
   text, since the update overwrites the field.
5. Convert relative dates such as "next Friday" to exact dates.
   Write a date without a time as `YYYY-MM-DDT00:00:00Z`.
6. Leave out fields that already hold the final value. If nothing would change, say so and stop.
7. Call `update_crm_record` once with all fields for the record. Pass `null` to clear a field that
   metadata marks nullable.

Ask before writing only when the record, the field, the final value, or the edit mode is unclear.

After the call, report what changed. RAP re-imports the record from the CRM 15 minutes or more after
the update, so until then `query_crm_data` still shows the old values. Do not read the record back to
confirm a change.

- On `timeout`, the CRM did not confirm in time. The change may still apply, and RAP cannot tell yet.
  Do not retry. Tell the user to check the record in their CRM, or to ask again later.
- On `validation_error` or `update_error`, report the CRM's message. Do not try other fields to get
  around it.
- On `internal_error`, try once more.
