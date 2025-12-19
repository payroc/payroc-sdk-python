from datetime import date, datetime

from .conftest import get_client, verify_request_count


def test_cardPayments_payments_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "card_payments.payments.list_.0"
    client = get_client(test_id)
    client.card_payments.payments.list(
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
        payment_link_id="JZURRJBUPS",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/payments",
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
            "paymentLinkId": "JZURRJBUPS",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_cardPayments_payments_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "card_payments.payments.create.0"
    client = get_client(test_id)
    client.card_payments.payments.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="web",
        processing_terminal_id="1234001",
        operator="Jane",
        order={"order_id": "OrderRef6543", "description": "Large Pepperoni Pizza", "amount": 4999, "currency": "USD"},
        customer={
            "first_name": "Sarah",
            "last_name": "Hopper",
            "billing_address": {
                "address_1": "1 Example Ave.",
                "address_2": "Example Address Line 2",
                "address_3": "Example Address Line 3",
                "city": "Chicago",
                "state": "Illinois",
                "country": "US",
                "postal_code": "60056",
            },
            "shipping_address": {
                "recipient_name": "Sarah Hopper",
                "address": {
                    "address_1": "1 Example Ave.",
                    "address_2": "Example Address Line 2",
                    "address_3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postal_code": "60056",
                },
            },
        },
        payment_method={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count(test_id, "POST", "/payments", None, 1)


def test_cardPayments_payments_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "card_payments.payments.retrieve.0"
    client = get_client(test_id)
    client.card_payments.payments.retrieve(payment_id="M2MJOG6O2Y")
    verify_request_count(test_id, "GET", "/payments/M2MJOG6O2Y", None, 1)


def test_cardPayments_payments_adjust() -> None:
    """Test adjust endpoint with WireMock"""
    test_id = "card_payments.payments.adjust.0"
    client = get_client(test_id)
    client.card_payments.payments.adjust(
        payment_id="M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        adjustments=[{"type": "customer"}, {"type": "order", "amount": 4999}],
    )
    verify_request_count(test_id, "POST", "/payments/M2MJOG6O2Y/adjust", None, 1)


def test_cardPayments_payments_capture() -> None:
    """Test capture endpoint with WireMock"""
    test_id = "card_payments.payments.capture.0"
    client = get_client(test_id)
    client.card_payments.payments.capture(
        payment_id="M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        operator="Jane",
        amount=4999,
        breakdown={
            "subtotal": 4999,
            "duty_amount": 499,
            "freight_amount": 500,
            "items": [{"unit_price": 4000, "quantity": 1}],
        },
    )
    verify_request_count(test_id, "POST", "/payments/M2MJOG6O2Y/capture", None, 1)
