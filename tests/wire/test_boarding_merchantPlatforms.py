from datetime import date

from .conftest import get_client, verify_request_count


def test_boarding_merchantPlatforms_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "boarding.merchant_platforms.list_.0"
    client = get_client(test_id)
    client.boarding.merchant_platforms.list(before="2571", after="8516", limit=1)
    verify_request_count(test_id, "GET", "/merchant-platforms", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_boarding_merchantPlatforms_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "boarding.merchant_platforms.create.0"
    client = get_client(test_id)
    client.boarding.merchant_platforms.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        business={
            "name": "Example Corp",
            "tax_id": "12-3456789",
            "organization_type": "privateCorporation",
            "country_of_operation": "US",
            "addresses": [
                {
                    "address_1": "1 Example Ave.",
                    "address_2": "Example Address Line 2",
                    "address_3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postal_code": "60056",
                    "type": "legalAddress",
                }
            ],
            "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
        },
        processing_accounts=[
            {
                "doing_business_as": "Pizza Doe",
                "owners": [
                    {
                        "first_name": "Jane",
                        "middle_name": "Helen",
                        "last_name": "Doe",
                        "date_of_birth": date.fromisoformat("1964-03-22"),
                        "address": {
                            "address_1": "1 Example Ave.",
                            "address_2": "Example Address Line 2",
                            "address_3": "Example Address Line 3",
                            "city": "Chicago",
                            "state": "Illinois",
                            "country": "US",
                            "postal_code": "60056",
                        },
                        "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                        "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
                        "relationship": {
                            "equity_percentage": 48.5,
                            "title": "CFO",
                            "is_control_prong": True,
                            "is_authorized_signatory": False,
                        },
                    }
                ],
                "website": "www.example.com",
                "business_type": "restaurant",
                "category_code": 5999,
                "merchandise_or_service_sold": "Pizza",
                "business_start_date": date.fromisoformat("2020-01-01"),
                "timezone": "America/Chicago",
                "address": {
                    "address_1": "1 Example Ave.",
                    "address_2": "Example Address Line 2",
                    "address_3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postal_code": "60056",
                },
                "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
                "processing": {
                    "transaction_amounts": {"average": 5000, "highest": 10000},
                    "monthly_amounts": {"average": 50000, "highest": 100000},
                    "volume_breakdown": {"card_present": 77, "mail_or_telephone": 3, "ecommerce": 20},
                    "is_seasonal": True,
                    "months_of_operation": ["jan", "feb"],
                    "ach": {
                        "naics": "5812",
                        "previously_terminated_for_ach": False,
                        "refunds": {
                            "written_refund_policy": True,
                            "refund_policy_url": "www.example.com/refund-poilcy-url",
                        },
                        "estimated_monthly_transactions": 3000,
                        "limits": {"single_transaction": 10000, "daily_deposit": 200000, "monthly_deposit": 6000000},
                        "transaction_types": ["prearrangedPayment", "other"],
                        "transaction_types_other": "anotherTransactionType",
                    },
                    "card_acceptance": {
                        "debit_only": False,
                        "hsa_fsa": False,
                        "cards_accepted": ["visa", "mastercard"],
                        "speciality_cards": {
                            "american_express_direct": {"enabled": True, "merchant_number": "abc1234567"},
                            "electronic_benefits_transfer": {"enabled": True, "fns_number": "6789012"},
                            "other": {
                                "wex_merchant_number": "abc1234567",
                                "voyager_merchant_id": "abc1234567",
                                "fleet_merchant_id": "abc1234567",
                            },
                        },
                    },
                },
                "funding": {
                    "funding_schedule": "nextday",
                    "accelerated_funding_fee": 1999,
                    "daily_discount": False,
                    "funding_accounts": [
                        {
                            "type": "checking",
                            "use": "creditAndDebit",
                            "name_on_account": "Jane Doe",
                            "payment_methods": [{"type": "ach"}],
                            "metadata": {"yourCustomField": "abc123"},
                        }
                    ],
                },
                "pricing": {"type": "intent", "pricing_intent_id": "6123"},
                "signature": {"type": "requestedViaDirectLink"},
                "contacts": [
                    {
                        "type": "manager",
                        "first_name": "Jane",
                        "middle_name": "Helen",
                        "last_name": "Doe",
                        "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                        "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
                    }
                ],
                "metadata": {"customerId": "2345"},
            }
        ],
        metadata={"customerId": "2345"},
    )
    verify_request_count(test_id, "POST", "/merchant-platforms", None, 1)


