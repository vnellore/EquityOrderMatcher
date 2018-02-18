def validate_order(equity_order):
    try:
        # validate quantity
        int(equity_order.quantity)

        # validate price
        float(equity_order.price)
        return True
    except ValueError:
        return False


def process_new_order(equity_order, order_book):
    """
    Validate orders of type New
    """
    order_status = str(equity_order.order_id) + \
        ' - Reject - 303 - Invalid order details'

    if validate_order(equity_order):

        if equity_order.order_id in order_book:
            print('duplicate order id in order book')
        else:
            order_book[equity_order.order_id] = equity_order
            order_status = str(equity_order.order_id) + ' - Accept'

    return order_status


def process_amend_order(equity_order, order_book):
    """
    Process an amend order
    """
    order_status = ''

    if equity_order.order_id in order_book:
        # if an order exists, check the record for only price and/or quantity modifications

        previous_order = order_book[equity_order.order_id]
        if (previous_order.symbol != equity_order.symbol) or \
            (previous_order.order_type != equity_order.order_type) or \
            (previous_order.transaction_side != equity_order.transaction_side):
            order_status = previous_order.order_id + \
                ' - AmendReject - 101 - Invalid amendment details'
        else:
            # Update the order in order book
            order_book[equity_order.order_id] = equity_order
            order_status = str(equity_order.order_id) + ' - AmendAccept'
    else:
        order_status = equity_order.order_id + \
            ' - AmendReject - 404 - Order does not exist'

    return order_status

def process_cancel_order(equity_order, order_book):
    """
    Validate a cancel order
    """
    order_status = ''

    if equity_order.order_id in order_book:
        order_status = str(equity_order.order_id) + ' - CancelAccept'
        # Remove the orders from order book
        del order_book[equity_order.order_id]
    else:
        order_status = equity_order.order_id + \
            ' - CancelReject - 404 - Order does not exist'

    return order_status

def perform_match(order_book):
    pass

def show_order_book(order_book):
    print(order_book)