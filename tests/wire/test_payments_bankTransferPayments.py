from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment
from datetime import datetime

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_bankTransferPayments_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_payments.list(
        processing_terminal_id="1234001",
        order_id="OrderRef6543",
        name_on_account="Sarah%20Hazel%20Hopper",
        last_4="7890",
        date_from=datetime.fromisoformat("2024-07-01T00:00:00+00:00"),
        date_to=datetime.fromisoformat("2024-07-31T23:59:59+00:00"),
        settlement_state="settled",
        settlement_date="2024-07-15",
        payment_link_id="JZURRJBUPS",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/bank-transfer-payments",
        {
            "processingTerminalId": "1234001",
            "orderId": "OrderRef6543",
            "nameOnAccount": "Sarah%20Hazel%20Hopper",
            "last4": "7890",
            "dateFrom": "2024-07-01T00:00:00Z",
            "dateTo": "2024-07-31T23:59:59Z",
            "settlementState": "settled",
            "settlementDate": "2024-07-15",
            "paymentLinkId": "JZURRJBUPS",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_bankTransferPayments_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_payments.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        order={
            "orderId": "OrderRef6543",
            "description": "Large Pepperoni Pizza",
            "amount": 4999,
            "currency": "USD",
            "breakdown": {
                "subtotal": 4347,
                "tip": {"type": "percentage", "percentage": 10},
                "taxes": [{"name": "Sales Tax", "rate": 5}],
            },
        },
        customer={"notificationLanguage": "en", "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}]},
        credential_on_file={"tokenize": True},
        payment_method={
            "nameOnAccount": "Shara Hazel Hopper",
            "accountNumber": "1234567890",
            "routingNumber": "123456789",
            "type": "ach",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/bank-transfer-payments", None, 1)


def test_payments_bankTransferPayments_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_payments.retrieve("M2MJOG6O2Y")
    verify_request_count("GET", "/bank-transfer-payments/M2MJOG6O2Y", None, 1)


def test_payments_bankTransferPayments_reverse() -> None:
    """Test reverse endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_payments.reverse(
        "M2MJOG6O2Y", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324"
    )
    verify_request_count("POST", "/bank-transfer-payments/M2MJOG6O2Y/reverse", None, 1)


def test_payments_bankTransferPayments_refund() -> None:
    """Test refund endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_payments.refund(
        "M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        amount=4999,
        description="amount to refund",
    )
    verify_request_count("POST", "/bank-transfer-payments/M2MJOG6O2Y/refund", None, 1)


def test_payments_bankTransferPayments_represent() -> None:
    """Test represent endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.bank_transfer_payments.represent(
        "M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        payment_method={
            "nameOnAccount": "Shara Hazel Hopper",
            "accountNumber": "1234567890",
            "routingNumber": "123456789",
            "type": "ach",
        },
    )
    verify_request_count("POST", "/bank-transfer-payments/M2MJOG6O2Y/represent", None, 1)
