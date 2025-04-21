import random  # 랜덤값 생성을 위해 random 모듈을 임포트합니다.

class DummySensor:
    def __init__(self):
        # 환경 값을 저장하는 딕셔너리입니다.
        self.env_values = {
            "mars_base_internal_temperature": None,       # 화성 기지 내부 온도 (섭씨 18~30도)
            "mars_base_external_temperature": None,       # 화성 기지 외부 온도 (섭씨 0~21도)
            "mars_base_internal_humidity": None,          # 화성 기지 내부 습도 (50~60%)
            "mars_base_external_illuminance": None,       # 화성 기지 외부 광량 (500~715 W/m2)
            "mars_base_internal_co2": None,               # 화성 기지 내부 CO2 농도 (0.02~0.1%)
            "mars_base_internal_oxygen": None             # 화성 기지 내부 산소 농도 (4~7%)
        }

    def set_env(self):
        # 내부 온도: 18~30도
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)

        # 외부 온도: 0~21도
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)

        # 내부 습도: 50~60%
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)

        # 외부 광량: 500~715 W/m^2
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)

        # 내부 이산화탄소 농도: 0.02~0.1%
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 4)

        # 내부 산소 농도: 4~7%
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        # 현재 환경 값을 반환합니다.
        return self.env_values


# DummySensor 클래스 인스턴스를 생성합니다.
ds = DummySensor()

# 환경 값을 랜덤으로 설정합니다.
ds.set_env()

# 설정된 환경 값을 출력하여 확인합니다.
env_data = ds.get_env()
print("현재 센서 측정값:")
for key, value in env_data.items():
    print(f"{key}: {value}")
