from .conftest import get_client, verify_request_count


def test_payrocCloud_refundInstructions_submit() -> None:
    """Test submit endpoint with WireMock"""
    test_id = "payroc_cloud.refund_instructions.submit.0"
    client = get_client(test_id)
    client.payroc_cloud.refund_instructions.submit(
        serial_number="1850010868",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        processing_terminal_id="1234001",
        order={
            "order_id": "OrderRef6543",
            "description": "Refund for order OrderRef6543",
            "amount": 4999,
            "currency": "USD",
        },
        customization_options={"entry_method": "manualEntry"},
    )
    verify_request_count(test_id, "POST", "/devices/1850010868/refund-instructions", None, 1)


def test_payrocCloud_refundInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "payroc_cloud.refund_instructions.retrieve.0"
    client = get_client(test_id)
    client.payroc_cloud.refund_instructions.retrieve(refund_instruction_id="a37439165d134678a9100ebba3b29597")
    verify_request_count(test_id, "GET", "/refund-instructions/a37439165d134678a9100ebba3b29597", None, 1)


def test_payrocCloud_refundInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "payroc_cloud.refund_instructions.delete.0"
    client = get_client(test_id)
    client.payroc_cloud.refund_instructions.delete(refund_instruction_id="a37439165d134678a9100ebba3b29597")
    verify_request_count(test_id, "DELETE", "/refund-instructions/a37439165d134678a9100ebba3b29597", None, 1)
