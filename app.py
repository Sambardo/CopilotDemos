"""Streamlit entry point: sidebar navigation between pages."""

import streamlit as st

from views import bill_splitter, home, receipt_builder, tip_jar

PAGES = {
    "Home": home.render,
    "Bill Splitter": bill_splitter.render,
    "Tip Jar": tip_jar.render,
    "Receipt Builder": receipt_builder.render,
}


def main() -> None:
    """Route to the page selected in the sidebar."""
    st.sidebar.title("Copilot Demos")
    choice = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[choice]()


main()
