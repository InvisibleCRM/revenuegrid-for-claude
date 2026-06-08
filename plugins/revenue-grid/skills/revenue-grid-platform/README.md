# Skill: revenue-grid-platform

Foundational knowledge skill for Revenue Grid's Revenue Action Platform (RAP). Provides Claude with the conceptual vocabulary needed to explain and reason about RAP outputs — artifacts, facts, intelligent linking, tenant configuration, and product areas.

## When It Activates

This skill loads automatically (it is not user-invocable) when a user asks about:

- How RAP works, what it is, or how its components fit together
- What a specific artifact means: Meeting Summary, Meeting Prep, Meeting Eval, Close Date Prediction, Stage Prediction, Action Item, Next Step, Required Action
- How facts are extracted or accumulated
- How intelligent linking associates communications with CRM records
- How RAP adapts to a specific tenant's CRM model

## Contents

```
revenue-grid-platform/
├── SKILL.md                          # Core concepts loaded when skill triggers
└── references/                       # Detailed documentation loaded as needed
    ├── action-items.md               # Action Item and Next Step lifecycle and semantics
    ├── fact-extraction.md            # How facts are extracted and what they represent
    ├── intelligent-linking.md        # How communications are associated with CRM records
    ├── meeting-artifacts.md          # Meeting Summary, Prep, Eval, Classification details
    ├── pipeline-artifacts.md         # CRM artifact types and their meaning
    └── tenant-configuration.md       # How RAP adapts to tenant-specific CRM models
```

## Design Notes

This skill is intentionally conceptual rather than operational. It does not prescribe MCP tool sequences — that is the role of the `revenue-grid-workflows` skill. Its purpose is to give Claude a stable, accurate vocabulary for RAP so that explanations, comparisons, and artifact interpretations are consistent with how the platform actually works.

The `revenue-grid-workflows` skill declares a dependency on this skill, so the two load together when operational tasks require semantic understanding of artifacts or facts.
