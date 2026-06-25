"""Bill splitter page: a thin UI over logic.bill_splitter."""

import streamlit as st

from logic.bill_splitter import split_evenly

DEFAULT_TOTAL = 100.0
DEFAULT_PEOPLE = 3
DEFAULT_TIP_PERCENT = 18.0
MIN_PEOPLE = 1


def render() -> None:
    """Render the bill splitter page."""
    st.title("Bill Splitter")
    st.write("Split a bill plus tip evenly across a group.")

    total = st.number_input("Total bill ($)", min_value=0.0, value=DEFAULT_TOTAL, step=1.0)
    people = st.number_input(
        "Number of people", min_value=MIN_PEOPLE, value=DEFAULT_PEOPLE, step=1
    )
    tip_percent = st.number_input(
        "Tip (%)", min_value=0.0, value=DEFAULT_TIP_PERCENT, step=1.0
    )

    if not st.button("Split it"):
        return

    shares = split_evenly(total, int(people), tip_percent)
    st.subheader("Per-person breakdown")
    for i, amount in enumerate(shares, start=1):
        st.write(f"Person {i}: ${amount:.2f}")

    st.metric("Total collected", f"${sum(shares):.2f}")
