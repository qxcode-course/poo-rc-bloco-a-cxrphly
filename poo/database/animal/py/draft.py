class Animal: 
    def __init__(self, species: str = "", sound: str = ""):
        self.species = species
        self.sound = sound
        self.age = 0

    def ageBy(self, increment:int) -> None:
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4

    def makeSound(self) -> str:
        match self.age:
            case 0:
                return f"---"
            case 4:
                return f"RIP"
            case _:
                return f"{self.sound}"
        return ""

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
def main():
    animal = Animal()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)
        if arg[0] == "end":
            break
        elif arg[0] == "init":
            animal : Animal = Animal(arg[1],arg[2])
        elif arg[0] == "show":
            print(animal)
        elif arg[0] == "grow":
            animal.ageBy(int(arg[1]))
        elif arg[0] == "noise":
            print(animal.makeSound())
        else:
           print("comando nao encontrado")

main()