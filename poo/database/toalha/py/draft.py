class Towel:
    def __init__ (self, color:str, size:str):
        self.color = color
        self.size = size
        self.wetness = 0
        
    def getMaxWetness(self) -> int: 
        match self.size:
            case "P":
                return 10
            case "M":
                return 20
            case "G":
                return 30
            case _:
                return 0
    
    def dry(self, amount:int)-> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def show(self) -> None:
        print(self)
        
    def __str__(self) -> str:
        return f"{self.color} {self.size} {self.wetness}"


towel = Towel("Azul", "P")
towel.show()
towel.dry(5)
towel.show()  # Azul P 5
print(towel.isDry()) # False
towel.dry(5)
towel.show()  # Azul P 10
towel.dry(5) # msg: toalha encharcada
towel.show()  # Azul P 10

towel.wringOut()
towel.show()  # Azul P 0

towel = Towel("Verde", "G")
print(towel.isDry()) # True
towel.dry(30)
towel.show()  # Verde G 30
print(towel.isDry()) # False
towel.dry(1)  # msg: toalha encharcada