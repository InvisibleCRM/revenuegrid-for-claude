# Stakeholders

For who is involved in a deal or account, their roles, coverage gaps, and which colleague knows a
contact best.

1. Resolve the record and call `get_crm_people_relationships`.
   Omit the dates for all history, or set a window when the user asks about recent engagement.
2. Read roles and missing role coverage before connections. Judge connections by strength and their
   short signal together, not by message counts.
3. If the user asks why a connection has its strength, call the tool again with
   `include_reasoning=true` and the same key and window.

Roles and strengths are RAP's assessment and carry no date. Missing coverage means the evidence did
not show that role, so present it as a question to check with the user's contacts. For a deal with
few linked contacts, also check its account.

Read `references/ai-outputs.md` for what each role and strength means.
