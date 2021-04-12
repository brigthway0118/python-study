#딕셔너리{}
#딕셔너리는 순서가 없다.
#딕셔너리의 value를 가져올 때는 dic[key]

#data=[1,2,3,4] # 리스트
#data=(1,2,3,4) # 튜플
# *리스트와 튜플은 index를 이용해서 값을 가져온다. ex) data[1], data[2]

# data={'a':10,'b':20,'c':30,'d':40}
# print(data['b'])
#print(data['a':]) #에러발생. 딕셔너리는 :이 안됨.

# data={'홍길동':22,'이순신':45}
# print(data['홍길동'],'살')
#
# data={'홍길동':[20, 165.5], '이순신':45}
# print(data['홍길동'][1],'cm')
#
# data={'홍길동':{'나이':20, '키':165.5}, '이순신':{'나이':45,'키':170.5}}
# print(data['홍길동']['키'],'cm')
# print(data['이순신']['키'],'cm')
# ###################################################
# data = {1:['홍길동', 20, 165.5],2:['이순신', 45, 170.5]}
# print(data[1][0])

#딕셔너리에 데이터 추가
# data = {}
# data['홍길동']=20 #data라는 dict가 있기때문에 넣을 수 있는것. *꼭 dict를 생성하고 넣기*
# data['이순신']=[45,170.8]
# print(data) #출력 : {'홍길동': 20, '이순신': [45, 170.8]}

#실습) 컴퓨터언어를 입력받아 딕셔너리에 저장
#{'backend':'java','frontend':'html5'}
# lang={}
# #lang 변수에 dict{}  생성.
# back = input('backend 언어를 입력 : ')
# lang['backend'] = back
# #lang[key] = value. backend key에 입력받은 back value 입력.
# front = input('frontend 언어를 입력 : ')
# lang['frontend'] = front
# print(lang)

data = {1:'고질라', 2:'귀멸의칼날', 3:'더박스'}
print(data.keys())
#print(data.keys()[0]) # 에러 발생. .key()는 주소값만 가져오기 때문에.
#print(list(data.keys())[0]) # 1 출력.
print(data.values())
#print(list(data.values())[0]) # 고질라 출력




#Set:{}. key가 없는{}.
#Set은 중복데이터가 저장되지 않는다. 순서와 인덱스가 없다.
asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
print(asia)#{'중국', '한국', '베트남', '일본'}
asia.remove('일본')
asia.update({'한국','홍콩','태국'})
print(asia) # {'베트남', '태국', '홍콩', '한국', '중국'} 중 순서가 상관없이 섞인다.

