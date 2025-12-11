from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment
from datetime import datetime

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_refunds_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.refunds.list(
        processing_terminal_id="1234001",
        order_id="OrderRef6543",
        operator="Jane",
        cardholder_name="Sarah%20Hazel%20Hopper",
        first_6="453985",
        last_4="7062",
        tender="ebt",
        date_from=datetime.fromisoformat("2024-07-01T15:30:00+00:00"),
        date_to=datetime.fromisoformat("2024-07-03T15:30:00+00:00"),
        settlement_state="settled",
        settlement_date="2024-07-02",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/refunds",
        {
            "processingTerminalId": "1234001",
            "orderId": "OrderRef6543",
            "operator": "Jane",
            "cardholderName": "Sarah%20Hazel%20Hopper",
            "first6": "453985",
            "last4": "7062",
            "tender": "ebt",
            "dateFrom": "2024-07-01T15:30:00Z",
            "dateTo": "2024-07-03T15:30:00Z",
            "settlementState": "settled",
            "settlementDate": "2024-07-02",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_refunds_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.refunds.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="pos",
        processing_terminal_id="1234001",
        order={
            "orderId": "OrderRef6543",
            "description": "Refund for order OrderRef6543",
            "amount": 4999,
            "currency": "USD",
        },
        refund_method={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/refunds", None, 1)


def test_payments_refunds_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.refunds.retrieve("CD3HN88U9F")
    verify_request_count("GET", "/refunds/CD3HN88U9F", None, 1)


def test_payments_refunds_adjust() -> None:
    """Test adjust endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.refunds.adjust(
        "CD3HN88U9F",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        adjustments=[{"type": "customer"}],
    )
    verify_request_count("POST", "/refunds/CD3HN88U9F/adjust", None, 1)


def test_payments_refunds_reverse() -> None:
    """Test reverse endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.refunds.reverse("CD3HN88U9F", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324")
    verify_request_count("POST", "/refunds/CD3HN88U9F/reverse", None, 1)
