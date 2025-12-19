from .conftest import get_client, verify_request_count


def test_boarding_pricingIntents_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "boarding.pricing_intents.list_.0"
    client = get_client(test_id)
    client.boarding.pricing_intents.list(before="2571", after="8516", limit=1)
    verify_request_count(test_id, "GET", "/pricing-intents", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_boarding_pricingIntents_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "boarding.pricing_intents.create.0"
    client = get_client(test_id)
    client.boarding.pricing_intents.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        country="US",
        version="5.0",
        base={
            "address_verification": 5,
            "annual_fee": {"bill_in_month": "june", "amount": 9900},
            "regulatory_assistance_program": 15,
            "pci_non_compliance": 4995,
            "merchant_advantage": 10,
            "platinum_security": {"billing_frequency": "monthly"},
            "maintenance": 500,
            "minimum": 100,
            "voice_authorization": 95,
            "chargeback": 2500,
            "retrieval": 1500,
            "batch": 1500,
            "early_termination": 57500,
        },
        processor={"card": {"plan_type": "interchangePlus", "fees": {"mastercard_visa_discover": {}}}},
        services=[{"name": "hardwareAdvantagePlan", "enabled": True}],
        key="Your-Unique-Identifier",
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count(test_id, "POST", "/pricing-intents", None, 1)


def test_boarding_pricingIntents_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.pricing_intents.retrieve.0"
    client = get_client(test_id)
    client.boarding.pricing_intents.retrieve(pricing_intent_id="5")
    verify_request_count(test_id, "GET", "/pricing-intents/5", None, 1)


def test_boarding_pricingIntents_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "boarding.pricing_intents.update.0"
    client = get_client(test_id)
    client.boarding.pricing_intents.update(
        pricing_intent_id="5",
        country="US",
        version="5.0",
        base={
            "address_verification": 5,
            "annual_fee": {"bill_in_month": "june", "amount": 9900},
            "regulatory_assistance_program": 15,
            "pci_non_compliance": 4995,
            "merchant_advantage": 10,
            "platinum_security": {"billing_frequency": "monthly"},
            "maintenance": 500,
            "minimum": 100,
            "voice_authorization": 95,
            "chargeback": 2500,
            "retrieval": 1500,
            "batch": 1500,
            "early_termination": 57500,
        },
        processor={
            "card": {"plan_type": "interchangePlus", "fees": {"mastercard_visa_discover": {}}},
            "ach": {
                "fees": {
                    "transaction": 50,
                    "batch": 5,
                    "returns": 400,
                    "unauthorized_return": 1999,
                    "statement": 800,
                    "monthly_minimum": 20000,
                    "account_verification": 10,
                    "discount_rate_under_10000": 5.25,
                    "discount_rate_above_10000": 10,
                }
            },
        },
        gateway={"fees": {"monthly": 2000, "setup": 5000, "per_transaction": 2000, "per_device_monthly": 10}},
        services=[{"name": "hardwareAdvantagePlan", "enabled": True}],
        key="Your-Unique-Identifier",
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count(test_id, "PUT", "/pricing-intents/5", None, 1)


def test_boarding_pricingIntents_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "boarding.pricing_intents.delete.0"
    client = get_client(test_id)
    client.boarding.pricing_intents.delete(pricing_intent_id="5")
    verify_request_count(test_id, "DELETE", "/pricing-intents/5", None, 1)


def test_boarding_pricingIntents_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    test_id = "boarding.pricing_intents.partially_update.0"
    client = get_client(test_id)
    client.boarding.pricing_intents.partially_update(
        pricing_intent_id="5",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}],
    )
    verify_request_count(test_id, "PATCH", "/pricing-intents/5", None, 1)
