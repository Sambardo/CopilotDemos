# Copilot instructions

This is a small Streamlit multi-page app used to demo GitHub Copilot live. Follow these conventions when adding or changing code.

## Architecture
- `app.py` is the entry point: a sidebar routes between pages.
- `views/` holds one module per page. Each view exposes a single `render()` function and contains only UI code.
- `logic/` holds pure, testable functions. Business logic lives here, never in a view.
- `tests/` holds pytest tests for the `logic/` package.

## Code style
- Python 3.11+, PEP 8.
- Type hints on all function signatures.
- One-line docstrings on every function.
- Prefer early returns over nested if/else.
- No magic numbers — use module-level named constants.
- Never hard-wrap comments, docstrings, or prose mid-sentence. Write each sentence, paragraph, or bullet as one line and let the editor soft-wrap. Only break at real boundaries (new paragraph, new bullet, new heading).

## Views
- Each `views/*.py` exposes exactly one `render()` function.
- Views call into `logic/`; they never implement business rules themselves.
- Keep the UI layer thin.

## Tests
- Use pytest.
- Name tests `test_<behavior>`.
- Each test is independent and asserts one behavior.

## The pattern to copy
`logic/bill_splitter.py` + `views/bill_splitter.py` together are the reference pattern. When asked to "add a new tool," mirror that structure: a pure function in `logic/`, a thin `render()` in `views/`, and pytest tests for the logic.
