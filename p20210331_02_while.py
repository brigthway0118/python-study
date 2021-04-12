#while문
#조건이 참일 '동안' 실행.

#조건이 계속 참이라서 무한 반복이다.
# while True:
#     print('python')
#
# a=0
# while True:
#     a+=1
#     if a>10:
#         break
#     print(a)
# print()
# print("===============================")

#실습) 1~10까지 합을 while문으로 출력
# total=0 #합계를 누적할 변수
# a=0 #증가하는 변수
# while True:
#     a += 1
#     total += a
#     print(total)
#     if a == 10:
#         break
# print('======================')

#while 조건을 활용한 1~10까지의 합
# a=0
# while a<10:
#     a+=1
#     print(a)
# print("===============================")

#실습) a가 증가하면서 합계를 구하고 그 합이 2000이 넘으면 반복문 종료.
    #방법 1
# s=0
# a=0
# while True:
#     a += 1
#     s += a
#     print('합 : ', s)
#     if s>2000:
#         print('그 수 : ', a)
#         break
    #방법 2
# s=0
# a=0
# while s<2000:
#     a+=1
#     s+=a
#     print('합 : ', s)
# print('그 수 : ', a)

#실습)사용자가 입력한 수를 누적 하다가 만약 0을 입력하면 누적한 결과를 보여주고 종료
    #1
# s=0
# while True:
#     a=int(input('더할 값은? '))
#     if a==0:
#         break
#     s+=a
# print(s)
#
    # #2

# a=1
# s=0
# while a!=0:
#     a = int(input('더할 값은? '))
#     s+=a
# print('누적 값은 : ', s)

