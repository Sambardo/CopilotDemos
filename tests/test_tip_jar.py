"""Tests for logic.tip_jar."""

import pytest

from logic.tip_jar import split_tips_by_hours, total_hours


def test_total_hours_sums_staff_hours():
    """Total hours returns the sum across staff."""
    assert total_hours({"Alex": 10.5, "Blair": 15.0, "Casey": 8.5}) == 34.0


def test_split_tips_by_hours_evenly_for_equal_hours():
    """Equal hours split pooled tips into equal shares."""
    assert split_tips_by_hours(90.0, {"Alex": 10.0, "Blair": 10.0}) == {
        "Alex": 45.0,
        "Blair": 45.0,
    }


def test_split_tips_by_hours_distributes_leftover_cents():
    """Remainder cents are distributed while preserving the total."""
    shares = split_tips_by_hours(10.0, {"Alex": 1.0, "Blair": 1.0, "Casey": 1.0})
    assert shares == {"Alex": 3.34, "Blair": 3.33, "Casey": 3.33}
    assert round(sum(shares.values()), 2) == 10.0


def test_split_tips_by_hours_uses_proportional_shares():
    """Hours worked determine each staff member's tip share."""
    shares = split_tips_by_hours(20.0, {"Alex": 4.0, "Blair": 6.0})
    assert shares == {"Alex": 8.0, "Blair": 12.0}


def test_split_tips_by_hours_requires_staff():
    """An empty staff mapping raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(20.0, {})


def test_split_tips_by_hours_requires_positive_hours():
    """Zero or negative hours raise ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(20.0, {"Alex": 0.0})

    with pytest.raises(ValueError):
        split_tips_by_hours(20.0, {"Alex": -1.0})


def test_split_tips_by_hours_rejects_negative_total_tips():
    """A negative tip pool raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(-1.0, {"Alex": 5.0})
