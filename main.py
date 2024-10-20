n = int(input('введите кол-во строк'))
m = int(input('введите кол-во столбцов'))
value = input('введите значение')
def get_matrix(n,m,Value):
    matrix=[]
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(Value)
    print(matrix)
    return matrix
matrix = get_matrix(n, m, value)
