import numpy as np

x=[[1,2,3], [4,5,6], [7,8,9]]

def solution(data):
    #리스트 x를 Numpy 배열로 출력합니다.
    array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

    #모든 원소가 0인 3×3의 배열을 출력합니다.
    array2 = np.zeros((3,3))

    #모든 원소가 1인 2×5의 배열을 출력합니다.
    array3 = np.ones((2,5))

    # 0 이상 1 미만의 랜덤 값을 갖는 5×3의 배열을 출력합니다.
    array4 = np.random.random((5,3))  

    # 0부터 9까지의 값을 원소로 하는 1×10 배열을 출력합니다.
    array5 = np.arange(1,10)
    
    return array1, array2, array3, array4, array5

def print_answer(**kwargs):
    for key in kwargs.keys():
        print(key,"\n", kwargs[key], "\n")

array1, array2, array3, array4, array5 = solution(x)

print_answer(array1=array1, array2=array2, array3=array3, array4=array4, array5=array5)
