# Team Focus

Use for manager questions about direct reports, workload, or where a team needs help.

## Flow

1. Resolve the anchor person.
2. Read the reporting-chain resource and work from visible users instead of rebuilding hierarchy from roles.
3. Fetch workload in small owner-by-owner slices, starting with open action items.
4. Add meetings, emails, summaries, or artifacts only for the owners who still need clarification.
5. Return themes, highest-risk areas, and where help is needed.

## Good Inputs

- `get_user_reports`
- `list_action_items`
- `list_appointments`
- `list_emails`
- `get_crm_summary_sections`
- `get_crm_summary_progression`
- `get_pipeline_suggestions`

## Notes

- Default `user/reports` gives direct reports; use `relation=all` only when the user asks for wider coverage.
- Keep slices small before expanding to the whole team.
