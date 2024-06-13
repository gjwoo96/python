# 방법 1

# %d %? 숫자를 나타낼때
#print("나는 %d 살 입니다." % 20)
# %s %? 문자를 나타낼때
#print("i'm like %s" %"python")
# %c 문자열 하나만 받음
#print("나는 %s살입니다."% "s")

# 방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아합니다.".format("파란","빨강"))
# print("나는 {1}색과 {1}색을 좋아합니다.".format("파란","빨강"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

# 방법 4 (파이썬 버전 3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")