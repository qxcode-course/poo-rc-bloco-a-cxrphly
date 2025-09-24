class Car:
    def __init__(self):
        self.pas :int = 0
        self.km:int = 0
        self.pasMax:int = 2
        self.gas:int = 0
        self.maxGas:int = 100

    def enterCar(self) -> None:
        self.pas += 1
        if self.pas > self.pasMax:
            print("fail: limite de pessoas atingido")
            self.pas = self.pasMax
            return

    def leaveCar(self) -> None:
        self.pas -= 1
        if self.pas < 0:
            print("fail: nao ha ninguem no carro")
            self.pas = 0
            return
    
    def fuelGas(self, increment:int) -> None:
        self.gas += increment
        if self.gas >= self.maxGas:
            self.gas = self.maxGas

    def driveDistance(self, distance:int) -> None:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
            return
        elif self.gas == 0:
            print("fail: tanque vazio")
            return
        elif distance <= self.gas:
            self.km += distance
            self.gas -= distance
        else:
            driven = self.gas
            self.km += driven
            self.gas = 0
            print(f"fail: tanque vazio apos andar {driven} km")
    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
def main():
    car :Car = Car()
    while True:
        line :str = input()
        arg : list[str] = line.split(" ")
        print("$"+line)

        if arg[0] == "end":
            break
        if arg[0] == "show":
            print(car)
        if arg[0] == "enter":
            car.enterCar()
        if arg[0] == "leave":
            car.leaveCar()
        if arg[0] == "fuel":
            car.fuelGas(int(arg[1]))
        if arg[0] == "drive":
            car.driveDistance(int(arg[1]))

if __name__ == "__main__":
    main()