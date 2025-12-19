from datetime import date

from .conftest import get_client, verify_request_count


def test_paymentLinks_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "payment_links.list_.0"
    client = get_client(test_id)
    client.payment_links.list(
        processing_terminal_id="1234001",
        merchant_reference="LinkRef6543",
        link_type="multiUse",
        charge_type="preset",
        status="active",
        recipient_name="Sarah Hazel Hopper",
        recipient_email="sarah.hopper@example.com",
        created_on=date.fromisoformat("2024-07-02"),
        expires_on=date.fromisoformat("2024-08-02"),
        before="2571",
        after="8516",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/processing-terminals/1234001/payment-links",
        {
            "merchantReference": "LinkRef6543",
            "linkType": "multiUse",
            "chargeType": "preset",
            "status": "active",
            "recipientName": "Sarah Hazel Hopper",
            "recipientEmail": "sarah.hopper@example.com",
            "createdOn": "2024-07-02",
            "expiresOn": "2024-08-02",
            "before": "2571",
            "after": "8516",
            "limit": "1",
        },
        1,
    )


def test_paymentLinks_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "payment_links.create.0"
    client = get_client(test_id)
    client.payment_links.create(
        processing_terminal_id="1234001",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request={
            "type": "multiUse",
            "merchant_reference": "LinkRef6543",
            "order": {"charge": {"type": "prompt", "currency": "AED"}},
            "auth_type": "sale",
            "payment_methods": ["card"],
        },
    )
    verify_request_count(test_id, "POST", "/processing-terminals/1234001/payment-links", None, 1)


def test_paymentLinks_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "payment_links.retrieve.0"
    client = get_client(test_id)
    client.payment_links.retrieve(payment_link_id="JZURRJBUPS")
    verify_request_count(test_id, "GET", "/payment-links/JZURRJBUPS", None, 1)


def test_paymentLinks_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    test_id = "payment_links.partially_update.0"
    client = get_client(test_id)
    client.payment_links.partially_update(
        payment_link_id="JZURRJBUPS",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"op": "remove", "path": "path"}],
    )
    verify_request_count(test_id, "PATCH", "/payment-links/JZURRJBUPS", None, 1)


def test_paymentLinks_deactivate() -> None:
    """Test deactivate endpoint with WireMock"""
    test_id = "payment_links.deactivate.0"
    client = get_client(test_id)
    client.payment_links.deactivate(payment_link_id="JZURRJBUPS")
    verify_request_count(test_id, "POST", "/payment-links/JZURRJBUPS/deactivate", None, 1)
