import math

#날아가 버린 천장의 돔의 길이를 재어보니 10m가 나왔다.
#돔의 전체 면적을 구하는 식 sphere_area() 함수 
#함수는 파라메터로 지름(diameter)을 입력받게 구현

# 전역변수
material = None
diameter = 10 #돔길이 10
thickness = 1 #두께 기본값 1
area = None
weight = None

def sphere_area(diameter, material = "유리", thickness = 1):
    diameter *=100
    r = diameter / 2
    area = 2 * r**2 * 3.141592
    gravity = 3.73 / 9.807

    if material == "유리":
        weight = 2.4 * area * gravity / 1000 * thickness
    elif material == "알루미늄":
        weight = 2.7 * area * gravity / 1000 * thickness
    elif material == "탄소강":
        weight = 7.85 * area * gravity / 1000 * thickness
    else:
        print("해당 제질의 대한 정보는 없습니다.")
        return area, 0

    return area, weight 
    
def main():
    global diameter, material, area, weight, thickness
    while True:
        try:
            diameter = float(input("지름(미터 단위, 0 입력 시 종료): "))
            if diameter == 0.0: 
                return
        except ValueError:
            print("숫자를 입력해주세요\n")
            continue

        material = input("재질(유리/알루미늄/탄소강, 기본값: 유리): ")
        if material.strip() == "":
            material = "유리"

        thickness_input = input("두께(cm 단위, 기본값: 1): ")
        if thickness_input.strip() == "":
            thickness = 1
        else:
            try:
                thickness = float(thickness_input)
            except ValueError:
                print("두께는 숫자로 입력되어야 합니다. 기본값 1을 사용합니다.")
                thickness = 1

        area, weight = sphere_area(diameter, material, thickness)

        print(f"재질 =⇒ {material}, 지름 =⇒ {diameter}, 두께 =⇒ {thickness}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg\n")

if __name__ == "__main__":
    main()