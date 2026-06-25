"""Pure tip-pool logic for the cafe tip jar.

A cafe pools all tips for the week and splits them among the staff who
worked, proportional to the hours each person worked that week.

These functions are intentionally left unimplemented so the logic can be
built live during the demo.
"""


def split_tips_by_hours(total_tips: float, staff_hours: dict[str, float]) -> dict[str, float]:
    """Split pooled weekly tips among staff in proportion to hours worked."""
    # DEMO GAP: implement live.
    raise NotImplementedError


def total_hours(staff_hours: dict[str, float]) -> float:
    """Return the total hours worked across all staff."""
    # DEMO GAP: implement live.
    raise NotImplementedError
