from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment
from datetime import datetime

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_bankTransferRefunds_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_refunds.list(
        processing_terminal_id="1234001",
        order_id="OrderRef6543",
        name_on_account="Sarah%20Hazel%20Hopper",
        last_4="7062",
        date_from=datetime.fromisoformat("2024-07-01T00:00:00+00:00"),
        date_to=datetime.fromisoformat("2024-07-31T23:59:59+00:00"),
        settlement_state="settled",
        settlement_date="2024-07-15",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/bank-transfer-refunds",
        {
            "processingTerminalId": "1234001",
            "orderId": "OrderRef6543",
            "nameOnAccount": "Sarah%20Hazel%20Hopper",
            "last4": "7062",
            "dateFrom": "2024-07-01T00:00:00Z",
            "dateTo": "2024-07-31T23:59:59Z",
            "settlementState": "settled",
            "settlementDate": "2024-07-15",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_bankTransferRefunds_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_refunds.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        order={
            "orderId": "OrderRef6543",
            "description": "Refund for order OrderRef6543",
            "amount": 4999,
            "currency": "USD",
        },
        customer={"notificationLanguage": "en", "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}]},
        refund_method={
            "nameOnAccount": "Shara Hazel Hopper",
            "accountNumber": "1234567890",
            "routingNumber": "123456789",
            "type": "ach",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/bank-transfer-refunds", None, 1)


def test_payments_bankTransferRefunds_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_refunds.retrieve("CD3HN88U9F")
    verify_request_count("GET", "/bank-transfer-refunds/CD3HN88U9F", None, 1)


def test_payments_bankTransferRefunds_reverse() -> None:
    """Test reverse endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_refunds.reverse(
        "CD3HN88U9F", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324"
    )
    verify_request_count("POST", "/bank-transfer-refunds/CD3HN88U9F/reverse", None, 1)
