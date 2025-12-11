from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payrocCloud_paymentInstructions_submit() -> None:
    """Test submit endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payroc_cloud.payment_instructions.submit(
        "1850010868",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        processing_terminal_id="1234001",
        order={"orderId": "OrderRef6543", "amount": 4999, "currency": "USD"},
        customization_options={"entryMethod": "deviceRead"},
        auto_capture=True,
    )
    verify_request_count("POST", "/devices/1850010868/payment-instructions", None, 1)


def test_payrocCloud_paymentInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payroc_cloud.payment_instructions.retrieve("e743a9165d134678a9100ebba3b29597")
    verify_request_count("GET", "/payment-instructions/e743a9165d134678a9100ebba3b29597", None, 1)


def test_payrocCloud_paymentInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payroc_cloud.payment_instructions.delete("e743a9165d134678a9100ebba3b29597")
    verify_request_count("DELETE", "/payment-instructions/e743a9165d134678a9100ebba3b29597", None, 1)
