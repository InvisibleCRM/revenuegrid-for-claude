# Revenue Grid Plugin

## What This Plugin Does

This plugin gives Claude access to Revenue Grid's **Revenue Action Platform (RAP)** via the MCP protocol. It provides:

- **MCP tools** for querying CRM records, meetings, emails, facts, action items, and pipeline artifacts — and for writing CRM updates safely.
- **A skill** that activates automatically to guide Claude through RAP data and common tasks.

## MCP Server

| Field | Value |
|---|---|
| Server name | `revenue-grid` |
| Endpoint | `https://mcp.revenuegrid.com/mcp` |
| Transport | HTTP |

The MCP server exposes tools for CRM queries, meeting artifacts, email lists, action item management, pipeline suggestions, and CRM updates. Claude reads tenant metadata at runtime — no schema configuration is required.

## Skills

### `revenue-grid-platform`

Covers how RAP data fits together and how to query it: CRM records, emails, meetings, facts, and AI outputs. It includes task recipes for record briefs, meetings, emails, pipeline and team views, stakeholders, action items, and CRM updates. It activates for any question about the user's accounts, deals, contacts, meetings, emails, pipeline, or team.

See [`skills/revenue-grid-platform/README.md`](skills/revenue-grid-platform/README.md) for details.

## Prerequisites

- Access to the Revenue Grid environment with Revenue Action Platform enabled.
