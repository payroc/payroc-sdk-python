"""
Security tests to verify that API keys and sensitive credentials are not exposed.

These tests ensure compliance with the requirement:
"Ensure API keys are not logged, stored, or appear in errors."
"""

import pytest
from payroc.core.api_error import ApiError


class TestApiErrorCredentialRedaction:
    """Test that ApiError properly redacts sensitive credentials."""

    def test_authorization_bearer_token_is_redacted(self):
        """Verify that Authorization Bearer tokens are redacted in error messages."""
        headers = {
            "Authorization": "Bearer secret_token_12345",
            "Content-Type": "application/json"
        }
        error = ApiError(status_code=401, headers=headers, body="Unauthorized")
        error_str = str(error)
        
        # Token should NOT appear in the error string
        assert "secret_token_12345" not in error_str
        assert "Bearer secret_token_12345" not in error_str
        
        # Should be replaced with [REDACTED]
        assert "[REDACTED]" in error_str
        
        # Non-sensitive headers should still appear
        assert "Content-Type" in error_str
        assert "application/json" in error_str

    def test_x_api_key_header_is_redacted(self):
        """Verify that x-api-key headers are redacted in error messages."""
        headers = {
            "x-api-key": "my_secret_api_key_abc123",
            "Accept": "application/json"
        }
        error = ApiError(status_code=403, headers=headers, body="Forbidden")
        error_str = str(error)
        
        # API key should NOT appear in the error string
        assert "my_secret_api_key_abc123" not in error_str
        
        # Should be replaced with [REDACTED]
        assert "[REDACTED]" in error_str
        
        # Non-sensitive headers should still appear
        assert "Accept" in error_str

    def test_multiple_sensitive_headers_are_redacted(self):
        """Verify that multiple sensitive headers are all redacted."""
        headers = {
            "Authorization": "Bearer token_123",
            "x-api-key": "api_key_456",
            "token": "token_789",
            "Content-Type": "application/json"
        }
        error = ApiError(status_code=401, headers=headers, body="Unauthorized")
        error_str = str(error)
        
        # None of the sensitive values should appear
        assert "token_123" not in error_str
        assert "api_key_456" not in error_str
        assert "token_789" not in error_str
        
        # Should have multiple [REDACTED] entries
        assert error_str.count("[REDACTED]") == 3
        
        # Non-sensitive header should still appear
        assert "Content-Type" in error_str

    def test_case_insensitive_header_redaction(self):
        """Verify that header redaction is case-insensitive."""
        headers = {
            "AUTHORIZATION": "Bearer token_upper",
            "X-API-KEY": "key_mixed_case",
            "authorization": "Bearer token_lower"
        }
        error = ApiError(status_code=401, headers=headers, body="Unauthorized")
        error_str = str(error)
        
        # None of the sensitive values should appear
        assert "token_upper" not in error_str
        assert "key_mixed_case" not in error_str
        assert "token_lower" not in error_str

    def test_api_key_variants_are_redacted(self):
        """Verify that different API key header variants are redacted."""
        test_cases = [
            ("api-key", "value1"),
            ("apikey", "value2"),
            ("API-Key", "value3"),
            ("client-secret", "value4"),
            ("auth-token", "value5"),
            ("access-token", "value6"),
        ]
        
        for header_name, value in test_cases:
            headers = {header_name: value}
            error = ApiError(status_code=401, headers=headers, body="Error")
            error_str = str(error)
            
            # The sensitive value should NOT appear
            assert value not in error_str, f"Header {header_name} was not redacted"
            assert "[REDACTED]" in error_str

    def test_empty_headers(self):
        """Verify that empty headers don't cause errors."""
        error = ApiError(status_code=500, headers={}, body="Internal error")
        error_str = str(error)
        
        # Should not crash and should contain basic error info
        assert "500" in error_str
        assert "Internal error" in error_str

    def test_none_headers(self):
        """Verify that None headers don't cause errors."""
        error = ApiError(status_code=500, headers=None, body="Internal error")
        error_str = str(error)
        
        # Should not crash and should contain basic error info
        assert "500" in error_str
        assert "None" in error_str or "headers: None" in error_str

    def test_original_headers_not_modified(self):
        """Verify that the original headers dict is not modified by redaction."""
        original_headers = {
            "Authorization": "Bearer secret_token",
            "x-api-key": "secret_key"
        }
        headers_copy = original_headers.copy()
        
        error = ApiError(status_code=401, headers=original_headers, body="Error")
        _ = str(error)  # Trigger __str__ which does redaction
        
        # Original headers should be unchanged
        assert error.headers == headers_copy
        assert error.headers["Authorization"] == "Bearer secret_token"
        assert error.headers["x-api-key"] == "secret_key"

    def test_non_sensitive_headers_preserved(self):
        """Verify that non-sensitive headers are preserved in error messages."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Payroc-SDK/1.0",
            "X-Request-ID": "req-12345",
            "Authorization": "Bearer secret_token"
        }
        error = ApiError(status_code=401, headers=headers, body="Error")
        error_str = str(error)
        
        # Non-sensitive headers should appear
        assert "Content-Type" in error_str
        assert "application/json" in error_str
        assert "User-Agent" in error_str
        assert "Payroc-SDK/1.0" in error_str
        assert "X-Request-ID" in error_str
        assert "req-12345" in error_str
        
        # Sensitive value should NOT appear
        assert "secret_token" not in error_str

    def test_error_body_preserved(self):
        """Verify that error body is not affected by header redaction."""
        headers = {"Authorization": "Bearer secret_token"}
        body_content = {"error": "Invalid credentials", "code": "AUTH_FAILED"}
        
        error = ApiError(status_code=401, headers=headers, body=body_content)
        error_str = str(error)
        
        # Body should be present
        assert "Invalid credentials" in error_str or str(body_content) in error_str
        
        # Token should still be redacted
        assert "secret_token" not in error_str


class TestSentryIntegration:
    """Test that Sentry integration filters sensitive data."""

    def test_sentry_module_exists(self):
        """Verify that the Sentry integration module exists and is importable."""
        try:
            from payroc import sentry_integration
            assert hasattr(sentry_integration, 'initialize_sentry')
            assert hasattr(sentry_integration, '_before_send')
        except ImportError:
            pytest.fail("Sentry integration module should be importable")

    def test_before_send_redacts_authorization_header(self):
        """Verify that _before_send redacts Authorization headers."""
        from payroc.sentry_integration import _before_send
        
        event = {
            'request': {
                'headers': {
                    'Authorization': 'Bearer secret_token_12345',
                    'Content-Type': 'application/json'
                }
            }
        }
        
        filtered_event = _before_send(event, {})
        
        # Authorization should be redacted
        assert filtered_event['request']['headers']['Authorization'] == '[REDACTED]'
        
        # Non-sensitive headers should remain
        assert filtered_event['request']['headers']['Content-Type'] == 'application/json'

    def test_before_send_redacts_api_key_header(self):
        """Verify that _before_send redacts API key headers."""
        from payroc.sentry_integration import _before_send
        
        event = {
            'request': {
                'headers': {
                    'X-API-Key': 'my_secret_api_key',
                    'Accept': 'application/json'
                }
            }
        }
        
        filtered_event = _before_send(event, {})
        
        # API key should be redacted
        assert filtered_event['request']['headers']['X-API-Key'] == '[REDACTED]'
        
        # Non-sensitive headers should remain
        assert filtered_event['request']['headers']['Accept'] == 'application/json'

    def test_before_send_redacts_exception_values(self):
        """Verify that _before_send redacts credentials in exception messages."""
        from payroc.sentry_integration import _before_send
        
        event = {
            'exception': {
                'values': [
                    {
                        'value': "Error: headers: {'Authorization': 'Bearer secret_token_123'}"
                    }
                ]
            }
        }
        
        filtered_event = _before_send(event, {})
        
        # Token should be redacted in exception message
        exception_value = filtered_event['exception']['values'][0]['value']
        assert 'secret_token_123' not in exception_value
        assert '[REDACTED]' in exception_value

    def test_before_send_handles_missing_request(self):
        """Verify that _before_send doesn't crash when request is missing."""
        from payroc.sentry_integration import _before_send
        
        event = {
            'message': 'Some error occurred'
        }
        
        # Should not crash
        filtered_event = _before_send(event, {})
        assert filtered_event is not None

    def test_before_send_handles_missing_exception(self):
        """Verify that _before_send doesn't crash when exception is missing."""
        from payroc.sentry_integration import _before_send
        
        event = {
            'request': {
                'headers': {
                    'Authorization': 'Bearer token'
                }
            }
        }
        
        # Should not crash
        filtered_event = _before_send(event, {})
        assert filtered_event is not None
        assert filtered_event['request']['headers']['Authorization'] == '[REDACTED]'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

