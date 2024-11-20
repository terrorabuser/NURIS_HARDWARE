import pyautogui
import time

# Запустите FlamMap
import subprocess

flammap_path = r"C:\Workspace\FlamMap6\FlamMap6.exe"
subprocess.Popen(flammap_path)
time.sleep(5)  # Подождите, пока программа запустится




pyautogui.doubleClick(x=589, y=388)

time.sleep(1)

file_path = r'Lassen Volcanic National Park.tif'
pyautogui.write(file_path)


print(pyautogui.position())