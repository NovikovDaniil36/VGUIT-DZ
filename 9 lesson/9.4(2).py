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


def input_matrix():
  n = int(input('N: '))
  matrix = []
  for i in range(n):
    matrix.append([])
    for _ in range(n):
      matrix[i].append(int(input()))
  return matrix


m = input_matrix()
replace(m)
