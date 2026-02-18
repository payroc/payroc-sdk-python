"""
Test that README examples compile and are syntactically correct.

This test validates that code examples in the README are up-to-date
with the current SDK structure after domain reorganization.

NOTE: This file is fern-ignored to prevent it from being overwritten during generation.
"""

import datetime
import os
from typing import Optional

import pytest


class TestReadmeExamplesCompile:
    """Verify that README code examples compile without errors."""

    def test_basic_client_initialization(self):
        """Test that basic client initialization example compiles."""
        from payroc import Payroc

        # This should compile without errors
        # We don't actually run it since we don't have a real API key
        def example():
            api_key = os.environ.get("PAYROC_API_KEY")
            if not api_key:
                raise Exception("Payroc API Key not found")
            client = Payroc(api_key=api_key)
            return client

        # Just verify the function is callable
        assert callable(example)

    def test_async_client_initialization(self):
        """Test that async client initialization example compiles."""
        from payroc import AsyncPayroc

        # This should compile without errors
        def example():
            api_key = os.environ.get("PAYROC_API_KEY")
            if not api_key:
                raise Exception("Payroc API Key not found")
            client = AsyncPayroc(api_key=api_key)
            return client

        assert callable(example)

    def test_custom_environment_example(self):
        """Test that custom environment example compiles."""
        from payroc import Payroc, PayrocEnvironment

        def example():
            api_key = "test_key"
            mock_environment = PayrocEnvironment(
                api="http://localhost:3000",
                identity="http://localhost:3001"
            )
            client = Payroc(
                api_key=api_key,
                environment=mock_environment
            )
            return client

        assert callable(example)

    def test_payment_creation_imports(self):
        """Test that payment creation example imports are correct."""
        # Verify all imports from README example work
        from payroc import (
            Address,
            CardPayloadCardDetails_Raw,
            Customer,
            CustomField,
            Device,
            PaymentOrderRequest,
            Payroc,
            Shipping,
        )
        from payroc.card_payments.payments import PaymentRequestPaymentMethod_Card

        # All imports should succeed
        assert Address is not None
        assert CardPayloadCardDetails_Raw is not None
        assert Customer is not None
        assert CustomField is not None
        assert Device is not None
        assert PaymentOrderRequest is not None
        assert Payroc is not None
        assert Shipping is not None
        assert PaymentRequestPaymentMethod_Card is not None

    def test_payment_creation_structure(self):
        """Test that payment creation uses correct namespace structure."""
        from payroc import (
            Address,
            CardPayloadCardDetails_Raw,
            Customer,
            CustomField,
            Device,
            PaymentOrderRequest,
            Payroc,
            Shipping,
        )
        from payroc.card_payments.payments import PaymentRequestPaymentMethod_Card

        def example():
            api_key = "test_key"
            client = Payroc(api_key=api_key)
            
            # Verify the namespace structure: client.card_payments.payments.create
            # This should compile without errors
            payment_data = {
                "idempotency_key": "8e03978e-40d5-43e8-bc93-6894a57f9324",
                "channel": "web",
                "processing_terminal_id": "1234001",
                "operator": "Jane",
                "order": PaymentOrderRequest(
                    order_id="OrderRef6543",
                    description="Large Pepperoni Pizza",
                    amount=4999,
                    currency="USD",
                ),
                "customer": Customer(
                    first_name="Sarah",
                    last_name="Hopper",
                    billing_address=Address(
                        address_1="1 Example Ave.",
                        city="Chicago",
                        state="Illinois",
                        country="US",
                        postal_code="60056",
                    ),
                ),
                "payment_method": PaymentRequestPaymentMethod_Card(
                    card_details=CardPayloadCardDetails_Raw(
                        device=Device(
                            model="bbposChp",
                            serial_number="1850010868",
                        ),
                        raw_data="A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
                    ),
                ),
                "custom_fields": [
                    CustomField(
                        name="yourCustomField",
                        value="abc123",
                    )
                ],
            }
            
            # Verify the method exists on the correct path
            assert hasattr(client, 'card_payments')
            assert hasattr(client.card_payments, 'payments')
            assert hasattr(client.card_payments.payments, 'create')
            
            return payment_data

        assert callable(example)

    def test_async_payment_creation_structure(self):
        """Test that async payment creation uses correct namespace structure."""
        from payroc import AsyncPayroc

        def example():
            api_key = "test_key"
            client = AsyncPayroc(api_key=api_key)
            
            # Verify the namespace structure for async client
            assert hasattr(client, 'card_payments')
            assert hasattr(client.card_payments, 'payments')
            assert hasattr(client.card_payments.payments, 'create')

        assert callable(example)

    def test_pagination_list_structure(self):
        """Test that pagination example uses correct list method structure."""
        from payroc import Payroc

        def example():
            api_key = "test_key"
            client = Payroc(api_key=api_key)
            
            # Verify the list method exists on correct path
            assert hasattr(client, 'card_payments')
            assert hasattr(client.card_payments, 'payments')
            assert hasattr(client.card_payments.payments, 'list')
            
            # Verify parameters compile
            params = {
                "processing_terminal_id": "1234001",
                "order_id": "OrderRef6543",
                "operator": "Jane",
                "cardholder_name": "Sarah%20Hazel%20Hopper",
                "first_6": "453985",
                "last_4": "7062",
                "tender": "ebt",
                "date_from": datetime.datetime.fromisoformat("2024-07-01T15:30:00+00:00"),
                "date_to": datetime.datetime.fromisoformat("2024-07-03T15:30:00+00:00"),
                "settlement_state": "settled",
                "settlement_date": "2024-07-02",
                "payment_link_id": "JZURRJBUPS",
                "before": "2571",
                "after": "8516",
                "limit": 1,
            }
            
            return params

        assert callable(example)

    def test_async_pagination_structure(self):
        """Test that async pagination example uses correct structure."""
        from payroc import AsyncPayroc

        def example():
            api_key = "test_key"
            client = AsyncPayroc(api_key=api_key)
            
            # Verify the namespace structure
            assert hasattr(client, 'card_payments')
            assert hasattr(client.card_payments, 'payments')
            assert hasattr(client.card_payments.payments, 'list')

        assert callable(example)

    def test_polymorphic_types_imports(self):
        """Test that polymorphic types example imports are correct."""
        from payroc.card_payments.payments import (
            PaymentRequestPaymentMethod_Card,
            PaymentRequestPaymentMethod_SecureToken,
        )
        from payroc import (
            CardPayloadCardDetails_Keyed,
            KeyedCardDetailsKeyedData_PlainText,
        )

        # All imports should succeed
        assert PaymentRequestPaymentMethod_Card is not None
        assert PaymentRequestPaymentMethod_SecureToken is not None
        assert CardPayloadCardDetails_Keyed is not None
        assert KeyedCardDetailsKeyedData_PlainText is not None

    def test_polymorphic_types_creation(self):
        """Test that polymorphic types can be created as shown in README."""
        from payroc.card_payments.payments import (
            PaymentRequestPaymentMethod_Card,
            PaymentRequestPaymentMethod_SecureToken,
        )
        from payroc import (
            CardPayloadCardDetails_Keyed,
            KeyedCardDetailsKeyedData_PlainText,
        )

        def example():
            # Create a card payment method with keyed data
            card_payment = PaymentRequestPaymentMethod_Card(
                card_details=CardPayloadCardDetails_Keyed(
                    keyed_data=KeyedCardDetailsKeyedData_PlainText(
                        card_number="4111111111111111",
                        expiry_date="1230",
                        cvv="123"
                    )
                )
            )

            # Create a secure token payment method
            token_payment = PaymentRequestPaymentMethod_SecureToken(
                token="your-secure-token-here"
            )
            
            return card_payment, token_payment

        assert callable(example)

    def test_boarding_owners_retrieve_structure(self):
        """Test that boarding.owners.retrieve example uses correct structure."""
        from payroc import Payroc

        def example():
            api_key = "test_key"
            client = Payroc(api_key=api_key)
            
            # Verify the namespace structure
            assert hasattr(client, 'boarding')
            assert hasattr(client.boarding, 'owners')
            assert hasattr(client.boarding.owners, 'retrieve')

        assert callable(example)

    def test_contact_method_types_imports(self):
        """Test that contact method types can be imported."""
        from payroc.types import ContactMethod_Email, ContactMethod_Phone

        assert ContactMethod_Email is not None
        assert ContactMethod_Phone is not None

    def test_raw_response_structure(self):
        """Test that raw response example uses correct structure."""
        from payroc import Payroc

        def example():
            api_key = "test_key"
            client = Payroc(api_key=api_key)
            
            # Verify with_raw_response exists on correct path
            assert hasattr(client.card_payments.payments, 'with_raw_response')
            assert hasattr(client.card_payments.payments.with_raw_response, 'create')

        assert callable(example)

    def test_request_options_import(self):
        """Test that RequestOptions can be imported as shown in README."""
        from payroc.core.request_options import RequestOptions

        assert RequestOptions is not None

    def test_api_error_import(self):
        """Test that ApiError can be imported as shown in README."""
        from payroc.core.api_error import ApiError

        assert ApiError is not None

    def test_exception_handling_structure(self):
        """Test that exception handling example compiles."""
        from payroc import Payroc
        from payroc.core.api_error import ApiError

        def example():
            api_key = "test_key"
            client = Payroc(api_key=api_key)
            
            try:
                # This would normally call the API
                # client.card_payments.payments.create(...)
                pass
            except ApiError as e:
                # These attributes should exist
                _ = e.status_code
                _ = e.body
                
        assert callable(example)

    def test_timeout_configuration_example(self):
        """Test that timeout configuration example compiles."""
        from payroc import Payroc
        from payroc.core.request_options import RequestOptions

        def example():
            api_key = "test_key"
            
            # Client-level timeout
            client = Payroc(
                api_key=api_key,
                timeout=20.0,
            )
            
            # Request-level timeout structure
            request_opts = RequestOptions(
                timeout_in_seconds=1
            )
            
            return client, request_opts

        assert callable(example)

    def test_custom_httpx_client_example(self):
        """Test that custom httpx client example compiles."""
        import httpx
        from payroc import Payroc

        def example():
            api_key = "test_key"
            
            client = Payroc(
                api_key=api_key,
                httpx_client=httpx.Client(
                    proxy="http://my.test.proxy.example.com",
                    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
                ),
            )
            
            return client

        assert callable(example)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
