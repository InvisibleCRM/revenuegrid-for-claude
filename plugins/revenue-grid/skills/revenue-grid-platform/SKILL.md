---
name: revenue-grid-platform
description: This skill should be used when a user asks about how Revenue Grid's Revenue Action Platform (RAP) works, what RAP's core concepts are, how facts, artifacts, intelligent linking, or tenant configuration fit together, or what a Meeting Summary, Meeting Eval, Meeting Prep, Close Date Prediction, Stage Prediction, Action Item, or Next Step means.
user-invocable: false
---

# Revenue Action Platform (RAP)

**Revenue Action Platform** (short name **RAP**) is Revenue Grid's AI layer around customer-facing work. It brings together CRM data, communications, and AI-generated business context so users can understand what is happening across communications and related CRM records.

## Core Concepts

**Tenant.** RAP always operates inside a tenant, which is a single customer organization. Data, configuration, terminology, and AI outputs are all tenant-specific.

**Knowledge Lake.** RAP builds a shared business memory from three layers:

1. **CRM data** such as records, fields, ownership, and lifecycle information
2. **Communications** such as emails, calendar events, and meetings
3. **Facts** which are short business statements extracted from the above

Most RAP outputs are built on top of this combined context rather than on one source alone.

**CRM Key.** RAP refers to CRM records through a CRM Key, a pair of `{object_type, object_id}`. This is how communications, facts, and artifacts stay connected to the right business records.

## Product Areas

- **Pipeline Assistant** helps users understand CRM records through summaries, predictions, priorities, and suggested direction.
- **Meetings Assistant** helps users prepare for meetings, capture what happened, and evaluate how well a conversation moved the business process forward.
- **AI Mentor** gives users a conversational way to work with RAP context across meetings, CRM records, communications, and generated artifacts.

## Tenant Setup and Configuration

RAP adapts to each tenant rather than assuming one universal CRM model.

- It builds a business profile for the tenant, including company identity and market context.
- It analyzes the tenant's CRM structure to understand which record types and fields matter.
- It uses that tenant-specific understanding to decide what RAP should import, reason about, and generate insights for.
- It respects CRM visibility boundaries, so RAP should not expose information a user would not be able to access in the source CRM.

For more detail, see `references/tenant-configuration.md`.

## Intelligent Linking

Intelligent linking gives communications business context by associating them with relevant CRM records.

- It helps RAP understand which account, customer process, or related business record a communication belongs to.
- It provides the context that facts and downstream artifacts inherit.
- It is conservative in ambiguous situations, because an incorrect business association is more damaging than leaving context broad.
- It supports continuity across related communications, so context can carry forward when a conversation evolves over time.

For more detail, see `references/intelligent-linking.md`.

## Fact Extraction

Facts are RAP's reusable business memory.

- A fact captures one useful piece of business information in a self-contained form.
- Facts let RAP accumulate context over time instead of treating each message or meeting as isolated.
- Facts connect raw source material to user-facing artifacts such as summaries, predictions, and meeting outputs.
- Facts are selective and structured. They are not meant to be verbatim copies of transcripts, emails, or notes.

For more detail, see `references/fact-extraction.md`.

## Meeting Artifacts

RAP generates four meeting-focused artifacts (Summary, Prep, Eval, Classification) to support preparation, capture outcomes, and assess meeting quality. See `references/meeting-artifacts.md`.

## CRM (Pipeline) Artifacts

RAP generates CRM-focused artifacts (Object Summaries, Close Date Predictions, Stage Predictions, Action Items, Next Steps, Required Actions, Communication Snippets) to help users manage pipeline execution and business progress. See `references/pipeline-artifacts.md` and `references/action-items.md`.