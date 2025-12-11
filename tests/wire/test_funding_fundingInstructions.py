from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_funding_fundingInstructions_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_instructions.list(
        before="2571", after="8516", limit=1, date_from="2024-07-01", date_to="2024-07-03"
    )
    verify_request_count(
        "GET",
        "/funding-instructions",
        {"before": "2571", "after": "8516", "limit": "1", "dateFrom": "2024-07-01", "dateTo": "2024-07-03"},
        1,
    )


def test_funding_fundingInstructions_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_instructions.create(idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324")
    verify_request_count("POST", "/funding-instructions", None, 1)


def test_funding_fundingInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_instructions.retrieve(1)
    verify_request_count("GET", "/funding-instructions/1", None, 1)


def test_funding_fundingInstructions_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_instructions.update(1)
    verify_request_count("PUT", "/funding-instructions/1", None, 1)


def test_funding_fundingInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_instructions.delete(1)
    verify_request_count("DELETE", "/funding-instructions/1", None, 1)
