# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def opencv():
    img = cv2.imread("mta_phone_unknown_803B410099__2020-12-30-09-19-54.jpg", cv2.IMREAD_GRAYSCALE)
    # img_200x200 = cv2.resize(img, (200, 200))
    cv2.imshow("image", img)
    print("imshow")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    opencv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
