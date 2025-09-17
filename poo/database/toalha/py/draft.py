class Towel:
    def __init__(self, color:str ,size:str):
        self.color:str = color
        self.size:str = size
        self.wetness:int = 0
    def __str__(self)->str:
        return f"{self.color}:{self.size}:{self.wetness}"
colorInput = input()
sizeInput = input()

minha:Towel = Towel(colorInput,sizeInput)

print(f"{minha}")


