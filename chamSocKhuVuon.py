class Game:
    tien = 10000
    soLuong = 0

    def __init__(self,ten):
        self.ten = ten
        self.nuoc = 0
        self.anhSang = 0
        Game.soLuong += 1
        Game.tien -= 200

    @property
    def tinhTrang(self):
        if self.nuoc == 0 and self.anhSang == 0:
            return "hạt mầm"
        elif self.nuoc == None and self.anhSang == None:
            return "đã bán"
        elif self.nuoc >0 and self.anhSang > 0 :
            return "sống"
        else:
            return "đã chết"
        
    def checkTinhTrang(self):
        if self.tinhTrang == "sống" or self.tinhTrang == "hạt mầm":
            return True
        else:
            return False
        
    @property
    def giaThanh(self):
        if self.nuoc == None and self.anhSang == None:
            return 0
        
        return max(0,self.nuoc+self.anhSang*10)
    
    @giaThanh.setter
    def giaThanh(self,value):
        nuoc , anhsang = value
        if self.checkTinhTrang():
            self.nuoc += nuoc
            self.anhSang += anhsang
    
    @giaThanh.deleter
    def giaThanh(self):
        Game.tien += self.giaThanh
        self.nuoc = None
        self.anhSang = None
    
    @staticmethod
    def chamCay():
        tenCay = input("Tên cây bạn muốn chăm là gì? ")
        for i in range(Game.soLuong):
            if game[i].ten == tenCay and game[i].checkTinhTrang():
                nuocTangThem = int(input("Bạn muốn tưới thêm bao nhiêu nước cho cây (ml)? "))
                anhSangTangThem = int(input("Bạn sẽ để cây ngoài trời mấy tiếng? "))
                game[i].giaThanh = (nuocTangThem, anhSangTangThem)
                print(game[i].getInfo())
                return True
        
        print("Cây không tồn tại hoặc không còn sống hoặc đã bán")
        return False

    @staticmethod
    def banCay():
        tenCay = input("Nhập tên cây cần bán: ")
        for i in range(Game.soLuong):
            if game[i].ten == tenCay and game[i].checkTinhTrang():
                del game[i].giaThanh
                return True
        
        print("Cây không tồn tại hoặc không còn sống hoặc đã bán")
        return False

    def getInfo(self):
        return f"Cây {self.ten} có tình trạng là {self.tinhTrang},chiều cao là {self.giaThanh} mm"

game = []
while True:
    print("Chọn một trong các tùy chọn sau:")
    print("1.Thêm cây mới")
    print("2.Chăm sóc cây")
    print("3.Bán cây")
    print("4.Xem danh sách cây")
    print("5. Thoát chương trình")
    print(f"Bạn đang có {Game.tien} đồng")
    choice = input("Nhập lựa chọn của bạn (1-5): ")
    if choice == "1":
        tenCay = input("Bạn muốn đặt tên cây là gì? ")
        cay = Game(tenCay)
        game.append(cay)
        print(f"Bạn đã thêm cây {tenCay} thành công")
    elif choice == "2":
        Game.chamCay()
    elif choice == "3":
        Game.banCay()
    elif choice == "4":
        for i in range(len(game)):
            print(f"{i+1}. {game[i].getInfo()}")
    elif choice == "5":
        break
    else:
        print("Lựa chọn không hợp lệ.Hãy chọn lại")
