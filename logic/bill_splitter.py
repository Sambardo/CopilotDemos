"""Pure bill-splitting logic, kept separate from the Streamlit UI."""

PERCENT_DIVISOR = 100
CENTS_PER_DOLLAR = 100


def split_evenly(total: float, people: int, tip_percent: float) -> list[float]:
    """Split a bill plus tip evenly, returning per-person amounts that sum to the total."""
    if people <= 0:
        raise ValueError("people must be a positive integer")
    if total < 0:
        raise ValueError("total must not be negative")
    if tip_percent < 0:
        raise ValueError("tip_percent must not be negative")

    grand_total = total * (1 + tip_percent / PERCENT_DIVISOR)
    total_cents = round(grand_total * CENTS_PER_DOLLAR)
    base_cents, remainder = divmod(total_cents, people)

    shares = [base_cents + (1 if i < remainder else 0) for i in range(people)]
    return [cents / CENTS_PER_DOLLAR for cents in shares]