def test_boarding_merchantPlatforms_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.merchant_platforms.retrieve.0"
    client = get_client(test_id)
    client.boarding.merchant_platforms.retrieve(merchant_platform_id="12345")
    verify_request_count(test_id, "GET", "/merchant-platforms/12345", None, 1)


def test_boarding_merchantPlatforms_list_processing_accounts() -> None:
    """Test listProcessingAccounts endpoint with WireMock"""
    test_id = "boarding.merchant_platforms.list_processing_accounts.0"
    client = get_client(test_id)
    client.boarding.merchant_platforms.list_processing_accounts(
        merchant_platform_id="12345", before="2571", after="8516", limit=1, include_closed=True
    )
    verify_request_count(
        test_id,
        "GET",
        "/merchant-platforms/12345/processing-accounts",
        {"before": "2571", "after": "8516", "limit": "1", "includeClosed": "true"},
        1,
    )


def test_boarding_merchantPlatforms_create_processing_account() -> None:
    """Test createProcessingAccount endpoint with WireMock"""
    test_id = "boarding.merchant_platforms.create_processing_account.0"
    client = get_client(test_id)
    client.boarding.merchant_platforms.create_processing_account(
        merchant_platform_id="12345",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        doing_business_as="Pizza Doe",
        owners=[
            {
                "first_name": "Jane",
                "middle_name": "Helen",
                "last_name": "Doe",
                "date_of_birth": date.fromisoformat("1964-03-22"),
                "address": {
                    "address_1": "1 Example Ave.",
                    "address_2": "Example Address Line 2",
                    "address_3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postal_code": "60056",
                },
                "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
                "relationship": {
                    "equity_percentage": 51.5,
                    "title": "CFO",
                    "is_control_prong": True,
                    "is_authorized_signatory": False,
                },
            }
        ],
        website="www.example.com",
        business_type="restaurant",
        category_code=5999,
        merchandise_or_service_sold="Pizza",
        business_start_date=date.fromisoformat("2020-01-01"),
        timezone="America/Chicago",
        address={
            "address_1": "1 Example Ave.",
            "address_2": "Example Address Line 2",
            "address_3": "Example Address Line 3",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postal_code": "60056",
        },
        contact_methods=[{"type": "email", "value": "jane.doe@example.com"}],
        processing={
            "transaction_amounts": {"average": 5000, "highest": 10000},
            "monthly_amounts": {"average": 50000, "highest": 100000},
            "volume_breakdown": {"card_present": 77, "mail_or_telephone": 3, "ecommerce": 20},
            "is_seasonal": True,
            "months_of_operation": ["jan", "feb"],
            "ach": {
                "naics": "5812",
                "previously_terminated_for_ach": False,
                "refunds": {"written_refund_policy": True, "refund_policy_url": "www.example.com/refund-poilcy-url"},
                "estimated_monthly_transactions": 3000,
                "limits": {"single_transaction": 10000, "daily_deposit": 200000, "monthly_deposit": 6000000},
                "transaction_types": ["prearrangedPayment", "other"],
                "transaction_types_other": "anotherTransactionType",
            },
            "card_acceptance": {
                "debit_only": False,
                "hsa_fsa": False,
                "cards_accepted": ["visa", "mastercard"],
                "speciality_cards": {
                    "american_express_direct": {"enabled": True, "merchant_number": "abc1234567"},
                    "electronic_benefits_transfer": {"enabled": True, "fns_number": "6789012"},
                    "other": {
                        "wex_merchant_number": "abc1234567",
                        "voyager_merchant_id": "abc1234567",
                        "fleet_merchant_id": "abc1234567",
                    },
                },
            },
        },
        funding={
            "funding_schedule": "nextday",
            "accelerated_funding_fee": 1999,
            "daily_discount": False,
            "funding_accounts": [
                {
                    "type": "checking",
                    "use": "creditAndDebit",
                    "name_on_account": "Jane Doe",
                    "payment_methods": [{"type": "ach"}],
                    "metadata": {"yourCustomField": "abc123"},
                }
            ],
        },
        pricing={"type": "intent", "pricing_intent_id": "6123"},
        signature={"type": "requestedViaDirectLink"},
        contacts=[
            {
                "type": "manager",
                "first_name": "Jane",
                "middle_name": "Helen",
                "last_name": "Doe",
                "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                "contact_methods": [{"type": "email", "value": "jane.doe@example.com"}],
            }
        ],
        metadata={"customerId": "2345"},
    )
    verify_request_count(test_id, "POST", "/merchant-platforms/12345/processing-accounts", None, 1)
