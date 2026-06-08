# Tenant Configuration

Tenant configuration defines the business boundary within which RAP operates.

## What It Accomplishes

RAP is not built around one fixed CRM model. Tenant configuration is what lets the product adapt to each customer's business reality.

- It defines which CRM structures matter to RAP.
- It shapes what kinds of business records RAP can reason about.
- It influences what communications, facts, and artifacts should be associated with.
- It gives RAP enough company context to speak about the tenant in a grounded way.

Tenant configuration is one of the reasons RAP should be understood as tenant-specific rather than universal.

## Business Profile

RAP maintains a high-level understanding of the tenant itself, such as:

- company identity
- business description
- market context
- notable competitors

This helps RAP interpret customer conversations and generated outputs in the context of the tenant's own business.

## CRM Model Understanding

Tenant configuration also helps RAP understand the customer's CRM model.

- Different tenants may use very different object types.
- The same business idea can be represented differently across CRMs.
- Some tenants organize work around account-like anchors and related process records.
- Others rely more heavily on custom or tenant-specific business objects.

RAP therefore needs tenant-specific guidance about what business objects matter and how they relate to one another.

## Persistent And Flow-Oriented Business Context

At a high level, tenant CRM models often contain two kinds of business records:

- **Persistent context** such as long-lived customer or relationship records
- **Flow-oriented context** such as deals, cases, projects, or other process records that move through a lifecycle

The exact names vary by tenant, but this distinction helps explain how RAP thinks about long-lived relationship context versus process-specific context.

## What Configuration Changes In RAP

Tenant configuration shapes RAP behavior in practical ways:

- what data is imported and available for reasoning
- which business records communications can meaningfully relate to
- which records can have summaries, predictions, or other artifacts
- how RAP should interpret the tenant's business model and terminology

This is why RAP should not assume that all tenants have the same supported object types or the same artifact surface.

## Visibility And Scope

RAP should stay within the tenant's visibility boundaries.

- User-visible RAP context should respect source-system access rules.
- The platform should not assume access to records that fall outside the configured business boundary.
- Missing data may reflect configuration or visibility limits, not necessarily product failure.

## What The Agent Should Know

The most important product assumptions are:

- RAP is tenant-aware and tenant-shaped.
- Not all tenants use the same CRM concepts or object names.
- Product outputs should be interpreted through the tenant's configured business model.
- When something appears absent, unsupported, or unusually broad, tenant configuration may be the reason.

For the agent, tenant configuration is the product context that makes RAP's business understanding possible.