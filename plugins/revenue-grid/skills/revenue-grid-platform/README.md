# Skill: revenue-grid-platform

Explains how Revenue Grid's Revenue Action Platform (RAP) data fits together: CRM records, emails, meetings, facts, and AI outputs. It also covers how to query that data through the MCP tools.

## When It Activates

This skill loads automatically (it is not user-invocable) when a user asks about their accounts, deals, contacts, meetings, emails, pipeline, or team, or wants to change CRM records or action items.

## Contents

```
revenue-grid-platform/
├── SKILL.md                    # Data model, query rules, where to look, reconstructing a record's history
├── recipes/                    # Task guides, loaded one at a time
│   ├── action-items.md         # Reviewing, creating, and resolving action items
│   ├── crm-update.md           # Changing CRM fields, and what an update result means
│   ├── emails.md               # Finding and reading emails, help with a reply
│   ├── meetings.md             # Finding, preparing for, and reviewing meetings
│   ├── pipeline.md             # Deal lists, forecasts, win rates, and team views
│   ├── record-brief.md         # Briefing on one account, deal, or contact
│   └── stakeholders.md         # Roles, coverage gaps, and who knows whom
└── references/
    └── ai-outputs.md           # What each AI output means and how far to trust it
```

## Design Notes

SKILL.md holds what applies to every task: how records, communications, links, and facts relate, when data arrives and expires, how visibility affects results, and how to write filters. Recipes hold only what is specific to one task.

To reconstruct a record's history, the skill reads either top down or bottom up:

- **Top down**, for what changed and why: summary progression, then facts, then raw communications only when needed.
- **Bottom up**, for who, when, and how often: email and meeting headers and snippets first, then the AI content for the items that matter.

CRM updates write with the user's own CRM permissions. Revenue Grid re-imports a changed record 15 or more minutes later, so the skill does not read records back to confirm an update.
