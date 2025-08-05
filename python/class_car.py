""" class_car.py """

class Car:
    
    def __init__(self):
        self.wheel_count = 4
        self.door_count = 2

    def start(self):
        print("started...")

    def drive(self):
        print("driving...")

    def stop(self):
        print("stopped...")


class ElectricCar(Car):

    def __init__(self):
        super().__init__()

    def introduce(self):
        print("I'm an electric car")

    def start(self):
        super().start()
        print("No sound...")


class CombustionEnginCar(Car):

    def __init__(self):
        super().__init__()

    def introduce(self):
        print("I'm an Combustion engin car")

    def start(self):
        super().start()
        print("vroooooom....")

ec = ElectricCar()
ec.introduce()
ec.start()
ec.drive()
ec.stop()

ec1 = ElectricCar()

# ElectricCar() 두번 호출 -> 각각 독립적인 인스턴스(객체) 생성
print(id(ec))   # 4304755680
print(id(ec1))  # 4304400976
print(ec is ec1) # False

# cc = CombustionEnginCar()
# cc.introduce()
# cc.start()
# cc.drive()
# cc.stop()