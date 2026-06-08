---
name: revenue-grid-workflows
description: This skill should be used when a user asks to summarize a deal, account, or contact; review a meeting or prepare for an upcoming one; check email activity around a record; see what a team member or direct report is working on; inspect, create, or resolve action items; or change a CRM field such as close date, stage, or owner.
user-invocable: false
---

# RAP MCP Workflows

## Global Rules

### Hard constraints — always apply

- Never guess CRM field names. If a field name was not read from tenant metadata in the current turn, do not use it in `select_fields`, `filter`, or `orderby`.
- Read CRM metadata before any CRM query or update that names a CRM type or field.
- Treat writes as destructive and require explicit confirmation before CRM updates.

### Sequencing defaults — apply unless a recipe says otherwise

- Resolve one stable identifier early and reuse it.
- Prefer structured surfaces before raw communications.
- Narrow first: small page sizes, tight date windows, few owners or records.

## Evidence Ladder

1. **Resolution and metadata** — establish identity and schema before anything else
2. **Structured state or open work** — summaries, action items, pipeline state
3. **Artifacts or facts** — distilled business memory from communications and CRM history
4. **Raw email bodies, transcripts, or notes** — only when higher levels are missing or insufficient

## Route By Task

- Find a record or person -> `recipes/resolve-record.md`
- Summarize a record or owner -> `recipes/record-brief.md`
- Review a team or manager surface -> `recipes/team-focus.md`
- Prepare or review a meeting -> `recipes/meeting-review.md`
- Review email activity -> `recipes/email-review.md`
- Inspect or change action items -> `recipes/action-items.md`
- Update CRM safely -> `recipes/safe-crm-update.md`

## Dependencies

Read `../revenue-grid-platform/SKILL.md` before working with artifact or fact semantics.

## Read When Needed

- Choosing between summaries, facts, artifacts, raw communications, and query rules -> `references/evidence-sources.md`
- Artifact and fact semantics -> `../revenue-grid-platform/SKILL.md`

## Notes

- Do not assume a fixed CRM schema.
- Do not fetch summaries, artifacts, transcripts, and full bodies all at once.
- If a higher-level source is enough, stop there.
