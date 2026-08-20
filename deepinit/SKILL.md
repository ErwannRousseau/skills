---
name: deepinit
description:
  Deep-map a repository and create or improve its AGENTS.md knowledge hierarchy.
---

# deepinit

Deeply understand the repository, then create or improve the **smallest useful
hierarchy of ****`AGENTS.md`**** files** for future coding agents.

The goal is not comprehensive documentation. Preserve only **non-obvious project
knowledge that materially changes how an agent should work**.

**Deep investigation, sparse documentation.**

## Scope

Modify **only ****`AGENTS.md`**** files**.

Use source code, tests, configuration, existing docs, Git history, issues/PRs,
and connected repository context as evidence when useful, but do not modify
them.

## Modes

### Update — default

Audit the existing hierarchy first. Preserve useful human guidance, but freely:

- correct strongly evidenced stale factual claims;
- remove generic, duplicated, obvious, or obsolete guidance;
- move guidance to the scope where it belongs;
- add or remove nested `AGENTS.md` files when knowledge boundaries warrant it.

### Rebuild

When explicitly requested, read all existing `AGENTS.md` files as evidence, then
reconstruct the hierarchy from the repository model.

Rebuild does not discard useful human intent.

## Principles

### Evidence over assumptions

Every project-specific claim written to `AGENTS.md` needs repository evidence.

Infer patterns only when multiple signals make them credible. Do not invent
rationale. If a boundary is clear but its reason is not, document the boundary
without guessing why.

Use Git history or connected issue/PR context only to resolve ambiguity,
establish durable rationale, or verify staleness.

### Knowledge boundaries over filesystem boundaries

Place `AGENTS.md` where **working context changes**, not where directory size
changes.

A local file is warranted when a scope has materially distinct architecture,
conventions, invariants, validation rules, gotchas, anti-patterns, or
technology-specific guidance.

A tiny critical domain may deserve one. A huge conventional directory may not.

**Complexity triggers investigation, not documentation.**

### Child is a delta from parent

Nested files inherit parent guidance.

Do not repeat parent content. A child contains only the local delta for its
scope.

### Capability-first, path-second

Prefer stable responsibilities, concepts, and boundaries over brittle path
catalogs.

Use exact paths when they are stable, non-obvious, and genuinely useful.

### Every line earns its context cost

Before retaining a line, ask:

> Would a future coding agent plausibly behave worse without this?

Remove generic advice, no-ops, duplication, stale detail, vague rules, and
trivially discoverable facts with no added value.

### Sub-agents discover; the parent decides

Run independent investigation axes as **parallel sub-agents** so assumptions and
local context from one axis do not pollute another.

Partition by the repository's actual needs, not a fixed agent template. Give
each sub-agent a distinct question or domain and only the context needed for it.

Scale the number and scope of sub-agents to the repository. Parallelism is for
**context isolation and independent evidence gathering**, not for satisfying a
fixed agent count.

Sub-agents return evidence and findings. The parent owns reconciliation,
placement, wording, and final decisions.

## Workflow

### 1. Reconnaissance

Build an initial repository map before deciding where documentation belongs.

Identify as applicable:

- project purpose and major runtime surfaces;
- packages/workspaces and architectural domains;
- entry points and dependency direction;
- data/state boundaries;
- build, test, and validation shape;
- generated, vendored, or boilerplate-heavy areas;
- existing `AGENTS.md` hierarchy;
- existing docs or skills already carrying detailed guidance.

Use the best inspection tools available in the current environment. Do not bind
the workflow to one harness, tool family, or agent API.

**Done when:** the major knowledge boundaries are clear enough to partition
deeper investigation.

### 2. Parallel investigation

Spawn parallel sub-agents across the independent domains or questions discovered
during reconnaissance.

Useful axes may include architecture, packages/apps, data,
auth/security-sensitive areas, validation, build/deployment, or project-specific
conventions.

Each investigation should return:

