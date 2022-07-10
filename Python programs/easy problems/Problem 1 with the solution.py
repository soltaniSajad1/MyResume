
my_list = [1, 2, 3, 4, 5]
result_list_square = []
result_list_cube = []

for i in range(5):
    result_square = my_list[i]**2
    result_list_square.append(result_square)


for i in range(5):
    result_cube = result_list_square[i] * my_list[i]
    result_list_cube.append(result_cube)


print("Your numbers were ", my_list)
print("Your square answers are : ", result_list_square)
print("Your cube answers are : ", result_list_cube)