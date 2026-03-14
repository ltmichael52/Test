import math

class hinhTron:
    def __init__(self,r=0):
        self.banKinh = r
        self.PI = 3.14
    
    @property
    def dienTich(self):
        return self.banKinh*self.banKinh * self.PI

    @dienTich.setter
    def dienTich(self,dienTichMoi):
        self.banKinh = math.sqrt(dienTichMoi/self.PI)

    @property
    def banKinhGetter(self):
        return self.banKinh

    @dienTich.deleter
    def dienTich(self):
        self.banKinh = None

circle = hinhTron(r=5)
print("Diện tích hình tròn: ",circle.dienTich)

print("Bán kính hiện tại: ",circle.banKinhGetter)

circle.dienTich = 50.24
print("Bán kính mới: ",circle.banKinhGetter)

del circle.dienTich
print("Bán kính hiện tại: ",circle.banKinhGetter)