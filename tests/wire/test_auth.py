from .conftest import get_client, verify_request_count


def test_auth_retrieve_token() -> None:
    """Test retrieveToken endpoint with WireMock"""
    test_id = "auth.retrieve_token.0"
    client = get_client(test_id)
    client.auth.retrieve_token(api_key="x-api-key")
    verify_request_count(test_id, "POST", "/authorize", None, 2)
