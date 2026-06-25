"""Tests for logic.bill_splitter.split_evenly."""

import pytest

from logic.bill_splitter import split_evenly


def test_even_split_no_tip():
    """An evenly divisible bill with no tip splits into equal shares."""
    assert split_evenly(90.0, 3, 0.0) == [30.0, 30.0, 30.0]


def test_uneven_split_distributes_remainder():
    """An uneven split spreads leftover cents and still sums to the total."""
    shares = split_evenly(100.0, 3, 0.0)
    assert shares == [33.34, 33.33, 33.33]
    assert round(sum(shares), 2) == 100.0


def test_tip_is_applied():
    """A tip percentage is added before splitting."""
    assert split_evenly(100.0, 2, 10.0) == [55.0, 55.0]


def test_uneven_split_with_tip_sums_to_grand_total():
    """An uneven split with tip still sums to the grand total."""
    shares = split_evenly(100.0, 3, 18.0)
    assert round(sum(shares), 2) == 118.0


def test_zero_people_raises():
    """Splitting among zero people raises ValueError."""
    with pytest.raises(ValueError):
        split_evenly(100.0, 0, 0.0)


def test_negative_people_raises():
    """Splitting among a negative number of people raises ValueError."""
    with pytest.raises(ValueError):
        split_evenly(100.0, -1, 0.0)
