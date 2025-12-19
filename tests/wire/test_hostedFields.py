from .conftest import get_client, verify_request_count


def test_hostedFields_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "hosted_fields.create.0"
    client = get_client(test_id)
    client.hosted_fields.create(
        processing_terminal_id="1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        lib_version="1.1.0.123456",
        scenario="payment",
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/hosted-fields-sessions", None, 1)
