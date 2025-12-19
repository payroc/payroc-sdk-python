from .conftest import get_client, verify_request_count


def test_boarding_terminalOrders_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.terminal_orders.retrieve.0"
    client = get_client(test_id)
    client.boarding.terminal_orders.retrieve(terminal_order_id="12345")
    verify_request_count(test_id, "GET", "/terminal-orders/12345", None, 1)
