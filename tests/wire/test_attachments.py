from .conftest import get_client, verify_request_count


def test_attachments_upload_to_processing_account() -> None:
    """Test uploadToProcessingAccount endpoint with WireMock"""
    test_id = "attachments.upload_to_processing_account.0"
    client = get_client(test_id)
    client.attachments.upload_to_processing_account(
        processing_account_id="38765",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        file="example_file",
        attachment={"type": "bankingEvidence"},
    )
    verify_request_count(test_id, "POST", "/processing-accounts/38765/attachments", None, 1)


def test_attachments_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "attachments.retrieve.0"
    client = get_client(test_id)
    client.attachments.retrieve(attachment_id="12876")
    verify_request_count(test_id, "GET", "/attachments/12876", None, 1)
