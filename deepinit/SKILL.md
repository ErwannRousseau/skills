---
name: deepinit
description: Map a repository and structure its AGENTS.md guidance.
disable-model-invocation: true
---

# deepinit

Deeply understand the repository, then create or improve the **smallest useful
hierarchy of `AGENTS.md` files** for future coding agents.

The goal is not comprehensive documentation. Preserve only **non-obvious project
knowledge that materially changes how an agent should work**.

**Deep investigation, sparse documentation.**

## Usage

Use `/deepinit` for the default upsert path. Add a mode when the task needs a
focused path:

```text
/deepinit rebuild
/deepinit audit
/deepinit scope <path>
```

## Scope

Mutating modes write only `AGENTS.md` files. `audit` applies clear, evidence-
backed fixes directly; it reports unresolved or normative choices instead of
silently deciding them. Treat source code, tests, configuration, existing docs,
Git history, issues/PRs, and connected repository context as evidence.

Keep generated or vendored material at its boundary unless project-specific
behavior there needs guidance.

## Modes

### Upsert — default

Audit the existing hierarchy first. Preserve useful human guidance while:

- correct strongly evidenced stale factual claims;
- remove generic, duplicated, obvious, or obsolete guidance;
- move guidance to the scope where it belongs;
- add or remove nested `AGENTS.md` files when knowledge boundaries warrant it.

### Rebuild

When explicitly requested, read all existing `AGENTS.md` files as evidence, then
reconstruct the hierarchy from a fresh repository model. Use it when the current
hierarchy is incoherent, obsolete, duplicated, or missing important boundaries.
It may move or remove `AGENTS.md` files while preserving useful human intent.

Rebuild is not the routine path; default upsert is safer for incremental
maintenance.

### Audit

Audit the hierarchy and apply unambiguous, evidence-backed `AGENTS.md` fixes.
Ask before resolving a normative contradiction. Read
[the progressive-disclosure audit prompt](references/progressive-disclosure-audit.md).

### Scope

Limit reconnaissance and investigation to the requested domain plus the parent
guidance it inherits. Record the local-versus-parent decision and the proposed
delta before writing. Use it for a package, app, or technical boundary such as
`scope packages/api`; it does not rebuild unrelated repository scopes.

## Principles

### Evidence over assumptions

Every project-specific claim written to `AGENTS.md` needs repository evidence.

Infer patterns when multiple signals make them credible. Keep rationale
evidence-bound; when a boundary is clear but its reason is not, document the
boundary without a reason.

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

Write only the local delta for the child scope; parent guidance is inherited.

### Capability-first, path-second

Prefer stable responsibilities, concepts, and boundaries over brittle path
catalogs.

Use a repository-relative path only as an actionable breadcrumb: pair it with
the invariant to preserve and the change that needs it. Omit paths that merely
locate ordinary code, list a directory, or restate the current tree.

### Every line earns its context cost

Before retaining a line, ask:

> Would a future coding agent plausibly behave worse without this?

Remove generic advice, no-ops, duplication, stale detail, vague rules, and
trivially discoverable facts with no added value.

### Source is not guidance

Never paraphrase nearby source, configuration, or tests into `AGENTS.md`. If an
agent can recover the exact behavior cheaply from the relevant scope, omit it;
do not create a local `AGENTS.md` whose only value is a prose copy of code.

A contract or invariant earns guidance only when its durable decision, rationale,
owner, or required cross-boundary action is not apparent from that source and
would otherwise be easy to break. State that non-obvious constraint, not the
currently visible mechanics.

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

Use the best inspection tools available in the current environment. Keep the
workflow independent of any one harness, tool family, or agent API.

**Done when:** the major knowledge boundaries are clear enough to partition
deeper investigation, and the map records project purpose, package/workspace
tooling, non-standard build/typecheck commands, runtime boundaries, existing
`AGENTS.md` files, and disclosed guidance sources.

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

**Done when:** every applicable investigation axis has returned findings,
evidence, placement input, and unresolved questions, or is explicitly marked not
applicable.

### 3. Reconcile

Aggregate findings into one repository model.

Resolve descriptive conflicts from evidence. When normative instructions
conflict and the choice changes behavior, pause and ask the user which version
to keep before writing either one.

Distinguish:

- **descriptive claims** — correct them when strong evidence shows they are
  stale;
- **normative instructions** — preserve explicit human intent unless clearly
  superseded; record the user's choice for any unresolved conflict.

Treat repeated observations as candidates; promote them to conventions only when
evidence supports intent.

Understand generated or vendored code at its boundary, then keep deep
investigation focused on project-owned behavior.

