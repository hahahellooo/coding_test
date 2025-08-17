from abc import ABC, abstractmethod

class Car(ABC):

    def start_engine(self):
        print("start...")

    # 직접 개체를 만들 수 없는 클래스
    # 자식 클래스에서 반드시 구현해야 하는 메서드를 정의 -> 자식 클래스에서 구현하지 않으면 에러
    @abstractmethod
    def turn_off_engine(self):
        raise NotImplementedError
    
# c = Car()

class Tesla(Car):
    def turn_off_engine(self):
        print("turning off...")

t = Tesla()
t.start_engine()
t.turn_off_engine()


# 추상 클래스(ABC 클래스)와 유사하게 어떤 속성이나 메서드를 반드시 가져야 한다는 규약
# 구현을 강제하지 않고 구조적 서브타이핑으로 동작
from typing import List, Protocol

# Item 타입으로 간주되려면 최소한 quantity와 price 속성을 가져야 함
class Item(Protocol):
    quantity: float
    price: float

class Product:
    def __init__(self, name:str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

class Stock:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

def calculate_total(items: List[Item]) -> float:
    return sum(([item.quantity * item.price for item in items]))

total = calculate_total([Product('A',10,150),Stock('B',5,250)])
print(total)
