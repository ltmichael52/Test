# class MayTinh:
#     brand = "DELL"

#     def __init__(self,ram1, boNho1):
#         self.ram = ram1
#         self.boNho = boNho1

    
# mayTinh1 = MayTinh(16,256)
# mayTinh2 = MayTinh(32,1024)
# mayTinh1.brand = "Asus"

# print("Hãng máy tính 1: ",mayTinh1.brand)
# print("Hãng của class Máy tính: ",MayTinh.brand)

# print("Ram máy tính 1: ",mayTinh1.ram)
# print("Ram máy tính 2: ",mayTinh2.ram)

# mayTinh1.giaTien = 1000
# print("Máy tính 1 giá tiền: ",mayTinh1.giaTien)

#Ctr + /

class HocSinh:
    soLuong = 0
    students = []

    def __init__(self,ten,toan,van,anh):
        self.ten = ten
        self.toan = toan
        self.van = van
        self.anh = anh
        HocSinh.soLuong +=1
        HocSinh.students.append(self)

    @classmethod
    def soLuongHocSinh(cls):
        return cls.soLuong
    
    @classmethod
    def danhSachHocSinh(cls):
        return cls.students
    
    @classmethod
    def diemTrungBinhCaLop(cls):
        total = 0
        for std in cls.students:
            total += std.averageScore()
        
        return total/len(cls.students)

    @staticmethod
    def tenTruong():
        return "Chu Văn An"

    def showInfo(self):
        print("Tên học sinh: ",self.ten)
    
    def averageScore(self):
        return (self.toan+self.van+self.anh)/3


hs1 = HocSinh("A",9,8,7)
hs2 = HocSinh("B",6,5,7)
soLuongHS = HocSinh.soLuongHocSinh()

print("Số lượng học sinh trong lớp: ",soLuongHS)
hs1.showInfo()

print("Tên trường: ",HocSinh.tenTruong())
print("Danh sách học sinh: ",HocSinh.danhSachHocSinh())

print("Điểm trung bình của cả lớp: ",HocSinh.diemTrungBinhCaLop())