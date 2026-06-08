# Skill: revenue-grid-workflows

Operational workflow skill for Revenue Grid's MCP tool sequences. Provides Claude with the correct evidence source ordering, sequencing rules, and step-by-step recipes for common RAP tasks involving CRM data, meetings, emails, and action items.

## When It Activates

This skill loads automatically (it is not user-invocable) when a user asks to:

- Summarize a deal, account, contact, or opportunity
- Review a past meeting or prepare for an upcoming one
- Check email or communication activity around a record
- See what a rep, team member, or direct report is working on
- List, create, or resolve action items
- Change a CRM field such as close date, stage, or owner

## Contents

```
revenue-grid-workflows/
├── SKILL.md                          # Global rules, evidence ladder, and task routing
├── recipes/                          # Step-by-step workflow guides loaded by task
│   ├── action-items.md               # Reviewing, creating, and resolving action items
│   ├── email-review.md               # Reviewing email activity around a record
│   ├── meeting-review.md             # Meeting prep and post-meeting review
│   ├── record-brief.md               # Concise record summaries (account, contact, deal)
│   ├── resolve-record.md             # Finding and identifying a CRM record or person
│   ├── safe-crm-update.md            # Writing CRM field changes with confirmation gates
│   └── team-focus.md                 # Team and manager-level activity surfaces
└── references/                       # Supporting rules loaded as needed
    └── evidence-sources.md           # When to use summaries vs. facts vs. raw communications; OData query rules
```

## Design Notes

SKILL.md acts as a router, not a detailed guide. It loads immediately when a task is recognized and routes to the appropriate recipe. Recipes are loaded individually per task — Claude does not load all seven at once.

The **evidence ladder** (defined in SKILL.md) governs source selection across all recipes: start at the highest-level source that can answer the question and descend only when necessary. Raw email bodies and full transcripts are always a last resort.

The `safe-crm-update` recipe enforces an explicit confirmation gate before any write. CRM updates are treated as destructive and require a `current -> proposed` diff shown to the user before execution.

This skill depends on `revenue-grid-platform` for artifact and fact semantics. Both skills load together when operational tasks require conceptual understanding.
