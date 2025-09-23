class Towel:
    def __init__ (self, color:str = "", size:str = ""):
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
        if self.wetness >= self.getMaxWetness(): # verifica a umidade, se maior que o maximo, imprime encharcada e atribui a umidade o valor maximo
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetness = 0
    def isDry(self) -> bool:
            if self.wetness == 0:
                return True
            else:
                return False
    def show(self) -> None:
        print(f"Cor: {self.color} Tamanho: {self.size} Umidade: {self.wetness}")
        
    def __str__(self) -> str:
        return f"Cor: {self.color} Tamanho: {self.size} Umidade: {self.wetness}"


def main():
    towel:Towel = Towel(size="", color="")
    while True:
        line = input()
        arg : list[str] = line.split(" ")

        if arg[0] == "end":
            break
        elif arg[0] == "criar":
            towel: Towel = Towel(color=arg[1], size=arg[2])
        elif arg[0] == "mostrar":
            towel.show()
        elif arg[0] == "seca":
            towel.isDry()
            print("sim" if towel.isDry() else "nao")
        elif arg[0] == "enxugar":
            amount:int = int(arg[1])
            towel.dry(amount)
        elif arg[0] == "torcer":
            towel.wringOut()
        else:
            print("comando nao encontrado")

main()