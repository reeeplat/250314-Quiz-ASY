import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

column1 = array1[:,1]
column2 = array1[:,2]

# array1 첫 번째 column 벡터와 두 번째 column 벡터를 더하여 봅시다.
array2 = array1[:,1] +array1[:,2]
print("1st column of array1 + 2nd column of array1:\n", array2)

# array1 첫 번째 row 벡터와 두 번째 row 벡터를 빼봅시다.
array3 = array1[0] - array1[1]
print("\n1st row of array1 - 2nd row of array1:\n", array3)

# array2과 array3을 곱하여 봅시다.
array4 = array2*array3
print("\narray2 * array3:\n", array4)

# array2, array3, array4값을 column으로 이어 붙인 배열
array5 = np.c_[array2, array3, array4]

# array1을 array5로 나누어 봅시다.
array6 = array1/array5
print("\narray1 / array5:\n", array6)
