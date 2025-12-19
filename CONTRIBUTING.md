# Contributing to Payroc API Python SDK

## Getting Started

### Prerequisites

To build and test this source code, you'll need:

- **Python 3.8 or higher** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/)
- **Poetry** (recommended) or pip for dependency management
- A code editor or IDE (e.g., Visual Studio Code, PyCharm, or Sublime Text)

### Building

Clone the repository and install dependencies:

```bash
git clone https://github.com/payroc/payroc-sdk-python.git
cd payroc-sdk-python
pip install -r requirements.txt
```

Or using Poetry:

```bash
poetry install
```

### Project Structure

- `src/payroc/` - Main SDK library
- `tests/` - Test suite
  - `tests/wire/` - Wire tests for API serialization/deserialization
  - `tests/custom/` - Custom feature tests (pagination, client)
  - `tests/security/` - Security tests (credential exposure)
  - `tests/utils/` - Utility tests
- `wiremock/` - WireMock mappings for testing

## Testing

### Prerequisites for Running Tests in VS Code

To run and debug tests directly in VS Code, install the following extensions:

- **[Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - Base Python language support and IntelliSense
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - Enhanced type checking and IntelliSense

#### Quick Setup

We've provided setup scripts to automatically install these extensions. Choose the appropriate script for your operating system:

**Windows (PowerShell):**
```powershell
.\scripts\vscode\setup-extensions.ps1
```

**macOS/Linux (Bash):**
```bash
bash scripts/vscode/setup-extensions.sh
```

After running the script, reload VS Code (`Ctrl+Shift+P` > `Reload Window`) to activate the extensions.

### Test Framework

This project uses **pytest** as the testing framework, with the following utilities:

- **pytest** - Test runner
- **pytest-asyncio** - Async test support
- **WireMock** - HTTP mocking for wire tests

### Running Tests

Execute all tests:

```bash
pytest
```

Run specific test categories:

```bash
# Wire tests (API serialization/deserialization)
pytest tests/wire/

# Custom feature tests
pytest tests/custom/

# Security tests
pytest tests/security/
```

Run tests with coverage:

```bash
pytest --cov=payroc --cov-report=html
```

Run tests with verbose output:

```bash
pytest -v
```

### Test Categories

- **Wire Tests** (`tests/wire/`) - Validate request/response serialization for all API endpoints
- **Custom Tests** (`tests/custom/`) - Test custom features like pagination and client configuration
- **Security Tests** (`tests/security/`) - Ensure credentials are not exposed in logs or errors
- **Utils Tests** (`tests/utils/`) - Test utility functions and helpers

## Code Quality

### Linting and Formatting

We recommend using the following tools:

```bash
# Format code with black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Type checking with mypy
mypy src/

# Linting with flake8
flake8 src/ tests/
```

### Type Hints

This SDK uses type hints throughout. Please ensure all new code includes proper type annotations.

## Development Workflow

1. **Create a branch** for your changes
2. **Write tests** for new functionality
3. **Implement** your changes
4. **Run tests** to ensure everything works
5. **Format code** using black and isort
6. **Submit a pull request**

## Contributing Guidelines

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

### Custom Files

The following files are custom and can be modified:

- `src/payroc/core/custom_pagination.py` - Custom pagination implementation
- `src/payroc/core/oauth_token_provider.py` - OAuth token management
- `src/payroc/core/sentry_integration.py` - Sentry error tracking
- `src/payroc/client.py` - Top-level client with API key authentication
- `tests/custom/` - Custom feature tests
- `tests/wire/` - Wire tests
- `tests/security/` - Security tests

## Questions or Issues?

If you have questions or run into issues, please:

1. Check the [README.md](./README.md) for usage examples
2. Review existing [GitHub Issues](https://github.com/payroc/payroc-sdk-python/issues)
3. Open a new issue with a clear description of the problem

Thank you for contributing to the Payroc Python SDK!
