from typing import Optional, Dict, Any
from payroc import Payroc, PayrocEnvironment

import pytest

import requests
from conftest import verify_request_count


 


def test_payrocCloud_signatureInstructions_submit() -> None:
    """Test submit endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payroc_cloud.signature_instructions.submit(
        "1850010868", idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9324", processing_terminal_id="1234001"
    )
    verify_request_count("POST", "/devices/1850010868/signature-instructions", None, 1)


def test_payrocCloud_signatureInstructions_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payroc_cloud.signature_instructions.retrieve("a37439165d134678a9100ebba3b29597")
    verify_request_count("GET", "/signature-instructions/a37439165d134678a9100ebba3b29597", None, 1)


def test_payrocCloud_signatureInstructions_delete() -> None:
    """Test delete endpoint with WireMock"""
    client = Payroc(environment=PayrocEnvironment(api="http://localhost:8080", identity="http://localhost:8080"))
    result = client.payroc_cloud.signature_instructions.delete("a37439165d134678a9100ebba3b29597")
    verify_request_count("DELETE", "/signature-instructions/a37439165d134678a9100ebba3b29597", None, 1)
