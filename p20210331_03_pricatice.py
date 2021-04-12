# #연습문제
# #1-1별찍기)
# for r in range(1,7):
#     print('*' * r)
# print('==========================')
# #1-2별찍기
# for r in range(6,0,-1):
#     print('*' * r)
# print('==========================')
#
# for r in range(1,7):
#     print(' '*(6-r),'*'*r)
# print('==========================')
#
#
# #실습2 구구단
# a=2
# for r in range(1,10):
#     print('%d * %d = %d'%(a, r, a*r))
# print('==========================')
#
#
#
# #실습3 범위 미만의 3의배수
# # cut = int(input('커트라인 : '))
# # a=0
# # mul=0;
# # print(cut)
# # while True:
# #     mul=a*3
# #     print('%d'%(mul), end=' ')
# #     a+=1
# #     if cut < (a*3):
# #         break
# print('==========================')
# #실습4
# #첫 번째 계산 마무리 후, 여부를 묻고, q일경우 종료하는 경우
# #두 번째 첫번째가 q면 종료. 그 외는 진행
# while True:
#     inType = input('사칙연산 기호 입력(q종료) : ')
#     if inType=='q':
#         break
#     data = input('두 숫자 입력 : ').split()
#     val1 = int(data[0])
#     val2 = int(data[1])
#     #data[1]=기호
#     if inType=='+':
#         print('%d + %d = %d'%(val1, val2, val1+val2))
#     elif inType=='-':
#         print('%d - %d = %d'%(val1, val2, val1-val2))
#     elif inType=='*':
#         print('%d * %d = %d'%(val1, val2, val1*val2))
#     elif inType=='/':
#         print('%d / %d = %.2f'%(val1, val2, val1/val2))
#     else:
#         print('잘못된 입력')
# print('==========================')
#실습5)
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92, 6:100, 7:89}
# print('90점 이상 학생')
# for x in list(dicA.keys()):
#     if(dicA[x]>=90):
#         print(x,'번')
# print('==========================')

#실습6)
# #입력 반복, 해서 list 내 이름 순회..
# listA = ['홍길동', '이순신', '김순희', '이철수']
# amount = 0
# aHistory = []
# for x in listA[:]:
#     print(x,'의 오늘 판매 수량을 입력 :', end=' ')
#     amount = int(input())
#     aHistory.append('*' * amount)
# print('판매 수량')
# for y in range(0,len(listA)):
#     print(listA[y],' : ', aHistory[y])
# # print('==========================')


#실습7 이름/몸무게/키를 입력받아서 비만여부 체크
# 평균체중 = (키-100)*0.9
#오차범위 = +- 5%
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

####################################################

#실습2) 구구단
# dan = int(input('단수는? '))
# for x in range(1,10):
#     print('%d * %d = %d' % (dan, x, dan*x))

# #실습2-2) 이중반복분 구구단
# for x in range(1,10):
#     print('=============')
#     print('%d단'%(x))
#     for y in range(1,10):
#         print('%d * %d = %d'%(x,y,x*y), end='\t')
#         if y%3==0:
#             print("")
#

#실습3)
# last = int(input('커트라인 입력 : '))
# for x in range(0, (last+1), 3):
#     print(x, end=' ')
# print()
# for x in range(0, last+1):
#     if x%3==0:
#         print(x, end=' ')


# #실습4)계산기
# while True:
#     a= input('first : ')
#     if a=='q':
#         print('종료')
#         break
#     a=int(a)
#     b= int(input('second : '))
# ####### + - * / 입력하면 빠져나가기####
#     while True:
#         sign = input('기호는? ')
#         if sign in ['+','-','*','/']:
#             break
# #######################################
#     if sign=='+':
#         print(a+b)
#     elif sign=='-':
#         print(a-b)
#     elif sign=='*':
#         print(a*b)
#     elif sign=='/':
#         print(a/b)
#     else:
#         print('잘못된 입력')

#실습5
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# print(dicA.keys()) #dict_keys([1, 2, 3, 4, 5])
# print(dicA.values()) #dict_values([94, 87, 91, 75, 92])
# print(dicA.items()) #dict_items([(1, 94), (2, 87), (3, 91), (4, 75), (5, 92)])
#
# for num,score in dicA.items():#items()는 리스트 안에 튜플을 반환.
#     #num, score in dicA.item()하면 앞쪽 아이템이 num에 뒤쪽 아이템이 score에 들어간다.
#     #ex) items에서 num=key값, score=value값
#     if score>=90:
#         print(num,'번')

#실습6
    #1) 사원의 판매수량 입력
    #2) 히스토그램 그리기
    #3) 판매수량 저장 타입을 [],{}등 뭐로 할 것인지 정한다.
    #4) 데이터 구조 : {'홍길동':10,'이순신':15,'김순희':5,'이철수':7}
    #[]의 경우 매칭이 순서,1:1매칭이 되어야한다. {}은 키-밸류를 매칭시킨다.
data = ['홍길동','이순신','김순희','이철수']
qty = {}
for name in data:
    qty[name] = int(input(name + '님의 판매수량 : '))
for x,y in qty.items():
    print(x+'의 판매수량 : '+'*'*y)