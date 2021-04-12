# #함수
# #내장함수
# #sum함수. 합을 구해주는 함수
#
# #사용자함수로 sum구현
# #매개변수:리스트, 반환값:합계. 반환값은 함수는 원칙적으로 하나의 값만 반환한다.
# #def 함수이름():
#     #내용 정의하기
# def mysum(data):
#     s=0
#     for x in data:
#         s+=x
#     #print(s)
#     return s
#
# data = [5,18,4,6]
# r = mysum(data)
# print('리턴값 : ',r)

#max함수
#data=[5,18,50,20,60,30,100,500]
# ma=max(data)
# print('가장 큰 값:',ma)
# mi=min(data)
# print('가장 작은 값',mi)
#
# #max함수를 사용자정의함수로..
# def mymax(data):
#     mx=data[0]
#     for x in data:
#         if mx<x:
#             mx=x
#     return mx
# data=[5,18,50,20,60,900,100,500]
# print('가장 큰 값 : ', mymax(data))
#
# data = [78, 8, 5, 16]
# print('가장 큰 값 : ', mymax(data))
#
# #min함수를 사용자정의함수로..
# def mymin(data):
#     mn=data[0]
#     for x in data:
#         if mn>x:
#             mn=x
#     return mn
# data=[5,18,50,20,1,900,100,500]
# print('가장 작은 값 : ', mymin(data))
#
# data = [78, 8, 3, 16]
# print('가장 작은 값 : ', mymin(data))

#ord() 함수. 문자->아스키코드값을 반환.
# #한글은 유니코드체계
# print(ord('A'), len('A')) # 65 1
# print(ord('가'), len('가'), '가'.encode(), len('가'.encode())) # 44032 1
#
# #chr() 함수. 아스키코드->문자로 반환
# print(chr(65))#A
# print(chr(44032))#가

#실습)사칙연산 함수
#매개 변수 : 두 수, 반환값 : 결과
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def cal(a,b):
    return a+b,a-b
inputData = input('두 수를 입력 : ').split()
val1 = int(inputData[0])
val2 = int(inputData[1])
print('더하기 : ', add(val1, val2))
print('빼  기 : ', sub(val1, val2))
print('곱하기 : ', mul(val1, val2))
print('나누기 : ', div(val1, val2))

print('계  산 : ',cal(10,20)) # 계  산 :  (30, -10)
print('계  산 : ',cal(10,20)[0],cal(10,20)[1]) # 계  산 :  30 -10

#실습)월급구하기
y = 3000
s = 10000
c = 3

def sal_cal(y, s, c):
    w = y/12+s*c
    return w
print(sal_cal(y,s,c),'만원')