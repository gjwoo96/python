# 지역변수 전역변수

#전역변수
gun = 10

def checkpoint(soldiers):
    # 지역변수
    #gun = 20
    # 전역변수를 함수내에서 사용
    global gun
    gun = gun - soldiers
    print ("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))