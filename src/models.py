
class EquityOrder:
    def __init__(self, order_id, time_stamp, symbol, 
        order_type, transaction_side,price, quantity):
        self.order_id = order_id
        self.time_stamp = time_stamp
        self.symbol = symbol
        self.order_type = order_type
        self.transaction_side = transaction_side
        self.price = price
        self.quantity = quantity

    def __str__(self):
        
        formatted_equity_order = '-- Equity Order for {symbol} --'.format(symbol = self.symbol)
        formatted_equity_order += '\n- order_id - {order_id}'.format(order_id = self.order_id) 
        formatted_equity_order += '\n- time_stamp - {time_stamp}'.format(time_stamp = self.time_stamp) 
        formatted_equity_order += '\n- symbol - {symbol}'.format(symbol = self.symbol) 
        formatted_equity_order += '\n- order_type - {order_type}'.format(order_type = self.order_type) 
        formatted_equity_order += '\n- transaction_side - {transaction_side}'.format(transaction_side = self.transaction_side)
        formatted_equity_order += '\n- price - {price}'.format(price = self.price)
        formatted_equity_order += '\n- quantity - {quantity}'.format(quantity = self.quantity)

        return formatted_equity_order
        
    def validate(self):
        pass