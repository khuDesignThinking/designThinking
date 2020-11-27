from os import error
import wmi

def recent_blink(path:str):
    # read recent blink number in path csv file
    with open(path, "r") as f:
        data = f.read()
    string_blink_count = data.split(",")
    int_blink_count = [int(blink_data) for blink_data in string_blink_count]
    last_index = int_blink_count[-1]
    return last_index


def change_brightness(degree: int):
    # brightness degree is between 0-100, Int type.
    # raise change brightness
    assert type(degree) is int
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(degree, 0)
    return None


def update_bright(path: str):
    """
    경계값(threshold) 분당 눈 감기는 횟수
    0-4 : 40
    5-9 : 60
    10-14 : 80
    15 이상 : 100

    raise : read recent blink_count & update bright ness
    """
    blink_num = recent_blink(path)
    if 0 <= blink_num < 5:
        change_brightness(degree = 30)
    elif 5 <= blink_num < 10:
        change_brightness(degree = 40)
    elif 10 <= blink_num < 15:
        change_brightness(degree = 50)
    elif 15 <= blink_num:
        change_brightness(degree = 60)
    else:
        raise error(f"csv file value is not nomal {blink_num}")
    return None


def main():
    update_bright(path = "resource/data/count_blink.csv")

if __name__ == "__main__":
    main()
