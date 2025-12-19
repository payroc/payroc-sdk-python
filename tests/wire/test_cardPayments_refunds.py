from datetime import date, datetime

from .conftest import get_client, verify_request_count


def test_cardPayments_refunds_reverse() -> None:
    """Test reverse endpoint with WireMock"""
    test_id = "card_payments.refunds.reverse.0"
    client = get_client(test_id)
    client.card_payments.refunds.reverse(
        payment_id="M2MJOG6O2Y", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324", amount=4999
    )
    verify_request_count(test_id, "POST", "/payments/M2MJOG6O2Y/reverse", None, 1)


def test_cardPayments_refunds_create_referenced_refund() -> None:
    """Test createReferencedRefund endpoint with WireMock"""
    test_id = "card_payments.refunds.create_referenced_refund.0"
    client = get_client(test_id)
    client.card_payments.refunds.create_referenced_refund(
        payment_id="M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        amount=4999,
        description="Refund for order OrderRef6543",
    )
    verify_request_count(test_id, "POST", "/payments/M2MJOG6O2Y/refund", None, 1)


def test_cardPayments_refunds_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "card_payments.refunds.list_.0"
    client = get_client(test_id)
    client.card_payments.refunds.list(
        processing_terminal_id="1234001",
        order_id="OrderRef6543",
        operator="Jane",
        cardholder_name="Sarah%20Hazel%20Hopper",
        first_6="453985",
        last_4="7062",
        tender="ebt",
        date_from=datetime.fromisoformat("2024-07-01T15:30:00Z"),
        date_to=datetime.fromisoformat("2024-07-03T15:30:00Z"),
        settlement_state="settled",
        settlement_date=date.fromisoformat("2024-07-02"),
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/refunds",
        {
            "processingTerminalId": "1234001",
            "orderId": "OrderRef6543",
            "operator": "Jane",
            "cardholderName": "Sarah%20Hazel%20Hopper",
            "first6": "453985",
            "last4": "7062",
            "tender": "ebt",
            "dateFrom": "2024-07-01T15:30:00Z",
            "dateTo": "2024-07-03T15:30:00Z",
            "settlementState": "settled",
            "settlementDate": "2024-07-02",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_cardPayments_refunds_create_unreferenced_refund() -> None:
    """Test createUnreferencedRefund endpoint with WireMock"""
    test_id = "card_payments.refunds.create_unreferenced_refund.0"
    client = get_client(test_id)
    client.card_payments.refunds.create_unreferenced_refund(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="pos",
        processing_terminal_id="1234001",
        order={
            "order_id": "OrderRef6543",
            "description": "Refund for order OrderRef6543",
            "amount": 4999,
            "currency": "USD",
        },
        refund_method={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count(test_id, "POST", "/refunds", None, 1)


def test_cardPayments_refunds_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "card_payments.refunds.retrieve.0"
    client = get_client(test_id)
    client.card_payments.refunds.retrieve(refund_id="CD3HN88U9F")
    verify_request_count(test_id, "GET", "/refunds/CD3HN88U9F", None, 1)


def test_cardPayments_refunds_adjust() -> None:
    """Test adjust endpoint with WireMock"""
    test_id = "card_payments.refunds.adjust.0"
    client = get_client(test_id)
    client.card_payments.refunds.adjust(
        refund_id="CD3HN88U9F",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        adjustments=[{"type": "customer"}],
    )
    verify_request_count(test_id, "POST", "/refunds/CD3HN88U9F/adjust", None, 1)


def test_cardPayments_refunds_reverse_refund() -> None:
    """Test reverseRefund endpoint with WireMock"""
    test_id = "card_payments.refunds.reverse_refund.0"
    client = get_client(test_id)
    client.card_payments.refunds.reverse_refund(
        refund_id="CD3HN88U9F", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324"
    )
    verify_request_count(test_id, "POST", "/refunds/CD3HN88U9F/reverse", None, 1)
