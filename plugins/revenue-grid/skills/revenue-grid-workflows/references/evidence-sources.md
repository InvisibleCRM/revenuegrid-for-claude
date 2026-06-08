# Evidence Sources

Use the cheapest source that can answer the question.

## Decision criteria

**Use CRM summaries** (`get_crm_summary_sections`, `get_crm_summary_progression`) when:
- The question is about current state of a record ("where does this deal stand?")
- You need a fast, high-signal view without reading raw activity
- The record has enough communication history for RAP to have generated a summary

**Use meeting or CRM artifacts** (`get_pipeline_suggestions`, `get_appointment_artifacts`) when:
- You need action priority, required actions, next steps, or close-date signals
- You are preparing for or debriefing after a meeting
- You need RAP's forward-looking view rather than a historical summary

**Use facts** when:
- The question requires sourced evidence from a specific time window
- You need to show where a claim came from (not just what it is)
- A summary exists but is insufficient for the level of detail the user needs

**Use raw email bodies, transcripts, or notes** only when:
- The user needs exact language from a communication
- No artifact or fact covers the time window or topic
- A higher-level source explicitly is missing for the record

## General principle

Stop at the highest level that answers the question. Do not descend to facts when a summary answers it. Do not read full bodies when snippets answer it.

For the meaning of summaries, facts, and artifacts, read `../revenue-grid-platform/SKILL.md` and its references.

## Query Rules

- Read CRM metadata before any CRM query or update that uses a concrete `crm_type`.
- Do not invent field names from memory, generic CRM knowledge, or user wording.
- Before using `select_fields`, `filter`, or `orderby`, read CRM metadata.
- Request only the fields you need.
- Prefer exact IDs once you have them.
- Prefer recent date windows over unbounded history.
- Prefer small page sizes first.
- OData inputs should be expressions only — do not include query-string prefixes like `$filter=`.
- Use ISO 8601 dates and datetimes without OData v2 wrappers like `datetime'...'`.
- Quote strings, not UUIDs, booleans, or numbers.
- Use each tool description as the source of truth for supported fields, navigation paths, sorting limits, and tool-specific constraints.
