"""The one rule, enforced in CI: a workshop checkout never holds a Nestor
database, and a bundle that has been cut must hold together.

Both assertions call the engine. Nothing here reimplements what
`forge.bundle` already knows — if this file grows logic, the logic belongs
in `forge-play`.
"""
from __future__ import annotations

from pathlib import Path

from forge import bundle

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_no_database_in_the_checkout() -> None:
    """docs/design/the-forge-workshop.md, @constraint severity=critical.

    The live database stays home under `paths.project_nestor(<id>)`. What
    the repository carries is the exported bundle, which is shape.
    """
    found = bundle.find_databases(REPO_ROOT)
    assert found == [], (
        "a Nestor database is in the checkout: "
        + ", ".join(found)
        + " — the live store stays home; the repo carries .forge/bundle.json"
    )


def test_the_bundle_holds_together() -> None:
    """The bundle and the head agree, and the digest recomputes.

    Three states, so this asserts rather than skips: `uncut` before the first
    cut, `ok` after one, `failed` for a half-pair, a bad digest, or a database
    in the checkout. Before forge-play 0.4.0 a fresh workshop reported the
    missing files as a failure and this test had to step around it.
    """
    c = bundle.check(REPO_ROOT)
    assert c.state in ("uncut", "ok"), f"state={c.state}: " + "; ".join(c.problems)
    assert c.ok, "; ".join(c.problems)
