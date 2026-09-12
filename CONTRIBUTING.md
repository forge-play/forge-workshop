# Contributing

The org keeps a CONTRIBUTING.md in `forge-play/.github`, and GitHub renders it
for every repository there. It never reaches a clone (see `CLAUDE.md`, "Why
this file exists at all"), so what this workshop actually expects is written
here, in the tree.

## Receipts, not claims

The test command is:

    python -m pytest tests/ -q

Run it before you open a PR and quote the result in the PR body. A red run is
a fact worth keeping (`CLAUDE.md`, Rule 3); report it rather than hiding it.

## The Idea-Id commit-trailer convention

A commit that lands an idea recorded in docs/ideas.md carries an
`Idea-Id: <corpus>-ideas-<num>` git trailer (add `Idea-Status: partial` when a
commit only partly lands it). It is the durable join key willow-reconciler
reads; a wrong id is worse than no id, so never type one by hand:

    reconciler id --repo ./ --doc docs/ideas.md --grep "words from the item"
    reconciler install-hook --repo ./        # derives it from a branch named idea-NN

`.github/workflows/trailers.yml` runs `reconciler verify` on every PR and fails
on a trailer that names an item the doc does not contain.

The repo is passed as `./`, not `.`: willow-reconciler reads a bare `.` as a
repo name to resolve beside the checkout, while anything carrying a slash is a
path.
