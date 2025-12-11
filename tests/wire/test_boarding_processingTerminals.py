from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_boarding_processingTerminals_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_terminals.retrieve("1234001")
    verify_request_count("GET", "/processing-terminals/1234001", None, 1)


def test_boarding_processingTerminals_retrieve_host_configuration() -> None:
    """Test retrieveHostConfiguration endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.boarding.processing_terminals.retrieve_host_configuration("1234001")
    verify_request_count("GET", "/processing-terminals/1234001/host-configurations", None, 1)
