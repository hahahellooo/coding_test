class Car:
    brand = "Generic"

    def __init__(self, body_type):
        self.body_type = body_type

    # 인스턴스 메서드: 인스턴스 상태 사용
    def show_body_type(self):
        print(f"My body type is {self.body_type}")

    # 클래스 메서드: 클래스 속성 변경이나 새로운 인스턴스 생성
    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand
        print(f"The new brand is {cls.brand}")

    # 스태틱 메서드: T/F (클래스/인스턴스 상태와 무관하게 동작하는 유틸리티 함수 작성 시 적합)
    @staticmethod
    def is_luxury(body_type):
        return body_type.lower() in ['luxury', 'sports']
    
c1 = Car("SUV")
c1.show_body_type()
c1.change_brand("Hyundai")
print(Car.is_luxury("sports"))
print(Car.is_luxury("SUV"))