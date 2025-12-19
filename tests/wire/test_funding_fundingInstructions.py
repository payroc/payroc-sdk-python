from datetime import date

from .conftest import get_client, verify_request_count


def test_funding_fundingInstructions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "funding.funding_instructions.list_.0"
    client = get_client(test_id)
    client.funding.funding_instructions.list(
        before="2571",
        after="8516",
        limit=1,
        date_from=date.fromisoformat("2024-07-01"),
        date_to=date.fromisoformat("2024-07-03"),
    )
    verify_request_count(
        test_id,
        "GET",
        "/funding-instructions",
        {"before": "2571", "after": "8516", "limit": "1", "dateFrom": "2024-07-01", "dateTo": "2024-07-03"},
        1,
    )


def test_funding_fundingInstructions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "funding.funding_instructions.create.0"
    client = get_client(test_id)
    client.funding.funding_instructions.create(idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324")
    verify_request_count(test_id, "POST", "/funding-instructions", None, 1)


def test_funding_fundingInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "funding.funding_instructions.retrieve.0"
    client = get_client(test_id)
    client.funding.funding_instructions.retrieve(instruction_id=1)
    verify_request_count(test_id, "GET", "/funding-instructions/1", None, 1)


def test_funding_fundingInstructions_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "funding.funding_instructions.update.0"
    client = get_client(test_id)
    client.funding.funding_instructions.update(instruction_id_=1)
    verify_request_count(test_id, "PUT", "/funding-instructions/1", None, 1)


def test_funding_fundingInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "funding.funding_instructions.delete.0"
    client = get_client(test_id)
    client.funding.funding_instructions.delete(instruction_id=1)
    verify_request_count(test_id, "DELETE", "/funding-instructions/1", None, 1)
