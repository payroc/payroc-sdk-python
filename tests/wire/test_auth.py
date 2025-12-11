from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_auth_retrieve_token() -> None:
    """Test retrieveToken endpoint with WireMock"""
    client = Payroc(
        environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"),
        _token_getter_override=lambda: "test_token",  # Bypass automatic token fetching for auth endpoint
    )
    result = client.auth.retrieve_token(api_key="x-api-key", client_id="client_id", client_secret="client_secret")
    verify_request_count("POST", "/authorize", None, 1)
