# AI outputs

What each RAP AI output means, what it is built from, and how far to trust it. RAP regenerates
outputs when new facts arrive, so an output is only as current as the facts behind it.

## Summary and progression

`get_crm_summary_sections` returns topical sections for one record, such as risks, competitors,
qualification, and decision process for a deal. RAP rewrites a section when new facts change it.
Each section's timestamp is the time of the newest fact that changed it, so sections have different
dates and an old date does not mean the summary is stale.

`get_crm_summary_progression` returns dated entries of one to three sentences, each describing a
change. Use it for "what happened since" questions. It skips routine scheduling.

Summaries are written from facts, the record's current CRM fields, and the previous summary. Risk and
qualification sections are RAP's assessment. Their gaps mean the facts did not mention something.

## Revenue IQ suggestions

These exist for deal-like records. RAP generates the close-date and stage predictions in one pass,
so they share a `reason`.

**Close date.** RAP compares its prediction with the CRM close date by fiscal period:

| Status | Meaning |
| :--- | :--- |
| On Track | Likely to close in the same fiscal period as the CRM close date |
| Pulled In | Likely to close in an earlier period |
| Pushed Out | Likely to close in a later period |
| Predicted Lost | Unlikely to close as won |

`suggested_close_date` is the end of the predicted period, not a specific day. It is null when the
prediction stays in the CRM close date's period. A null `close_date_suggestion` means RAP has not
analyzed the deal yet, which the RAP UI shows as "Will Be Analyzed Soon". When the CRM close date has
already passed, RAP predicts only the close date and stage, so expect no new next steps or action
priority.

**Stage.** `suggested_stage_name` is the stage RAP thinks fits the evidence. When it equals
`original_stage_name`, RAP agrees with the CRM. Both are stage API values from metadata.

**Next steps.** Open steps that would move the deal forward. They can be AI-generated or written by
users (`origin`). RAP closes AI steps when they are done or no longer relevant, drops its own steps
when it predicts the deal lost, and cancels every open step when the deal closes.

**Action priority.** High, Medium, or Low urgency, with a short statement of the situation in
`action_priority_details`. No action priority is stored for a deal predicted lost.

Use `include_reasoning=true` when the user asks why. The reasoning covers recent developments,
analysis, and risks. RAP treats the CRM close date as the rep's estimate and weighs engagement and
customer statements above it.

## Health

Health exists for account-like records.

| Status | Meaning |
| :--- | :--- |
| Healthy | Positive signals outweigh negatives, with active two-way engagement |
| Caution | Mixed signals, with mild negatives and no strong ones |
| At Risk | A strong negative signal, such as a complaint, competitor evaluation, escalation, cancellation request, or long unexplained silence |

The health output also carries next steps and an action priority with the same meaning as above. RAP
treats a lack of recent facts as a warning sign, except for new relationships. A Caution or At Risk
rating on a record with little captured activity can reflect missing coverage, so check recent
emails and meetings before calling it a confirmed problem. Health is often weeks old, so compare
`inference_date` with the latest activity.

## Roles and connections

`get_crm_people_relationships` returns roles for external contacts on one record and a strength for
each pair of colleague and contact.

| Role | Meaning on this record |
| :--- | :--- |
| Decision-maker | Final authority, may appear only for approval |
| Champion | Runs the work day to day and drives decisions |
| Legal lead | Owns contracts, legal terms, and compliance |
| Finance lead | Owns pricing, budget, and procurement |
| Influencer | Shapes the outcome through expertise or end-user impact |
| Gatekeeper | Manages access and scheduling, without decision authority |

RAP assigns a role only on clear evidence. An unassigned role, or a role listed under missing
coverage, means the evidence did not show one. It does not mean nobody holds it. The same person can
hold different roles on different records.

Strength is Strong, Medium, or Weak, judged against the contact's role and the deal's phase. It is
not a measure of message volume. A rarely contacted decision-maker can be Strong, and frequent
scheduling with a gatekeeper can be Weak. RAP re-checks Strong and Medium connections as new facts
arrive, so silence can lower them. Not assessed means RAP has no assessment for that pair.

Roles and strengths are current assessments over all history, and the output gives no date for them.
The date window changes only the activity counts and last-touch dates. Inbound and outbound are from
the user's team's perspective.

## Meeting prep, summary, and eval

- **Prep** is generated before a meeting from the linked records' AI outputs, open action items, and
  facts. It reflects what RAP knew when it was generated.
- **Summary** is generated from the transcript or user notes after the meeting. It is null when the
  meeting was not recorded or is still processing.
- **Eval** scores the meeting from 1 to 5 against criteria the tenant configured for that meeting
  type, with recommendations. A criterion missing from the eval was not scored.

The meeting type, tags, and keywords on `list_appointments` are assigned from the transcript, so
meetings without a transcript have none. `rap://meetings/classification` lists the values the tenant
uses.

## Action items

Action items are concrete follow-ups the team owes, such as a promised document or a requested call.
RAP extracts them from internal-side facts and closes them when later facts show the work was done.
Users can also create and resolve them.

- Every item has a responsible user, an internal CRM user. RAP falls back to the record owner when the
  facts do not name one.
- Every item has a due date. When nobody stated a deadline, RAP sets one 14 days after the item was
  last updated, so a due date is often an estimate.
- RAP usually links AI items to the account rather than the deal, and to the meeting they came from.
- Priority comes from the responsible user's ranking. Unranked, new, and manual items are Low, so Low
  often means "not ranked yet".
- `IsResolved eq true` includes items that were cancelled or replaced, not only completed work.

## Comparing outputs with the CRM

When an output disagrees with a CRM field, report both and the evidence for each. Do not overwrite the
user's CRM values or forecast with RAP's view unless they ask.
