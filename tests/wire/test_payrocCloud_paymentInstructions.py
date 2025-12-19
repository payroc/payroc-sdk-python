from .conftest import get_client, verify_request_count


def test_payrocCloud_paymentInstructions_submit() -> None:
    """Test submit endpoint with WireMock"""
    test_id = "payroc_cloud.payment_instructions.submit.0"
    client = get_client(test_id)
    client.payroc_cloud.payment_instructions.submit(
        serial_number="1850010868",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        operator="Jane",
        processing_terminal_id="1234001",
        order={"order_id": "OrderRef6543", "amount": 4999, "currency": "USD"},
        customization_options={"entry_method": "deviceRead"},
        auto_capture=True,
    )
    verify_request_count(test_id, "POST", "/devices/1850010868/payment-instructions", None, 1)


def test_payrocCloud_paymentInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "payroc_cloud.payment_instructions.retrieve.0"
    client = get_client(test_id)
    client.payroc_cloud.payment_instructions.retrieve(payment_instruction_id="e743a9165d134678a9100ebba3b29597")
    verify_request_count(test_id, "GET", "/payment-instructions/e743a9165d134678a9100ebba3b29597", None, 1)


def test_payrocCloud_paymentInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "payroc_cloud.payment_instructions.delete.0"
    client = get_client(test_id)
    client.payroc_cloud.payment_instructions.delete(payment_instruction_id="e743a9165d134678a9100ebba3b29597")
    verify_request_count(test_id, "DELETE", "/payment-instructions/e743a9165d134678a9100ebba3b29597", None, 1)
