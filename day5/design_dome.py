import numpy as np
import os

# design_dome.py 기준으로 문제5 폴더 경로 설정
base_path = os.path.join(os.path.dirname(__file__), "문제5")

def load_csv_files(base_path, files):
    arr_list = []
    for i, file in enumerate(files):
        path = os.path.join(base_path, file)
        try:
            data = np.loadtxt(path, delimiter=',', dtype=object, encoding='utf-8-sig')
            print(f"arr{i + 1} type : {type(data)}")
            arr_list.append(data)
        except Exception as e:
            print(f"Error occurred while loading {file}: {e}")
    return arr_list

def calculate_average_strength(parts):
    data = parts[1:]  # 헤더 제외
    unique_parts = np.unique(data[:, 0])
    result = [['parts', 'avg_strength']]

    for part in unique_parts:
        mask = data[:, 0] == part
        matched_rows = data[mask]

        strengths = matched_rows[:, 1].astype(float)
        avg_strength = np.mean(strengths)

        result.append([part, str(round(avg_strength, 2))])

    return np.array(result)

def filter_and_save_result(result_array, output_path):
    try:
        data_only = result_array[1:]  # 헤더 제외
        avg_values = data_only[:, 1].astype(float)
        mask = avg_values < 50
        filtered_data = data_only[mask]

        final_result = np.vstack([result_array[0], filtered_data])
        np.savetxt(output_path, final_result, fmt="%s", delimiter=",")
        print(f"CSV 저장 완료: {output_path}")
    except Exception as e:
        print(f"Error occurred while saving {output_path}: {e}")

def main():
    files = [
        "mars_base_main_parts-001.csv",
        "mars_base_main_parts-002.csv",
        "mars_base_main_parts-003.csv"
    ]

    arr_list = load_csv_files(base_path, files)

    if not arr_list:
        print("파일 로드 실패로 프로그램 종료.")
        return

    # 첫 배열은 헤더 포함, 나머지는 헤더 제외하여 병합
    parts = np.vstack([arr_list[0]] + [arr[1:] for arr in arr_list[1:]])

    result_array = calculate_average_strength(parts)
    
    output_path = os.path.join(os.path.dirname(__file__), "parts_to_work_on.csv")
    filter_and_save_result(result_array, output_path)
if __name__ == "__main__":
    main()
