from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_paymentLinks_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.list(
        "1234001",
        merchant_reference="LinkRef6543",
        link_type="multiUse",
        charge_type="preset",
        status="active",
        recipient_name="Sarah Hazel Hopper",
        recipient_email="sarah.hopper@example.com",
        created_on="2024-07-02",
        expires_on="2024-08-02",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/processing-terminals/1234001/payment-links",
        {
            "merchantReference": "LinkRef6543",
            "linkType": "multiUse",
            "chargeType": "preset",
            "status": "active",
            "recipientName": "Sarah Hazel Hopper",
            "recipientEmail": "sarah.hopper@example.com",
            "createdOn": "2024-07-02",
            "expiresOn": "2024-08-02",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_paymentLinks_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.create(
        "1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request={
            "merchantReference": "LinkRef6543",
            "order": {"charge": {"currency": "AED", "type": "prompt"}},
            "authType": "sale",
            "paymentMethods": ["card"],
            "type": "multiUse",
        },
    )
    verify_request_count("POST", "/processing-terminals/1234001/payment-links", None, 1)


def test_payments_paymentLinks_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.retrieve("JZURRJBUPS")
    verify_request_count("GET", "/payment-links/JZURRJBUPS", None, 1)


def test_payments_paymentLinks_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.partially_update(
        "JZURRJBUPS", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324", request=[{"path": "path", "op": "remove"}]
    )
    verify_request_count("PATCH", "/payment-links/JZURRJBUPS", None, 1)


def test_payments_paymentLinks_deactivate() -> None:
    """Test deactivate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.deactivate("JZURRJBUPS")
    verify_request_count("POST", "/payment-links/JZURRJBUPS/deactivate", None, 1)
