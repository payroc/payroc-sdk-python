from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_currencyConversion_retrieve_fx_rates() -> None:
    """Test retrieveFxRates endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.currency_conversion.retrieve_fx_rates(
        channel="web",
        processing_terminal_id="1234001",
        operator="Jane",
        base_amount=10000,
        base_currency="USD",
        payment_method={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
    )
    verify_request_count("POST", "/fx-rates", None, 1)
