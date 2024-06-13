#print("백문이 불여일견 \n 백견이 불여일타")
#print("저는 \"나도코딩\" 입니다.")

# \\ : 문장 내에서 \ 
#print("C:\\users\\test")

# \r : 커서를 맨 앞으로 이동
#print("Red Apple \r Pine")

# \b : 백스페이스 (한 글자 삭제)
#print("Redd\bApple")

# \t : 탭
#print("Red\tApple")

url = "http://youtube.com"
rule1 = url[7:]
#rule1 = url.replace("http://","")
rule2 = rule1[:rule1.index(".")]
rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count("e"))+"!" 
#print(rule1)
#print(rule2)
#print(rule3)

# 배열

subway = ["유재석","조세호","박명수"]

# 인덱스 추출
#print(subway.index("조세호"))

# 배열 값 추가(마지막에 추가)
subway.append("하하")
#print(subway)

# 특정 인덱스에 값을 추가
subway.insert(1, "정형돈")
#print(subway)

# 배열에 제일 뒤값을 가져옴
#print(subway.pop())
#print(subway)

# 정렬
num_list = [5,2,1,3,4]
mix_list = ["조세호",20,True]
# num_list.sort()

# print(num_list)

# # 순서 뒤집기
# num_list.reverse()

# print(num_list)

# # 모두지우기
# num_list.clear()

# print(num_list)

# 리스트 확장
num_list.extend(mix_list)

print(num_list)