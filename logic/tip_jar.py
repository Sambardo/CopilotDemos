"""Pure tip-pool logic for the cafe tip jar.
A cafe pools all tips for the week and splits them among the staff who worked, proportional to the hours each person worked that week.
"""


def split_tips_by_hours(total_tips: float, staff_hours: dict[str, float]) -> dict[str, float]:
    """Split pooled weekly tips among staff in proportion to hours worked."""
    total = total_hours(staff_hours)
    if total == 0:
        return {staff: 0 for staff in staff_hours}
    return {staff: (hours / total) * total_tips for staff, hours in staff_hours.items()}


def total_hours(staff_hours: dict[str, float]) -> float:
    """Return the total hours worked across all staff."""
    return sum(staff_hours.values())
