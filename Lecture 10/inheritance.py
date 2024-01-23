class Human:
    age=0
class GrandFather(Human):
    def __init__(self):
      
       self.house=15
       print(f"I have {self.house} ghar")
class Mother(GrandFather):
    def __init__(self):
       print("I am Mother.")
    jewlary="gold,Diamond"
class Father(GrandFather):
    def __init__(self):
       super().__init__()
       self.house=9
       print(f"I have {self.house} house")
    def __eq__(self, obj):
        return self.age==obj.age
    car="Lambo,Ferrari,Toyata-Supra"
    Bike="Benali,Duke"
class Son(Father, Mother):

    # def __init__(self):
    #     print("I am Son.")
    gaming_console="PS5,Xbox"
    
sujal=Father()
Diya=Mother()
print(sujal==Diya)
# print(sujal.car)
# print(sujal.jewlary)
# print(sujal.gaming_console)
# print(sujal.house)
