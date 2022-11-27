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


def input_matrix():
  m = int(input('M: '))
  n = int(input('N: '))
  matrix = []
  for i in range(m):
    matrix.append([])
    for _ in range(n):
      matrix[i].append(int(input()))
  return matrix


m = input_matrix()
print(m)
find_min_and_max(m)
