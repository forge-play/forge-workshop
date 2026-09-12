# Ideas

The numbered pile for this workshop. It is read by
`reconciler run --repo ./ --doc docs/ideas.md --validate`, which classifies each
item landed / partial / not started against this repository's own git history.

Legend: ✅ shipped · 🟡 partial · (untagged) proposed

**Numbers are permanent join keys.** `reconciler/ids.py` derives
`<corpus>-ideas-<num>` from the number written on the line, so a number is an
identity, not an ordinal. Never renumber; never write a markdown-auto-numbered
list — retire a number instead and leave the gap.

A tag counts only when it leads the item text, and only where git history
shows it. An untagged item is a proposal; the reconciler may still infer a
landing from an `Idea-Id` trailer, and says so as inferred, never as settled.

## A. After the first bite

1. Cut the first bundle at the ledger head and commit `.forge/bundle.json` and `.forge/HEAD` beside the code — `.forge/` is absent until the first cut, and that commit is the first thing the store pull can read (README, "After the first bite").

## B. Fleet conventions

2. adopt `Idea-Id` commit trailers (fleet CONVENTION, decision-2026-09-11)
3. Nestor pin raised to `>=0.20,<1` after S6-nestor-seam (fleet plan Wave 6, S6-pins)
