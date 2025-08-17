# 객체를 직렬화하고 역직렬화하는 표준 모듈
# 파이썬 전용으로 다른 언어와 호환 불가
import pickle
data = {"name": "Tesla", "battery": 75, "colors": ["white", "black"]}

with open("car.pkl", "wb") as f:
    pickle.dump(data, f)

with open("car.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)