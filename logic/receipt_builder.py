"""Pure receipt-building logic, kept separate from the Streamlit UI."""

TAX_RATE = 0.10
CENTS_PER_DOLLAR = 100

ReceiptItem = dict[str, str | float]
Receipt = dict[str, object]


def subtotal(items: list[ReceiptItem]) -> float:
    """Calculate the subtotal for receipt items."""
    total = 0.0
    for item in items:
        price = float(item["price"])
        if price < 0:
            raise ValueError("item price must not be negative")
        total += price

    return _round_currency(total)


def apply_tax(amount: float, rate: float) -> float:
    """Calculate tax for an amount at the given rate."""
    if amount < 0:
        raise ValueError("amount must not be negative")
    if rate < 0:
        raise ValueError("rate must not be negative")

    return _round_currency(amount * rate)


def build_receipt(items: list[ReceiptItem], rate: float) -> Receipt:
    """Build an itemized receipt with subtotal, tax, and total."""
    receipt_subtotal = subtotal(items)
    tax = apply_tax(receipt_subtotal, rate)
    total = _round_currency(receipt_subtotal + tax)

    return {
        "items": items,
        "subtotal": receipt_subtotal,
        "tax": tax,
        "total": total,
    }


def _round_currency(amount: float) -> float:
    """Round a dollar amount to the nearest cent."""
    return round(amount * CENTS_PER_DOLLAR) / CENTS_PER_DOLLAR