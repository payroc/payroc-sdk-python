from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_singleUseTokens_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.single_use_tokens.create(
        "1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="web",
        operator="Jane",
        source={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
    )
    verify_request_count("POST", "/processing-terminals/1234001/single-use-tokens", None, 1)
