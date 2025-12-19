from .conftest import get_client, verify_request_count


def test_paymentFeatures_cards_verify_card() -> None:
    """Test verifyCard endpoint with WireMock"""
    test_id = "payment_features.cards.verify_card.0"
    client = get_client(test_id)
    client.payment_features.cards.verify_card(
        idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324",
        processing_terminal_id="1234001",
        operator="Jane",
        card={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
    )
    verify_request_count(test_id, "POST", "/cards/verify", None, 1)


def test_paymentFeatures_cards_view_ebt_balance() -> None:
    """Test viewEbtBalance endpoint with WireMock"""
    test_id = "payment_features.cards.view_ebt_balance.0"
    client = get_client(test_id)
    client.payment_features.cards.view_ebt_balance(
        processing_terminal_id="1234001",
        operator="Jane",
        currency="USD",
        card={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
    )
    verify_request_count(test_id, "POST", "/cards/balance", None, 1)


def test_paymentFeatures_cards_lookup_bin() -> None:
    """Test lookupBin endpoint with WireMock"""
    test_id = "payment_features.cards.lookup_bin.0"
    client = get_client(test_id)
    client.payment_features.cards.lookup_bin(
        processing_terminal_id="1234001",
        card={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
    )
    verify_request_count(test_id, "POST", "/cards/bin-lookup", None, 1)


def test_paymentFeatures_cards_retrieve_fx_rates() -> None:
    """Test retrieveFxRates endpoint with WireMock"""
    test_id = "payment_features.cards.retrieve_fx_rates.0"
    client = get_client(test_id)
    client.payment_features.cards.retrieve_fx_rates(
        channel="web",
        processing_terminal_id="1234001",
        operator="Jane",
        base_amount=10000,
        base_currency="USD",
        payment_method={
            "type": "card",
            "card_details": {
                "entry_method": "raw",
                "device": {"model": "bbposChp", "serial_number": "1850010868"},
                "raw_data": "A1B2C3D4E5F67890ABCD1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
            },
        },
    )
    verify_request_count(test_id, "POST", "/fx-rates", None, 1)
