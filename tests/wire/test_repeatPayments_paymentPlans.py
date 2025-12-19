from .conftest import get_client, verify_request_count


def test_repeatPayments_paymentPlans_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "repeat_payments.payment_plans.list_.0"
    client = get_client(test_id)
    client.repeat_payments.payment_plans.list(processing_terminal_id="1234001", before="2571", after="8516", limit=1)
    verify_request_count(
        test_id,
        "GET",
        "/processing-terminals/1234001/payment-plans",
        {"before": "2571", "after": "8516", "limit": "1"},
        1,
    )


def test_repeatPayments_paymentPlans_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "repeat_payments.payment_plans.create.0"
    client = get_client(test_id)
    client.repeat_payments.payment_plans.create(
        processing_terminal_id_="1234001",
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
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/payment-plans", None, 1)


def test_repeatPayments_paymentPlans_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "repeat_payments.payment_plans.retrieve.0"
    client = get_client(test_id)
    client.repeat_payments.payment_plans.retrieve(processing_terminal_id="1234001", payment_plan_id="PlanRef8765")
    verify_request_count(test_id, "GET", "/processing-terminals/1234001/payment-plans/PlanRef8765", None, 1)


def test_repeatPayments_paymentPlans_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "repeat_payments.payment_plans.delete.0"
    client = get_client(test_id)
    client.repeat_payments.payment_plans.delete(processing_terminal_id="1234001", payment_plan_id="PlanRef8765")
    verify_request_count(test_id, "DELETE", "/processing-terminals/1234001/payment-plans/PlanRef8765", None, 1)


def test_repeatPayments_paymentPlans_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    test_id = "repeat_payments.payment_plans.partially_update.0"
    client = get_client(test_id)
    client.repeat_payments.payment_plans.partially_update(
        processing_terminal_id="1234001",
        payment_plan_id="PlanRef8765",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}],
    )
    verify_request_count(test_id, "PATCH", "/processing-terminals/1234001/payment-plans/PlanRef8765", None, 1)
