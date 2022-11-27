from copy import deepcopy

def replace(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] > 0:
        matrix[i][j] = 1
      elif matrix[i][j] < 0:
        matrix[i][j] = 0
  for i in range(len(matrix)):
    for j in range(0, i):
      print(matrix[i][j], end=' ')
    print()
  triangal_matrix = deepcopy(matrix)
  for i in range(len(triangal_matrix)):
    for j in range(i, len(triangal_matrix)):
      triangal_matrix[i][j] = ' '
  return triangal_matrix
  

def input_matrix():
  n = int(input('N: '))
  matrix = []
  for i in range(n):
    matrix.append([])
    for _ in range(n):
      matrix[i].append(int(input()))
  return matrix

import json

def input_matrix():
  filename = 'vvod.json'
  with open(filename, 'r') as file:
    matrix = json.load(file)
  return matrix

def write_matrix(matrix):
  filename = 'vivod.json'
  with open(filename, 'w') as file:
    json.dump(matrix, file)


m = input_matrix()
write_matrix(replace(m))
