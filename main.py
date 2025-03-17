print('Hello mars')

try:
    with open("C:\\Users\\이종엽\\Desktop\\mission_computer_main.log", 'r')as read_f:
    #비동기 처리
        read_lines = read_f.readlines()
    with open("C:\pythonproject\log_analysis.md", 'w', encoding="utf-8")as write_f:
        for Line in read_lines:
            Line = Line.strip()
            print(Line)
        write_f.writelines("""
                               #사고 원인 분석 보고서 
2023-08-27 11:35:00,INFO,Oxygen tank unstable.
2023-08-27 11:40:00,INFO,Oxygen tank explosion.
2023-08-27 12:00:00,INFO,Center and mission control systems powered down.
                               """
            )
except FileExistsError as e:
    print(f"파일을 찾을 수 없습니다 {e}")
except IOError as e: 
    print(f"입출력 오류 발생{e}")
except Exception as e:
    print(f"예상치 못한 오류 발생 {e}")
