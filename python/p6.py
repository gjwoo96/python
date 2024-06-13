# 튜플
## 리스트와 다른게 값을 변경할수없다.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 집합(set)
# 중복 안됨, 순서없음
my_set = {1,2,3,3,3,3}
print(my_set)

# 교집합 찾기
java = {1,2,3,4,5,6,}
python = set([1,3,5,6,8,9])

print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python) #java에서 python에서 겹치지 않는 숫자
print(java.difference(python))

# 값 추가
python.add("김태호")
print(python)

# 값 제거
python.remove("김태호")
print(python)

# 자료구조의 변경
menu = {"커피","우유","주스"}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

