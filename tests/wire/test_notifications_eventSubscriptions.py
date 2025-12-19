from .conftest import get_client, verify_request_count


def test_notifications_eventSubscriptions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "notifications.event_subscriptions.list_.0"
    client = get_client(test_id)
    client.notifications.event_subscriptions.list(status="registered", event="processingAccount.status.changed")
    verify_request_count(
        test_id, "GET", "/event-subscriptions", {"status": "registered", "event": "processingAccount.status.changed"}, 1
    )


def test_notifications_eventSubscriptions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "notifications.event_subscriptions.create.0"
    client = get_client(test_id)
    client.notifications.event_subscriptions.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        enabled=True,
        event_types=["processingAccount.status.changed"],
        notifications=[
            {
                "type": "webhook",
                "uri": "https://my-server/notification/endpoint",
                "secret": "aBcD1234eFgH5678iJkL9012mNoP3456",
                "support_email_address": "supportEmailAddress",
            }
        ],
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count(test_id, "POST", "/event-subscriptions", None, 1)


def test_notifications_eventSubscriptions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "notifications.event_subscriptions.retrieve.0"
    client = get_client(test_id)
    client.notifications.event_subscriptions.retrieve(subscription_id=1)
    verify_request_count(test_id, "GET", "/event-subscriptions/1", None, 1)


def test_notifications_eventSubscriptions_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "notifications.event_subscriptions.update.0"
    client = get_client(test_id)
    client.notifications.event_subscriptions.update(
        subscription_id=1,
        enabled=True,
        event_types=["processingAccount.status.changed"],
        notifications=[
            {
                "type": "webhook",
                "uri": "https://my-server/notification/endpoint",
                "secret": "aBcD1234eFgH5678iJkL9012mNoP3456",
                "support_email_address": "supportEmailAddress",
            }
        ],
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count(test_id, "PUT", "/event-subscriptions/1", None, 1)


def test_notifications_eventSubscriptions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "notifications.event_subscriptions.delete.0"
    client = get_client(test_id)
    client.notifications.event_subscriptions.delete(subscription_id=1)
    verify_request_count(test_id, "DELETE", "/event-subscriptions/1", None, 1)


def test_notifications_eventSubscriptions_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    test_id = "notifications.event_subscriptions.partially_update.0"
    client = get_client(test_id)
    client.notifications.event_subscriptions.partially_update(
        subscription_id=1,
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request=[{"op": "remove", "path": "path"}],
    )
    verify_request_count(test_id, "PATCH", "/event-subscriptions/1", None, 1)
