from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_cards_verify() -> None:
    """Test verify endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.cards.verify(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        operator="Jane",
        card={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
    )
    verify_request_count("POST", "/cards/verify", None, 1)


def test_payments_cards_view_balance() -> None:
    """Test viewBalance endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.cards.view_balance(
        processing_terminal_id="1234001",
        operator="Jane",
        currency="USD",
        card={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
    )
    verify_request_count("POST", "/cards/balance", None, 1)


def test_payments_cards_lookup_bin() -> None:
    """Test lookupBin endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.cards.lookup_bin(
        processing_terminal_id="1234001",
        card={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
    )
    verify_request_count("POST", "/cards/bin-lookup", None, 1)
