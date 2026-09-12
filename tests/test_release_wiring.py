"""Structural wiring, asserted with the standard library only.

A repository with a numbered idea pile runs `reconciler verify` in CI, or a
dangling `Idea-Id` trailer reads as the strongest landing evidence the
reconciler has (fleet convention `required_when_pile_exists`). This file
checks the wiring is present; it does not reimplement the verifier.
"""
from __future__ import annotations

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IDEAS = REPO_ROOT / "docs" / "ideas.md"
TRAILERS = REPO_ROOT / ".github" / "workflows" / "trailers.yml"


class ReleaseWiring(unittest.TestCase):
    def test_the_pile_is_planted(self) -> None:
        """The plant: this repo carries the pile, so the guard below is
        exercised rather than vacuously true."""
        self.assertTrue(IDEAS.is_file(), f"{IDEAS} is missing")

    def test_trailers_workflow_exists_wherever_the_pile_does(self) -> None:
        if not IDEAS.is_file():
            self.skipTest("no docs/ideas.md — nothing to verify trailers against")
        self.assertTrue(
            TRAILERS.is_file(),
            f"{IDEAS.relative_to(REPO_ROOT)} exists, so "
            f"{TRAILERS.relative_to(REPO_ROOT)} must run `reconciler verify`",
        )


if __name__ == "__main__":
    unittest.main()
