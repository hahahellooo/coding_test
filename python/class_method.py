class Car:

    def __init__(self, body_type):
        self.body_type = body_type
    
    def __repr__(self): # represent 방식을 선언
        return f"Car(body_type={self.body_type})"
    
    def set_body_type(self, body_type):
        self.body_type = body_type

    @classmethod
    def hyundai(cls):
        return cls(body_type="Sedan")
    
    @classmethod
    def kia(cls):
        return cls(body_type="SUV")

    @classmethod
    def benz(cls):
        return cls(body_type="Luxury")
    
c = Car(body_type="Sedan")
# print(c)
c.set_body_type(body_type="sport")
# print(c)
print(Car.hyundai())
print(Car.kia())
print(Car.benz())