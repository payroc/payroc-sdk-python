from datetime import date, datetime

from .conftest import get_client, verify_request_count


def test_bankTransferPayments_payments_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "bank_transfer_payments.payments.list_.0"
    client = get_client(test_id)
    client.bank_transfer_payments.payments.list(
        processing_terminal_id="1234001",
        order_id="OrderRef6543",
        name_on_account="Sarah%20Hazel%20Hopper",
        last_4="7890",
        date_from=datetime.fromisoformat("2024-07-01T00:00:00Z"),
        date_to=datetime.fromisoformat("2024-07-31T23:59:59Z"),
        settlement_state="settled",
        settlement_date=date.fromisoformat("2024-07-15"),
        payment_link_id="JZURRJBUPS",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/bank-transfer-payments",
        {
            "processingTerminalId": "1234001",
            "orderId": "OrderRef6543",
            "nameOnAccount": "Sarah%20Hazel%20Hopper",
            "last4": "7890",
            "dateFrom": "2024-07-01T00:00:00Z",
            "dateTo": "2024-07-31T23:59:59Z",
            "settlementState": "settled",
            "settlementDate": "2024-07-15",
            "paymentLinkId": "JZURRJBUPS",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_bankTransferPayments_payments_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "bank_transfer_payments.payments.create.0"
    client = get_client(test_id)
    client.bank_transfer_payments.payments.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        order={
            "order_id": "OrderRef6543",
            "description": "Large Pepperoni Pizza",
            "amount": 4999,
            "currency": "USD",
            "breakdown": {
                "subtotal": 4347,
                "tip": {"type": "percentage", "percentage": 10},
                "taxes": [{"type": "rate", "rate": 5, "name": "Sales Tax"}],
            },
        },
        customer={
            "notification_language": "en",
            "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
        },
        credential_on_file={"tokenize": True},
        payment_method={
            "type": "ach",
            "name_on_account": "Shara Hazel Hopper",
            "account_number": "1234567890",
            "routing_number": "123456789",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count(test_id, "POST", "/bank-transfer-payments", None, 1)


def test_bankTransferPayments_payments_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "bank_transfer_payments.payments.retrieve.0"
    client = get_client(test_id)
    client.bank_transfer_payments.payments.retrieve(payment_id="M2MJOG6O2Y")
    verify_request_count(test_id, "GET", "/bank-transfer-payments/M2MJOG6O2Y", None, 1)


def test_bankTransferPayments_payments_represent() -> None:
    """Test represent endpoint with WireMock"""
    test_id = "bank_transfer_payments.payments.represent.0"
    client = get_client(test_id)
    client.bank_transfer_payments.payments.represent(
        payment_id="M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        payment_method={
            "type": "ach",
            "name_on_account": "Shara Hazel Hopper",
            "account_number": "1234567890",
            "routing_number": "123456789",
        },
    )
    verify_request_count(test_id, "POST", "/bank-transfer-payments/M2MJOG6O2Y/represent", None, 1)
