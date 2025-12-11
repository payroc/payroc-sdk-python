from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_secureTokens_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.secure_tokens.list(
        "1234001",
        secure_token_id="MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        customer_name="Sarah%20Hazel%20Hopper",
        phone="2025550165",
        email="sarah.hopper@example.com",
        token="296753123456",
        first_6="453985",
        last_4="7062",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/processing-terminals/1234001/secure-tokens",
        {
            "secureTokenId": "MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
            "customerName": "Sarah%20Hazel%20Hopper",
            "phone": "2025550165",
            "email": "sarah.hopper@example.com",
            "token": "296753123456",
            "first6": "453985",
            "last4": "7062",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_secureTokens_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.secure_tokens.create(
        "1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        mit_agreement="unscheduled",
        customer={
            "firstName": "Sarah",
            "lastName": "Hopper",
            "dateOfBirth": "1990-07-15",
            "referenceNumber": "Customer-12",
            "billingAddress": {
                "address1": "1 Example Ave.",
                "address2": "Example Address Line 2",
                "address3": "Example Address Line 3",
                "city": "Chicago",
                "state": "Illinois",
                "country": "US",
                "postalCode": "60056",
            },
            "shippingAddress": {
                "recipientName": "Sarah Hopper",
                "address": {
                    "address1": "1 Example Ave.",
                    "address2": "Example Address Line 2",
                    "address3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postalCode": "60056",
                },
            },
            "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
            "notificationLanguage": "en",
        },
        ip_address={"type": "ipv4", "value": "104.18.24.203"},
        source={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/processing-terminals/1234001/secure-tokens", None, 1)


def test_payments_secureTokens_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.secure_tokens.retrieve("1234001", "MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa")
    verify_request_count(
        "GET", "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa", None, 1
    )


def test_payments_secureTokens_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.secure_tokens.delete("1234001", "MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa")
    verify_request_count(
        "DELETE", "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa", None, 1
    )


def test_payments_secureTokens_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.secure_tokens.partially_update(
        "1234001",
        "MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}],
    )
    verify_request_count(
        "PATCH", "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa", None, 1
    )


def test_payments_secureTokens_update_account() -> None:
    """Test updateAccount endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.secure_tokens.update_account(
        "1234001",
        "MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request={
            "token": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            "type": "singleUseToken",
        },
    )
    verify_request_count(
        "POST",
        "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa/update-account",
        None,
        1,
    )
