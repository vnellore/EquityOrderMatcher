from order_matcher import models
from order_matcher import validation

order_book = []

# Complete the function below.


def processQueries(queries):
    # Write your code here.

    for i in queries:
        query = i.split(',')
        input_cmd = query[0].strip()
        if input_cmd in models.valid_queries:
            print(f'{input_cmd} is a valid command')

            if input_cmd == 'N':  # New command

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
                print(f'{equity_order}')

                validation.validate_order(equity_order)

            elif input_cmd == 'A':
                pass

        else:
            print(f'{input_cmd} is not a valid command')

    return list(queries)
