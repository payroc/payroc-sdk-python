from datetime import date, datetime

from .conftest import get_client, verify_request_count


def test_bankTransferPayments_refunds_reverse_payment() -> None:
    """Test reversePayment endpoint with WireMock"""
    test_id = "bank_transfer_payments.refunds.reverse_payment.0"
    client = get_client(test_id)
    client.bank_transfer_payments.refunds.reverse_payment(
        payment_id="M2MJOG6O2Y", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324"
    )
    verify_request_count(test_id, "POST", "/bank-transfer-payments/M2MJOG6O2Y/reverse", None, 1)


def test_bankTransferPayments_refunds_refund() -> None:
    """Test refund endpoint with WireMock"""
    test_id = "bank_transfer_payments.refunds.refund.0"
    client = get_client(test_id)
    client.bank_transfer_payments.refunds.refund(
        payment_id="M2MJOG6O2Y",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        amount=4999,
        description="amount to refund",
    )
    verify_request_count(test_id, "POST", "/bank-transfer-payments/M2MJOG6O2Y/refund", None, 1)


def test_bankTransferPayments_refunds_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "bank_transfer_payments.refunds.list_.0"
    client = get_client(test_id)
    client.bank_transfer_payments.refunds.list(
        processing_terminal_id="1234001",
        order_id="OrderRef6543",
        name_on_account="Sarah%20Hazel%20Hopper",
        last_4="7062",
        date_from=datetime.fromisoformat("2024-07-01T00:00:00+00:00"),
        date_to=datetime.fromisoformat("2024-07-31T23:59:59+00:00"),
        settlement_state="settled",
        settlement_date=date.fromisoformat("2024-07-15"),
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/bank-transfer-refunds",
        {
            "processingTerminalId": "1234001",
            "orderId": "OrderRef6543",
            "nameOnAccount": "Sarah%20Hazel%20Hopper",
            "last4": "7062",
            "dateFrom": "2024-07-01T00:00:00Z",
            "dateTo": "2024-07-31T23:59:59Z",
            "settlementState": "settled",
            "settlementDate": "2024-07-15",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_bankTransferPayments_refunds_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "bank_transfer_payments.refunds.create.0"
    client = get_client(test_id)
    client.bank_transfer_payments.refunds.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        order={
            "order_id": "OrderRef6543",
            "description": "Refund for order OrderRef6543",
            "amount": 4999,
            "currency": "USD",
        },
        customer={
            "notification_language": "en",
            "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
        },
        refund_method={
            "type": "ach",
            "name_on_account": "Shara Hazel Hopper",
            "account_number": "1234567890",
            "routing_number": "123456789",
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count(test_id, "POST", "/bank-transfer-refunds", None, 1)


def test_bankTransferPayments_refunds_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "bank_transfer_payments.refunds.retrieve.0"
    client = get_client(test_id)
    client.bank_transfer_payments.refunds.retrieve(refund_id="CD3HN88U9F")
    verify_request_count(test_id, "GET", "/bank-transfer-refunds/CD3HN88U9F", None, 1)


def test_bankTransferPayments_refunds_reverse_refund() -> None:
    """Test reverseRefund endpoint with WireMock"""
    test_id = "bank_transfer_payments.refunds.reverse_refund.0"
    client = get_client(test_id)
    client.bank_transfer_payments.refunds.reverse_refund(
        refund_id="CD3HN88U9F", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324"
    )
    verify_request_count(test_id, "POST", "/bank-transfer-refunds/CD3HN88U9F/reverse", None, 1)
