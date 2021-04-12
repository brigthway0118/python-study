#컨트롤 + / 주석 설정/해제
#변수 : 데이터를 저장하기 위한 공간
#변수명 : 저장된 데이터를 접근하기 위한 이름
#= : 대입연산자
# a = 10
# print(a)
#
# a='hello python'
# print(a)
# a=3.14
# print(a)

a=50
b=3
print('a+b=', a+b)
print('a-b=', a-b)
print('a*b=', a*b)
print('a/b=', round(a/b,2) ) # a/b= 16.67
print('a/b=%f'%(a/b)) # a/b=16.666667
print('a/b= %.2f' % (a/b)) # a/b= 16.67 출력
print('a//b=', a//b) #몫 연산자 % : a%b= 16
print('a%b=', a%b) #나머지연산자 % : a%b= 2
val = 10000
tHour = 3600
tMin = 60
print('시간 : ' ,val//tHour)
print('분 : ' ,(val-((val//tHour)*tHour))//tMin )
print('초 : ' , val-
      (tHour*(val//tHour))
      -(tMin*((val-((val//tHour)*tHour))//tMin))
      )
# t=10000
# r=t//3600
# print(h,'시간')
#m=r//60
# print(m,'분')
# s=r%60
# print(s,'초')

#포맷문자열
a=30
b=20
print(a,'+',b,'=',a+b) # 30 + 20 = 50
print('%d + %d = %d'%(a,b,a+b)) # 30 + 20 = 50
print('%d - %d = %d'%(a,b,a-b)) #30 - 20 = 10
print('%d * %d = %d'%(a,b,a*b)) #30 * 20 = 600
print('%d / %d = %d'%(a,b,a/b)) #30 / 20 = 1
print('%d / %d = %f'%(a,b,a/b)) #디폴트 소수점 6자리
print('%d %% %d = %.2f'%(a,b,a/b))

