from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_contacts_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.contacts.retrieve(1)
    verify_request_count("GET", "/contacts/1", None, 1)


def test_boarding_contacts_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.contacts.update(
        1,
        type="manager",
        first_name="Jane",
        middle_name="Helen",
        last_name="Doe",
        identifiers=[{"type": "nationalId", "value": "000-00-4320"}],
        contact_methods=[{"value": "jane.doe@example.com", "type": "email"}],
    )
    verify_request_count("PUT", "/contacts/1", None, 1)


def test_boarding_contacts_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.contacts.delete(1)
    verify_request_count("DELETE", "/contacts/1", None, 1)
