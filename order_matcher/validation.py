def validate_order(equity_order):
    try:
        # validate quantity
        int(equity_order.quantity)

        # validate price
        float(equity_order.price)
        return True
    except ValueError:
        return False


def validate_new_order(equity_order, order_book):
    """
    Validate orders of type New
    """
    order_status = str(equity_order.order_id) + \
        ' - Reject - 303 - Invalid order details'

    if equity_order.order_id in order_book:
        print('duplicate order id in order book')
    else:
        order_book[equity_order.order_id] = equity_order
        order_status = str(equity_order.order_id) + ' - Accept'

    return order_status


def validate_amend_order(equity_order, order_book):
    """
    Validate an amend order
    """
    order_status = ''

    if equity_order.order_id in order_book:
        # if an order exists, check the record for only price and/or quantity modifications

        previous_order = order_book[equity_order.order_id]
        if (previous_order.symbol != equity_order.symbol) or (previous_order.order_type != equity_order.order_type) or (previous_order.transaction_side != equity_order.transaction_side):
            order_status = previous_order.order_id + \
                ' - AmendReject - 101 - Invalid amendment details'
        else:
            order_status = str(equity_order.order_id) + ' - AmendAccept'
    else:
        order_status = equity_order.order_id + \
            ' - AmendReject - 404 - Order does not exist'

    return order_status
