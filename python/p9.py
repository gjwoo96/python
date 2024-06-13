# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance,money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commisiion = 100
    return commisiion, balance - money - commisiion

balance = 0
balance = deposit(balance,1000)
#balance = withdraw(balance,2000)
#balance = withdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원, 잔액은{1}원".format(commission,balance))


# 기본값
# 파라미터 부분에 기본값을 지정해줄수있다.
def profile (name, age = 17, main_lang = "파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어 : {2}".format(name,age,main_lang))

profile("유재석",20,"파이썬")
profile("김태호",25,"자바")
profile("정준하")

# 키워드값
def profile2(name,age,main_lang):
    print(name,age,main_lang)

# 함수 파라미터 부분에 키워드를 적고 값을 넣어주면 순서와 상관없이 해당 키워드의 값이 전달이 된다.
profile2(name="유재석",main_lang="파이썬", age=20)

# 가변인자 *를 붙여서 사용가능
def profile3(name,age,*lang):
    print("이름 : {0}\tskdl : {1}\t".format(name,age), end = " ")
    for langstr in lang:
         print(langstr, end =" ")
    print()

profile3("유재석",20,"Python","aaa","bbbb")
profile3("김태호",25,"ㅊㅊㅊㅊ","ㅁㅁㅁㅁㅁ","ㄹㄹㄹㄹㄹ")