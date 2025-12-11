from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment
from datetime import datetime

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.list(
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
        payment_link_id="JZURRJBUPS",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/payments",
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
            "paymentLinkId": "JZURRJBUPS",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="web",
        processing_terminal_id="1234001",
        operator="Jane",
        order={"orderId": "OrderRef6543", "description": "Large Pepperoni Pizza", "amount": 4999, "currency": "USD"},
        customer={
            "firstName": "Sarah",
            "lastName": "Hopper",
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
        },
        payment_method={
            "cardDetails": {
                "device": {"model": "bbposChp", "serialNumber": "1850010868"},
                "rawData": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                "entryMethod": "raw",
            },
            "type": "card",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/payments", None, 1)


def test_payments_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.retrieve("M2MJOG6O2Y")
    verify_request_count("GET", "/payments/M2MJOG6O2Y", None, 1)


def test_payments_adjust() -> None:
    """Test adjust endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.adjust(
        "M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        adjustments=[{"type": "customer"}, {"amount": 4999, "type": "order"}],
    )
    verify_request_count("POST", "/payments/M2MJOG6O2Y/adjust", None, 1)


def test_payments_capture() -> None:
    """Test capture endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.capture(
        "M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        operator="Jane",
        amount=4999,
        breakdown={
            "subtotal": 4999,
            "dutyAmount": 499,
            "freightAmount": 500,
            "items": [{"unitPrice": 4000, "quantity": 1}],
        },
    )
    verify_request_count("POST", "/payments/M2MJOG6O2Y/capture", None, 1)


def test_payments_reverse() -> None:
    """Test reverse endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.reverse("M2MJOG6O2Y", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324", amount=4999)
    verify_request_count("POST", "/payments/M2MJOG6O2Y/reverse", None, 1)


def test_payments_refund() -> None:
    """Test refund endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.refund(
        "M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        amount=4999,
        description="Refund for order OrderRef6543",
    )
    verify_request_count("POST", "/payments/M2MJOG6O2Y/refund", None, 1)
