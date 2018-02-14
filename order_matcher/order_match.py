from order_matcher import models
from order_matcher import validation

order_book = {}

# Complete the function below.


def buildEquityOrder(query):

    # TODO : Add more validation for query
    order_id = query[1].strip()
    time_stamp = query[2].strip()
    symbol = query[3].strip()
    order_type = query[4].strip()
    transaction_side = query[5].strip()
    price = query[6].strip()
    quantity = query[7].strip()

    equity_order = models.EquityOrder(order_id, time_stamp,
                                      symbol, order_type,
                                      transaction_side, price, quantity)
    return equity_order


def processQueries(queries):
    # Write your code here.

    # TODO: Add more validation for queries on boundary conditions
    for i in queries:
        query = i.split(',')

        # TODO - validate query after split
        input_cmd = query[0].strip()
        if input_cmd in models.valid_queries:
            print(f'{input_cmd} is a valid command')

            equity_order = buildEquityOrder(query)
            print(equity_order)
            if input_cmd == 'N':  # New command

                print(validation.validate_new_order(
                    equity_order, order_book))

            elif input_cmd == 'A':

                print(validation.validate_amend_order(
                    equity_order, order_book))

        else:
            print(f'{input_cmd} is not a valid command')

    return list(queries)
