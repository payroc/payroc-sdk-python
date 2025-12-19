from .conftest import get_client, verify_request_count


def test_payrocCloud_signatureInstructions_submit() -> None:
    """Test submit endpoint with WireMock"""
    test_id = "payroc_cloud.signature_instructions.submit.0"
    client = get_client(test_id)
    client.payroc_cloud.signature_instructions.submit(
        serial_number="1850010868",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
    )
    verify_request_count(test_id, "POST", "/devices/1850010868/signature-instructions", None, 1)


def test_payrocCloud_signatureInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "payroc_cloud.signature_instructions.retrieve.0"
    client = get_client(test_id)
    client.payroc_cloud.signature_instructions.retrieve(signature_instruction_id="a37439165d134678a9100ebba3b29597")
    verify_request_count(test_id, "GET", "/signature-instructions/a37439165d134678a9100ebba3b29597", None, 1)


def test_payrocCloud_signatureInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "payroc_cloud.signature_instructions.delete.0"
    client = get_client(test_id)
    client.payroc_cloud.signature_instructions.delete(signature_instruction_id="a37439165d134678a9100ebba3b29597")
    verify_request_count(test_id, "DELETE", "/signature-instructions/a37439165d134678a9100ebba3b29597", None, 1)
