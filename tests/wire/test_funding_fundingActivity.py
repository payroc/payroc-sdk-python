from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_funding_fundingActivity_retrieve_balance() -> None:
    """Test retrieveBalance endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_activity.retrieve_balance(
        before="2571", after="8516", limit=1, merchant_id="4525644354"
    )
    verify_request_count(
        "GET", "/funding-balance", {"before": "2571", "after": "8516", "limit": "1", "merchantId": "4525644354"}, 1
    )


def test_funding_fundingActivity_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.funding.funding_activity.list(
        before="2571", after="8516", limit=1, date_from="2024-07-02", date_to="2024-07-03", merchant_id="4525644354"
    )
    verify_request_count(
        "GET",
        "/funding-activity",
        {
            "before": "2571",
            "after": "8516",
            "limit": "1",
            "dateFrom": "2024-07-02",
            "dateTo": "2024-07-03",
            "merchantId": "4525644354",
        },
        1,
    )
