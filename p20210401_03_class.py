#class : 객체를 만들기 위한 틀

class Car:
    #속성(필드)
    name = '아이오닉5'
    color = '실버'
    pw = False
    #기능(메소드)
    def power(self):
        Car.pw = True

c1=Car()

print(c1.pw)
print(c1.name)
c1.power()
print(c1.pw)