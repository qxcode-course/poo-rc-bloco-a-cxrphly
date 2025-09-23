class Towel:
    def __init__ (self, color: str = "", size: str = ""):
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

    def dry (self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0
        
    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():
    towel: Towel = Towel("","")

    while True:
        line: str = input()
        arg : list[str] = line.split(" ")
        print("$" + line)
        if arg[0] == "end":
            break
        elif arg[0] == "criar":
            towel = Towel(color=arg[1], size=arg[2])
        elif arg[0] == "mostrar":
            print(towel)
        elif arg[0] == "seca":
            print("sim" if towel.isDry() else "nao")
        elif arg[0] == "enxugar":
            amount:int = int(arg[1])
            towel.dry(amount)
        elif arg[0] == "torcer":
            towel.wringOut()
        else:
            print("comando nao encontrado")

main()