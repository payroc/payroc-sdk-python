"""
Quick verification script to check if the integration test imports work correctly.
This doesn't run the actual test, just verifies the structure is valid.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

try:
    print("Checking imports...")
    
    # Check main SDK imports
    from payroc import Payroc, PayrocEnvironment
    print("✓ Main SDK imports successful")
    
    # Check type imports
    from payroc import (
        Device,
        KeyedCardDetailsKeyedData_PlainText,
        CardPayloadCardDetails_Keyed,
        RefundOrder,
    )
    print("✓ Type imports successful")
    
    # Check refund-specific imports
    from payroc.card_payments.refunds import UnreferencedRefundRefundMethod_Card
    print("✓ Refund method import successful")
    
    # Verify PayrocEnvironment.UAT exists
    assert hasattr(PayrocEnvironment, 'UAT'), "PayrocEnvironment.UAT not found"
    print(f"✓ UAT environment exists: {PayrocEnvironment.UAT.api}")
    
    # Verify client structure
    print("\nVerifying client structure...")
    test_client = Payroc(api_key="test_key", environment=PayrocEnvironment.UAT)
    assert hasattr(test_client, 'card_payments'), "card_payments not found on client"
    assert hasattr(test_client.card_payments, 'refunds'), "refunds not found on card_payments"
    assert hasattr(test_client.card_payments.refunds, 'create_unreferenced_refund'), \
        "create_unreferenced_refund not found on refunds client"
    print("✓ Client structure is correct")
    
    print("\n✅ All verification checks passed!")
    print("\nThe integration test structure is valid.")
    print("To run the actual test, you need:")
    print("  1. pytest installed")
    print("  2. Environment variables set:")
    print("     - PAYROC_API_KEY_PAYMENTS")
    print("     - TERMINAL_ID_AVS")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except AssertionError as e:
    print(f"❌ Assertion error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
