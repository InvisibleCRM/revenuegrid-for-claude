# Revenue Grid Plugin

## What This Plugin Does

This plugin gives Claude access to Revenue Grid's **Revenue Action Platform (RAP)** via the MCP protocol. It provides:

- **MCP tools** for querying CRM records, meetings, emails, facts, action items, and pipeline artifacts — and for writing CRM updates safely.
- **Two skills** that activate automatically to guide Claude through RAP concepts and workflows.

## MCP Server

| Field | Value |
|---|---|
| Server name | `revenue-grid` |
| Endpoint | `https://mcp.revenuegrid.com/mcp` |
| Transport | HTTP |

The MCP server exposes tools for CRM queries, meeting artifacts, email lists, action item management, pipeline suggestions, and CRM updates. Claude reads tenant metadata at runtime — no schema configuration is required.

## Skills

### `revenue-grid-platform`

Foundational knowledge skill covering RAP's core concepts. Activates automatically when a user asks about how RAP works, what artifacts mean, how facts accumulate, or how intelligent linking operates.

See [`skills/revenue-grid-platform/README.md`](skills/revenue-grid-platform/README.md) for details.

### `revenue-grid-workflows`

Operational workflow skill providing step-by-step MCP tool sequences for common RAP tasks. Activates when a user asks to summarize a record, review a meeting, inspect action items, or update CRM fields.

See [`skills/revenue-grid-workflows/README.md`](skills/revenue-grid-workflows/README.md) for details.

## Prerequisites

- Access to the Revenue Grid environment with Revenue Action Platform enabled.
