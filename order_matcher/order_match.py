import os
import sys
from order_matcher.models import EquityOrder, valid_order_types, valid_queries
from order_matcher.validation import validate_order

order_book = []

# Complete the function below.

def processQueries(queries):
    # Write your code here.

    for i in queries:
        query = i.split(',')
        input_cmd = query[0].strip()
        if input_cmd in valid_queries:
            print(f'{input_cmd} is a valid command')

            if input_cmd == 'N': # New command
                
                order_id = query[1].strip()
                time_stamp = query[2].strip()            
                symbol = query[3].strip()
                order_type = query[4].strip()
                transaction_side = query[5].strip()
                price = query[6].strip()
                quantity = query[7].strip()

                equity_order = EquityOrder(order_id, time_stamp, 
                                symbol, order_type, 
                                transaction_side, price, quantity)
                print(f'{equity_order}')

                validate_order(equity_order)

            elif input_cmd == 'A':
                pass

        else:
            print(f'{input_cmd} is not a valid command')    

    return list(queries)

def readQueryFile():
    queryFile = open('..\\data\\queries.txt')
    queryList = []
    with queryFile:
        for line in queryFile:
            queryList.append(line)
    
    return queryList

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')
    f = open('..\\data\\gs_output.txt','w')
    f.seek(0)
    f.truncate()

    #print('Enter query size : ')
    #queries_size = int(input())

    #queries = []
    #for _ in range(queries_size):
    #    print('Enter query - ')
    #    queries_item = input()
    #    queries.append(queries_item)
    
    queries = readQueryFile()

    response = processQueries(queries)

    f.write("\n".join(response))

    f.write('\n')

    f.close()