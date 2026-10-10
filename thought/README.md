# thought

Get an independent, critical opinion on an idea before acting on it. The agent
checks assumptions, weighs objections and alternatives, and explains its
recommendation. It can agree when the evidence supports your idea.

## Install

```sh
npx skills add ErwannRousseau/skills --skill thought
```

## Use

Append `$thought` to your idea. No extra question or instructions are needed.

```text
I propose replacing X with Y. $thought
```

In Codex, this skill requires explicit invocation. It can investigate in
read-only mode; implementation requires a separate request.
