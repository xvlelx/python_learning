import numpy as np

'''
# 문제: numpy 배열 만들기
arr = np.arange(10)
print(arr)

arr2 = np.arange(1, 10, 1)
print(arr2)

# 문제: 2차원 배열 (reshape)
arr = np.arange(12)
print(arr)

arr2d = arr.reshape(3, 4)
print(arr2d)


# 문제: 배열 인덱싱
arr = np.array([[1,2,3],
                [4,5,6]])

print(arr[0])

print(arr[1][1])

print(arr[:, 2])


# 문제: 배열 인덱싱
arr = np.arange(20).reshape(4,5)
print(arr)

print(arr[:2,:3])

print(arr[2:4, 3:5])


# 문제: 배열 값 수정
arr = np.arange(9).reshape(3, 3)
print(arr)

arr[1][2] = 50

arr[0] = [10, 20, 30]

print(arr)


# Boolean 인덱싱
arr = np.array([10,25,30,45,50,15])

result = arr[arr >= 30]
print(result)

result2 = arr[arr % 2 == 0]
print(result2)

result3 = arr[(arr>=20) & (arr<=40)]
print(result3)


# 문제: 배열 연산

arr = np.array([1,2,3,4,5])

result1 = arr + 10
print(result1)

result2 = arr * 2
print(result2)

result3 = arr.sum()
print(result3)

avarge = arr.mean()
print(avarge)

'''