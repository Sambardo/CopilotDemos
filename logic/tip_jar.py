"""Pure tip-pool logic for the cafe tip jar.

A cafe pools all tips for the week and splits them among the staff who
worked, proportional to the hours each person worked that week.
"""

CENTS_PER_DOLLAR = 100


def total_hours(staff_hours: dict[str, float]) -> float:
    """Return the total hours worked across all staff."""
    return sum(staff_hours.values())


def split_tips_by_hours(total_tips: float, staff_hours: dict[str, float]) -> dict[str, float]:
    """Split pooled weekly tips among staff in proportion to hours worked."""
    if total_tips < 0:
        raise ValueError("total_tips must not be negative")
    if not staff_hours:
        raise ValueError("staff_hours must not be empty")

    hrs_total = total_hours(staff_hours)
    if hrs_total <= 0:
        raise ValueError("total hours worked must be positive")

    total_cents = round(total_tips * CENTS_PER_DOLLAR)
    allocated = 0
    result: dict[str, float] = {}
    staff = list(staff_hours.items())

    for i, (name, hours) in enumerate(staff):
        if i == len(staff) - 1:
            cents = total_cents - allocated
        else:
            cents = round(total_cents * hours / hrs_total)
            allocated += cents
        result[name] = cents / CENTS_PER_DOLLAR

    return result
