from .conftest import get_client, verify_request_count


def test_tokenization_singleUseTokens_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "tokenization.single_use_tokens.create.0"
    client = get_client(test_id)
    client.tokenization.single_use_tokens.create(
        processing_terminal_id="1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        channel="web",
        operator="Jane",
        source={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/single-use-tokens", None, 1)
