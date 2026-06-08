# Action Items

Use for open-work review, action-item creation, and action-item resolution.

## Review Flow

1. Start with filtered action items.
2. Keep windows tight and compare overdue, oldest-open, or near-due slices.
3. Use linked CRM keys or linked appointments to stay scoped to the right work.

## Create Flow

1. Create an action item only when the user explicitly wants new tracked work.
2. Include clear content, linked CRM keys, a responsible CRM user, and concrete resolution criteria.
3. Set a due date only when the user gives one or the timing is obvious.

## Resolve Flow

1. Resolve an action item only when the user wants it closed.
2. Use the action-item ID, responsible user's CRM ID, and short resolution reasoning.

## Good Inputs

- `list_action_items`
- `create_action_item`
- `resolve_action_item`

## Notes

- Action Item semantics and lifecycle details are in `../revenue-grid-platform/references/action-items.md`.
- If `resolve_action_item` returns an error, report the error exactly and do not mark the item closed.
