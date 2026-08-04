# Backend API Tests

This directory contains pytest-based tests for the FastAPI backend in [src/app.py](../src/app.py).

## What is covered

The tests exercise the API endpoints for:

- redirecting the root route to the static frontend page
- listing activities
- signing up for an activity
- rejecting duplicate signups
- handling missing activities and participants during removal

## Running the tests

From the project root, run:

```bash
source .venv/bin/activate
pytest -q
```

To run a specific test:

```bash
pytest tests/test_api.py::test_signup_success -q
```
