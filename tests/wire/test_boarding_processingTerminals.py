from .conftest import get_client, verify_request_count


def test_boarding_processingTerminals_retrieve() -> None:
    """Test retrieve endpoint with WireMock"""
    test_id = "boarding.processing_terminals.retrieve.0"
    client = get_client(test_id)
    client.boarding.processing_terminals.retrieve(processing_terminal_id="1234001")
    verify_request_count(test_id, "GET", "/processing-terminals/1234001", None, 1)


def test_boarding_processingTerminals_retrieve_host_configuration() -> None:
    """Test retrieveHostConfiguration endpoint with WireMock"""
    test_id = "boarding.processing_terminals.retrieve_host_configuration.0"
    client = get_client(test_id)
    client.boarding.processing_terminals.retrieve_host_configuration(processing_terminal_id="1234001")
    verify_request_count(test_id, "GET", "/processing-terminals/1234001/host-configurations", None, 1)
