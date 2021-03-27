import pyautogui
import time

choicevar = "y"

print("Are You Sure To Run This Virus? MAKER OF THIS SOFTWARE DOESN'T RESPONSE ANY DAMAGE!(Y/N)")
choice = input()
if choice == choicevar:
    pyautogui.click(500, 40)
    time.sleep(0.5)
    pyautogui.typewrite("asdhasuidhasuidhasduihasdiuasdiuhahsdiuhasdiuashdaish")
    pyautogui.tripleClick(30, 500)
    pyautogui.leftClick(63, 500)
else:
    print("GoodBye! Have a Nice Day!")
    exit()