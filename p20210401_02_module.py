#모듈
#import 모듈
#from 모듈 import 클래스
#=======================================
import time #타이머
import datetime #날짜
from datetime import datetime #날짜 모듈의 datetime 클래스 사용
from time import sleep
import random #난수(랜덤) 모듈
import calendar # 달력모듈
import turtle # gui. turtle이 객체임.


# print(time.localtime())
# #time.struct_time(tm_year=2021, tm_mon=4, tm_mday=1, tm_hour=16, tm_min=0, tm_sec=2, tm_wday=3, tm_yday=91, tm_isdst=0)
# print(list(time.localtime()))#[2021, 4, 1, 16, 0, 28, 3, 91, 0]
# print(time.localtime().tm_year,'년')#2021 년
#
# print(time.localtime().tm_year,'년 ',
#       time.localtime().tm_mon,'월 ',
#       time.localtime().tm_mday,'일 ',
#       time.localtime().tm_hour,'시 ',
#       time.localtime().tm_min,'분 입니다.'
# ,sep='')


# now = datetime.datetime.now()
# print(now)#2021-04-01 16:09:55.026755
# newNow = now.strftime('%Y-%m-%d')
# print(newNow)#2021-04-01

# from datetime import datetime
# now = datetime.now() #2021-04-01 16:32:02.443280
# print(now)

# print('시작')
# time.sleep(3)#sleep함수. (3)이면 3초
# print('3초지남')

# #실습) timer 만들기
# sec = int(input('몇초?'))
# print('시작')
# for x in range(1, sec+1):
#     sleep(1)
#     print(x, '초', sep='')
# print('종료')
#==================================================
#난수모듈(random)
#a = random.randint(1, 6)# 1~6까지 랜덤생성
#주사위게임
# countA = 0
# countB = 0
# while countA!=2 and countB!=2:
#     a = random.randint(1, 6)# 1~6까지 랜덤생성
#     b = random.randint(1, 6)
#     if a>b:
#         print('a는 ',a,'\tb는 ',b, sep='')
#         print('승자는 a')
#         countA += 1
#     elif b>a:
#         print('a는 ', a, '\tb는 ', b, sep='')
#         print('승자는 b')
#         countB += 1
#     else:
#         print('a는 ', a, '\tb는 ', b, sep='')
#         print('무승부')
# print('결과')
# if countA>countB:
#     print('a는',countA, '\tb는',countB)
#     print('승자는 A')
# else:
#     print('b는', countB, '\ta는', countA)
#     print('승자는 b')


#sample()
#random.sample(a,b) : a중에서 b개를 뽑아라.
#ex.. random.sample(range(1,46), 6). 1~45중에서 6개를 고르기
# print(random.sample(range(1,46), 6))#[21, 2, 43, 24, 6, 1]

#choice()
#random.choice([1,2,3,4,5,6]) : 1,2,3,4,5,6 중 하나뽑기.
#random.choice(['가위','바위','보']) : 가위, 바위, 보 중 하나 뽑기
# print(random.choice(['가위','바위','보'])) #1

#shuffle()
# data=[1,2,3,4,5]
# random.shuffle(data) # [1,2,3,4,5]를 무작위로 재배열
# print(data) # [4, 2, 3, 5, 1]

#turtle
# turtle.shape('turtle')
# turtle.color('yellow')
# for x in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.done
# #

#야구게임
answer = random.randint(100,999) #1부터 999까지 생성.
print(answer)
myAnswer = 0
while True:
    if myAnswer == answer:
        print('예측성공')
        break
    myAnswer = input('정답예측 : ')
    if myAnswer != answer:
        print('예측실패')
