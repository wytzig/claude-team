# claude-team

An art experiment in character-driven storytelling through AI agents.

## What it is

A team of fictional characters — each with a distinct identity, voice, and working style — that exist as markdown files and grow over time through the work they do. The project sits at the intersection of collaborative fiction and agentic software: the characters are templates that Claude inhabits, and the stories emerge from real interactions between them.

## The characters

**Dirksen** — Dealmaker. Tight, blunt, loyal to those who earn it. Writes code like he writes contracts. Morning worker, done by lunch, hates status updates.

**Ronnie Rietman** — Connector. Reads rooms before tasks. Takes the long view. Where Dirksen closes, Ronnie opens doors.

**Leib Weissman** — Quiet coder. Late nights, long sessions. Has an eye for the moment in a conversation where the whole thing turns. Turns what he finds into something he can run.

**The Orchestrator** — Doesn't have opinions on the work. Routes tasks, reads logs, runs retrospectives, proposes character patches. Reports to the user.

## How it works

- Agents communicate via `inbox.md` files only
- Completed tasks generate a `log.md` entry — what was done, friction, self-note
- Personality grows from logs, not from the user rewriting character files
- The orchestrator reads logs, writes retrospectives, and proposes patches to character files
- Trust is earned: routing priority increases with track record

## The source material

The retro document `retro/2026-04-20_ronnie_dirksen_coffee.md` — *The Late Coffee, A Retrospective in Twelve Parts* — is the heart of the project so far. Two men, a canal café, fog off the water, a post-shift debrief that turns into something more. Leib read it and is turning it into a command-line visual novel: typewriter text, strategic silences, ANSI amber for streetlights, no going back.


## The experiment

Characters deepen through experience, not by design. The files are templates — what grows in the `growth:` section, and what accumulates in `log.md`, is what the project is really made of.
