#!/usr/bin/env python3

import os  # 운영체제 및 시스템 정보 접근을 위한 모듈
import platform  # 플랫폼 정보 제공 모듈
import time  # 시간 제어를 위한 모듈
import json  # JSON 포맷 출력을 위한 모듈


class DummySensor:
    """
    화성 기지 환경 데이터를 모사하는 더미 센서 클래스
    """
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


class MissionComputer:
    """
    미션 컴퓨터 시스템 정보 및 부하를 출력하는 클래스
    """
    def __init__(self):
        # 환경 값 저장용 딕셔너리 초기화
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }
        self.ds = DummySensor()

    def get_sensor_data(self):
        """
        5초 간격으로 센서 데이터를 읽어 JSON 형태로 출력
        """
        while True:
            self.env_values['mars_base_internal_temperature'] = (
                self.ds.get_mars_base_internal_temperature()
            )
            self.env_values['mars_base_external_temperature'] = (
                self.ds.get_mars_base_external_temperature()
            )
            self.env_values['mars_base_internal_humidity'] = (
                self.ds.get_mars_base_internal_humidity()
            )
            self.env_values['mars_base_external_illuminance'] = (
                self.ds.get_mars_base_external_illuminance()
            )
            self.env_values['mars_base_internal_co2'] = (
                self.ds.get_mars_base_internal_co2()
            )
            self.env_values['mars_base_internal_oxygen'] = (
                self.ds.get_mars_base_internal_oxygen()
            )

            print(json.dumps(self.env_values, indent=4))
            time.sleep(5)

    def get_mission_computer_info(self):
        """
        운영체제, 버전, CPU 타입, 코어 수, 총 메모리 크기를 수집하여 JSON 형식으로 출력
        """
        try:
            os_name = platform.system()
        except Exception:
            os_name = None
        try:
            os_version = platform.release()
        except Exception:
            os_version = None
        try:
            cpu_type = platform.processor() or None
        except Exception:
            cpu_type = None
        try:
            cpu_cores = os.cpu_count()
        except Exception:
            cpu_cores = None

        mem_total_bytes = None
        try:
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal:'):
                        parts = line.split()
                        if len(parts) >= 2:
                            mem_kb = int(parts[1])
                            mem_total_bytes = mem_kb * 1024
                        break
        except Exception:
            mem_total_bytes = None

        info = {
            'os_name': os_name,
            'os_version': os_version,
            'cpu_type': cpu_type,
            'cpu_cores': cpu_cores,
            'memory_total_bytes': mem_total_bytes
        }

        print(json.dumps(info, indent=4))

    def get_mission_computer_load(self):
        """
        CPU 및 메모리 실시간 사용률을 수집하여 JSON 형식으로 출력
        """
        # CPU 사용량 측정
        cpu_usage_percent = None
        try:
            def read_cpu_times():
                with open('/proc/stat', 'r') as f:
                    fields = f.readline().split()[1:]
                    return list(map(int, fields))

            cpu1 = read_cpu_times()
            total1 = sum(cpu1)
            idle1 = cpu1[3]
            time.sleep(0.1)
            cpu2 = read_cpu_times()
            total2 = sum(cpu2)
            idle2 = cpu2[3]

            diff_total = total2 - total1
            diff_idle = idle2 - idle1
            if diff_total > 0:
                cpu_usage_percent = (diff_total - diff_idle) / diff_total * 100
            else:
                cpu_usage_percent = 0.0
        except Exception:
            cpu_usage_percent = None

        # 메모리 사용량 측정
        mem_usage_percent = None
        try:
            mem_total = None
            mem_available = None
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal:'):
                        mem_total = int(line.split()[1])
                    elif line.startswith('MemAvailable:'):
                        mem_available = int(line.split()[1])
                    if mem_total is not None and mem_available is not None:
                        break
            if mem_total and mem_available is not None:
                mem_usage_percent = (mem_total - mem_available) / mem_total * 100
        except Exception:
            mem_usage_percent = None

        load = {
            'cpu_usage_percent': (
                round(cpu_usage_percent, 1)
                if isinstance(cpu_usage_percent, float)
                else None
            ),
            'memory_usage_percent': (
                round(mem_usage_percent, 1)
                if isinstance(mem_usage_percent, float)
                else None
            )
        }

        print(json.dumps(load, indent=4))


if __name__ == '__main__':
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
    # 센서 데이터 확인 시 아래 주석 해제
    # runComputer.get_sensor_data()
