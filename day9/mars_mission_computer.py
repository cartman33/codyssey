import os  # 운영체제 정보 및 시스템 호출을 위한 모듈
import platform  # 시스템 정보(프로세서, 버전 등) 획득을 위한 모듈
import json  # JSON 형식의 문자열 출력을 위한 모듈
import time  # 주기적 실행을 위한 시간 지연 모듈
import threading  # 멀티스레드를 위한 모듈
import multiprocessing  # 멀티프로세스를 위한 모듈
import random  # 센서 데이터 시뮬레이션을 위한 난수 생성 모듈


class MissionComputer:
    """
    우주선 미션 컴퓨터의 정보, 부하, 센서 데이터를
    조회하여 주기적으로 출력하는 클래스
    """

    def get_mission_computer_info(self):
        """
        시스템(OS, 프로세서, 메모리 등) 정보를
        20초마다 JSON 형식으로 출력
        """
        while True:
            # 운영체제 이름
            os_name = os.name
            # 운영체제 버전
            os_version = platform.version()
            # 프로세서 종류
            cpu_type = platform.processor()
            # CPU 코어 수
            cpu_cores = os.cpu_count()

            # 물리 메모리 크기 조회 (POSIX 지원 환경)
            try:
                page_size = os.sysconf('SC_PAGE_SIZE')
                phys_pages = os.sysconf('SC_PHYS_PAGES')
                memory_bytes = page_size * phys_pages
            except (AttributeError, ValueError):
                # 정보 획득 실패 시 'N/A'로 표시
                memory_bytes = 'N/A'

            # 딕셔너리에 시스템 정보 저장
            info = {
                'os': os_name,
                'os_version': os_version,
                'cpu_type': cpu_type,
                'cpu_cores': cpu_cores,
                'memory_bytes': memory_bytes,
            }

            # JSON 문자열로 변환 후 출력
            print(json.dumps({'computer_info': info}))
            # 20초 대기
            time.sleep(20)

    def get_mission_computer_load(self):
        """
        시스템 부하(CPU load average 등)을
        20초마다 JSON 형식으로 출력
        """
        while True:
            # 1분 평균 부하 조회 (Unix-like 환경)
            try:
                load1, load5, load15 = os.getloadavg()
            except (AttributeError, OSError):
                load1 = load5 = load15 = 'N/A'

            # 부하 정보 딕셔너리 생성
            load = {
                'load_avg_1min': load1,
                'load_avg_5min': load5,
                'load_avg_15min': load15,
            }

            # JSON 문자열로 변환 후 출력
            print(json.dumps({'computer_load': load}))
            # 20초 대기
            time.sleep(20)

    def get_sensor_data(self):
        """
        센서(온도, 압력, 습도) 데이터를
        5초마다 JSON 형식으로 출력
        """
        while True:
            # 임의의 센서 값 생성
            temperature = random.uniform(-20.0, 50.0)
            pressure = random.uniform(950.0, 1050.0)
            humidity = random.uniform(0.0, 100.0)

            # 센서 데이터 딕셔너리 생성
            data = {
                'temperature': temperature,
                'pressure': pressure,
                'humidity': humidity,
            }

            # JSON 문자열로 변환 후 출력
            print(json.dumps({'sensor_data': data}))
            # 5초 대기
            time.sleep(5)


if __name__ == '__main__':
    # --------------------------------------------
    # 1) 단일 인스턴스 멀티스레드 실행 예시
    # --------------------------------------------
    # MissionComputer 클래스 인스턴스 생성
    runComputer = MissionComputer()

    # 실행할 메서드를 스레드로 등록
    threads = []
    threads.append(threading.Thread(target=runComputer.get_mission_computer_info))
    threads.append(threading.Thread(target=runComputer.get_mission_computer_load))
    threads.append(threading.Thread(target=runComputer.get_sensor_data))

    # 데몬 스레드로 설정 후 시작
    for thread in threads:
        thread.daemon = True
        thread.start()

    # --------------------------------------------
    # 2) 세 개의 인스턴스를 멀티프로세스로 실행
    # --------------------------------------------
    # 인스턴스 3개 생성
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    # 각 인스턴스에서 서로 다른 메서드를 프로세스로 실행
    processes = []
    processes.append(multiprocessing.Process(
        target=runComputer1.get_mission_computer_info
    ))
    processes.append(multiprocessing.Process(
        target=runComputer2.get_mission_computer_load
    ))
    processes.append(multiprocessing.Process(
        target=runComputer3.get_sensor_data
    ))

    # 프로세스 시작
    for process in processes:
        process.start()

    # (참고) 메인 프로세스에서 이후 쿠드가 더 필요하다면 수행 가능
    # 무한 루프에 의해 프로세스가 중단되지 않으므로 join 호출 시 블로킹 됨
    for process in processes:
        process.join()