- findings that would materially affect future coding work;
- supporting evidence;
- candidate invariants, conventions, validation rules, or gotchas;
- ambiguities or contradictions;
- whether local `AGENTS.md` guidance appears warranted.

### 3. Reconcile

Aggregate findings into one repository model.

When sub-agents conflict, inspect the evidence and resolve the contradiction
yourself.

Distinguish:

- **descriptive claims** — correct them when strong evidence shows they are
  stale;
- **normative instructions** — preserve explicit human intent unless clearly
  superseded; report unresolved contradictions instead of silently inventing
  policy.

Observed repetition alone is not proof of an intended convention.

Understand generated or vendored code at its boundary, then exclude it from deep
investigation unless project-specific behavior there must be preserved.

### 4. Coverage pass

Try to falsify the repository model.

Look for a material architectural boundary, local convention, invariant,
validation rule, or gotcha that is still uncovered.

Launch targeted sub-agent investigations when important gaps or conflicts
remain.

Stop when another meaningful coverage pass finds no material uncovered knowledge
boundary.

**Completion criterion:** every important project-specific fact that could
materially change how a future coding agent works is either covered by validated
evidence or explicitly identified as unresolved.

### 5. Distill

Keep only persistent guidance worth loading on future tasks.

Prioritize:

- non-obvious architecture and boundaries;
- where to make classes of changes;
- project-specific conventions;
- durable rationale when evidenced;
- invariants that must survive refactors;
- special validation requirements;
- dangerous local anti-patterns;
- recurring gotchas.

Usually omit full trees, exhaustive file lists, generic framework advice,
obvious scripts, standard behavior, and facts easy to recover just-in-time.

**Investigation depth does not determine documentation length.**

### 6. Place

Create the hierarchy from **knowledge scope**.

Root contains only repository-wide guidance.

Create a nested `AGENTS.md` only when local context materially differs from the
parent.

Use existing docs or skills for progressive disclosure when useful, but do not
create or modify those external files.

For every significant domain considered, decide consciously:

- local `AGENTS.md` warranted; or
- parent guidance sufficient.

### 7. Write

Use the following structure as the **default for each ****`AGENTS.md`** and
actively look for useful project-specific information for each section:

```md
# <scope>

<one-sentence purpose>

## WHERE TO LOOK

## ARCHITECTURE

## CONVENTIONS

## INVARIANTS

## ANTI-PATTERNS

## VALIDATION

## NOTES
```

Include these sections whenever useful information for them can be established
from the repository. Omit a section only when the investigation found nothing
meaningful to put there; never invent or pad content just to satisfy the
structure.

#### WHERE TO LOOK

Prefer capabilities and responsibilities over brittle path lists. Use exact
paths when they are useful.

#### ANTI-PATTERNS

Include project-specific approaches that are known to be wrong, dangerous, or
contrary to the repository's intended architecture.

#### NOTES

Include important gotchas, context, or project-specific knowledge that does not
fit naturally in another section.

## Review gates

Review the resulting hierarchy as one merged context.

Verify that:

- every line has project-specific value;
- stale, generic, obvious, and duplicated guidance is gone;
- parent/child duplication is gone;
- inferred conventions have enough evidence;
- rationale is not invented;
- explicit normative guidance was not silently overturned;
- each child contains a real local delta;
- root contains only repository-wide guidance;
- no file exists merely because a directory is large;
- referenced files actually exist;
- only `AGENTS.md` files were modified.

Prefer the **shortest ****`AGENTS.md`**** that preserves all high-value guidance
for its scope**. There are no target line counts.

## Final report

Finish with a compact recap:

```text
deepinit complete

Mode
- update | rebuild

Investigated
- major boundaries/domains examined
- targeted follow-up investigations, if any

AGENTS.md
- <path> — created | updated | removed

Deliberately not created
- <scope> — parent guidance is sufficient

Cleaned up
- stale, duplicated, generic, or misplaced guidance corrected/removed

Unresolved
- genuine ambiguities that could not be established from evidence
```

Do not report file counts, line counts, or agent counts as quality metrics.
Report coverage and documentation decisions.
