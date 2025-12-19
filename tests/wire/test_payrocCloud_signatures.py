from .conftest import get_client, verify_request_count


def test_payrocCloud_signatures_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "payroc_cloud.signatures.retrieve.0"
    client = get_client(test_id)
    client.payroc_cloud.signatures.retrieve(signature_id="JDN4ILZB0T")
    verify_request_count(test_id, "GET", "/signatures/JDN4ILZB0T", None, 1)
