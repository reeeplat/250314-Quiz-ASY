import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])

# 배열 x를 reshape를 사용하여 (3,3) 배열로 변환해봅시다.
array1 = x.reshape(3,3)
print("(3x3) 배열 x:\n", array1)

# 변환된 배열 array1의 2번째 column을 구해봅니다. 
# (3, 1) 형태로 array2에 저장합니다.
array2 = array1[:, 1].reshape(3, 1)
print("\narray1의 2번째 column :\n", array2)

# array1에 column 방향으로 array2를 붙여봅니다.
array3 = np.c_[array1,array2]
print("\narray1에 column 방향으로 array2 붙이기:\n", array3)

# array3을 reshape를 사용하여 (3,2,2) 배열로 변환해봅시다.
array4 = np.reshape(array3,(3,2,2))
print("\n(3,2,2) array4:\n", array4)

# array4의 3개의 (2,2)행렬 중 첫 번째 행렬을 구합니다.
array5 = array4[0]
print("\narray4의 3개의 (2,2)행렬 중 첫 번째 행렬:\n", array5)

