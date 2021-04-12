#리스트[] : 연속적인 메모리의 할당.
# data = [10,20,30,40,50]
# print(data)
# print(data[0])
# print(data[1:3])#[20, 30]출력. 여러 개를 가져오니 리스트 타입.
# print(data[2:])#[30, 40, 50]
# print(data[:-1])#[10, 20, 30, 40]. 마지막 데이터를 제외.
# data[1] = 200
# #data[5] = 100. data는 0~4까지 연속적으로 할당되어있음.
# # data[5]=100은 index 초과로 에러발생.
# data.append(60)
# print(data) # [10, 200, 30, 40, 50, 60]
# data.clear() # 비우기
# print(data)


data = ['홍길동', 20, 165.8]
print(data[0], data[1], data[2])
data=[['홍길동', 20, 165.8], ['이순신', 40, 170.5]]
print(data[1][0])
