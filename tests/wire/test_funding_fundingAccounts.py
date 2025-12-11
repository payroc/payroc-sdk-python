from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_funding_fundingAccounts_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_accounts.list(before="2571", after="8516", limit=1)
    verify_request_count("GET", "/funding-accounts", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_funding_fundingAccounts_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_accounts.retrieve(1)
    verify_request_count("GET", "/funding-accounts/1", None, 1)


def test_funding_fundingAccounts_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_accounts.update(
        1, type="checking", use="credit", name_on_account="Jane Doe", payment_methods=[{"type": "ach"}]
    )
    verify_request_count("PUT", "/funding-accounts/1", None, 1)


def test_funding_fundingAccounts_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_accounts.delete(1)
    verify_request_count("DELETE", "/funding-accounts/1", None, 1)
