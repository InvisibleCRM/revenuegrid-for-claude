# Emails

## Find emails

- About a record: filter `crm_links` on its key. Each email lists its `linked_crm_objects`.
- With a person: `recipients/any(r: r/CrmType eq 'Contact' and r/CrmId eq '<id>')`. When the
  person has no CRM key, use `r/EmailAddress eq '<address>'` or a domain match such as
  `contains(tolower(r/EmailAddress), '@acme.com')`.
- Sent by the user: `Type eq 1 and recipients/any(r: r/Type eq 0 and r/CrmType eq 'User' and r/CrmId eq '<user CRM ID>')`.
- One thread: `ThreadId eq '<thread ID>'`.
- On a topic: `contains(tolower(Subject), '<word>')`.
  For a topic discussed inside emails, read the record's email facts (`PrimarySourceType eq 'email'`) over a date window.

## Read

- Triage with snippets and headers first. Request bodies only for the few emails you need to quote
  or read closely, with a narrow filter and a small `take`.
- Bodies are cut at 3000 characters and replies can repeat quoted history. An old email may have no
  body left under retention, while its snippet and facts remain.
- For the last interaction, sort descending and take a few. Report who wrote last, the direction,
  and the date.
- To find unanswered emails, compare the latest inbound and outbound timestamps in the thread.

## Help with a reply

Read the latest emails in the thread with bodies. Check whether the user has already replied before
you suggest a follow-up. If the email refers to a call, read that meeting's summary. You cannot send
email, so give the draft as text.
