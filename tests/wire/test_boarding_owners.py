from datetime import date

from .conftest import get_client, verify_request_count


def test_boarding_owners_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.owners.retrieve.0"
    client = get_client(test_id)
    client.boarding.owners.retrieve(owner_id=1)
    verify_request_count(test_id, "GET", "/owners/1", None, 1)


def test_boarding_owners_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "boarding.owners.update.0"
    client = get_client(test_id)
    client.boarding.owners.update(
        owner_id_=1,
        first_name="Jane",
        middle_name="Helen",
        last_name="Doe",
        date_of_birth=date.fromisoformat("1964-03-22"),
        address={
            "address_1": "1 Example Ave.",
            "address_2": "Example Address Line 2",
            "address_3": "Example Address Line 3",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        identifiers=[{"type": "nationalId", "value": "000-00-4320"}],
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}],
        relationship={
            "equity_percentage": 48.5,
            "title": "CFO",
            "is_control_prong": True,
            "is_authorized_signatory": False,
        },
    )
    verify_request_count(test_id, "PUT", "/owners/1", None, 1)


def test_boarding_owners_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "boarding.owners.delete.0"
    client = get_client(test_id)
    client.boarding.owners.delete(owner_id=1)
    verify_request_count(test_id, "DELETE", "/owners/1", None, 1)
