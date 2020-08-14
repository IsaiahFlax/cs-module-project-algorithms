#!/usr/bin/python

import sys
import itertools
from itertools import product
def rock_paper_scissors(turns):
  arr = [['rock'], ['paper'], ['scissors']]
  if turns == 1:
    return arr
  elif turns == 0:
    return [[]]
  count = 0
  while count < turns-1:
    print('\nfirst count\n', count)
    print('\nturns\n', turns)
    arr2 = []
    count2 = 0
    if count == turns:
      return arr2
    for a in arr:
      print('\ncount2\n', count2)
      print(count)
      count2 += 1
      #print('a', a)
      temp_array1 = [(a +['rock'])]
      temp_array2 = [(a +['paper'])]
      temp_array3 = [(a +['scissors'])]
      arr2 += temp_array1
      arr2 += temp_array2
      arr2 += temp_array3
    print(count)
    print(arr2)
    count += 1
    arr = arr2
  print(count)
  return arr
  # while len(arr)<3**turns:
  #   for a in arr:
  #     arr2.append([a, 'rock'])
  #     arr2.append([a, 'paper'])
  #     arr2.append([a, 'scissors'])
  #   arr = arr2
  # return arr
print(rock_paper_scissors(2))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
    
