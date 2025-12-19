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
        tax_id="123456789",
        doing_business_as="doingBusinessAs",
        address={
            "address_1": "1 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}],
        owners=[
            {
                "first_name": "Jane",
                "last_name": "Doe",
                "date_of_birth": date.fromisoformat("1964-03-22"),
                "address": {
                    "address_1": "1 Example Ave.",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postal_code": "60056",
                },
                "identifiers": [{"type": "nationalId", "value": "xxxxx4320"}],
                "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
                "relationship": {"is_control_prong": True},
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
        tax_id="123456789",
        doing_business_as="doingBusinessAs",
        address={
            "address_1": "1 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}],
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
        type="checking",
        use="credit",
        name_on_account="Jane Doe",
        payment_methods=[{"type": "ach"}],
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
        first_name="Jane",
        last_name="Doe",
        date_of_birth=date.fromisoformat("1964-03-22"),
        address={
            "address_1": "1 Example Ave.",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        identifiers=[{"type": "nationalId", "value": "xxxxx4320"}],
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}],
        relationship={"is_control_prong": True},
    )
    verify_request_count(test_id, "POST", "/funding-recipients/1/owners", None, 1)
