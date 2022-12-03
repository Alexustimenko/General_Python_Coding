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