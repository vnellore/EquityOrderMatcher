def validate_order(equity_order):
    try:
        # validate quantity
        int(equity_order.quantity)
        
        # validate price
        float(equity_order.price)
        
        print(f'{equity_order.order_id} - Accept')

    except ValueError:
        print(f'{equity_order.order_id} - Reject - 303 - Invalid order details')
