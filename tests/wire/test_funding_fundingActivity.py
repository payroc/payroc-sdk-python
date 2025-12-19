from datetime import date

from .conftest import get_client, verify_request_count


def test_funding_fundingActivity_retrieve_balance() -> None:
    """Test retrieveBalance endpoint with WireMock"""
    test_id = "funding.funding_activity.retrieve_balance.0"
    client = get_client(test_id)
    client.funding.funding_activity.retrieve_balance(before="2571", after="8516", limit=1, merchant_id="4525644354")
    verify_request_count(
        test_id,
        "GET",
        "/funding-balance",
        {"before": "2571", "after": "8516", "limit": "1", "merchantId": "4525644354"},
        1,
    )


def test_funding_fundingActivity_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "funding.funding_activity.list_.0"
    client = get_client(test_id)
    client.funding.funding_activity.list(
        before="2571",
        after="8516",
        limit=1,
        date_from=date.fromisoformat("2024-07-02"),
        date_to=date.fromisoformat("2024-07-03"),
        merchant_id="4525644354",
    )
    verify_request_count(
        test_id,
        "GET",
        "/funding-activity",
        {
            "before": "2571",
            "after": "8516",
            "limit": "1",
            "dateFrom": "2024-07-02",
            "dateTo": "2024-07-03",
            "merchantId": "4525644354",
        },
        1,
    )
