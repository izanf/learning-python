#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
  response = [0, 0]

  for i in range(len(a)):
    if a[i] > b[i]:
      response[0] = response[0] + 1
    if a[i] < b[i]:
      response[1] = response[1] + 1

    # print('ee', a[i], b[j], response)

  return response
            
result = compareTriplets([17, 28, 30], [99, 16, 8])

print("Result: ", result)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
