"""
Global fixtures for integration tests.

This module provides shared fixtures for integration tests that run against
the Payroc UAT environment. API keys and terminal IDs are loaded from
environment variables.

NOTE: This file is in tests/integration which is fern-ignored and will not
be overwritten during SDK generation.
"""

import os
import pytest
from payroc import Payroc, PayrocEnvironment


def get_env(name: str) -> str:
    """
    Get an environment variable or raise an error if not set.
    
    Args:
        name: The name of the environment variable
        
    Returns:
        The value of the environment variable
        
    Raises:
        ValueError: If the environment variable is not set
    """
    value = os.environ.get(name)
    if not value:
        raise ValueError(f"Environment variable '{name}' is not set.")
    return value


@pytest.fixture(scope="session")
def payments_client():
    """
    Create a Payroc client configured for payments using UAT environment.
    
    Requires PAYROC_API_KEY_PAYMENTS environment variable.
    """
    api_key = get_env("PAYROC_API_KEY_PAYMENTS")
    return Payroc(api_key=api_key, environment=PayrocEnvironment.UAT)


@pytest.fixture(scope="session")
def generic_client():
    """
    Create a Payroc client configured for generic operations using UAT environment.
    
    Requires PAYROC_API_KEY_GENERIC environment variable.
    """
    api_key = get_env("PAYROC_API_KEY_GENERIC")
    return Payroc(api_key=api_key, environment=PayrocEnvironment.UAT)


@pytest.fixture(scope="session")
def terminal_id_avs():
    """
    Get the terminal ID with AVS enabled.
    
    Requires TERMINAL_ID_AVS environment variable.
    """
    return get_env("TERMINAL_ID_AVS")


@pytest.fixture(scope="session")
def terminal_id_no_avs():
    """
    Get the terminal ID without AVS.
    
    Requires TERMINAL_ID_NO_AVS environment variable.
    """
    return get_env("TERMINAL_ID_NO_AVS")
