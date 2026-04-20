## Structure

```
_team.md              # norms, message format, character file contract
_orchestrator.md      # routing logic and retro cycle
dirksen/
  _dirksen.md         # character file
  inbox.md            # incoming tasks
  log.md              # completed work
ronnie/               # same structure
leib/                 # same structure
retro/                # dated retrospective documents
```
## How it works

- Agents communicate via `inbox.md` files only
- Completed tasks generate a `log.md` entry — what was done, friction, self-note
- Personality grows from logs, not from the user rewriting character files
- The orchestrator reads logs, writes retrospectives, and proposes patches to character files
- Trust is earned: routing priority increases with track record