from enum import Enum

class Car(Enum):
    HYUNDAI = 1
    KIA = 2
    TESLA = 3
    FORD = 4

print(Car.HYUNDAI)
print(Car.HYUNDAI.name)
print(Car.HYUNDAI.value)
print(type(Car.HYUNDAI))

for car in list(Car):
    print(f"{car.name}: {car.value}")

# 실전 예시
class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELED = "canceled"

def check_order(status: OrderStatus):
    if status == OrderStatus.PENDING:
        print("주문 대기 중...")
    elif status == OrderStatus.COMPLETED:
        print("주문 완료!")

check_order(OrderStatus.PENDING)