"""Tip jar page.

"""

import streamlit as st

from logic.tip_jar import split_tips_by_hours

DEFAULT_TOTAL_TIPS = 250.0
DEFAULT_STAFF_COUNT = 3
DEFAULT_HOURS = 8.0
MIN_STAFF_COUNT = 1
MIN_HOURS = 0.0
MIN_TIPS = 0.0
STAFF_COUNT_STEP = 1
MONEY_STEP = 1.0
HOURS_STEP = 0.5
DISPLAY_INDEX_OFFSET = 1


def render() -> None:
    """Render the tip jar page."""
    st.title("Tip Jar")
    st.write("Split a cafe's pooled weekly tips among staff by hours worked.")

    total_tips = st.number_input(
        "Total pooled tips ($)",
        min_value=MIN_TIPS,
        value=DEFAULT_TOTAL_TIPS,
        step=MONEY_STEP,
    )
    staff_count = st.number_input(
        "Number of staff",
        min_value=MIN_STAFF_COUNT,
        value=DEFAULT_STAFF_COUNT,
        step=STAFF_COUNT_STEP,
    )

    staff_entries: list[tuple[str, float]] = []
    for index in range(int(staff_count)):
        display_index = index + DISPLAY_INDEX_OFFSET
        st.markdown(f"**Staff member {display_index}**")
        name_column, hours_column = st.columns(2)
        with name_column:
            name = st.text_input("Name", value=f"Staff {display_index}", key=f"staff_name_{index}")
        with hours_column:
            hours = st.number_input(
                "Hours worked",
                min_value=MIN_HOURS,
                value=DEFAULT_HOURS,
                step=HOURS_STEP,
                key=f"staff_hours_{index}",
            )
        staff_entries.append((name.strip(), hours))

    if not st.button("Split tips"):
        return

    names = [name for name, _ in staff_entries]
    if len(names) != len(set(names)):
        st.error("Staff names must be unique")
        return

    try:
        # Pour the UI inputs into the pure logic before serving the breakdown.
        staff_hours = dict(staff_entries)
        shares = split_tips_by_hours(total_tips, staff_hours)
    except ValueError as error:
        st.error(str(error))
        return

    st.subheader("Tip breakdown")
    for name, amount in shares.items():
        st.write(f"{name}: ${amount:.2f}")

    st.metric("Total distributed", f"${sum(shares.values()):.2f}")
