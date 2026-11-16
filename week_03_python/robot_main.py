from robot_utils import tinh_cv


if __name__ == "__main__":
    r = float(input("Nhap ban kinh: "))
    result = tinh_cv(r)
    print("Chu vi la:", result)
