from datetime import date

from .conftest import get_client, verify_request_count


def test_funding_fundingRecipients_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "funding.funding_recipients.list_.0"
    client = get_client(test_id)
    client.funding.funding_recipients.list(before="2571", after="8516", limit=1)
    verify_request_count(test_id, "GET", "/funding-recipients", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_funding_fundingRecipients_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "funding.funding_recipients.create.0"
    client = get_client(test_id)
    client.funding.funding_recipients.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        recipient_type="privateCorporation",
        tax_id="12-3456789",
        doing_business_as="Pizza Doe",
        address={
            "address_1": "1 Example Ave.",
            "address_2": "Example Address Line 2",
            "address_3": "Example Address Line 3",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}, {"type": "phone", "value": "2025550164"}],
        metadata={"yourCustomField": "abc123"},
        owners=[
            {
                "first_name": "Jane",
                "middle_name": "Helen",
                "last_name": "Doe",
                "date_of_birth": date.fromisoformat("1964-03-22"),
                "address": {
                    "address_1": "1 Example Ave.",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postal_code": "60056",
                },
                "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                "contact_methods": [
                    {"type": "email", "value": "jane.doe@example.com"},
                    {"type": "phone", "value": "2025550164"},
                ],
                "relationship": {
                    "equity_percentage": 48.5,
                    "title": "CFO",
                    "is_control_prong": True,
                    "is_authorized_signatory": False,
                },
            }
        ],
        funding_accounts=[
            {"type": "checking", "use": "credit", "name_on_account": "Jane Doe", "payment_methods": [{"type": "ach"}]}
        ],
    )
    verify_request_count(test_id, "POST", "/funding-recipients", None, 1)


def test_funding_fundingRecipients_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "funding.funding_recipients.retrieve.0"
    client = get_client(test_id)
    client.funding.funding_recipients.retrieve(recipient_id=1)
    verify_request_count(test_id, "GET", "/funding-recipients/1", None, 1)


def test_funding_fundingRecipients_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "funding.funding_recipients.update.0"
    client = get_client(test_id)
    client.funding.funding_recipients.update(
        recipient_id_=1,
        recipient_type="privateCorporation",
        tax_id="12-3456789",
        doing_business_as="Doe Hot Dogs",
        address={
            "address_1": "2 Example Ave.",
            "address_2": "Example Address Line 2",
            "address_3": "Example Address Line 3",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}, {"type": "phone", "value": "2025550164"}],
        metadata={"responsiblePerson": "Jane Doe"},
        owners=[
            {
                "owner_id": 12346,
                "link": {"rel": "owner", "href": "https://api.payroc.com/v1/owners/12346", "method": "get"},
            }
        ],
        funding_accounts=[
            {
                "funding_account_id": 124,
                "status": "approved",
                "link": {
                    "rel": "fundingAccount",
                    "href": "https://api.payroc.com/v1/funding-accounts/124",
                    "method": "get",
                },
            }
        ],
    )
    verify_request_count(test_id, "PUT", "/funding-recipients/1", None, 1)


def test_funding_fundingRecipients_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "funding.funding_recipients.delete.0"
    client = get_client(test_id)
    client.funding.funding_recipients.delete(recipient_id=1)
    verify_request_count(test_id, "DELETE", "/funding-recipients/1", None, 1)


def test_funding_fundingRecipients_list_accounts() -> None:
    """Test listAccounts endpoint with WireMock"""
    test_id = "funding.funding_recipients.list_accounts.0"
    client = get_client(test_id)
    client.funding.funding_recipients.list_accounts(recipient_id=1)
    verify_request_count(test_id, "GET", "/funding-recipients/1/funding-accounts", None, 1)


def test_funding_fundingRecipients_create_account() -> None:
    """Test createAccount endpoint with WireMock"""
    test_id = "funding.funding_recipients.create_account.0"
    client = get_client(test_id)
    client.funding.funding_recipients.create_account(
        recipient_id=1,
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        type="savings",
        use="credit",
        name_on_account="Fred Nerk",
        payment_methods=[{"type": "ach"}],
        metadata={"responsiblePerson": "Jane Doe"},
    )
    verify_request_count(test_id, "POST", "/funding-recipients/1/funding-accounts", None, 1)


def test_funding_fundingRecipients_list_owners() -> None:
    """Test listOwners endpoint with WireMock"""
    test_id = "funding.funding_recipients.list_owners.0"
    client = get_client(test_id)
    client.funding.funding_recipients.list_owners(recipient_id=1)
    verify_request_count(test_id, "GET", "/funding-recipients/1/owners", None, 1)


def test_funding_fundingRecipients_create_owner() -> None:
    """Test createOwner endpoint with WireMock"""
    test_id = "funding.funding_recipients.create_owner.0"
    client = get_client(test_id)
    client.funding.funding_recipients.create_owner(
        recipient_id=1,
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        first_name="Fred",
        middle_name="Jim",
        last_name="Nerk",
        date_of_birth=date.fromisoformat("1980-01-19"),
        address={
            "address_1": "2 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        identifiers=[{"type": "nationalId", "value": "000-00-9876"}],
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}, {"type": "phone", "value": "2025550164"}],
        relationship={
            "equity_percentage": 51.5,
            "title": "CEO",
            "is_control_prong": False,
            "is_authorized_signatory": True,
        },
    )
    verify_request_count(test_id, "POST", "/funding-recipients/1/owners", None, 1)
