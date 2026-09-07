# This workshop

A workshop is where the first question gets asked. The engine is a
dependency (`forge-play`), not a fork — everything that runs here ships in
that package, and this repository is a layout.

## Why this file exists at all

The org keeps `CONTRIBUTING.md`, `SECURITY.md`, the issue templates and the
pull request template in `forge-play/.github`. GitHub renders those into the
web UI for every repository in the org, and that inheritance is real — for
humans.

It does not reach you. Those files live in a *different repository*; a clone
of this one does not contain them, so an agent reading the working tree sees
none of them. Anything you are actually expected to follow has to be written
here, in the tree, or it may as well not exist.

## Rule 1 — Nestor is the first tool, not an available one

Ask Nestor before you search the tree, and before you reach for the network.
`forge.entry` enforces the first half: it refuses to start a build that never
asked (`the-forge-shape.md` §11). The rest is on you.

Nestor answers one question — **has a human checked this?**

- `sealed` — a named person verified it. Serve it verbatim and cite them.
- `draft` — machine-produced. Never present it as verified.
- `pending` — nothing verified matched. Say so rather than improvising.

You may propose. You may not confirm. Sealing is a human act with a name
attached, and a model marking its own output verified would empty the word.

## Rule 2 — the live store stays home

The database is at `~/.forge/projects/<project-id>/nestor/keep/nestor.db`.
This repository carries `.forge/bundle.json` and `.forge/HEAD`, which are
shape, never content.

**A workshop checkout never contains a Nestor database.**
`tests/test_workshop_rule.py` fails the build if one appears, and the engine
refuses to cut a bundle beside the thing the bundle exists to replace. If you
find yourself copying a `.db` in here to make something work, the thing you
are making work is wrong.

The project id is this repository's name. Nothing declares it, so nothing can
drift from it.

## Rule 3 — record the negative

A build that fails is a fact worth keeping. "CI failed at this sha for this
reason" is often the more useful row, and it is the difference between
*nobody ran it* and *it was run and it broke here*. Do not suppress a red
job to make a report look clean; a suite that keeps only green outcomes is
the empty-success trap the Forge exists to avoid.

## Rule 4 — the `Decision:` trailer is a hex prefix, not prose

The PR-time deposit reads `^\s*decision:\s*([0-9a-fA-F]{8,})\s*$` from the PR
body — a pair id prefix from the project store, 8 or more hex characters.
Prose does not match and is discarded in silence. One trailer per line;
repeat the line for more than one. If there is no decision to point at,
delete the line rather than inventing a value.

## Rule 5 — nothing here grows logic

If a file in this repository has logic in it, it belongs in the engine. Open
an issue against `forge-play/Forge` instead of working around it here — a
workaround in a template is a workaround copied into every workshop
instantiated from it afterwards.

## The commands

```
python -m forge.entry "<sentence>" --project <repo-name> --builder <you>
forge-export --repo-root . --check      # uncut | ok | failed
forge-export --project-id <repo-name> --repo-root .   # cut the bundle
```
