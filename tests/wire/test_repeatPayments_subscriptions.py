from datetime import date

from .conftest import get_client, verify_request_count


def test_repeatPayments_subscriptions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.list_.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.list(
        processing_terminal_id="1234001",
        customer_name="Sarah%20Hazel%20Hopper",
        last_4="7062",
        payment_plan="Premium%20Club",
        frequency="weekly",
        status="active",
        end_date=date.fromisoformat("2025-07-01"),
        next_due_date=date.fromisoformat("2024-08-01"),
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
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


def test_repeatPayments_subscriptions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.create.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.create(
        processing_terminal_id="1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        subscription_id="SubRef7654",
        payment_plan_id="PlanRef8765",
        payment_method={"type": "secureToken", "token": "1234567890123456789"},
        name="Premium Club",
        description="Premium Club subscription",
        setup_order={
            "order_id": "OrderRef6543",
            "amount": 4999,
            "description": "Initial setup fee for Premium Club subscription",
        },
        recurring_order={
            "amount": 4999,
            "description": "Monthly Premium Club subscription",
            "breakdown": {"subtotal": 4347, "taxes": [{"type": "rate", "rate": 5, "name": "Sales Tax"}]},
        },
        start_date=date.fromisoformat("2024-07-02"),
        end_date=date.fromisoformat("2025-07-01"),
        length=12,
        pause_collection_for=0,
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/subscriptions", None, 1)


def test_repeatPayments_subscriptions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.retrieve.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.retrieve(processing_terminal_id="1234001", subscription_id="SubRef7654")
    verify_request_count(test_id, "GET", "/processing-terminals/1234001/subscriptions/SubRef7654", None, 1)


def test_repeatPayments_subscriptions_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.partially_update.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.partially_update(
        processing_terminal_id="1234001",
        subscription_id="SubRef7654",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}],
    )
    verify_request_count(test_id, "PATCH", "/processing-terminals/1234001/subscriptions/SubRef7654", None, 1)


def test_repeatPayments_subscriptions_deactivate() -> None:
    """Test deactivate endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.deactivate.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.deactivate(processing_terminal_id="1234001", subscription_id="SubRef7654")
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/subscriptions/SubRef7654/deactivate", None, 1)


def test_repeatPayments_subscriptions_reactivate() -> None:
    """Test reactivate endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.reactivate.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.reactivate(processing_terminal_id="1234001", subscription_id="SubRef7654")
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/subscriptions/SubRef7654/reactivate", None, 1)


def test_repeatPayments_subscriptions_pay() -> None:
    """Test pay endpoint with WireMock"""
    test_id = "repeat_payments.subscriptions.pay.0"
    client = get_client(test_id)
    client.repeat_payments.subscriptions.pay(
        processing_terminal_id="1234001",
        subscription_id="SubRef7654",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        order={"order_id": "OrderRef6543", "amount": 4999, "description": "Monthly Premium Club subscription"},
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/subscriptions/SubRef7654/pay", None, 1)
