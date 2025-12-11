from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_subscriptions_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.list(
        "1234001",
        customer_name="Sarah%20Hazel%20Hopper",
        last_4="7062",
        payment_plan="Premium%20Club",
        frequency="weekly",
        status="active",
        end_date="2025-07-01",
        next_due_date="2024-08-01",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/processing-terminals/1234001/subscriptions",
        {
            "customerName": "Sarah%20Hazel%20Hopper",
            "last4": "7062",
            "paymentPlan": "Premium%20Club",
            "frequency": "weekly",
            "status": "active",
            "endDate": "2025-07-01",
            "nextDueDate": "2024-08-01",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_subscriptions_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.create(
        "1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        subscription_id="SubRef7654",
        payment_plan_id="PlanRef8765",
        payment_method={"token": "1234567890123456789", "type": "secureToken"},
        name="Premium Club",
        description="Premium Club subscription",
        setup_order={
            "orderId": "OrderRef6543",
            "amount": 4999,
            "description": "Initial setup fee for Premium Club subscription",
            "breakdown": {"subtotal": 4347, "taxes": [{"type": "rate", "rate": 5, "name": "Sales Tax"}]},
        },
        recurring_order={
            "amount": 4999,
            "description": "Monthly Premium Club subscription",
            "breakdown": {"subtotal": 4347, "taxes": [{"type": "rate", "rate": 5, "name": "Sales Tax"}]},
        },
        start_date="2024-07-02",
        end_date="2025-07-01",
        length=12,
        pause_collection_for=0,
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/processing-terminals/1234001/subscriptions", None, 1)


def test_payments_subscriptions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.retrieve("1234001", "SubRef7654")
    verify_request_count("GET", "/processing-terminals/1234001/subscriptions/SubRef7654", None, 1)


def test_payments_subscriptions_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.partially_update(
        "1234001",
        "SubRef7654",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}],
    )
    verify_request_count("PATCH", "/processing-terminals/1234001/subscriptions/SubRef7654", None, 1)


def test_payments_subscriptions_deactivate() -> None:
    """Test deactivate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.deactivate("1234001", "SubRef7654")
    verify_request_count("POST", "/processing-terminals/1234001/subscriptions/SubRef7654/deactivate", None, 1)


def test_payments_subscriptions_reactivate() -> None:
    """Test reactivate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.reactivate("1234001", "SubRef7654")
    verify_request_count("POST", "/processing-terminals/1234001/subscriptions/SubRef7654/reactivate", None, 1)


def test_payments_subscriptions_pay() -> None:
    """Test pay endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.subscriptions.pay(
        "1234001",
        "SubRef7654",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        order={
            "orderId": "OrderRef6543",
            "amount": 4999,
            "description": "Monthly Premium Club subscription",
            "breakdown": {"subtotal": 4999, "taxes": [{"name": "Sales Tax", "rate": 5}]},
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count("POST", "/processing-terminals/1234001/subscriptions/SubRef7654/pay", None, 1)
