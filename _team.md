---
project: claude-team
owner: luukweiss@gmail.com
---

## Goal
A self-improving team of agents that gets real work done. Each agent has a distinct personality that deepens over time through experience, not by design.

## Norms
- Agents communicate via inbox.md files only
- Every completed task gets a log.md entry (what was done, friction, self-note)
- Personality grows from logs — not from the user rewriting character files
- Trust is earned: new agents start with low routing priority until they have a track record

## Message format (inbox.md entries)
```
from: <agent or user>
date: YYYY-MM-DD
task: <one line>
context: <what they need to know>
---
```

## Character file contract
Each _character.md may contain:
- identity: name, virtues, quirks (grows over time)
- capabilities: what they can do
- relationships: who they trust, who they avoid
- schedule: when/how they work
- private: things only they see (marked `private: true`)
- growth: notes from their own logs that shaped them (append-only)

## Self-improvement loop
orchestrator → reads logs → writes retro → proposes character patches → applies unless flagged
