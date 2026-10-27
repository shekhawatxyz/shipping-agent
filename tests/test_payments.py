import pytest
from shipping_agent.payments import list_payments, OrderNotFoundError


def test_list_payments_returns_only_payments_for_requested_order():
    orders = [{"order_id": "ORD1"}, {"order_id": "ORD2"}]
    payments = [
        {"payment_id": "PAY1", "order_id": "ORD1", "payment_status": "pending"},
        {"payment_id": "PAY2", "order_id": "ORD1", "payment_status": "successful"},
        {"payment_id": "PAY3", "order_id": "ORD2", "payment_status": "successful"},
    ]
    result = list_payments("ORD1", payments, orders)
    assert payments[0] in result
    assert payments[1] in result
    assert len(result) == 2


def test_list_payments_returns_empty_for_no_payment():
    orders = [{"order_id": "ORD1"}]
    payments = []
    result = list_payments("ORD1", payments, orders)
    assert result == []


def test_list_payments_raises_for_missing_order():
    orders = [{"order_id": "ORD1"}]
    payments = []
    with pytest.raises(OrderNotFoundError):
        list_payments("ORD9", payments, orders)


def test_list_payments_fails_on_malformed_order():
    orders = [{}]
    payments = []
    with pytest.raises(KeyError):
        list_payments("ORD1", payments, orders)
