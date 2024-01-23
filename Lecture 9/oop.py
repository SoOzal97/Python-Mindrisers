a=input("Ghar you want to know About:")
class House:
    window=15
    color='red'
    room=7
    door=3
    
     
    
    def ghar(self):
        print(f"About {a} Ghar:\n Color:{self.set_color}\n Window:{self.window}\n Room:{self.room}")
    def set_color(self,color):
        set.color= color

if a =='ram':
    ram = House()
    ram.set_color=('Green')
    ram.room=8
    # print(ram.color)
    ram.ghar()
elif a== 'shyam':
    shyam = House()
    shyam.ghar()
# shyam.color='Green'
# print(shyam.color, shyam.room)
