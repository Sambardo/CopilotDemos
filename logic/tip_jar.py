"""Pure tip-pool logic for the cafe tip jar.

A cafe pools all tips for the week and splits them among the staff who
worked, proportional to the hours each person worked that week.

"""

from math import floor

CENTS_PER_DOLLAR = 100


def split_tips_by_hours(total_tips: float, staff_hours: dict[str, float]) -> dict[str, float]:
    """Split pooled weekly tips among staff in proportion to hours worked."""
    if total_tips < 0:
        raise ValueError("total_tips must not be negative")
    if not staff_hours:
        raise ValueError("staff_hours must not be empty")
    if any(not name.strip() for name in staff_hours):
        raise ValueError("staff names must not be empty")
    if any(hours <= 0 for hours in staff_hours.values()):
        raise ValueError("hours worked must be positive")

    hours_worked = total_hours(staff_hours)
    total_cents = round(total_tips * CENTS_PER_DOLLAR)
    exact_cents = [total_cents * hours / hours_worked for hours in staff_hours.values()]
    base_cents = [floor(share) for share in exact_cents]
    remaining_cents = total_cents - sum(base_cents)
    remainder_order = sorted(
        range(len(base_cents)),
        key=lambda index: (-(exact_cents[index] - base_cents[index]), index),
    )

    for index in remainder_order[:remaining_cents]:
        base_cents[index] += 1

    return {
        name: cents / CENTS_PER_DOLLAR
        for (name, _), cents in zip(staff_hours.items(), base_cents)
    }


def total_hours(staff_hours: dict[str, float]) -> float:
    """Return the total hours worked across all staff."""
    if any(hours < 0 for hours in staff_hours.values()):
        raise ValueError("hours worked must not be negative")

    return sum(staff_hours.values())
