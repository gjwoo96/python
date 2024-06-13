from random import *

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 예제
# students = ["Iron Man","Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

totalCustomer = 0
#Quiz
for i in range(1,51):
    min = randint(5,50)
    if min >= 5 and min <= 15:
        print("[o]{0}번째 손님 (소요시간: {1}분)".format(i,min))
        totalCustomer += 1
    else :
        print("[ ]{0}번째 손님 (소요시간: {1}분)".format(i,min))

print("총 탑승 승객 : {0}분".format(totalCustomer))