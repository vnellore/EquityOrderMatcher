import os
import sys
from order_matcher import order_match


def read_query_file(inputFile):
    queryFile = open(inputFile)
    queryList = []
    with queryFile:
        for line in queryFile:
            queryList.append(line)

    return queryList


def write_output(outputFile, response):
    #f = open(os.environ['OUTPUT_PATH'], 'w')
    f = open(outputFile, 'w')
    f.seek(0)
    f.truncate()
    f.write("\n".join(response))

    f.write('\n')

    f.close()


if __name__ == '__main__':

    #print('Enter query size : ')
    #queries_size = int(input())

    #queries = []
    # for _ in range(queries_size):
    #    print('Enter query - ')
    #    queries_item = input()
    #    queries.append(queries_item)

    queries = read_query_file('.\\data\\queries.txt')

    response = order_match.process_queries(queries)

    write_output('.\\data\\gs_output.txt', response)
