"""Pure tip-pool logic for the cafe tip jar.

A cafe pools all tips for the week and splits them among the staff who
worked, proportional to the hours each person worked that week.

"""

CENTS_PER_DOLLAR = 100


def split_tips_by_hours(total_tips: float, staff_hours: dict[str, float]) -> dict[str, float]:
    """Split pooled weekly tips among staff in proportion to hours worked."""
    if total_tips < 0:
        raise ValueError("total_tips must not be negative")
    if not staff_hours:
        raise ValueError("staff_hours must include at least one staff member")

    for name, hours in staff_hours.items():
        if not name.strip():
            raise ValueError("staff names must not be blank")
        if hours < 0:
            raise ValueError("staff hours must not be negative")

    hours_total = total_hours(staff_hours)
    if hours_total <= 0:
        raise ValueError("total staff hours must be greater than zero")

    total_cents = round(total_tips * CENTS_PER_DOLLAR)
    raw_shares = {
        name: total_cents * hours / hours_total for name, hours in staff_hours.items()
    }
    share_cents = {name: int(raw_share) for name, raw_share in raw_shares.items()}
    remainder = total_cents - sum(share_cents.values())

    # Add the last few cents where the crema is thickest: largest fractions first.
    staff_by_fraction = sorted(
        raw_shares,
        key=lambda name: (raw_shares[name] - share_cents[name], name),
        reverse=True,
    )
    for name in staff_by_fraction[:remainder]:
        share_cents[name] += 1

    return {name: cents / CENTS_PER_DOLLAR for name, cents in share_cents.items()}


def total_hours(staff_hours: dict[str, float]) -> float:
    """Return the total hours worked across all staff."""
    return sum(staff_hours.values())
