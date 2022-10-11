# import numpy as np
# import math

# x = [1,2,3]

# x = np.array(x)
# x = np.array([[1,2],[3,4]]) # 행렬화

# print(x) 

# y = np.array([[0,1],[1,0]])

# print(x*y)
# print(x+y)  
# print(x@y) #  행렬곱셈
# print(np.log(1))
# print(np.log(np.e))
# print(round(1,2))
# print(math.ceil(1.2)) #천장 (올림)
# print(math.floor(1.6)) # 바닥  (내림)

# value = 0
# index = 1
# while index<= 10:
#     value += index **2
#     index += 1
# print(index)
# print(value)

# name = 'chan ho Park'
# for idx, value in enumerate(name):
#     print(value)

# import random

# class Test:
#     def __init__(self):
#         self.score = 0
#     def addTest(self):
#         a = random.randint(1,10)
#         b = random.randint(1,10)
#         c = a+b
#         print(a, "+", b, "=", end= " ")
#         ans = int(input())
#         if ans == c:
#             self.score += 1
#     def subTest(self):
#         a = random.randint(1,10)
#         b = random.randint(1,10)
#         c = a-b
#         print(a, "-", b, "=", end="")
#         ans = int(input())
#         if ans == c:
#             self.score += 1
# test = Test()

# while True:
#     print("--------")
#     print("[1] add")
#     print("[2] substract")
#     print("[q] Exit")

#     m = input("select menu: ")

#     if(m=='q'):
#         break
#     elif (m == '1'):
#         test.addTest()
#     elif (m == '2'):
#         test.SubTest()


# print("Your score is", test.score)

data = [41, 32, 30, 23, 24, 32, 11, 39, 24, 46, 50, 18, 41, 14, 33, 50, 38, 25, 32, 16,
43, 19, 35, 22, 46, 43, 10, 22, 17, 47, 66, 48, 25, 43, 28, 31, 12, 25, 12, 48]
no_classes = 6
unit = 1
class1 = []
class2 = []
class3 = []
class4 = []
class5 = []
class6 = []

def gubun(x):
    return 9.5<=x<=19.5 

result = list((filter(gubun,data))
print(result)