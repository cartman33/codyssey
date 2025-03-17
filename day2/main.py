import json
#json 파일로 저장하기 위해 모듈 추가 

try:
    with open('D:\Python project\day2\mission_computer_main.log', 'r')as f:
        data = [line.strip().split(",",2) for line in f]
        #with와 split을 이용해 파일을 읽고, 
        #콤마를 기준으로 내용 분류 및 리스트 객체로 전환
        print(data)
        #전환된 리스트 객체 화면에 출력
        #파일 읽기 완료 
except FileExistsError as e:
    print(f"파일을 찾을 수 없습니다 {e}")
except IOError as e:
    print(f"입출력 오류 발생{e}")    
except Exception as e:
    print(f"예상치 못한 오류 발생 {e}")

try:
    data.sort(reverse=True)
    #sort reverse를 통해 역순 정렬
    #역순 정렬 완료
    
except Exception as e:
    print(f"데이터 정렬 중 오류 발생: {e}")

try:
    dict = [{"time": entry[0], "type": entry[1], "message": entry[2]} for entry in data]
    #dict로 변환
except IndexError as e:
    print(f"데이터 변환 중 오류 발생 (리스트 인덱스 오류): {e}")
except Exception as e:
    print(f"데이터 변환 중 알 수 없는 오류 발생: {e}")


try:
    json_file_path = r'D:\Python project\day2\mission_computer_main.json'  
    # 저장할 파일 경로
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(dict, json_file, indent=4, ensure_ascii=False)
        #json 성공시 
except FileNotFoundError:
    print(f"JSON 저장 경로 오류: {json_file_path}")
except PermissionError:
    print(f"JSON 파일 저장 권한이 없습니다: {json_file_path}")
except Exception as e:
    print(f"JSON 저장 중 알 수 없는 오류 발생: {e}")    
    

#mission_coputer_main.json을 지우고 다시 실행하면 json 파일 생성됨 
#실행시 json 파일 생성되는게 보고싶다면 지우고 다시 실행해볼 것 