# CRM (Pipeline) Artifacts

Pipeline artifacts are RAP's AI outputs around CRM records and revenue execution. They are meant to help users understand where a record stands, what may happen next, and what needs attention.

## CRM Object Summaries

CRM Object Summaries give users a compact view of a record's current state.

They usually combine two kinds of understanding:

- **Current-state view** for what matters now
- **Progression view** for how the record has evolved over time

The value of a summary is not just compression. It helps users see the business story of the record without reading every communication or field update.

## Close Date Predictions

Close Date Predictions express RAP's view of timing and momentum for time-bound records such as opportunities.

Common statuses include:

| Status | Product meaning |
|---|---|
| **On Track** | The record appears aligned with its expected timing. |
| **Pulled In** | The record appears likely to close sooner than expected. |
| **Pushed Out** | The record appears likely to close later than expected. |
| **Predicted Lost** | The record appears unlikely to close successfully. |
| **Will Be Analyzed Soon** | RAP does not yet have enough context for a meaningful prediction. |

These predictions help users understand timing risk, urgency, and momentum rather than treating the CRM close date as a static truth.

## Stage Predictions

Stage Predictions express RAP's view of where a record belongs in the business process.

- They compare the current CRM stage with the communication and fact pattern around the record.
- They help surface when a record appears ahead of, behind, or misaligned with its stated stage.
- They are most useful when users want a reality check on process progression.

## Action Items

Action Items are concrete pieces of follow-through that the tenant team is expected to complete.

- They usually reflect commitments, requests, or promised deliverables.
- They are more operational than strategic.
- They can change over time as the underlying situation changes.

For a dedicated explanation, see `action-items.md`.

## Next Steps

Next Steps describe the most meaningful business moves that should advance a CRM record.

- They are directional and strategic.
- They are about what would materially move the record forward.
- They are not the same as every small follow-up task.

Next Steps help users focus on progress, not just activity.

## Required Actions

Required Actions highlight issues or risks that need attention.

- They describe what is pressing or blocking progress.
- They are a prioritization signal rather than a plan.
- They help users distinguish between ordinary follow-up and situations that deserve closer attention.

In other words, Next Steps point toward progress, while Required Actions point toward urgency or risk.

## Communication Snippets

Communication Snippets are very short summaries of emails or meetings.

- They are designed for scanning rather than deep understanding.
- They help users move quickly through activity history.
- They are useful as a lightweight preview, not as a substitute for a full artifact.

## What The Agent Should Know

Pipeline artifacts are not all trying to answer the same question.

- Summary answers: **What is going on?**
- Close Date Prediction answers: **When does this appear likely to happen?**
- Stage Prediction answers: **Where does this appear to be in the process?**
- Action Items answer: **What follow-through exists?**
- Next Steps answer: **What should move the record forward?**
- Required Actions answer: **What needs attention right now?**

This distinction matters when the agent explains RAP outputs or compares them to one another.
