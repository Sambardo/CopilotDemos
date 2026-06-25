# CopilotDemos

A small Streamlit multi-page app used to demo GitHub Copilot features live to new and intermediate users. Logic lives in plain, testable functions under `logic/`; the Streamlit UI layer in `views/` stays thin.

## Structure

- `app.py` — entry point with sidebar navigation.
- `views/` — one module per page, each exposing a `render()` function.
- `logic/` — pure, unit-testable functions.
- `tests/` — pytest tests for the logic.

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser and auto-reloads on save.

## Run the tests

```bash
pytest
```
