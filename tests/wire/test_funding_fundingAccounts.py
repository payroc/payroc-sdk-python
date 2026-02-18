from .conftest import get_client, verify_request_count


def test_funding_fundingAccounts_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "funding.funding_accounts.list_.0"
    client = get_client(test_id)
    client.funding.funding_accounts.list(before="2571", after="8516", limit=1)
    verify_request_count(test_id, "GET", "/funding-accounts", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_funding_fundingAccounts_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "funding.funding_accounts.retrieve.0"
    client = get_client(test_id)
    client.funding.funding_accounts.retrieve(funding_account_id=1)
    verify_request_count(test_id, "GET", "/funding-accounts/1", None, 1)


def test_funding_fundingAccounts_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "funding.funding_accounts.update.0"
    client = get_client(test_id)
    client.funding.funding_accounts.update(
        funding_account_id_=1,
        type="savings",
        use="credit",
        name_on_account="Fred Nerk",
        payment_methods=[{"type": "ach"}],
        metadata={"responsiblePerson": "Jane Doe"},
    )
    verify_request_count(test_id, "PUT", "/funding-accounts/1", None, 1)


def test_funding_fundingAccounts_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "funding.funding_accounts.delete.0"
    client = get_client(test_id)
    client.funding.funding_accounts.delete(funding_account_id=1)
    verify_request_count(test_id, "DELETE", "/funding-accounts/1", None, 1)
