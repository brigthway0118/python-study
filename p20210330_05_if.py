#조건문(if)
# a=-1
# if a>0:#조건. 참이면 실행. if 이후 들여쓰기 된 코드들이 참일 경우 실행되는 코드.
#     print('양수')
#     print(a)
# else:#거짓이면 실행. else 이후 들여쓰기 된 코드딜이 실행되는 코드
#     print('음수')
#     print(a)
# print('==============')
# print('프로그램 종료')

#실습)회원등급 출력
#a가 90보다 크면 good, 아니면 try 출력.
# a=int(input('사용자 점수 입력 : '))
# if a>90:
#     print('good')
# else:
#     print('try')
# print('======================================')

#실습)비밀번호 체크
#비밀번호가 일치하면 '문이 열립니다.' 출력
#일치하지 않으면 '다시 확인하세요' 출력

# pw = '0000' #초기 비밀번호
# inputPw = input('비밀번호 입력 : ')
# if pw == inputPw:
#     print('문이 열립니다')
# else:
#     print('다시 확인하세요')
# print('=================================')


# #어떤 수가 짝수면 '짝수' 출력, 홀수이면 '홀수'출력
# a=int(input('숫자는? '))
# if a==0:
#     print('0입니다')
# elif a%2==0:
#     print('짝수')
# else:
#     print('홀수')
# print('=================================')

# #실습)~90 A, 89~80 B, 79~70 C, 69~60 D, 59~ F
# point = 85
# if point >= 90:
#     print('A')
# elif point >= 80:
#     print('B')
# elif point >= 70:
#     print('C')
# elif point >= 60:
#     print('D')
# #elif point >= 60 and 69>=point:
#     print('D')
# else:
#     print('F')
# print('====================================')

#실습) 이름/몸무게/키를 입력받아서 비만여부 체크
# 평균체중 = (키-100)*0.9
# 오차범위 = +- 5%
# name = input('이름을 입력해주세요 : ')
# weight = float(input('몸무게를 입력해주세요 : '))
# height = float(input('키를 입력해주세요 : '))
# averWeight = (height-100)*0.9
# # print('정상체중 : ', averWeight)
# # print('비만체중 : ', averWeight*1.05)
# # print('저체중 : ', averWeight*0.95)
#
# if weight > averWeight*1.05:
#     print(name, '님은 비만입니다.')
# elif weight < averWeight*0.95:
#     print(name,'님은 저체중입니다.')
# else:
#     print(name, '님은 적정 체중입니다.')
# print("=====================================")

# #실습)계산기
# #두 수와 기호를 입력 받아 사칙연산(+,-,*/)를 출력
# # 30 + 20 = 50
# data = input('식 입력 : ').split()
# val1 = int(data[0])
# val2 = int(data[2])
# if data[1] == '+':
#     #print(val1,'+',val2,'=',val1+val2)
#     print('%d + %d = %d'%(val1,val2,val1+val2))
# elif data[1] == '-':
#     #print(val1, '-', val2, '=', val1 - val2)
#     print('%d - %d = %d' %(val1, val2, val1 - val2))
# elif data[1] == '*':
#     #print(val1, '*', val2, '=', val1 * val2)
#     print('%d * %d = %d' %( val1, val2, val1 * val2))
# elif data[1] == '/':
#     #print(val1, '/', val2, '=', val1 / val2)
#     print('%d / %d = %.2f' % (val1, val2, val1 / val2))
# else:
#     print('잘못된 접근입니다.')
# print('==================================')

#실습)계산기
#두 수와 기호를 입력 받아 사칙연산(+,-,*/)를 출력
import os
#print(os.listdir())

# data = input('식 입력 : ')
# cal = eval(data) # 문자를 식으로 처리하여 반환. 모든 문자를 처리하기때문에 보안상 이슈 발생.
#                  #쓰지 않는 것을 권장.
# print(cal)

#실습) 두 수를 입력을 받아서 큰 수를 화면에 출력
# data=input('두 수를 입력 : ').split()
# a=data[0]
# b=data[1]
# if a>b:
#     print(a)
# elif b>a:
#     print(b)
# else:
#     print('두 수는 같다')

#실습)거스름돈 계산
#현재 있는 금액과 물품구입금액을 입력받고 비교하여 거스름돈을 작성
# cash = int(input("소지금 : "))
# pay = int(input("지불금액 : "))
# if cash==pay:
#     print('계산완료')
# elif cash>pay:
#     print('거스름돈 ',cash-pay,'원', sep='')
# else:
#     print('돈이 ', pay-cash, '원 부족', sep='')
# print('==========================')

#논리연산자
# a=10; b=20;
# print(a>0)#결과값 True
# print(a>0 and b>0)#결과값 True
# print(a>0 and b<0)#결과값 False
# print(a>0 or b<0)#결과값 True
# print(not(a>0))#결과값 False. not연산자 활용

a=10; b=-20;
if a==0 or b==0:
    print('0이 아닌 수를 입력하세요')
elif a>0 and b>0:
    print('둘 다 양수')
elif a>0 or b>0: #첫번째 if문으로 둘다 양수인 경우를 필터 했으니 or로 둘중 하나를 처리.
    print('둘 중 하나가 음수')
else:
    print('두 수는 음수입니다.')
#====================================================#
price = {1:['자장면',5000,'중식'], 2:['짬뽕',6000,'중식'],
         3:['설렁탕',8000,'한식'], 4:['비빔밥',7000,'한식'],
         5:['피자',9000,'양식'], 6:['스파게티',8500,'양식']}
#print('1.자장면   2.짬뽕    3.설렁탕   4.비빔밥   5.피자   6.스파게티')
print('1.자장면\t2.짬뽕\t3.설렁탕\t4.비빔밥\t5.피자\t6.스파게티')
print('-' * 90)
select = int(input('메뉴를 선택하세요 : '))
#if select == 1 or select == 2:
menukey = price.keys()
if select in menukey:
    print(price[select][0],'선택')
    print(price[select][1],'원')
    print(price[select][2],'코너')
else:
    print('잘못된 선택')


# if 변수 in []. in : 포함여부.
# if select in [1, 2]:
#     print('중식코너')
# elif select in [3, 4]:
#     print('한식코너')
# elif select in [5, 6]:
#     print('양식코너')
# else:
#     print('잘못된 번호')
