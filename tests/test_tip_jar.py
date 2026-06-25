"""Tests for logic.tip_jar."""

import pytest

from logic.tip_jar import split_tips_by_hours, total_hours


def test_total_hours_sums_values():
    """total_hours returns the sum of all hours worked."""
    assert total_hours({"Alice": 40.0, "Bob": 20.0}) == 60.0


def test_total_hours_single_staff():
    """total_hours works with a single staff member."""
    assert total_hours({"Alice": 35.0}) == 35.0


def test_total_hours_empty_returns_zero():
    """total_hours returns 0 for an empty dict."""
    assert total_hours({}) == 0.0


def test_equal_hours_split_evenly():
    """Staff working equal hours receive equal shares."""
    shares = split_tips_by_hours(100.0, {"Alice": 20.0, "Bob": 20.0})
    assert shares == {"Alice": 50.0, "Bob": 50.0}


def test_proportional_split():
    """Tips are split proportionally to hours worked."""
    shares = split_tips_by_hours(120.0, {"Alice": 40.0, "Bob": 20.0})
    assert shares["Alice"] == pytest.approx(80.0, abs=0.01)
    assert shares["Bob"] == pytest.approx(40.0, abs=0.01)


def test_split_sums_to_total():
    """All shares always sum to the total pooled tips."""
    shares = split_tips_by_hours(100.0, {"Alice": 30.0, "Bob": 25.0, "Carol": 15.0})
    assert round(sum(shares.values()), 2) == 100.0


def test_single_staff_receives_all():
    """A single staff member receives the full tip pool."""
    shares = split_tips_by_hours(75.0, {"Alice": 40.0})
    assert shares == {"Alice": 75.0}


def test_negative_tips_raises():
    """Negative total tips raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(-10.0, {"Alice": 40.0})


def test_empty_staff_raises():
    """Empty staff dict raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(100.0, {})


def test_zero_total_hours_raises():
    """Staff all working zero hours raises ValueError."""
    with pytest.raises(ValueError):
        split_tips_by_hours(100.0, {"Alice": 0.0, "Bob": 0.0})
