import numpy as np

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

array1 = np.array(list_1)
array2 = np.array(list_2)
result_array = np.concatenate((array1, array2))

print("Array 1:", array1)
print("Array 2:", array2)
print("Concatenated Array:", result_array)
