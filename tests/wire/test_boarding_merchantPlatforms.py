from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_merchantPlatforms_list() -> None:
    """Test list endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.merchant_platforms.list(before="2571", after="8516", limit=1)
    verify_request_count("GET", "/merchant-platforms", {"before": "2571", "after": "8516", "limit": "1"}, 1)


def test_boarding_merchantPlatforms_create() -> None:
    """Test create endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.merchant_platforms.create(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        business={
            "name": "Example Corp",
            "taxId": "12-3456789",
            "organizationType": "privateCorporation",
            "countryOfOperation": "US",
            "addresses": [
                {
                    "address1": "1 Example Ave.",
                    "address2": "Example Address Line 2",
                    "address3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postalCode": "60056",
                    "type": "legalAddress",
                }
            ],
            "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
        },
        processing_accounts=[
            {
                "doingBusinessAs": "Pizza Doe",
                "owners": [
                    {
                        "firstName": "Jane",
                        "middleName": "Helen",
                        "lastName": "Doe",
                        "dateOfBirth": "1964-03-22",
                        "address": {
                            "address1": "1 Example Ave.",
                            "address2": "Example Address Line 2",
                            "address3": "Example Address Line 3",
                            "city": "Chicago",
                            "state": "Illinois",
                            "country": "US",
                            "postalCode": "60056",
                        },
                        "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                        "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
                        "relationship": {
                            "equityPercentage": 48.5,
                            "title": "CFO",
                            "isControlProng": True,
                            "isAuthorizedSignatory": False,
                        },
                    }
                ],
                "website": "www.example.com",
                "businessType": "restaurant",
                "categoryCode": 5999,
                "merchandiseOrServiceSold": "Pizza",
                "businessStartDate": "2020-01-01",
                "timezone": "America/Chicago",
                "address": {
                    "address1": "1 Example Ave.",
                    "address2": "Example Address Line 2",
                    "address3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postalCode": "60056",
                },
                "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
                "processing": {
                    "transactionAmounts": {"average": 5000, "highest": 10000},
                    "monthlyAmounts": {"average": 50000, "highest": 100000},
                    "volumeBreakdown": {
                        "cardPresentKeyed": 47,
                        "cardPresentSwiped": 30,
                        "mailOrTelephone": 3,
                        "ecommerce": 20,
                    },
                    "isSeasonal": True,
                    "monthsOfOperation": ["jan", "feb"],
                    "ach": {
                        "naics": "5812",
                        "previouslyTerminatedForAch": False,
                        "refunds": {
                            "writtenRefundPolicy": True,
                            "refundPolicyUrl": "www.example.com/refund-poilcy-url",
                        },
                        "estimatedMonthlyTransactions": 3000,
                        "limits": {"singleTransaction": 10000, "dailyDeposit": 200000, "monthlyDeposit": 6000000},
                        "transactionTypes": ["prearrangedPayment", "other"],
                        "transactionTypesOther": "anotherTransactionType",
                    },
                    "cardAcceptance": {
                        "debitOnly": False,
                        "hsaFsa": False,
                        "cardsAccepted": ["visa", "mastercard"],
                        "specialityCards": {
                            "americanExpressDirect": {"enabled": True, "merchantNumber": "abc1234567"},
                            "electronicBenefitsTransfer": {"enabled": True, "fnsNumber": "6789012"},
                            "other": {
                                "wexMerchantNumber": "abc1234567",
                                "voyagerMerchantId": "abc1234567",
                                "fleetMerchantId": "abc1234567",
                            },
                        },
                    },
                },
                "funding": {
                    "fundingSchedule": "nextday",
                    "acceleratedFundingFee": 1999,
                    "dailyDiscount": False,
                    "fundingAccounts": [
                        {
                            "type": "checking",
                            "use": "creditAndDebit",
                            "nameOnAccount": "Jane Doe",
                            "paymentMethods": [{"type": "ach"}],
                            "metadata": {"yourCustomField": "abc123"},
                        }
                    ],
                },
                "pricing": {"pricingIntentId": "6123", "type": "intent"},
                "signature": {"type": "requestedViaDirectLink"},
                "contacts": [
                    {
                        "type": "manager",
                        "firstName": "Jane",
                        "middleName": "Helen",
                        "lastName": "Doe",
                        "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                        "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
                    }
                ],
                "metadata": {"customerId": "2345"},
            }
        ],
        metadata={"customerId": "2345"},
    )
    verify_request_count("POST", "/merchant-platforms", None, 1)


