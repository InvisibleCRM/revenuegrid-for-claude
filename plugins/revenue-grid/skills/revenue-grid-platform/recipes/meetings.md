# Meetings

## Find meetings

- With a company or deal: filter `crm_links` on its key. Do not search for the company name, since
  `search` does not match linked records.
- With a person: `attendees/any(a: a/CrmType eq 'Contact' and a/CrmId eq '<id>')`. For the user's
  own meetings, use their CRM key.
- On a topic: use `search`, which matches the subject, attendee names and emails, tags, and keywords.
- In a period: filter `Start` with UTC bounds converted from the user's local day. Sort ascending for
  upcoming meetings and descending for past ones.
- Meetings that took place: add `IsCanceled eq false`.
- Customer meetings: add `attendees/any(a: a/IsInternal eq false)`.
- By meeting type, tag, or keyword: read `rap://meetings/classification` for the tenant's values first.

Each result has the organizer, internal and external attendees, linked records, a short snippet, and
the meeting type, tags, and keywords. That is often enough to answer without further calls.

To count meetings, use `take=1` and read `total_items`, and state which filter you counted. Do not
page through meetings to count them.

## Prepare for a meeting

1. Find the meeting and call `get_appointment_artifacts` with `prep`.
2. If prep is missing, or the user wants more, brief the linked records with
   `recipes/record-brief.md` and add the summary of the last meeting with the same people.

## Review a meeting

Call `get_appointment_artifacts` with `summary`, and `eval` when the user asks how the meeting went.
Read the transcript only for exact wording or when the artifacts are missing.

## Transcripts and notes

Call `get_meeting_transcript_or_notes` with `include_transcript=true`, and `include_notes=true` for notes users wrote.
The transcript can be long, so fetch one or two meetings at a time. When the user wants transcripts for many meetings, confirm the list first.
A null transcript means the meeting was not recorded, is still processing (up to four hours after it ends), or the transcript has expired.
