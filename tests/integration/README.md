# Integration Tests

This directory contains integration tests that run against the Payroc UAT environment.

**NOTE:** This directory is fern-ignored and will not be overwritten during SDK generation.

## Environment Variables

The integration tests require the following environment variables to be set:

- `PAYROC_API_KEY_PAYMENTS` - API key for payment operations
- `PAYROC_API_KEY_GENERIC` - API key for generic operations
- `TERMINAL_ID_AVS` - Terminal ID with AVS enabled
- `TERMINAL_ID_NO_AVS` - Terminal ID without AVS

## Running the Tests

To run all integration tests:

```bash
pytest tests/integration -m integration
```

To run a specific test file:

```bash
pytest tests/integration/card_payments/refunds/test_create.py
```

To run with verbose output:

```bash
pytest tests/integration -m integration -v
```

## Test Structure

The integration tests mirror the structure of the .NET SDK functional tests:

```
tests/integration/
├── __init__.py
├── conftest.py                    # Global fixtures (clients, terminal IDs)
├── README.md                      # This file
├── test_data/                     # JSON test data files
│   └── unreferenced_refund.json
└── card_payments/
    └── refunds/
        ├── __init__.py
        └── test_create.py         # Mirrors CreateTests.cs
```

## Test Data

Test data is stored in JSON files in the `test_data/` directory. These files contain
baseline request data that can be overridden with test-specific values (e.g., unique
idempotency keys, specific terminal IDs).

## Markers

All integration tests are marked with `@pytest.mark.integration` to allow selective
execution.
