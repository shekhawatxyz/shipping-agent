class OrderNotFoundError(Exception):
    pass


def list_payments(
    order_id: str, payments: list[dict[str, str]], orders: list[dict[str, str]]
) -> list[dict[str, str]]:
    check = False
    for order in orders:
        if order_id == order["order_id"]:
            check = True
            break
    if not check:
        raise OrderNotFoundError("Invalid order_id")
    matching_payments = []
    for payment in payments:
        if payment["order_id"] == order_id:
            matching_payments.append(payment)
    return matching_payments
