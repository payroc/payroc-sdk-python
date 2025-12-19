from .conftest import get_client, verify_request_count


def test_paymentFeatures_bank_verify() -> None:
    """Test verify endpoint with WireMock"""
    test_id = "payment_features.bank.verify.0"
    client = get_client(test_id)
    client.payment_features.bank.verify(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        bank_account={
            "type": "pad",
            "name_on_account": "Sarah Hazel Hopper",
            "account_number": "1234567890",
            "transit_number": "76543",
            "institution_number": "543",
        },
    )
    verify_request_count(test_id, "POST", "/bank-accounts/verify", None, 1)
