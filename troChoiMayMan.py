import random

class Game:
    def __init__(self,type="xúc xắc"):
        self.type = type
        self.scoreList = []
    
    @property
    def score(self):
        if self.type == "xúc xắc":
            return random.randint(1,6)
        elif self.type == "đồng xu":
            return random.randint(0,1)
        
    @property
    def quantity(self):
        return len(self.scoreList)
    
    @quantity.setter
    def quantity(self,newQuantity):
        for i in range(newQuantity):
            self.scoreList.append(self.score)

    @quantity.deleter
    def quantity(self):
        self.scoreList = []
    
    @property
    def totalScore(self):
        sum = 0
        for i in self.scoreList:
            sum +=i 

        return sum

    def play(self,quantity= 0):
        del self.quantity
        self.quantity = quantity

        print(f"Điểm {self.quantity} lần gieo {self.type}: {self.scoreList}")
        print(f"Tổng điểm {self.type}: {self.totalScore}")


game1 = Game("đồng xu")
game1.play(quantity=5)

game2 = Game()
game1.play(quantity=3)
    