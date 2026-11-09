---
name: revenue-grid-platform
description: "How Revenue Grid (RAP) data fits together and how to query it: CRM records, emails, meetings, facts, and AI outputs. Use for any question about the user's accounts, deals, contacts, meetings, emails, pipeline, or team, and before changing CRM records or action items."
user-invocable: false
---

# RAP data

Revenue Grid's Revenue Action Platform (RAP) combines the tenant's CRM, the emails and meetings of
connected users, and AI outputs built from them. This file explains how that data fits together and
how to query it. Task recipes are listed at the end.

## At the start of a conversation

- Call `get_crm_metadata` without `crm_type` once per conversation. It lists the imported CRM types,
  each type's semantic category, and the AI outputs RAP generates for it. Call it with `crm_type`
  once per type before you use that type's fields. Metadata does not change, so reuse what an earlier
  turn already read.
- For questions about the user's own records, such as "my deals" or "my meetings", call
  `get_current_user` once for their CRM user key.

## How the data fits together

**CRM records.** RAP does not have a direct API connection to the underlying CRM system.
Instead it imports a configured (sub)set of CRM types and fields.
CRM changes arrive on schedule, on average from 15 minutes to a couple of hours.
Closed and historical records are kept, and deleted records disappear.
A field missing from metadata was never imported and cannot be read any other way.
A CRM key is `{"type": "...", "id": "..."}`.

Find types by their semantic category, since type names vary by tenant:

- `what (flow)` is deal-like.
- `what (persistent, company-like)` is account-like.
- `who (external)` is contacts and leads.
- `who (internal)` is CRM users, the user's colleagues.

**Emails and meetings.** RAP captures the mailboxes and calendars of users connected to Revenue Grid.
Some tenants also sync activities from the CRM. A conversation that no connected user took part in is not in RAP.

**Links.** RAP links each email and meeting to CRM records: accounts, deals, contacts, leads, users. Filters reach them through `crm_links`.

- A deal is linked only if it was open when the communication happened. Once a deal closes, new
  communications link only to its account.
- When RAP cannot tell which deal a conversation is about, or the account has 30 or more open deals,
  it links only the account. Cold inbound messages and internal-only threads are often not linked.
- An account's links include its communications as a partner or competitor in other deals.
- Linking finishes a few minutes after an email arrives. A meeting is linked again after its
  transcript is processed, and the links can change.

For a deal, filter on the deal's key. When that returns little, also filter on its account key and
say the figures are account-wide. For a person, filter `recipients` or `attendees` by CRM key. A
person's CRM key is null when their address matched no CRM record or matched several, so fall back to
the email address or domain.

**Facts.** RAP extracts short statements, called facts, from linked emails, meeting transcripts,
some CRM field changes, user notes, and action items. Most AI outputs below are built from them.

- `Side` follows the source, not the speaker. Email facts are external when the email was inbound
  and internal when outbound, whoever is quoted. Transcript facts are external when a customer said
  it. CRM, note, and action-item facts are internal.
- Facts about one deal are linked to the deal and its account. Facts RAP could not place on a deal
  are linked to the account only. Every fact from a communication is also linked to all of that
  communication's contacts, so a contact link does not mean the contact said it.
- `Timestamp` is the email time, the moment in the call, the CRM import time, or, for user notes, the
  time RAP processed the note.
- Some facts only record activity, such as "The meeting ... was held and recorded". Use them to
  confirm that a communication happened.
- RAP rebuilds a communication's facts when its linking changed, so facts are a current snapshot, not
  a log.

**Timing and retention.** New emails get links, snippets, and facts within minutes. Transcripts,
meeting summaries, and transcript facts appear minutes to hours after a meeting ends. Email bodies
and transcripts expire under the tenant's retention policy, 180 days by default. The email record,
its snippet, and its facts remain.

**Visibility.** Every list tool applies the user's CRM visibility rules after pagination. A short page
does not mean there are no more results. An empty page with `skip` below `total_items` means the
matches exist but the user cannot see them. Do not describe or guess at hidden records.

## Querying

- Write filters as bare OData expressions. Quote strings and IDs, not numbers or booleans. Write
  datetimes as `2026-05-01T00:00:00Z`.
- `eq` and `contains` are case-sensitive. Match names with `contains(tolower(Name), 'acme')`.
- Filters compare datetimes in UTC. Results come back in the user's timezone with its offset. For
  "today" or "this week", convert the user's local bounds to UTC with that offset. CRM date fields
  such as close date are stored as midnight UTC.
- Filter by link with `crm_links/any(l: l/CrmType eq 'Opportunity' and l/CrmId eq '<id>')`. To
  list items for several records in one call, use
  `crm_links/any(l: l/CrmType eq 'Opportunity' and (l/CrmId eq '<a>' or l/CrmId eq '<b>'))`. For items
  linked to both A and B, use two separate `any(...)` clauses.