**Done when:** every finding has a status—accepted evidence, stale claim,
explicit human instruction, user-resolved conflict, or unresolved question—and
the repository model contains no silently chosen normative policy.

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

Treat package manifests, configuration, scripts, directory layout, and `--help`
output as sources of truth. Document the unwritten convention, durable reason,
gotcha, or expensive lookup that the environment cannot provide cheaply.

Usually omit full trees, exhaustive file lists, generic framework advice,
standard behavior, and facts easy to recover just-in-time.

Keep these root essentials when evidenced:

- one-sentence project purpose;
- the package manager when it is not npm, including workspace usage;
- non-standard build or typecheck commands;
- instructions relevant to every task in the repository.

Keep language-, package-, and domain-specific detail in nested `AGENTS.md` files
or existing reference docs, reached through a conditional pointer.

**Investigation depth does not determine documentation length.**

**Done when:** every candidate line has a retain, remove, or disclose decision,
with evidence or explicit human intent, and root content contains only the root
essentials plus repository-wide guidance.

### 6. Place

Create the hierarchy from **knowledge scope**.

Root contains only repository-wide guidance.

Create a nested `AGENTS.md` only when local context materially differs from the
parent.

Use existing docs or skills for progressive disclosure. When no suitable
reference exists, use a nested `AGENTS.md` at the domain boundary.

Each pointer names its subject and its trigger, for example: “For TypeScript
changes, see `docs/TYPESCRIPT.md`.” Keep one pointer per distinct branch.

For every significant domain considered, decide consciously:

- local `AGENTS.md` warranted; or
- parent guidance sufficient.

**Done when:** every significant domain has an explicit parent/local/disclosed
decision, every disclosed target exists, and every pointer has a clear trigger.

### 7. Write

Use the following headings as a vocabulary for each `AGENTS.md`. They are
optional: include a section only when evidence supports useful content.

```md
# <scope>

<one-sentence purpose>

<only evidence-backed sections relevant to this scope>
```

Root files start with purpose and essentials; domain files contain only their
local delta. Available headings: `WHERE TO LOOK`, `DISCLOSURE`, `ARCHITECTURE`,
`CONVENTIONS`, `INVARIANTS`, `ANTI-PATTERNS`, `VALIDATION`, and `NOTES`. Choose
only evidence-backed headings and omit empty sections.

#### WHERE TO LOOK

Prefer capabilities and responsibilities over brittle path lists. Use exact
paths only as actionable breadcrumbs for a non-obvious change.

Add a conditional pointer when detailed guidance lives elsewhere.

Use a Markdown link for each disclosed file. Put the condition before the link,
and keep the pointer at the scope that first needs it.

#### ANTI-PATTERNS

Include project-specific approaches that are known to be wrong, dangerous, or
contrary to the repository's intended architecture. Omit this heading unless the
repository proves a concrete local trap, consequence, and safe route that a
competent agent cannot infer from the code or configuration. Omit generic
prohibitions, restatements of the current structure, and ordinary hygiene.

#### NOTES

Include important gotchas, context, or project-specific knowledge that does not
fit naturally in another section.

**Done when:** every selected file contains only accepted, scoped guidance; root
essentials are present when evidenced; conditional pointers resolve; and the
resulting hierarchy is ready for the review gates below.

## Review gates

Review the resulting hierarchy as one merged context.

Verify that:

- every line has project-specific value;
- stale, generic, obvious, and duplicated guidance is gone;
- parent/child duplication is gone;
- inferred conventions have enough evidence;
- rationale is not invented;
- explicit normative guidance is preserved or changed with user confirmation;
- each child contains a real local delta;
- no `AGENTS.md` merely paraphrases source, configuration, or tests that agents
  can inspect cheaply;
- each `ANTI-PATTERNS` entry names an evidenced local trap; absent entries are
  omitted;
- each `ARCHITECTURE` path is an actionable breadcrumb for an invariant, not a
  structural description;
- root contains only repository-wide guidance;
- no file exists merely because a directory is large;
- every disclosed target exists and every pointer names its trigger;
- root essentials are present when evidenced;
- the diff contains only `AGENTS.md` paths.

Prefer the **shortest `AGENTS.md` that preserves all high-value guidance for its
scope**. There are no target line counts.

**Done when:** the merged hierarchy passes every gate above and no unresolved
normative conflict remains unconfirmed by the user.

## Final report

Finish with a compact recap:

```text
deepinit complete

Mode
- default | rebuild | audit | scope

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

Report coverage and documentation decisions. Use file, line, and agent counts
only as operational details, never as quality metrics.
