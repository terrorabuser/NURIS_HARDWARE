# 1. перекинуть 2 файла из input_flammap в csv и переделать их в формат csv
# 2. переделать 7 файлов из папки not_csv закинуть в csv 
# 3. сделать зип файла 
# 4. удалить файлы из not_csv  и csv 
import os
import pyperclip
import pyautogui
import time
import keyboard

def write_via_clipboard(text):
        pyperclip.copy(text)  # Скопировать текст в буфер обмена
        pyautogui.hotkey('ctrl', 'v')  # Вставить текст через Ctrl+V
    
photo_path = os.path.normpath(r"C:\Users\Nikita\Desktop\flammap\files\Lassen Volcanic National Park.tif")

# import pyperclip

# pyperclip.copy('Test')  # Копировать текст
# print(pyperclip.paste())  # Проверить содержимое буфера обмена


import pyperclip
import keyboard
import time

# Функция для вставки текста из буфера обмена
def paste_text():
    text = pyperclip.paste()  # Получаем текст из буфера обмена
    keyboard.write(text)  # Вставляем текст с помощью библиотеки keyboard

# Копируем текст в буфер обмена
pyperclip.copy("Привет! Это тестовая строка для вставки.")

# Задержка перед вставкой
time.sleep(2)

# Вставляем текст
paste_text()


pyautogui.press('right')
time.sleep(5)
# write_via_clipboard(photo_path)