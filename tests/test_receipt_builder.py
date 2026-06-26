"""Tests for logic.receipt_builder."""

import pytest

from logic.receipt_builder import apply_tax, build_receipt, subtotal


def test_subtotal_sums_item_prices():
    """Subtotal sums the prices for multiple items."""
    items = [
        {"name": "Latte", "price": 4.50},
        {"name": "Croissant", "price": 3.25},
    ]

    assert subtotal(items) == 7.75


def test_empty_subtotal_is_zero():
    """Subtotal for an empty order is zero."""
    assert subtotal([]) == 0.0


def test_apply_tax_uses_rate():
    """Tax is calculated from amount and rate."""
    assert apply_tax(10.00, 0.10) == 1.00


def test_build_receipt_returns_totals():
    """A receipt includes subtotal, tax, and total."""
    receipt = build_receipt(
        [
            {"name": "Coffee", "price": 3.00},
            {"name": "Muffin", "price": 2.50},
        ],
        0.10,
    )

    assert receipt["subtotal"] == 5.50
    assert receipt["tax"] == 0.55
    assert receipt["total"] == 6.05


def test_negative_item_price_raises():
    """A negative item price raises ValueError."""
    with pytest.raises(ValueError):
        subtotal([{"name": "Refund", "price": -1.00}])


def test_negative_amount_raises():
    """A negative amount raises ValueError."""
    with pytest.raises(ValueError):
        apply_tax(-1.00, 0.10)


def test_negative_rate_raises():
    """A negative tax rate raises ValueError."""
    with pytest.raises(ValueError):
        apply_tax(10.00, -0.10)