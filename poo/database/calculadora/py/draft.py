class Calculator:
        def __init__(self):
            self.battery:int = 0
            self.batteryMax:int = 0
            self.display:float = 0
        def setBatteryMax(self, max:int):
            self.batteryMax = max
            self.battery = 0
        def charge(self, amount:int):
            self.battery += amount
            if self.battery > self.batteryMax:
                    self.battery = self.batteryMax
        def funcSum(self, a:int , b:int):
            if self.battery == 0:
                 print("fail: bateria insuficiente")
            else:
                self.battery -= 1
                self.display = a + b 
        def funcDiv(self, a:int, b:int):
            if self.battery == 0:
                 print("fail: bateria insuficiente")
            elif b == 0:
                print("fail: divisao por zero")
                self.battery -= 1
            else:
                self.battery -= 1
                self.display = a / b 
        def __str__(self) -> str:
            return f"display = {self.display:.2f}, battery = {self.battery}"
        
def main():
    calc:Calculator = Calculator()
    while True:
        line : str= input()
        arg:list[str] = line.split(" ")
        print("$"+line)
        if arg[0] == "end":
            break
        elif arg[0] == "show":
            print(calc)
        elif arg[0] == "init":
            calc.setBatteryMax(int(arg[1]))
        elif arg[0] == "charge":
            calc.charge(int(arg[1]))
        elif arg[0] == "sum":
            calc.funcSum(int(arg[1]), int(arg[2]))
        elif arg[0] == "div":
                calc.funcDiv(int(arg[1]), int(arg[2]))
        else:
            print("comando nao encontrado")

if __name__ == "__main__":
    main()