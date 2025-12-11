from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_paymentPlans_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_plans.list("1234001", before="2571", after="8516", limit=1)
    verify_request_count(
        "GET", "/processing-terminals/1234001/payment-plans", {"before": "2571", "after": "8516", "limit": "1"}, 1
    )


def test_payments_paymentPlans_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_plans.create(
        "1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        payment_plan_id="PlanRef8765",
        name="Premium Club",
        description="Monthly Premium Club subscription",
        currency="USD",
        length=12,
        type="automatic",
        frequency="monthly",
        on_update="continue",
        on_delete="complete",
        custom_field_names=["yourCustomField"],
        setup_order={
            "amount": 4999,
            "description": "Initial setup fee for Premium Club subscription",
            "breakdown": {"subtotal": 4347, "taxes": [{"name": "Sales Tax", "rate": 5}]},
        },
        recurring_order={
            "amount": 4999,
            "description": "Monthly Premium Club subscription",
            "breakdown": {"subtotal": 4347, "taxes": [{"name": "Sales Tax", "rate": 5}]},
        },
    )
    verify_request_count("POST", "/processing-terminals/1234001/payment-plans", None, 1)


def test_payments_paymentPlans_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_plans.retrieve("1234001", "PlanRef8765")
    verify_request_count("GET", "/processing-terminals/1234001/payment-plans/PlanRef8765", None, 1)


def test_payments_paymentPlans_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_plans.delete("1234001", "PlanRef8765")
    verify_request_count("DELETE", "/processing-terminals/1234001/payment-plans/PlanRef8765", None, 1)


def test_payments_paymentPlans_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_plans.partially_update(
        "1234001",
        "PlanRef8765",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}],
    )
    verify_request_count("PATCH", "/processing-terminals/1234001/payment-plans/PlanRef8765", None, 1)
