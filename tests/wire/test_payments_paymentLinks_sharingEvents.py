from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payments_paymentLinks_sharingEvents_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.sharing_events.list(
        "JZURRJBUPS",
        recipient_name="Sarah Hazel Hopper",
        recipient_email="sarah.hopper@example.com",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        "GET",
        "/payment-links/JZURRJBUPS/sharing-events",
        {
            "recipientName": "Sarah Hazel Hopper",
            "recipientEmail": "sarah.hopper@example.com",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_payments_paymentLinks_sharingEvents_share() -> None:
    """Test share endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payments.payment_links.sharing_events.share(
        "JZURRJBUPS",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        sharing_method="email",
        merchant_copy=True,
        message="Dear Sarah,Your insurance is expiring this month. Please, pay the renewal fee by the end of the month to renew it.",
        recipients=[{"name": "Sarah Hazel Hopper", "email": "sarah.hopper@example.com"}],
    )
    verify_request_count("POST", "/payment-links/JZURRJBUPS/sharing-events", None, 1)
