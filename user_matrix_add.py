rows = int(input('ENter number of rows: '))
cols  = int(input('ENter number of column: '))
print()
print('Enter values for matrix A')
matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(cols)] for i in range(rows) ]  
print()
print('Enter values for matrix B ')
matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(cols)] for i in range(rows)]  
print() 
print('Matrix-A :')
for i in matrix_A:
    print(i)
print() 
print('Matrix-B :')
for i in matrix_B:
    print(i)
result = [[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]
print()
print('Addition of Matrix-A and Matrix-B is :')
for i in result:
    print(i)
