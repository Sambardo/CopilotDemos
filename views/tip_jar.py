"""Tip jar page: a thin UI over logic.tip_jar."""

import streamlit as st

from logic.tip_jar import split_tips_by_hours

DEFAULT_TOTAL_TIPS = 200.0
DEFAULT_STAFF_COUNT = 3
MIN_STAFF = 1


def render() -> None:
    """Render the tip jar page."""
    st.title("Tip Jar")
    st.write("Split a cafe's pooled weekly tips among staff by hours worked.")

    total_tips = st.number_input(
        "Total pooled tips ($)", min_value=0.0, value=DEFAULT_TOTAL_TIPS, step=1.0
    )
    num_staff = st.number_input(
        "Number of staff members", min_value=MIN_STAFF, value=DEFAULT_STAFF_COUNT, step=1
    )

    staff_hours: dict[str, float] = {}
    for i in range(int(num_staff)):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(f"Staff member {i + 1} name", value=f"Staff {i + 1}", key=f"name_{i}")
        with col2:
            hours = st.number_input(
                f"Hours worked", min_value=0.0, value=40.0, step=0.5, key=f"hours_{i}"
            )
        if name:
            staff_hours[name] = hours

    if not st.button("Split tips"):
        return

    try:
        shares = split_tips_by_hours(total_tips, staff_hours)
    except ValueError as exc:
        st.error(str(exc))
        return

    st.subheader("Per-staff breakdown")
    for name, amount in shares.items():
        st.write(f"{name}: ${amount:.2f}")

    st.metric("Total distributed", f"${sum(shares.values()):.2f}")
