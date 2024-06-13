str = """
asdasdasdasdasd
asdasda

a
sdas
das
da
sd
asd
aasd
"""

print(str)

jumin = "990120-1234567"
print(jumin[7])
print(jumin[0:2])
print(jumin[2:4])
print(jumin[4:6])

# 처음부터 index 6까지
print(jumin[:6])
# 7부터 끝까지
print(jumin[7:])
# 뒤에서부터
print(jumin[-1])


p = "Python is Amazing"
# 소문자 
print(p.lower())
# 대문자
print(p.upper())
# [?]번째 대문자인지 return boolean
print(p[0].isupper())
# 문자열 길이
print(len(p))
# 특정문자열 변환
print(p.replace("Python","Java"))

# 특정문자열 인덱스 확인
index = p.index("n")
print(index)

# 특정문자열 인덱스 + n 인덱스 문자열 확인
index2 = p.index("n",index +1)
print(index2)

# 위와 같은 함수
print(p.find("Java"))

# find와 index 의 차이점 
# find에서는 원하는값이 없으면 -1 index는 오류가 발생

# 특정문자열에서 특정문자가 몇번있는지 확인
print(p.count("n"))