class Bike:
    def __init__(self,marka,speed,price,color):
        self.marka =marka
        self.speed=speed
        self.price=price
        self.color=color
    def model(self,model):
        if model=='aist':
            return "cool bike"
        if model=='delta':
            return "very cool bike"
        else:
            return "kolhoz"
    def skor(self,s):
        if s ==50:
            return "fast"
        if s == 150:
            return "very faaaaast"
        else:
            return "turtle"
    def cost(self,pr):
        if pr == 1000:
            return 'exp'
        if pr == 100000:
            return "very exp"
        else:
            return "unbeluevable"
class ship:
    def __init__(self,cost,type,eng,pas):
        self.cost = cost
        self.type=type
        self.eng=eng
        self.pas=pas
    def typeeee(self,t):
        if t=='cargo':
            return "no pass"
        if t=='pass':
            return "no cargo"
        else:
            return 'err'
    def costttttttttt(self,c):
        if c == 100:
            return 'not exp'
        if c ==1000:
            return 'exp'
        else:
            return "err"
    def pas(self,p):
        if p == 1085:
            return 'not big'
        if p == 1100000:
            return 'big'
        else:
            return 'err'
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
