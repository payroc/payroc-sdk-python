from datetime import datetime

from .conftest import get_client, verify_request_count


def test_boarding_processingAccounts_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.processing_accounts.retrieve.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.retrieve(processing_account_id="38765")
    verify_request_count(test_id, "GET", "/processing-accounts/38765", None, 1)


def test_boarding_processingAccounts_list_processing_account_funding_accounts() -> None:
    """Test listProcessingAccountFundingAccounts endpoint with WireMock"""
    test_id = "boarding.processing_accounts.list_processing_account_funding_accounts.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.list_processing_account_funding_accounts(processing_account_id="38765")
    verify_request_count(test_id, "GET", "/processing-accounts/38765/funding-accounts", None, 1)


def test_boarding_processingAccounts_list_contacts() -> None:
    """Test listContacts endpoint with WireMock"""
    test_id = "boarding.processing_accounts.list_contacts.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.list_contacts(
        processing_account_id="38765", before="2571", after="8516", limit=1
    )
    verify_request_count(
        test_id, "GET", "/processing-accounts/38765/contacts", {"before": "2571", "after": "8516", "limit": "1"}, 1
    )


def test_boarding_processingAccounts_get_processing_account_pricing_agreement() -> None:
    """Test getProcessingAccountPricingAgreement endpoint with WireMock"""
    test_id = "boarding.processing_accounts.get_processing_account_pricing_agreement.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.get_processing_account_pricing_agreement(processing_account_id="38765")
    verify_request_count(test_id, "GET", "/processing-accounts/38765/pricing", None, 1)


def test_boarding_processingAccounts_list_owners() -> None:
    """Test listOwners endpoint with WireMock"""
    test_id = "boarding.processing_accounts.list_owners.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.list_owners(processing_account_id="38765", before="2571", after="8516", limit=1)
    verify_request_count(
        test_id, "GET", "/processing-accounts/38765/owners", {"before": "2571", "after": "8516", "limit": "1"}, 1
    )


def test_boarding_processingAccounts_create_reminder() -> None:
    """Test createReminder endpoint with WireMock"""
    test_id = "boarding.processing_accounts.create_reminder.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.create_reminder(
        processing_account_id="38765",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        request={"type": "pricingAgreement"},
    )
    verify_request_count(test_id, "POST", "/processing-accounts/38765/reminders", None, 1)


def test_boarding_processingAccounts_list_terminal_orders() -> None:
    """Test listTerminalOrders endpoint with WireMock"""
    test_id = "boarding.processing_accounts.list_terminal_orders.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.list_terminal_orders(
        processing_account_id="38765",
        status="open",
        from_date_time=datetime.fromisoformat("2024-09-08T12:00:00Z"),
        to_date_time=datetime.fromisoformat("2024-12-08T11:00:00Z"),
    )
    verify_request_count(
        test_id,
        "GET",
        "/processing-accounts/38765/terminal-orders",
        {"status": "open", "fromDateTime": "2024-09-08T12:00:00Z", "toDateTime": "2024-12-08T11:00:00Z"},
        1,
    )


def test_boarding_processingAccounts_create_terminal_order() -> None:
    """Test createTerminalOrder endpoint with WireMock"""
    test_id = "boarding.processing_accounts.create_terminal_order.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.create_terminal_order(
        processing_account_id="38765",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        training_provider="payroc",
        shipping={
            "preferences": {"method": "nextDay", "saturday_delivery": True},
            "address": {
                "recipient_name": "Recipient Name",
                "business_name": "Company Ltd",
                "address_line_1": "1 Example Ave.",
                "address_line_2": "Example Address Line 2",
                "city": "Chicago",
                "state": "Illinois",
                "postal_code": "60056",
                "email": "example@mail.com",
                "phone": "2025550164",
            },
        },
        order_items=[
            {
                "type": "solution",
                "solution_template_id": "Roc Services_DX8000",
                "solution_quantity": 1,
                "device_condition": "new",
                "solution_setup": {
                    "timezone": "America/Chicago",
                    "industry_template_id": "Retail",
                    "gateway_settings": {
                        "merchant_portfolio_id": "Company Ltd",
                        "merchant_template_id": "Company Ltd Merchant Template",
                        "user_template_id": "Company Ltd User Template",
                        "terminal_template_id": "Company Ltd Terminal Template",
                    },
                    "application_settings": {
                        "clerk_prompt": False,
                        "security": {"refund_password": True, "keyed_sale_password": False, "reversal_password": True},
                    },
                    "device_settings": {"number_of_mobile_users": 2, "communication_type": "wifi"},
                    "batch_closure": {"batch_close_type": "automatic"},
                    "receipt_notifications": {"email_receipt": True, "sms_receipt": False},
                    "taxes": [{"tax_rate": 6, "tax_label": "Sales Tax"}],
                    "tips": {"enabled": False},
                    "tokenization": True,
                },
            }
        ],
    )
    verify_request_count(test_id, "POST", "/processing-accounts/38765/terminal-orders", None, 1)


def test_boarding_processingAccounts_list_processing_terminals() -> None:
    """Test listProcessingTerminals endpoint with WireMock"""
    test_id = "boarding.processing_accounts.list_processing_terminals.0"
    client = get_client(test_id)
    client.boarding.processing_accounts.list_processing_terminals(
        processing_account_id="38765", before="2571", after="8516", limit=1
    )
    verify_request_count(
        test_id,
        "GET",
        "/processing-accounts/38765/processing-terminals",
        {"before": "2571", "after": "8516", "limit": "1"},
        1,
    )
