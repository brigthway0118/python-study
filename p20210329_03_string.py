#문자열다루기
txt = 'python is esay!'
print(txt)
print(txt[0]) # 0번째 출력. p
print(txt[-1]) # 맨 뒷글자 출력. n
print(txt[7:8])# 공백도 포함된다. python i 출력.
# txt[strat index:stop index].
# start인덱스 출력, stop인덱스에서 멈추기 때문에 8번쨰는 출력이 안된다.
# ex) txt[7:8]은 i만 출력

print(txt[:2]) # [0:2] 같은 의미
print(txt[10:14])#esay
print(txt[10:-1])#esay
print(txt[-5:-1])#esay

#실습
s = 'my house'
print(s[3:])
txt = '012345678901234567890123456'
print(txt[0:10])
print(txt[10:20])
print(txt[20:])
