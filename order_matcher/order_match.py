from order_matcher import models
from order_matcher import processor

order_book = {}

# Complete the function below.




def process_queries(queries):
    # Write your code here.

    # TODO: Add more validation for queries on boundary conditions
    for i in queries:
        query = i.split(',')

        # TODO - validate query after split
        input_cmd = query[0].strip()
        if input_cmd in models.valid_queries:
            
            #print(equity_order)
            if input_cmd == 'N':  # New command
                equity_order = models.build_equity_order(query, input_cmd)
                print(processor.process_new_order(
                    equity_order, order_book))

            elif input_cmd == 'A':
                equity_order = models.build_equity_order(query, input_cmd)
                print(processor.process_amend_order(
                    equity_order, order_book))
            
            elif input_cmd == 'X':
                equity_order = models.build_equity_order(query, input_cmd)
                print(processor.process_cancel_order(
                    equity_order, order_book))
            
            elif input_cmd == 'M':
                match_query = models.build_match_query(query)
                processor.perform_match(match_query, order_book)
                            
            elif input_cmd == 'Q':
                equity_order = models.build_query_eq_order(query)
                print(processor.show_order_book(order_book))

        else:
            print(f'{input_cmd} is not a valid command')

    return list(queries)
