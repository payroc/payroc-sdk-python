from datetime import date

from .conftest import get_client, verify_request_count


def test_tokenization_secureTokens_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "tokenization.secure_tokens.list_.0"
    client = get_client(test_id)
    client.tokenization.secure_tokens.list(
        processing_terminal_id="1234001",
        secure_token_id="MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        customer_name="Sarah%20Hazel%20Hopper",
        phone="2025550165",
        email="sarah.hopper@example.com",
        token="296753123456",
        first_6="453985",
        last_4="7062",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/processing-terminals/1234001/secure-tokens",
        {
            "secureTokenId": "MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
            "customerName": "Sarah%20Hazel%20Hopper",
            "phone": "2025550165",
            "email": "sarah.hopper@example.com",
            "token": "296753123456",
            "first6": "453985",
            "last4": "7062",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_tokenization_secureTokens_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "tokenization.secure_tokens.create.0"
    client = get_client(test_id)
    client.tokenization.secure_tokens.create(
        processing_terminal_id="1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        mit_agreement="unscheduled",
        customer={
            "first_name": "Sarah",
            "last_name": "Hopper",
            "date_of_birth": date.fromisoformat("1990-07-15"),
            "reference_number": "Customer-12",
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
            "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
            "notification_language": "en",
        },
        ip_address={"type": "ipv4", "value": "104.18.24.203"},
        source={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
        custom_fields=[{"name": "yourCustomField", "value": "abc123"}],
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/secure-tokens", None, 1)


def test_tokenization_secureTokens_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "tokenization.secure_tokens.retrieve.0"
    client = get_client(test_id)
    client.tokenization.secure_tokens.retrieve(
        processing_terminal_id="1234001", secure_token_id="MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa"
    )
    verify_request_count(
        test_id,
        "GET",
        "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        None,
        1,
    )


def test_tokenization_secureTokens_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "tokenization.secure_tokens.delete.0"
    client = get_client(test_id)
    client.tokenization.secure_tokens.delete(
        processing_terminal_id="1234001", secure_token_id="MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa"
    )
    verify_request_count(
        test_id,
        "DELETE",
        "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        None,
        1,
    )


def test_tokenization_secureTokens_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    test_id = "tokenization.secure_tokens.partially_update.0"
    client = get_client(test_id)
    client.tokenization.secure_tokens.partially_update(
        processing_terminal_id="1234001",
        secure_token_id="MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}, {"op": "remove", "path": "path"}],
    )
    verify_request_count(
        test_id,
        "PATCH",
        "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        None,
        1,
    )


def test_tokenization_secureTokens_update_account() -> None:
    """Test updateAccount endpoint with WireMock"""
    test_id = "tokenization.secure_tokens.update_account.0"
    client = get_client(test_id)
    client.tokenization.secure_tokens.update_account(
        processing_terminal_id="1234001",
        secure_token_id="MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request={
            "type": "singleUseToken",
            "token": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
        },
    )
    verify_request_count(
        test_id,
        "POST",
        "/processing-terminals/1234001/secure-tokens/MREF_abc1de23-f4a5-6789-bcd0-12e345678901fa/update-account",
        None,
        1,
    )
