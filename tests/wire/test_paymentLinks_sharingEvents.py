from .conftest import get_client, verify_request_count


def test_paymentLinks_sharingEvents_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "payment_links.sharing_events.list_.0"
    client = get_client(test_id)
    client.payment_links.sharing_events.list(
        payment_link_id="JZURRJBUPS",
        recipient_name="Sarah Hazel Hopper",
        recipient_email="sarah.hopper@example.com",
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/payment-links/JZURRJBUPS/sharing-events",
        {
            "recipientName": "Sarah Hazel Hopper",
            "recipientEmail": "sarah.hopper@example.com",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_paymentLinks_sharingEvents_share() -> None:
    """Test share endpoint with WireMock"""
    test_id = "payment_links.sharing_events.share.0"
    client = get_client(test_id)
    client.payment_links.sharing_events.share(
        payment_link_id="JZURRJBUPS",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        sharing_method="email",
        merchant_copy=True,
        message="Dear Sarah,\n\nYour insurance is expiring this month.\nPlease, pay the renewal fee by the end of the month to renew it.\n",
        recipients=[{"name": "Sarah Hazel Hopper", "email": "sarah.hopper@example.com"}],
    )
    verify_request_count(test_id, "POST", "/payment-links/JZURRJBUPS/sharing-events", None, 1)
