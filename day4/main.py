material = 0
diameter = 10
thickness = 1
area = 0
weight = 0

def sphere_area(diameter, material = "유리", thickness = 1 ):

    diameter *= 100
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
    return area, weight 
    
def main():
    global diameter, material, area, weight
    while True:
        try:
            diameter = float(input("지름(미터 단위, 0 입력 시 종료): "))
            if diameter == 0.0: 
                return
        except ValueError:
            print("숫자를 입력해주세요\n")
            continue
        
        material = input("재질(유리/알루미늄/탄소강, 기본값: 유리): ")
        
        area, weight = sphere_area(diameter, material, thickness)

        print(f"재질 =⇒ {material}, 지름 =⇒ {diameter}, 두께 =⇒ {thickness}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg\n")

if __name__ == "__main__":
    main()4
    