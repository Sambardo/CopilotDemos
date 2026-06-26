"""Tip jar page.

A cafe pools its weekly tips and splits them among staff in proportion
to hours worked.
"""

import streamlit as st

from logic.tip_jar import split_tips_by_hours, total_hours

DEFAULT_TOTAL_TIPS = 250.0
DEFAULT_STAFF_COUNT = 3
MIN_STAFF_COUNT = 1
DEFAULT_HOURS_WORKED = 20.0
DEFAULT_STAFF_NAMES = ("Alex", "Blair", "Casey")


def render() -> None:
    """Render the tip jar page."""
    st.title("Tip Jar")
    st.write("Split a cafe's pooled weekly tips among staff by hours worked.")

    total_tips = st.number_input(
        "Total pooled tips ($)", min_value=0.0, value=DEFAULT_TOTAL_TIPS, step=1.0
    )
    staff_count = st.number_input(
        "Number of staff", min_value=MIN_STAFF_COUNT, value=DEFAULT_STAFF_COUNT, step=1
    )

    staff_entries: list[tuple[str, float]] = []
    for index in range(int(staff_count)):
        default_name = (
            DEFAULT_STAFF_NAMES[index]
            if index < len(DEFAULT_STAFF_NAMES)
            else f"Staff {index + 1}"
        )
        name_column, hours_column = st.columns(2)
        name = name_column.text_input(
            f"Staff member {index + 1} name", value=default_name
        )
        hours = hours_column.number_input(
            f"Staff member {index + 1} hours",
            min_value=0.0,
            value=DEFAULT_HOURS_WORKED,
            step=1.0,
        )
        staff_entries.append((name.strip(), hours))

    if not st.button("Split tips"):
        return

    staff_hours: dict[str, float] = {}
    for name, hours in staff_entries:
        if not name:
            st.error("Each staff member needs a name.")
            return
        if name in staff_hours:
            st.error("Staff member names must be unique.")
            return
        staff_hours[name] = hours

    try:
        shares = split_tips_by_hours(total_tips, staff_hours)
    except ValueError as error:
        st.error(str(error))
        return

    st.subheader("Tip breakdown")
    for name, amount in shares.items():
        st.write(f"{name}: ${amount:.2f}")

    st.metric("Total hours", f"{total_hours(staff_hours):.2f}")
    st.metric("Total distributed", f"${sum(shares.values()):.2f}")
