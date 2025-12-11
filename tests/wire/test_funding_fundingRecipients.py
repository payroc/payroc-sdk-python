from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_funding_fundingRecipients_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.list(before="2571", after="8516", limit=1)
    verify_request_count("GET", "/funding-recipients", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_funding_fundingRecipients_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        recipient_type="privateCorporation",
        tax_id="123456789",
        doing_business_as="doingBusinessAs",
        address={
            "address1": "1 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postalCode": "60056",
        },
        contact_methods=[{"value": "jane.doe@example.com", "type": "email"}],
        owners=[
            {
                "firstName": "Jane",
                "lastName": "Doe",
                "dateOfBirth": "1964-03-22",
                "address": {
                    "address1": "1 Example Ave.",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postalCode": "60056",
                },
                "identifiers": [{"type": "nationalId", "value": "xxxxx4320"}],
                "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
                "relationship": {"isControlProng": True},
            }
        ],
        funding_accounts=[
            {"type": "checking", "use": "credit", "nameOnAccount": "Jane Doe", "paymentMethods": [{"type": "ach"}]}
        ],
    )
    verify_request_count("POST", "/funding-recipients", None, 1)


def test_funding_fundingRecipients_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.retrieve(1)
    verify_request_count("GET", "/funding-recipients/1", None, 1)


def test_funding_fundingRecipients_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.update(
        1,
        recipient_type="privateCorporation",
        tax_id="123456789",
        doing_business_as="doingBusinessAs",
        address={
            "address1": "1 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postalCode": "60056",
        },
        contact_methods=[{"value": "jane.doe@example.com", "type": "email"}],
    )
    verify_request_count("PUT", "/funding-recipients/1", None, 1)


def test_funding_fundingRecipients_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.delete(1)
    verify_request_count("DELETE", "/funding-recipients/1", None, 1)


def test_funding_fundingRecipients_list_accounts() -> None:
    """Test listAccounts endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.list_accounts(1)
    verify_request_count("GET", "/funding-recipients/1/funding-accounts", None, 1)


def test_funding_fundingRecipients_create_account() -> None:
    """Test createAccount endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.create_account(
        1,
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        type="checking",
        use="credit",
        name_on_account="Jane Doe",
        payment_methods=[{"type": "ach"}],
    )
    verify_request_count("POST", "/funding-recipients/1/funding-accounts", None, 1)


def test_funding_fundingRecipients_list_owners() -> None:
    """Test listOwners endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.list_owners(1)
    verify_request_count("GET", "/funding-recipients/1/owners", None, 1)


def test_funding_fundingRecipients_create_owner() -> None:
    """Test createOwner endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_recipients.create_owner(
        1,
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        first_name="Jane",
        last_name="Doe",
        date_of_birth="1964-03-22",
        address={
            "address1": "1 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postalCode": "60056",
        },
        identifiers=[{"type": "nationalId", "value": "xxxxx4320"}],
        contact_methods=[{"value": "jane.doe@example.com", "type": "email"}],
        relationship={"isControlProng": True},
    )
    verify_request_count("POST", "/funding-recipients/1/owners", None, 1)
