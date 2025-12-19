"""
Integration tests for card payment refunds - Create operation.

This test mirrors the .NET test at:
src/Payroc.TestFunctional/CardPayments/Refunds/CreateTests.cs

Tests run against Payroc UAT environment and require the following environment variables:
- PAYROC_API_KEY_PAYMENTS
- TERMINAL_ID_AVS

NOTE: This file is in tests/integration which is fern-ignored and will not
be overwritten during SDK generation.
"""

import json
import os
import uuid
from pathlib import Path

import pytest

from payroc import (
    Device,
    KeyedCardDetailsKeyedData_PlainText,
    CardPayloadCardDetails_Keyed,
    RefundOrder,
)
from payroc.card_payments.refunds import UnreferencedRefundRefundMethod_Card


@pytest.mark.integration
class TestCreateRefunds:
    """Integration tests for creating unreferenced refunds."""

    def load_test_data(self, filename: str) -> dict:
        """
        Load test data from JSON file.
        
        Args:
            filename: Name of the JSON file (without path)
            
        Returns:
            Dictionary containing the test data
        """
        test_data_dir = Path(__file__).parent.parent.parent / "test_data"
        file_path = test_data_dir / filename
        
        if not file_path.exists():
            raise FileNotFoundError(f"Test data file not found: {file_path}")
        
        with open(file_path, 'r') as f:
            return json.load(f)

    def test_smoke_test(self, payments_client, terminal_id_avs):
        """
        Smoke test for creating an unreferenced refund.
        
        This test creates an unreferenced refund and verifies that the transaction
        result status is 'ready'.
        
        Mirrors: CreateTests.SmokeTest() in .NET SDK
        """
        # Load base test data
        data = self.load_test_data("unreferenced_refund.json")
        
        # Generate unique idempotency key
        idempotency_key = str(uuid.uuid4())
        
        # Override with test-specific values
        processing_terminal_id = terminal_id_avs
        
        # Build the refund request matching the JSON structure
        refund_method = UnreferencedRefundRefundMethod_Card(
            card_details=CardPayloadCardDetails_Keyed(
                keyed_data=KeyedCardDetailsKeyedData_PlainText(
                    device=Device(
                        model=data["refund_method"]["card_details"]["keyed_data"]["device"]["model"],
                        serial_number=data["refund_method"]["card_details"]["keyed_data"]["device"]["serial_number"],
                    ),
                    card_number=data["refund_method"]["card_details"]["keyed_data"]["card_number"],
                    expiry_date=data["refund_method"]["card_details"]["keyed_data"]["expiry_date"],
                )
            )
        )
        
        order = RefundOrder(
            amount=data["order"]["amount"],
            currency=data["order"]["currency"],
            order_id=data["order"]["order_id"],
            description=data["order"]["description"],
        )
        
        # Create the unreferenced refund
        created_refund_response = payments_client.card_payments.refunds.create_unreferenced_refund(
            idempotency_key=idempotency_key,
            channel=data["channel"],
            processing_terminal_id=processing_terminal_id,
            order=order,
            refund_method=refund_method,
        )
        
        # Assert the transaction result status is 'ready'
        assert created_refund_response.transaction_result.status == "ready", \
            f"Expected status 'ready', got '{created_refund_response.transaction_result.status}'"
