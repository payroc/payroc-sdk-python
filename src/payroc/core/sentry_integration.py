"""Sentry integration for Payroc SDK with opt-out mechanism."""

import os
import re
from typing import TYPE_CHECKING, Any, Dict, Optional, cast

if TYPE_CHECKING:
    from sentry_sdk.types import Event

_sentry_initialized = False


def _before_send(event: "Event", hint: Dict[str, Any]) -> Optional["Event"]:
    """
    Filter sensitive data before sending events to Sentry.
    
    This function redacts:
    - Authorization headers (Bearer tokens)
    - API keys
    - Other sensitive credentials
    
    Args:
        event: The Sentry event dictionary
        hint: Additional context about the event
    
    Returns:
        The filtered event dictionary, or None to drop the event
    """
    # Event is a TypedDict but we can treat it as a dict at runtime
    event_dict = cast(Dict[str, Any], event)
    
    # Redact sensitive headers from request data
    if 'request' in event_dict and 'headers' in event_dict['request']:
        headers = event_dict['request']['headers']
        sensitive_keys = [
            'Authorization', 'authorization',
            'X-API-Key', 'x-api-key',
            'API-Key', 'api-key',
            'Token', 'token',
            'Auth-Token', 'auth-token',
            'Access-Token', 'access-token',
            'Client-Secret', 'client-secret',
            'Secret', 'secret',
        ]
        for key in sensitive_keys:
            if key in headers:
                headers[key] = '[REDACTED]'
    
    # Redact sensitive data from exception messages and values
    if 'exception' in event_dict:
        for exception in event_dict['exception'].get('values', []):
            if 'value' in exception:
                # Redact Bearer tokens
                exception['value'] = re.sub(
                    r'(Authorization[\'"]?\s*:\s*[\'"]?Bearer\s+)[^\s\'"]+',
                    r'\1[REDACTED]',
                    exception['value'],
                    flags=re.IGNORECASE
                )
                # Redact API keys
                exception['value'] = re.sub(
                    r'(x-api-key[\'"]?\s*:\s*[\'"]?)[^\s\'"]+',
                    r'\1[REDACTED]',
                    exception['value'],
                    flags=re.IGNORECASE
                )
                exception['value'] = re.sub(
                    r'(api[_-]?key[\'"]?\s*[:=]\s*[\'"]?)[^\s\'"]+',
                    r'\1[REDACTED]',
                    exception['value'],
                    flags=re.IGNORECASE
                )
    
    # Redact sensitive data from extra context
    if 'extra' in event_dict:
        for key in list(event_dict['extra'].keys()):
            if any(sensitive in key.lower() for sensitive in ['token', 'key', 'secret', 'auth', 'password']):
                event_dict['extra'][key] = '[REDACTED]'
    
    return event


def initialize_sentry() -> None:
    """
    Initialize Sentry for error tracking and monitoring.
    
    Users can opt-out by setting the PAYROC_DISABLE_SENTRY environment variable to 'true', '1', or 'yes'.
    
    Security Features:
    - Sensitive headers are automatically redacted
    - API keys and tokens are filtered from error messages
    - PII is not sent by default
    """
    global _sentry_initialized
    
    # Check if already initialized to avoid double initialization
    if _sentry_initialized:
        return
    
    # Check for opt-out via environment variable
    disable_sentry = os.environ.get("PAYROC_DISABLE_SENTRY", "").lower() in ("true", "1", "yes")
    
    if disable_sentry:
        return
    
    try:
        import sentry_sdk
        
        # Hard-coded Sentry configuration (as per requirements)
        sentry_sdk.init(
            dsn="https://c3d832677ad08b915dcc3fdafc8afe26@o4505201678483456.ingest.us.sentry.io/4509367402954752",
            # DO NOT send PII to protect user privacy and credentials
            send_default_pii=False,
            # Set traces_sample_rate to 1.0 to capture 100% of transactions for tracing
            traces_sample_rate=1.0,
            # Set profile_session_sample_rate to 1.0 to collect all profile sessions
            profile_session_sample_rate=1.0,
            # Profiles will be automatically collected while there is an active span
            profile_lifecycle="trace",
            # Enable logs to be sent to Sentry
            enable_logs=True,
            # Set release version for better tracking
            release=_get_sdk_version(),
            # Configure environment
            environment=os.environ.get("PAYROC_ENVIRONMENT", "production"),
            # Filter sensitive data before sending to Sentry
            before_send=_before_send,
        )
        
        _sentry_initialized = True
    except ImportError:
        # Silently fail if sentry_sdk is not installed
        # This allows the SDK to work even if sentry-sdk is not available
        pass
    except Exception:
        # Silently catch any other initialization errors
        # We don't want Sentry initialization to break the SDK
        pass


def _get_sdk_version() -> Optional[str]:
    """Get the SDK version for Sentry release tracking."""
    try:
        from ..version import __version__
        return f"payroc-python-sdk@{__version__}"
    except Exception:
        return None

