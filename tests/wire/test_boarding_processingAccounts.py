from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment
from datetime import datetime

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_processingAccounts_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.retrieve("38765")
    verify_request_count("GET", "/processing-accounts/38765", None, 1)


def test_boarding_processingAccounts_list_processing_account_funding_accounts() -> None:
    """Test listProcessingAccountFundingAccounts endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.list_processing_account_funding_accounts("38765")
    verify_request_count("GET", "/processing-accounts/38765/funding-accounts", None, 1)


def test_boarding_processingAccounts_list_contacts() -> None:
    """Test listContacts endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.list_contacts("38765", before="2571", after="8516", limit=1)
    verify_request_count(
        "GET", "/processing-accounts/38765/contacts", {"before": "2571", "after": "8516", "limit": "1"}, 1
    )


def test_boarding_processingAccounts_get_processing_account_pricing_agreement() -> None:
    """Test getProcessingAccountPricingAgreement endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.get_processing_account_pricing_agreement("38765")
    verify_request_count("GET", "/processing-accounts/38765/pricing", None, 1)


def test_boarding_processingAccounts_list_owners() -> None:
    """Test listOwners endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.list_owners("38765", before="2571", after="8516", limit=1)
    verify_request_count(
        "GET", "/processing-accounts/38765/owners", {"before": "2571", "after": "8516", "limit": "1"}, 1
    )


def test_boarding_processingAccounts_create_reminder() -> None:
    """Test createReminder endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.create_reminder(
        "38765", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324", request={"type": "pricingAgreement"}
    )
    verify_request_count("POST", "/processing-accounts/38765/reminders", None, 1)


def test_boarding_processingAccounts_list_terminal_orders() -> None:
    """Test listTerminalOrders endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.list_terminal_orders(
        "38765", 
        status="open", 
        from_date_time=datetime.fromisoformat("2024-09-08T12:00:00+00:00"), 
        to_date_time=datetime.fromisoformat("2024-12-08T11:00:00+00:00")
    )
    verify_request_count(
        "GET",
        "/processing-accounts/38765/terminal-orders",
        {"status": "open", "fromDateTime": "2024-09-08T12:00:00Z", "toDateTime": "2024-12-08T11:00:00Z"},
        1,
    )


def test_boarding_processingAccounts_create_terminal_order() -> None:
    """Test createTerminalOrder endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.create_terminal_order(
        "38765",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        training_provider="payroc",
        shipping={
            "preferences": {"method": "nextDay", "saturdayDelivery": True},
            "address": {
                "recipientName": "Recipient Name",
                "businessName": "Company Ltd",
                "addressLine1": "1 Example Ave.",
                "addressLine2": "Example Address Line 2",
                "city": "Chicago",
                "state": "Illinois",
                "postalCode": "60056",
                "email": "example@mail.com",
                "phone": "2025550164",
            },
        },
        order_items=[
            {
                "type": "solution",
                "solutionTemplateId": "Roc Services_DX8000",
                "solutionQuantity": 1,
                "deviceCondition": "new",
                "solutionSetup": {
                    "timezone": "America/Chicago",
                    "industryTemplateId": "Retail",
                    "gatewaySettings": {
                        "merchantPortfolioId": "Company Ltd",
                        "merchantTemplateId": "Company Ltd Merchant Template",
                        "userTemplateId": "Company Ltd User Template",
                        "terminalTemplateId": "Company Ltd Terminal Template",
                    },
                    "applicationSettings": {
                        "clerkPrompt": False,
                        "security": {"refundPassword": True, "keyedSalePassword": False, "reversalPassword": True},
                    },
                    "deviceSettings": {"numberOfMobileUsers": 2, "communicationType": "wifi"},
                    "batchClosure": {"batchCloseType": "automatic"},
                    "receiptNotifications": {"emailReceipt": True, "smsReceipt": False},
                    "taxes": [{"taxRate": 6, "taxLabel": "Sales Tax"}],
                    "tips": {"enabled": False},
                    "tokenization": True,
                },
            }
        ],
    )
    verify_request_count("POST", "/processing-accounts/38765/terminal-orders", None, 1)


def test_boarding_processingAccounts_list_processing_terminals() -> None:
    """Test listProcessingTerminals endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_accounts.list_processing_terminals(
        "38765", before="2571", after="8516", limit=1
    )
    verify_request_count(
        "GET", "/processing-accounts/38765/processing-terminals", {"before": "2571", "after": "8516", "limit": "1"}, 1
    )
