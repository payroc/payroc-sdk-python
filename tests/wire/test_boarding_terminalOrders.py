from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_terminalOrders_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.terminal_orders.retrieve("12345")
    verify_request_count("GET", "/terminal-orders/12345", None, 1)
