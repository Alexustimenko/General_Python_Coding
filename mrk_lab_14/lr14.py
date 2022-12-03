class Planes:
    def __init__(self,model,typeeng,price,flydist,fuelType):
        self.model =model
        self.typeeng=typeeng
        self.price=price
        self.flydist=flydist
        self.fuelType = fuelType
    def fly(self,distance):
        if distance =="Minsk":
            return "lets flyyyyyyyyyyyyyyyy"
        if distance =="Tokyo":
            return "some problems with booking"
        else:
            return "choose dest"
    def cost(self,cost):
        if cost==100:
            return "cheap"
        if cost==1000:
            return "expensive"
        else:
            return "impossible"
    def type(self,type):
        if type == "Boeing":
            return "have a good flight"
        if type=='airbus':
            return "good luck"
        else:
            return 'oh noooooooooooooooooooooo'
class samoliot(Planes):
    def __init__(self,model,typeeng,price,flydist,fuelType,pas,ticketpr):
        Planes.__init__(self,model,typeeng,price,flydist,fuelType)
        self.pas=pas
        self.ticketpr=ticketpr
    def __str__(self):
        return f"model = {self.model} tepeeng = {self.typeeng} price = {self.price} flydist = {self.flydist} fuelType = {self.fuelType} pas = {self.pas} ticketpr = {self.ticketpr}"
pl1=samoliot("boeing",'a332',1005874,6587774,"aaa254",225,140)
print(str(pl1))
print(pl1.fly("Minsk"))
print(pl1.cost(1000))
print(pl1.type("Boeing"))