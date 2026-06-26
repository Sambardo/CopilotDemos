"""Tests for logic.tip_jar."""

from logic.tip_jar import split_tips_by_hours, total_hours


def test_total_hours_adds_staff_hours():
    """Total hours adds each staff member's hours."""
    assert total_hours({"Avery": 10.0, "Blake": 15.5, "Casey": 4.5}) == 30.0


def test_split_tips_by_hours_splits_proportionally():
    """Tips are split in proportion to hours worked."""
    shares = split_tips_by_hours(120.0, {"Avery": 10.0, "Blake": 20.0})

    assert shares == {"Avery": 40.0, "Blake": 80.0}


def test_split_tips_by_hours_handles_equal_hours():
    """Staff with equal hours receive equal tip shares."""
    shares = split_tips_by_hours(90.0, {"Avery": 8.0, "Blake": 8.0, "Casey": 8.0})

    assert shares == {"Avery": 30.0, "Blake": 30.0, "Casey": 30.0}


def test_split_tips_by_hours_handles_zero_total_hours():
    """Staff receive zero tips when nobody worked any hours."""
    shares = split_tips_by_hours(100.0, {"Avery": 0.0, "Blake": 0.0})

    assert shares == {"Avery": 0, "Blake": 0}


def test_split_tips_by_hours_handles_empty_staff():
    """An empty staff list returns an empty split."""
    assert split_tips_by_hours(100.0, {}) == {}