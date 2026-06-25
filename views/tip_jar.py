"""Tip jar page.

STUBBED OUT for live building. A cafe pools its weekly tips and splits
them among staff in proportion to hours worked. Wire this UI up to
logic.tip_jar during the demo.
"""

import streamlit as st


def render() -> None:
    """Render the tip jar page."""
    st.title("Tip Jar")
    st.write("Split a cafe's pooled weekly tips among staff by hours worked.")

    # DEMO GAP: collect total pooled tips for the week.

    # DEMO GAP: collect each staff member's name and hours worked.

    # DEMO GAP: on button press, call logic.tip_jar.split_tips_by_hours and
    # show each staff member's share.

    st.info("This tool is not built yet — coming together live in the demo.")
