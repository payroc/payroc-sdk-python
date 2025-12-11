from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_pricingIntents_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.pricing_intents.list(before="2571", after="8516", limit=1)
    verify_request_count("GET", "/pricing-intents", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_boarding_pricingIntents_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.pricing_intents.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        country="US",
        version="5.0",
        base={
            "addressVerification": 5,
            "annualFee": {"billInMonth": "june", "amount": 9900},
            "regulatoryAssistanceProgram": 15,
            "pciNonCompliance": 4995,
            "merchantAdvantage": 10,
            "platinumSecurity": {"billingFrequency": "monthly"},
            "maintenance": 500,
            "minimum": 100,
            "voiceAuthorization": 95,
            "chargeback": 2500,
            "retrieval": 1500,
            "batch": 1500,
            "earlyTermination": 57500,
        },
        processor={"card": {"fees": {"mastercardVisaDiscover": {}}, "planType": "interchangePlus"}},
        services=[{"enabled": True, "name": "hardwareAdvantagePlan"}],
        key="Your-Unique-Identifier",
        metadata={"yourCustomField": "abc123"},
        
    )
    verify_request_count("POST", "/pricing-intents", None, 1)


def test_boarding_pricingIntents_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.pricing_intents.retrieve("5")
    verify_request_count("GET", "/pricing-intents/5", None, 1)


def test_boarding_pricingIntents_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.pricing_intents.update(
        "5",
        country="US",
        version="5.0",
        base={
            "addressVerification": 5,
            "annualFee": {"billInMonth": "june", "amount": 9900},
            "regulatoryAssistanceProgram": 15,
            "pciNonCompliance": 4995,
            "merchantAdvantage": 10,
            "platinumSecurity": {"billingFrequency": "monthly"},
            "maintenance": 500,
            "minimum": 100,
            "voiceAuthorization": 95,
            "chargeback": 2500,
            "retrieval": 1500,
            "batch": 1500,
            "earlyTermination": 57500,
        },
        processor={
            "card": {"fees": {"mastercardVisaDiscover": {}}, "planType": "interchangePlus"},
            "ach": {
                "fees": {
                    "transaction": 50,
                    "batch": 5,
                    "returns": 400,
                    "unauthorizedReturn": 1999,
                    "statement": 800,
                    "monthlyMinimum": 20000,
                    "accountVerification": 10,
                    "discountRateUnder10000": 5.25,
                    "discountRateAbove10000": 10,
                }
            },
        },
        gateway={"fees": {"monthly": 2000, "setup": 5000, "perTransaction": 2000, "perDeviceMonthly": 10}},
        services=[{"enabled": True, "name": "hardwareAdvantagePlan"}],
        key="Your-Unique-Identifier",
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count("PUT", "/pricing-intents/5", None, 1)


def test_boarding_pricingIntents_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.pricing_intents.delete("5")
    verify_request_count("DELETE", "/pricing-intents/5", None, 1)


def test_boarding_pricingIntents_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.pricing_intents.partially_update(
        "5",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}, {"path": "path", "op": "remove"}],
    )
    verify_request_count("PATCH", "/pricing-intents/5", None, 1)
