#Input()함수
# a = input('이름을 입력해주세요 : ')
# print('입력한 값은? ', a)

#나이를 입력받아 화면에 출력
# age=input('나이를 입력해주세요 : ')
# print('입력한 나이는?', age)
# print('당신의 나이는',age,'입니다')
# print('당신의 나이는',age,'입니다',sep='/')
# print('당신의 나이는'+age+'입니다')# +가 되니까 age는 문자형
# # 주의. 입력한 값은 *문자형*으로 취급한다.

# c=input('오늘의 날씨 : ')
# txt='오늘의 날씨는'
# print(txt, c)
# print(txt, c, sep='**')
# print('============================')
#
# #help(함수). 함수 설명
# help(print)
# help(input)

#사용자가 입력한 값에 100을 더해서 출력
# a=input('숫자는? ')
# #a=int(a) #int()함수. 매개변수를 int형으로 *반환*. a를 int형으로 반환.
# a=float(a)# 매개변수를 float(실수)형으로 반환.
# print(a+100)


#실습)1-1사용자에게 두 수를 입력받아서 사칙연산 프로그램을 만들자
# a=int(input('입력1 '))
# b=int(input('입력2 '))
# #a=int(a)
# #b=int(b)
# print('더하기' ,a+b)
# print('%d + %d = %d'%(a,b,a+b))
# print('빼기',a-b)
# print('%d - %d = %d'%(a,b,a-b))
# print('곱하기',a*b)
# print('%d * %d = %d'%(a,b,a*b))
# print('나누기',a/b)
# print('%d / %d = %.1f'%(a,b,a/b))
# print('두 수를 더한값은',a+b,'입니다.')

#실습)1-2사용자에게 두 수를 입력받아서 사칙연산 프로그램을 만들자
# data = input('두 수를 입력 ')
# a = int(data.split()[0])
# b = int(data.split()[1])
# print('%d + %d = %d'%(a,b,a+b))
# print("====================================")
# data = input('두 수를 입력 ').split() #두 수를 분리
# a,b = map(int,data) #data의 각각의 값을 int함수를 적용시켜서 대입
# print(a,'+',b,'=',a+b)

#실습) 반지름을 사용자로부터 입력받아 원의 넓이를 구해보자.
#원주율 3.14
# r = int(input('반지름의 길이는? '))
# p = 3.14
# print('원의 넓이는 ', r*r*p, '입니다.')
# print('원의 넓이는 ', r**2 * p, '입니다.')# 제곱연산






