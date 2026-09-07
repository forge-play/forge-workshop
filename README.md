# What is the first bite?

Type the answer as one sentence, and the workshop will argue with you about it.

```
pip install -e .
python -m forge.entry "<your sentence>" --project <this-repo-name> --builder <you>
```

That call is the whole of it. Nestor is asked first or the call refuses; the
project store is created on this call and did not exist a minute before; the
keyword scan finds a major or asks you once, and your answer is recorded with
your name on it.

## The one rule

**The live store stays home. This repository carries the bundle.**

The database lives at `~/.forge/projects/<project-id>/nestor/keep/nestor.db`
and holds content — every draft's text, every rationale you typed, every
rejection's reason. The repository carries `.forge/bundle.json` and
`.forge/HEAD`, which are shape: questions, commitments, edges, warrants with
their recipes and digests, rejections, and the ledger chain they were cut at.

A workshop checkout never contains a Nestor database. `tests/test_workshop_rule.py`
fails the build if one appears, and the engine refuses to diff against one.

The project id is this repository's name. Nothing declares it, so nothing can
drift from it — and a rename orphans the store on purpose, visibly, rather than
quietly pointing at the wrong one.

## What is here

| file | why |
|---|---|
| `pyproject.toml` | depends on `forge-play`. The engine is a package, not a fork. |
| `.forge/` | the bundle and the ledger head it was cut at. Absent until the first cut. |
| `.github/workflows/tests.yml` | so a merged PR has check runs for the deposit to read |
| `CLAUDE.md` | the rules, in the tree. The org's copies never reach a clone. |
| `.mcp.json.example` | Nestor first, willow second. No orchestrator seat. |
| `tests/` | yours. One test ships, and it guards the rule above. |
| `LICENSE` | Apache-2.0, matching the engine. Replace it: your workshop is your work. |

On instantiation, copy `.mcp.json.example` to `.mcp.json` and replace
`WORKSHOP_NAME` in it with this repository's name. The live config is
gitignored on purpose — an MCP config carries box-local paths. That is the
only setup the layout asks for.

There is no code in this repository and there should not be. If a file here
grows logic, it belongs in the engine.

## After the first bite

Decide, build, open a PR. The merge deposits how CI went and what connected to
what. Then cut the bundle at the ledger head and commit it beside the code —
that commit is the first thing the store pull can read.
