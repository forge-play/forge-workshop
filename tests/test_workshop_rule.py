"""The one rule, enforced in CI: a workshop checkout never holds a Nestor
database, and a bundle that has been cut must hold together.

Both assertions call the engine. Nothing here reimplements what
`forge.bundle` already knows — if this file grows logic, the logic belongs
in `forge-play`.
"""
from __future__ import annotations

from pathlib import Path

import pytest

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
    """Once a bundle has been cut, HEAD and bundle.json must agree and the
    digest must recompute where Nestor is installed to recompute it.

    Skipped before the first cut. `bundle.check` reports a missing bundle as
    a problem, which is the right answer for a workshop that has cut one and
    lost it and the wrong one for a workshop that never has — so the
    distinction is drawn here rather than read out of a failure.
    """
    if not (REPO_ROOT / bundle.BUNDLE_DIR / bundle.HEAD_NAME).is_file():
        pytest.skip("nothing cut yet — no .forge/HEAD in the checkout")
    c = bundle.check(REPO_ROOT)
    assert c.ok, "; ".join(c.problems)
