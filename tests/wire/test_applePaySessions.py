from .conftest import get_client, verify_request_count


def test_applePaySessions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "apple_pay_sessions.create.0"
    client = get_client(test_id)
    client.apple_pay_sessions.create(
        processing_terminal_id="1234001",
        apple_domain_id="DUHDZJHGYY",
        apple_validation_url="https://apple-pay-gateway.apple.com/paymentservices/startSession",
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/apple-pay-sessions", None, 1)
