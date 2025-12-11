from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_owners_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.owners.retrieve(1)
    verify_request_count("GET", "/owners/1", None, 1)


def test_boarding_owners_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.owners.update(
        1,
        first_name="Jane",
        middle_name="Helen",
        last_name="Doe",
        date_of_birth="1964-03-22",
        address={
            "address1": "1 Example Ave.",
            "address2": "Example Address Line 2",
            "address3": "Example Address Line 3",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postalCode": "60056",
        },
        identifiers=[{"type": "nationalId", "value": "000-00-4320"}],
        contact_methods=[{"value": "jane.doe@example.com", "type": "email"}],
        relationship={"equityPercentage": 48.5, "title": "CFO", "isControlProng": True, "isAuthorizedSignatory": False},
    )
    verify_request_count("PUT", "/owners/1", None, 1)


def test_boarding_owners_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.owners.delete(1)
    verify_request_count("DELETE", "/owners/1", None, 1)