- To count, call with `take=1` and read `total_items`. It counts matches before visibility
  filtering, so present it as approximate. Do not page through results to count them.
- `take` is at most 50. Start with the narrowest window that answers the question, and keep paging
  when the answer needs the full set.
- `search` in `query_crm_data` matches words by prefix in names, and in email addresses for people.
  Only its top 100 hits are filtered further. In `list_appointments` it matches subject, attendees,
  tags, and keywords, not the linked company. `list_emails` has no text search, so filter on links,
  recipients, or `Subject`.
- Name lookups return lookalikes, such as "Rambus" for "ambu". When several records fit, use the
  exact match or ask, and name the record you used.
- Before you report that nothing exists, check the filter: the key type, deal versus account, the
  date window, and cancelled meetings. Say what you searched.

## Where to look

| Question | Start with |
| :--- | :--- |
| Field values, owners, amounts, stages, counts | `query_crm_data` |
| Current state of a record, in prose | `get_crm_summary_sections` |
| What changed on a record and when | `get_crm_summary_progression` |
| Whether a deal will close on time, at its stage | `get_revenue_iq_suggestions` |
| Customer health of an account-like record | `get_crm_health_artifacts` |
| Who is involved and who knows whom | `get_crm_people_relationships` |
| Follow-ups the team owes | `list_action_items` |
| Recent meetings or meetings with a person | `list_appointments` |
| What happened in a meeting, or prep for one | `get_appointment_artifacts` |
| Exact words said in a meeting | `get_meeting_transcript_or_notes` |
| Email activity and who replied | `list_emails` |
| What the customer said or asked over time | `list_facts` |
| Notes the user's team wrote in Revenue Grid | `get_crm_user_notes` |
| The user's direct and indirect reports | `get_user_reports` |

Call independent tools in parallel. A tool named here can be missing when the tenant's plan lacks
that feature. Then say so and use the closest other source.

## Reconstructing what happened

A record's history can be read at three levels. Higher levels are already interpreted and cover
months in one call. Lower levels are complete and exact.

1. Summary progression: dated changes RAP recorded on the record.
2. Facts: dated statements from each linked email, meeting, CRM change, and note.
3. Communications: email and meeting headers with snippets, and last of all, email bodies and
   transcripts.

Choose the direction by the question.

- **Top down**, for what changed, why, and what was agreed.
  Read the progression first, then facts for the period or point you need to support.
  Open an email body or transcript only for exact wording, or when the higher levels say nothing
  about the point.
- **Bottom up**, for who talked to whom, when, and how often: the last contact, gaps in engagement,
  unanswered emails, or a complete timeline of a period. List emails and meetings without bodies
  first. Headers give participants, direction, dates, and subjects, and snippets give the gist.
  Then get the meaning of the items that matter from meeting summaries, or from the facts of one
  communication, with `appointment/Id eq '<id>'` or `email/ThreadId eq '<id>'`.

Go bottom up also when a record has no progression, or its latest entry is older than the latest
activity.
AI outputs lag communications by minutes to hours.

## AI outputs

RAP generates these in the background. Most carry an `inference_date` or timestamp, so say how old an output is when that matters.
A missing output means RAP has not generated one. It is not evidence about the record.
The metadata overview lists which outputs each CRM type has, so do not request outputs a type lacks.

- **Summary** sections describe a record's current state by topic, such as risks and decision
  process. The progression timeline records dated changes.
- **Revenue IQ suggestions** on deals: a close-date prediction, a stage prediction, open next steps, and an action priority.
- **Health** on account-like records: Healthy, Caution, or At Risk, with next steps and an action priority.
- **Relationship IQ** on deals and accounts: roles of external contacts and the strength of each colleague-to-contact connection.
- **Meeting** prep before a meeting, and a summary and eval after it.
- **Action items**: concrete follow-ups the team owes, extracted from communications or created by users.

Read `references/ai-outputs.md` before you explain what an output means, compare it with the CRM, or rely on its values in a recommendation.

## Recipes

Load the recipe that matches the request together with this file.

- Brief on an account, deal, or contact: `recipes/record-brief.md`
- Pipeline, forecast, win rate, or a team's deals: `recipes/pipeline.md`
- Find, prepare for, or review meetings: `recipes/meetings.md`
- Email history, last contact, or context for a reply: `recipes/emails.md`
- Stakeholders, roles, and who knows whom: `recipes/stakeholders.md`
- Review, create, or resolve action items: `recipes/action-items.md`
- Change CRM fields: `recipes/crm-update.md`

## Product names

Users may ask about RAP features by name. Revenue IQ covers CRM summaries and deal predictions.
Meetings IQ covers meeting prep, summaries, and evals.
Relationship IQ covers stakeholder roles and connection strength.
Kora AI is the assistant inside the Revenue Grid app.
