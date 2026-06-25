"""Tests for logic.tip_jar."""

import pytest

from logic.tip_jar import split_tips_by_hours, total_hours


def test_total_hours_sums_staff_hours():
    """Total hours returns the sum of all staff hours."""
    assert total_hours({"Avery": 8.0, "Blake": 6.5}) == 14.5


def test_split_tips_by_hours_splits_proportionally():
    """Tips are split in proportion to hours worked."""
    shares = split_tips_by_hours(120.0, {"Avery": 8.0, "Blake": 4.0})
    assert shares == {"Avery": 80.0, "Blake": 40.0}


def test_split_tips_by_hours_distributes_leftover_cents():
    """Rounding leftovers are distributed while preserving the total."""
    shares = split_tips_by_hours(100.0, {"Avery": 1.0, "Blake": 1.0, "Casey": 1.0})
    assert shares == {"Avery": 33.33, "Blake": 33.33, "Casey": 33.34}
    assert round(sum(shares.values()), 2) == 100.0


def test_split_tips_by_hours_rejects_negative_tips():
    """Negative pooled tips raise ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(-1.0, {"Avery": 1.0})


def test_split_tips_by_hours_rejects_empty_staff():
    """An empty staff list raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(10.0, {})


def test_split_tips_by_hours_rejects_blank_staff_name():
    """A blank staff name raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(10.0, {" ": 1.0})


def test_split_tips_by_hours_rejects_negative_hours():
    """Negative staff hours raise ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(10.0, {"Avery": -1.0})


def test_split_tips_by_hours_rejects_zero_total_hours():
    """A staff list with no worked hours raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(10.0, {"Avery": 0.0})
