valid_queries = ('N', 'A', 'X', 'M', 'Q')
valid_order_types = ('M', 'L', 'I')


class MatchQuery:
    def __init__(self, time_stamp, symbol):
        self.time_stamp = time_stamp
        self.symbol = symbol

    def __str__(self):
        return str(self.__dict__)
    

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

def build_equity_order(query, input_cmd):

    # TODO : Add more validation for query
    order_id = query[1].strip()
    time_stamp = query[2].strip()

    if input_cmd != 'X':
        symbol = query[3].strip()
        order_type = query[4].strip()
        transaction_side = query[5].strip()
        price = query[6].strip()
        quantity = query[7].strip()
    else:
        symbol = ''
        order_type = ''
        transaction_side = ''
        price = ''
        quantity = ''

    equity_order = EquityOrder(order_id, time_stamp,
                                      symbol, order_type,
                                      transaction_side, price, quantity)
    return equity_order


def build_match_query(query):
    input_cmd = query[0].strip()
    if input_cmd != 'M':
        print('Invalid query')
        return None
    else:
        #TODO : Validate
        time_stamp = query[1]
        if len(query) == 3:
            symbol = query[2]
        else:
            symbol = ''
                
        match_query = MatchQuery(time_stamp, symbol)
        return match_query

def build_query_eq_order(query):
    input_cmd = query[0].strip()
    if input_cmd != 'Q':
        print('Invalid query')
        return None
    else:
        time_stamp = ''
        order_id = ''
        symbol = ''
        order_type = ''
        transaction_side = ''
        price = ''
        quantity = ''
        equity_order = EquityOrder(order_id, time_stamp,
                                      symbol, order_type,
                                      transaction_side, price, quantity)
        return equity_order                              
        