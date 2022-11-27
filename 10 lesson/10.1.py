def find_min_and_max(matrix):
  min_sum = float('inf')
  min_sum_row = []
  max_sum = float('-inf')
  max_sum_row = []
  for i in matrix:
    if sum(i) < min_sum:
      min_sum = sum(i)
      min_sum_row = i
    if sum(i) > max_sum:
      max_sum = sum(i)
      max_sum_row = i
  print('Min sum = ' + str(min_sum))
  print('Min sum row = ' + str(min_sum_row))
  print('Max sum = ' + str(max_sum))
  print('Max sum row = ' + str(max_sum_row))
  return (min_sum, min_sum_row, max_sum, max_sum_row)

import json

def input_matrix():
  filename = 'vvod.json'
  with open(filename, 'r') as file:
    matrix = json.load(file)
  return matrix


def write_min_max(answer):
  filename = 'vivod.json'
  with open(filename, 'w') as file:
    for i in answer:
      file.write(str(i) + '\n')


m = input_matrix()
print(m)
answer = find_min_and_max(m)
write_min_max(answer)
