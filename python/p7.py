from random import *

# randomCnt = range(1,21)
# users = list(randomCnt)
# shuffle(users)

# winners = sample(users,4)
# print(winners[0])
# print(winners[1:])

# weaher = input("오늘날씨어때요?")
# if weaher == "비":
#     print("우산")
# elif weaher == "먼지":
#     print("마스크")
# else: print("맑음")

# if 문
# temp = int (input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요") 

# for wait in [0,1,2,3,4]:
#     print("대기번호: {0}".format(wait))

# for wait2 in range(1,6):
#     print("대기번호: {0}".format(wait2))

# while
index = 5
while index >= 1:
    print("{0}번 남음".format(index))
    index-= 1
    if index == 0:
        print("exit")