from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_notifications_eventSubscriptions_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.notifications.event_subscriptions.list(
        status="registered", event="processingAccount.status.changed"
    )
    verify_request_count(
        "GET", "/event-subscriptions", {"status": "registered", "event": "processingAccount.status.changed"}, 1
    )


def test_notifications_eventSubscriptions_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.notifications.event_subscriptions.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        enabled=True,
        event_types=["processingAccount.status.changed"],
        notifications=[
            {
                "uri": "https://my-server/notification/endpoint",
                "secret": "aBcD1234eFgH5678iJkL9012mNoP3456",
                "supportEmailAddress": "supportEmailAddress",
                "type": "webhook",
            }
        ],
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count("POST", "/event-subscriptions", None, 1)


def test_notifications_eventSubscriptions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.notifications.event_subscriptions.retrieve(1)
    verify_request_count("GET", "/event-subscriptions/1", None, 1)


def test_notifications_eventSubscriptions_update() -> None:
    """Test update endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.notifications.event_subscriptions.update(
        1,
        enabled=True,
        event_types=["processingAccount.status.changed"],
        notifications=[
            {
                "uri": "https://my-server/notification/endpoint",
                "secret": "aBcD1234eFgH5678iJkL9012mNoP3456",
                "supportEmailAddress": "supportEmailAddress",
                "type": "webhook",
            }
        ],
        metadata={"yourCustomField": "abc123"},
    )
    verify_request_count("PUT", "/event-subscriptions/1", None, 1)


def test_notifications_eventSubscriptions_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.notifications.event_subscriptions.delete(1)
    verify_request_count("DELETE", "/event-subscriptions/1", None, 1)


def test_notifications_eventSubscriptions_partially_update() -> None:
    """Test partiallyUpdate endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.notifications.event_subscriptions.partially_update(
        1, idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324", request=[{"path": "path", "op": "remove"}]
    )
    verify_request_count("PATCH", "/event-subscriptions/1", None, 1)
