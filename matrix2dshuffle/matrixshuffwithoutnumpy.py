import random
a = [[11, 12, 13, 12], [14, 15, 16, 12], [17, 18, 19, 12], [22, 22, 22, 12]]
matrix_1d = []
counter_column = 0
counter_row = 0
for i in a:
    if type(i) is list:
        counter_column += 1
        for x in i:
            counter_row += 1
            matrix_1d.append(x)
    else:
        counter_row += 1
        matrix_1d.append(i)
print(matrix_1d)
print(counter_column)
random.shuffle(matrix_1d)
counter = 0
temp_list = []
output_matrix = []
for value in matrix_1d:
    counter += 1
    temp_list.append(value)
    if counter == counter_column:
        print(counter)
        output_matrix.append(temp_list)
        temp_list = []
        counter = 0
        
print(matrix_1d)
print(output_matrix)
