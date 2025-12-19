from .conftest import get_client, verify_request_count


def test_boarding_contacts_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.contacts.retrieve.0"
    client = get_client(test_id)
    client.boarding.contacts.retrieve(contact_id=1)
    verify_request_count(test_id, "GET", "/contacts/1", None, 1)


def test_boarding_contacts_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "boarding.contacts.update.0"
    client = get_client(test_id)
    client.boarding.contacts.update(
        contact_id_=1,
        type="manager",
        first_name="Jane",
        middle_name="Helen",
        last_name="Doe",
        identifiers=[{"type": "nationalId", "value": "000-00-4320"}],
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}],
    )
    verify_request_count(test_id, "PUT", "/contacts/1", None, 1)


def test_boarding_contacts_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "boarding.contacts.delete.0"
    client = get_client(test_id)
    client.boarding.contacts.delete(contact_id=1)
    verify_request_count(test_id, "DELETE", "/contacts/1", None, 1)
