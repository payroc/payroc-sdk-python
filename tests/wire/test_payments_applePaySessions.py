from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_applePaySessions_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.apple_pay_sessions.create(
        "1234001",
        apple_domain_id="DUHDZJHGYY",
        apple_validation_url="https://apple-pay-gateway.apple.com/paymentservices/startSession",
    )
    verify_request_count("POST", "/processing-terminals/1234001/apple-pay-sessions", None, 1)
