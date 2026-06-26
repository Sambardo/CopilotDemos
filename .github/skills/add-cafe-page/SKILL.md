---
name: add-cafe-page
description: "Use when adding a new Streamlit cafe page to this project with logic, view, tests, and sidebar routing."
argument-hint: "Name and behavior of the new cafe page"
---

# Add Cafe Page

Use this skill when the user asks to add a new tool or page to the CopilotDemos Streamlit cafe app.

## Workflow

1. Create pure business logic in `logic/<page_name>.py`.
2. Create a thin Streamlit view in `views/<page_name>.py` with exactly one `render() -> None` function.
3. Add focused pytest coverage in `tests/test_<page_name>.py`.
4. Register the page in `app.py` so it appears in the sidebar.
5. Keep calculations and validation in `logic/`, not in `views/`.
6. Run the focused pytest file for the new logic.

## Local Pattern

Use `logic/bill_splitter.py`, `views/bill_splitter.py`, and `tests/test_bill_splitter.py` as the reference pattern for a small page.