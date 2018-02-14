valid_queries = ('N', 'A', 'X', 'M', 'Q')
valid_order_types = ('M', 'L', 'I')


class EquityOrder:
    def __init__(self, order_id, time_stamp, symbol,
                 order_type, transaction_side, price, quantity):
        self.order_id = order_id
        self.time_stamp = time_stamp
        self.symbol = symbol
        self.order_type = order_type
        self.transaction_side = transaction_side
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str(self.__dict__)

    def validate(self):
        pass