def test_boarding_merchantPlatforms_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.merchant_platforms.retrieve("12345")
    verify_request_count("GET", "/merchant-platforms/12345", None, 1)


def test_boarding_merchantPlatforms_list_processing_accounts() -> None:
    """Test listProcessingAccounts endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.merchant_platforms.list_processing_accounts(
        "12345", before="2571", after="8516", limit=1, include_closed=True
    )
    verify_request_count(
        "GET",
        "/merchant-platforms/12345/processing-accounts",
        {"before": "2571", "after": "8516", "limit": "1", "includeClosed": "true"},
        1,
    )


def test_boarding_merchantPlatforms_create_processing_account() -> None:
    """Test createProcessingAccount endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.merchant_platforms.create_processing_account(
        "12345",
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        doing_business_as="Pizza Doe",
        owners=[
            {
                "firstName": "Jane",
                "middleName": "Helen",
                "lastName": "Doe",
                "dateOfBirth": "1964-03-22",
                "address": {
                    "address1": "1 Example Ave.",
                    "address2": "Example Address Line 2",
                    "address3": "Example Address Line 3",
                    "city": "Chicago",
                    "state": "Illinois",
                    "country": "US",
                    "postalCode": "60056",
                },
                "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
                "relationship": {
                    "equityPercentage": 51.5,
                    "title": "CFO",
                    "isControlProng": True,
                    "isAuthorizedSignatory": False,
                },
            }
        ],
        website="www.example.com",
        business_type="restaurant",
        category_code=5999,
        merchandise_or_service_sold="Pizza",
        business_start_date="2020-01-01",
        timezone="America/Chicago",
        address={
            "address1": "1 Example Ave.",
            "address2": "Example Address Line 2",
            "address3": "Example Address Line 3",
            "city": "Chicago",
            "state": "Illinois",
            "country": "US",
            "postalCode": "60056",
        },
        contact_methods=[{"value": "jane.doe@example.com", "type": "email"}],
        processing={
            "transactionAmounts": {"average": 5000, "highest": 10000},
            "monthlyAmounts": {"average": 50000, "highest": 100000},
            "volumeBreakdown": {"cardPresentKeyed": 47, "cardPresentSwiped": 30, "mailOrTelephone": 3, "ecommerce": 20},
            "isSeasonal": True,
            "monthsOfOperation": ["jan", "feb"],
            "ach": {
                "naics": "5812",
                "previouslyTerminatedForAch": False,
                "refunds": {"writtenRefundPolicy": True, "refundPolicyUrl": "www.example.com/refund-poilcy-url"},
                "estimatedMonthlyTransactions": 3000,
                "limits": {"singleTransaction": 10000, "dailyDeposit": 200000, "monthlyDeposit": 6000000},
                "transactionTypes": ["prearrangedPayment", "other"],
                "transactionTypesOther": "anotherTransactionType",
            },
            "cardAcceptance": {
                "debitOnly": False,
                "hsaFsa": False,
                "cardsAccepted": ["visa", "mastercard"],
                "specialityCards": {
                    "americanExpressDirect": {"enabled": True, "merchantNumber": "abc1234567"},
                    "electronicBenefitsTransfer": {"enabled": True, "fnsNumber": "6789012"},
                    "other": {
                        "wexMerchantNumber": "abc1234567",
                        "voyagerMerchantId": "abc1234567",
                        "fleetMerchantId": "abc1234567",
                    },
                },
            },
        },
        funding={
            "fundingSchedule": "nextday",
            "acceleratedFundingFee": 1999,
            "dailyDiscount": False,
            "fundingAccounts": [
                {
                    "type": "checking",
                    "use": "creditAndDebit",
                    "nameOnAccount": "Jane Doe",
                    "paymentMethods": [{"type": "ach"}],
                    "metadata": {"yourCustomField": "abc123"},
                }
            ],
        },
        pricing={"pricingIntentId": "6123", "type": "intent"},
        signature={"type": "requestedViaDirectLink"},
        contacts=[
            {
                "type": "manager",
                "firstName": "Jane",
                "middleName": "Helen",
                "lastName": "Doe",
                "identifiers": [{"type": "nationalId", "value": "000-00-4320"}],
                "contactMethods": [{"value": "jane.doe@example.com", "type": "email"}],
            }
        ],
        metadata={"customerId": "2345"},
    )
    verify_request_count("POST", "/merchant-platforms/12345/processing-accounts", None, 1)
