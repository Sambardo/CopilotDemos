"""Landing page describing the demo app."""

import streamlit as st


def render() -> None:
    """Render the home page."""
    st.title("Copilot Demos")
    st.write(
        "A small collection of tools used to demo GitHub Copilot live. "
        "Use the sidebar to switch between tools."
    )

    st.subheader("Tools")
    st.markdown(
        "- **Bill Splitter** — split a bill plus tip evenly across a group.\n"
        "- **Tip Jar** — split a cafe's pooled weekly tips among staff by hours worked."
    )

    st.info(
        "Each page is a thin UI in `views/` that calls pure functions in `logic/`, "
        "which are covered by tests in `tests/`."
    )
