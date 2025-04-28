import time

class DummySensor:
    def get_mars_base_internal_temperature(self):
        return 22.5

    def get_mars_base_external_temperature(self):
        return -55.0

    def get_mars_base_internal_humidity(self):
        return 45.0

    def get_mars_base_external_illuminance(self):
        return 12000

    def get_mars_base_internal_co2(self):
        return 400

    def get_mars_base_internal_oxygen(self):
        return 21.0

# MissionComputer 클래스 정의
class MissionComputer:
    def __init__(self):
        # 화성 기지 환경 정보를 담을 env_values 딕셔너리 생성
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }
        # DummySensor 인스턴스를 ds라는 이름으로 생성
        self.ds = DummySensor()

    def get_sensor_data(self):
        # 무한 반복하여 5초마다 센서 데이터를 갱신하고 출력
        while True:
            # 센서로부터 데이터 읽어오기
            self.env_values['mars_base_internal_temperature'] = self.ds.get_mars_base_internal_temperature()
            self.env_values['mars_base_external_temperature'] = self.ds.get_mars_base_external_temperature()
            self.env_values['mars_base_internal_humidity'] = self.ds.get_mars_base_internal_humidity()
            self.env_values['mars_base_external_illuminance'] = self.ds.get_mars_base_external_illuminance()
            self.env_values['mars_base_internal_co2'] = self.ds.get_mars_base_internal_co2()
            self.env_values['mars_base_internal_oxygen'] = self.ds.get_mars_base_internal_oxygen()

            # JSON처럼 보이게 직접 출력 (json 모듈 없이)
            print('{')
            for key, value in self.env_values.items():
                # 키와 값 출력. 문자열은 작은따옴표 사용, float은 소수점 1자리까지만 표현
                if isinstance(value, float):
                    print('    \'{0}\': {1:.1f},'.format(key, value))
                else:
                    print('    \'{0}\': {1},'.format(key, value))
            print('}')

            # 5초 대기
            time.sleep(5)

# MissionComputer 클래스를 RunComputer 인스턴스로 생성
RunComputer = MissionComputer()

# get_sensor_data 메소드 호출하여 지속적으로 데이터 출력
RunComputer.get_sensor_data()
