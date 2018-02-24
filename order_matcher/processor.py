import copy

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

def perform_match(match_query, order_book):
    # check if symbol is passed in match query
    if match_query.symbol is None or match_query.symbol == '':
        symbol_match = False
    else:
        symbol_match = True

    int_time_stamp = int(match_query.time_stamp)
       
    if symbol_match:
        filtered_orders = { order_id : order for order_id, order in order_book.items()\
         if order.symbol == match_query.symbol }
    else:
        filtered_orders = { order_id : order for order_id, order in order_book.items()\
         if int(order.time_stamp) <= int_time_stamp }
    
    updated_order_book = find_match(filtered_orders)    
        

def find_match(order_book):
    
    working_order_book = copy.deepcopy(order_book)
    wo_keys = list(working_order_book.keys())

    for j in wo_keys:
        if j in working_order_book:
            order_to_match = working_order_book[j]    
            for i in wo_keys:
                if i != j and i in working_order_book:
                    matched_order = working_order_book[i]
                    if order_to_match.symbol == matched_order.symbol and order_to_match.transaction_side != matched_order.transaction_side:
                        
                        # check for quantity
                        if order_to_match.quantity == matched_order.quantity:
                            print_matched_order(order_to_match, matched_order, matched_order.quantity)

                            del working_order_book[order_to_match.order_id]
                            del working_order_book[i]
                            
                        elif order_to_match.quantity > matched_order.quantity:
                            match_quantity = matched_order.quantity
                            print_matched_order(order_to_match, matched_order, match_quantity)
                            working_order_book[order_to_match.order_id].quantity -= matched_order.quantity
                            del working_order_book[i]
                        else:
                            match_quantity = order_to_match.quantity
                            print_matched_order(order_to_match, matched_order, match_quantity)
                            working_order_book[i].quantity -= order_to_match.quantity
                            del working_order_book[order_to_match.order_id]

    return working_order_book

def print_matched_order(order_to_match, matched_order, match_quantity):
    # ALN|1,L,100,60.90|60.90,100,L,10
    print(f'{order_to_match.symbol}|{order_to_match.order_id}, {order_to_match.order_type},{match_quantity},{order_to_match.price}|{matched_order.price},{match_quantity},{matched_order.order_type},{matched_order.order_id}')

                            
def show_order_book(order_book):
    print(order_book)