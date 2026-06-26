"""Tip jar page: a thin UI over logic.tip_jar."""

import streamlit as st

from logic.tip_jar import split_tips_by_hours

DEFAULT_TOTAL_TIPS = 250.0
DEFAULT_STAFF_COUNT = 3
MIN_STAFF_COUNT = 1


def render() -> None:
    """Render the tip jar page."""
    st.title("Tip Jar")
    st.write("Split a cafe's pooled weekly tips among staff by hours worked.")

    total_tips = st.number_input("Total pooled tips ($)", min_value=0.0, value=DEFAULT_TOTAL_TIPS, step=1.0)
    staff_count = st.number_input("Number of staff", min_value=MIN_STAFF_COUNT, value=DEFAULT_STAFF_COUNT, step=1)

    staff_hours: dict[str, float] = {}
    for index in range(int(staff_count)):
        st.subheader(f"Staff member {index + 1}")
        name = st.text_input("Name", value=f"Staff {index + 1}", key=f"staff_name_{index}")
        hours = st.number_input("Hours worked", min_value=0.0, value=0.0, step=0.5, key=f"staff_hours_{index}")
        staff_hours[name] = hours

    if not st.button("Split tips"):
        return

    shares = split_tips_by_hours(total_tips, staff_hours)
    st.subheader("Tip breakdown")
    for staff, amount in shares.items():
        st.write(f"{staff}: ${amount:.2f}")

    st.metric("Total distributed", f"${sum(shares.values()):.2f}")
