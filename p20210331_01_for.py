#반복문, for문
#for 변수 in 범위:
#   실행문 # 범위만큼 반복적으로 실행
#
# for x in [1,20,30,7,17]:#[ ] 안에 *5개*의 데이터가 있어서 5번 반복.
#     print('python', x)
#python 1 python 20 .... python 17출력
# data=['홍길동', '이순신', '유관순']
# for x in data:
#     print(x) # 홍길동, 이순신, 유관순 출력
# print('====================================')
# for x in [0,1,2]:
#     print(data[x]) # 홍길동, 이순신, 유관순 출력

#실습)0부터 9까지 출력
#1) []하드코딩 이용
# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x)
# print('==================================')
# #2) range이용
# for x in range(10):
#         print(x)
# print('==================================')
# for x in range(0,10,2): #짝수만 출력
#     print(x)
#2)range(start, stop, step). 정수를 생성해주는 함수
# print(list(range(10)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], stop
# print(list(range(0,10,1)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], start, stop, step
# print(list(range(1,10,2)))#[1, 3, 5, 7, 9],
# print(list(range(5,10)))#[5, 6, 7, 8, 9], start, stop

#합계를 구하기
# s = 0 #합계를 저장할 변수
# for x in range(1,101):
#     s+=x
# print(s)
# print('================================')

#실습)사용자에게 마지막 숫자를 입력받아
#1부터 그 수까지 더하기

# a = int(input('숫자 크기 입력 : '))
# total = 0
# for x in range(1,a+1):
#     total+=x
# print(total)

#for-break문
#실습) 1부터 100까지 합이 2000이 넘을때의 수를 출력()
# s=0
# for x in range(1,101):
#     s+=x
#     if s>2000:
#         break#반복문을 빠져나갈 때..종료할 때 사용하는 키워드
# print('합 : ', s, ' 커트라인 : ', x)
#
# #for-else문
# #실습)바보라는 글자가 발견되면 강퇴
# data = ['안녕', '방가', '반가워', '헬로우','바','오늘만나']
# bad = ['바보', '멍청이']
# for x in data:
#     print(x)
#     if x in bad: # bad에 x가 포함되어 있다면...
#         print('강퇴')
#         break
# else: #for문의 else : for문이 정상수행(break문 실행X)했을 때 실행.
#     print('바른말 사용 유저') # for문이 break를 만나지 않고 끝까지 실행되어서 출력된다.


#continue문 : skip의미. 해당하는 반복을 넘기고 그 다음 반복으로 진행.
# data = [3,4,6,8,7,10]
#
# for x in data:
#     if x%2==1:
#         continue
#     print(x, end='  ')
# print()
# print('==============================')
#


#실습) 60점 과락
# data = [65,45,95,55,70]
# data1 = [65,68,96,86,72]
# data = input('점수는 ? ').split() # 문자형을 리스트로 반환.
# print(data)# ['50', '60', '70', '80', '90'] 출력
# data = map(int, data) # map() : data의 각 인자를 int형 객체로 반환
# print(data)# <map object at 0x00000254075E4FA0> 출력
# data = list(data)
# print(data)# [50, 60, 70, 80, 90] 출력
# for x in data:
#     print(x, end=' ')
#     if x < 60:
#         print('불합격')
#         break
# else:
#     print('합격')


#실습) 300점 기준으로 과락
total = 0
data = input('점수는 ? ').split() # 문자형을 리스트로 반환.
data = map(int, data) # map() : data의 각 인자를 int형 객체로 반환
data = list(data)
for x in data:
    total += x
    if total >= 300:
        print('합격')
        break
else:
    print('불합격')