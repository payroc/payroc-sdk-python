from datetime import date

from .conftest import get_client, verify_request_count


def test_reporting_settlement_list_batches() -> None:
    """Test listBatches endpoint with WireMock"""
    test_id = "reporting.settlement.list_batches.0"
    client = get_client(test_id)
    client.reporting.settlement.list_batches(
        before="2571", after="8516", limit=1, date=date.fromisoformat("2027-07-02"), merchant_id="4525644354"
    )
    verify_request_count(
        test_id,
        "GET",
        "/batches",
        {"before": "2571", "after": "8516", "limit": "1", "date": "2027-07-02", "merchantId": "4525644354"},
        1,
    )


def test_reporting_settlement_retrieve_batch() -> None:
    """Test retrieveBatch endpoint with WireMock"""
    test_id = "reporting.settlement.retrieve_batch.0"
    client = get_client(test_id)
    client.reporting.settlement.retrieve_batch(batch_id=1)
    verify_request_count(test_id, "GET", "/batches/1", None, 1)


def test_reporting_settlement_list_transactions() -> None:
    """Test listTransactions endpoint with WireMock"""
    test_id = "reporting.settlement.list_transactions.0"
    client = get_client(test_id)
    client.reporting.settlement.list_transactions(
        before="2571",
        after="8516",
        limit=1,
        date=date.fromisoformat("2024-07-02"),
        batch_id=1,
        merchant_id="4525644354",
        transaction_type="Capture",
    )
    verify_request_count(
        test_id,
        "GET",
        "/transactions",
        {
            "before": "2571",
            "after": "8516",
            "limit": "1",
            "date": "2024-07-02",
            "batchId": "1",
            "merchantId": "4525644354",
            "transactionType": "Capture",
        },
        1,
    )


def test_reporting_settlement_retrieve_transaction() -> None:
    """Test retrieveTransaction endpoint with WireMock"""
    test_id = "reporting.settlement.retrieve_transaction.0"
    client = get_client(test_id)
    client.reporting.settlement.retrieve_transaction(transaction_id=1)
    verify_request_count(test_id, "GET", "/transactions/1", None, 1)


def test_reporting_settlement_list_authorizations() -> None:
    """Test listAuthorizations endpoint with WireMock"""
    test_id = "reporting.settlement.list_authorizations.0"
    client = get_client(test_id)
    client.reporting.settlement.list_authorizations(
        before="2571",
        after="8516",
        limit=1,
        date=date.fromisoformat("2024-07-02"),
        batch_id=1,
        merchant_id="4525644354",
    )
    verify_request_count(
        test_id,
        "GET",
        "/authorizations",
        {
            "before": "2571",
            "after": "8516",
            "limit": "1",
            "date": "2024-07-02",
            "batchId": "1",
            "merchantId": "4525644354",
        },
        1,
    )


def test_reporting_settlement_retrieve_authorization() -> None:
    """Test retrieveAuthorization endpoint with WireMock"""
    test_id = "reporting.settlement.retrieve_authorization.0"
    client = get_client(test_id)
    client.reporting.settlement.retrieve_authorization(authorization_id=1)
    verify_request_count(test_id, "GET", "/authorizations/1", None, 1)


def test_reporting_settlement_list_disputes() -> None:
    """Test listDisputes endpoint with WireMock"""
    test_id = "reporting.settlement.list_disputes.0"
    client = get_client(test_id)
    client.reporting.settlement.list_disputes(
        before="2571", after="8516", limit=1, date=date.fromisoformat("2024-07-02"), merchant_id="4525644354"
    )
    verify_request_count(
        test_id,
        "GET",
        "/disputes",
        {"before": "2571", "after": "8516", "limit": "1", "date": "2024-07-02", "merchantId": "4525644354"},
        1,
    )


def test_reporting_settlement_list_disputes_statuses() -> None:
    """Test listDisputesStatuses endpoint with WireMock"""
    test_id = "reporting.settlement.list_disputes_statuses.0"
    client = get_client(test_id)
    client.reporting.settlement.list_disputes_statuses(dispute_id=1)
    verify_request_count(test_id, "GET", "/disputes/1/statuses", None, 1)


def test_reporting_settlement_list_ach_deposits() -> None:
    """Test listAchDeposits endpoint with WireMock"""
    test_id = "reporting.settlement.list_ach_deposits.0"
    client = get_client(test_id)
    client.reporting.settlement.list_ach_deposits(
        before="2571", after="8516", limit=1, date=date.fromisoformat("2024-07-02"), merchant_id="4525644354"
    )
    verify_request_count(
        test_id,
        "GET",
        "/ach-deposits",
        {"before": "2571", "after": "8516", "limit": "1", "date": "2024-07-02", "merchantId": "4525644354"},
        1,
    )


def test_reporting_settlement_retrieve_ach_deposit() -> None:
    """Test retrieveAchDeposit endpoint with WireMock"""
    test_id = "reporting.settlement.retrieve_ach_deposit.0"
    client = get_client(test_id)
    client.reporting.settlement.retrieve_ach_deposit(ach_deposit_id=1)
    verify_request_count(test_id, "GET", "/ach-deposits/1", None, 1)


def test_reporting_settlement_list_ach_deposit_fees() -> None:
    """Test listAchDepositFees endpoint with WireMock"""
    test_id = "reporting.settlement.list_ach_deposit_fees.0"
    client = get_client(test_id)
    client.reporting.settlement.list_ach_deposit_fees(
        before="2571",
        after="8516",
        limit=1,
        date=date.fromisoformat("2024-07-02"),
        ach_deposit_id=1,
        merchant_id="4525644354",
    )
    verify_request_count(
        test_id,
        "GET",
        "/ach-deposit-fees",
        {
            "before": "2571",
            "after": "8516",
            "limit": "1",
            "date": "2024-07-02",
            "achDepositId": "1",
            "merchantId": "4525644354",
        },
        1,
    )
