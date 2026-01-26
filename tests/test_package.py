"""Tests for molsim."""

from __future__ import annotations

import molsim


def test_version() -> None:
    """Test that version is defined."""
    assert hasattr(molsim, "__version__")
    assert isinstance(molsim.__version__, str)


def test_all_exports() -> None:
    """Test that __all__ is defined."""
    assert hasattr(molsim, "__all__")
    assert isinstance(molsim.__all__, list)
