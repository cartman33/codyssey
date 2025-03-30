import csv
#csv import

try:
    with open("D:\\Python project\\codyssey\\day3\\Mars_Base_Inventory_List.csv", 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            #1번 문제 Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력한다.
            
except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")
except IOError as e:
    print(f"입출력 오류 발생: {e}")    
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")
    
try:
    with open("D:\\Python project\\codyssey\\day3\\Mars_Base_Inventory_List.csv", 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        inventory_list = list(reader) 
        print("\n리스트로 변환")
        print(inventory_list) 
        #2번문제 Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환한다.  

except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")
    inventory_list = []  # 예외 발생 시 빈 리스트 할당
except IOError as e:
    print(f"입출력 오류 발생: {e}")
    inventory_list = []  # 예외 발생 시 빈 리스트 할당
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")
    inventory_list = []  # 예외 발생 시 빈 리스트 할당
    
try:
    if not inventory_list:
        raise ValueError("CSV 파일이 비어 있습니다.")  # 빈 파일 예외 처리
    
    header = inventory_list[0]  # 헤더 (컬럼명)
    data = inventory_list[1:]  # 데이터 부분

    # "Flammability" 컬럼의 인덱스 찾기
    flammability_index = header.index("Flammability")  # "Flammability" 컬럼이 없으면 IndexError 발생

    # 인화성을 높은거부터 낮은거로 정렬 (숫자로 변환 후 정렬)
    sorted_data = sorted(data, key=lambda x: float(x[flammability_index]), reverse=True)

    # 정렬된 리스트
    sorted_inventory = [header] + sorted_data

    print("\n정렬 완료")
    for row in sorted_inventory:
        print(row)

except ValueError as e:
    print(f"데이터 오류 발생: {e}")
    sorted_inventory = []
except IndexError as e:
    print(f"인덱스 오류 발생 (Flammability 컬럼이 없을 가능성 있음): {e}")
    sorted_inventory = []
except IOError as e:
    print(f"입출력 오류 발생: {e}")
    sorted_inventory = []
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")
    sorted_inventory = []
    
#3번 문제 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다. 
#4번 문제 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장한다. 
try:
    if not sorted_inventory:
        raise ValueError("정렬된 데이터가 없습니다.")  # 정렬된 데이터가 없을 경우 예외 처리
    
    #가연성 지수가 0.7 이상인 데이터 필터링
    filtered_data = [row for row in sorted_data if float(row[flammability_index]) >= 0.7]

    #헤더 포함된 최종 리스트
    filtered_inventory = [header] + filtered_data

    #필터링된 데이터를 출력
    print("\n가연성 0.7 이상")
    for row in filtered_inventory:
        print(row)

    # 필터링된 데이터를 CSV 파일로 저장
    danger_csv_path = "D:\\Python project\\codyssey\\day3\\Mars_Base_Inventory_danger.csv"
    with open(danger_csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_inventory)

    print(f"저장 완료")

except ValueError as e:
    print(f"데이터 오류 발생: {e}")
except IndexError as e:
    print(f"인덱스 오류 발생 (Flammability 컬럼이 없을 가능성 있음): {e}")
except IOError as e:
    print(f"입출력 오류 발생: {e}")
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")