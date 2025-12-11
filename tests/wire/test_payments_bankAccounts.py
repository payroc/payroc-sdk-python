from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_bankAccounts_verify() -> None:
    """Test verify endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_accounts.verify(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        bank_account={
            "nameOnAccount": "Sarah Hazel Hopper",
            "accountNumber": "1234567890",
            "transitNumber": "76543",
            "institutionNumber": "543",
            "type": "pad",
        },
    )
    verify_request_count("POST", "/bank-accounts/verify", None, 1)
