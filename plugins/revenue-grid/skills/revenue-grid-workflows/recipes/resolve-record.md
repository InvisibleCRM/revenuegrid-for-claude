# Resolve Record

Use for finding a person or CRM record by name before deeper analysis.

## Flow

1. If the object type is unknown, read CRM metadata overview first.
2. Read object-specific CRM metadata before querying fields.
3. Use `query_crm_data` with full-text `search` for searchable CRM types, or an OData `filter` for exact known fields.
4. If search is weak or empty, switch to a metadata-guided direct CRM query with a tighter filter.
5. Keep the narrowest stable identifier and reuse it.

## Good Inputs

- `get_crm_metadata`
- `query_crm_data`

## Notes

- Do not assume a fixed CRM schema.
- Prefer exact IDs once you have them.
