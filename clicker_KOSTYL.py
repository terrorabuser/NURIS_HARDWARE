import pyautogui
import time
import json
import keyboard
import subprocess
from generate import *


# Файл для хранения разметки
COORDINATES_FILE = "clicks.json"

def record_clicks():
    """Режим записи координат кликов и ввода числа из переменной."""
    print("Режим разметки включён. Используйте клавиши:")
    print("- ЛКМ (Ctrl): добавляет клик ЛКМ")
    print("- ПКМ (Alt): добавляет клик ПКМ")
    print("- Ввод числа (N): добавляет число из переменной")
    print("Нажмите 'q', чтобы завершить.")
    spd, dir = gen()
    
    actions = []
    
    try:
        while True:
            # Ждем события
            x, y = pyautogui.position()
            
            # ЛКМ разметка
            if keyboard.is_pressed('ctrl'):
                print(f"ЛКМ добавлена: ({x}, {y})")
                actions.append({"action": "click", "button": "left", "position": (x, y)})
                time.sleep(0.5)
            
            # ПКМ разметка
            if keyboard.is_pressed('alt'):
                print(f"ПКМ добавлена: ({x}, {y})")
                actions.append({"action": "click", "button": "right", "position": (x, y)})
                time.sleep(0.5)
            
            # Ввод числа
            if keyboard.is_pressed('n'):
                # Пример переменной, число будет вставлено
                variable_number = int(spd)  # Переменная с числом
                print(f"Ввод числа {variable_number} добавлен.")
                actions.append({"action": "type", "number": variable_number})
                time.sleep(0.5)
                
            if keyboard.is_pressed('m'):
                # Пример переменной, число будет вставлено
                variable_number = int(dir)  # Переменная с числом
                print(f"Ввод числа {variable_number} добавлен.")
                actions.append({"action": "type", "number": variable_number})
                time.sleep(0.5)
                
            if keyboard.is_pressed('b'):
                print("Добавлен макрос для Backspace.")
                actions.append({"action": "backspace"})
                time.sleep(0.5)
            
            # Выход из режима разметки
            if keyboard.is_pressed('q'):
                print("Запись завершена.")
                break
    except KeyboardInterrupt:
        print("Прерывание записи.")
    
    # Сохранить разметку в файл
    with open(COORDINATES_FILE, "w") as f:
        json.dump(actions, f)
    print(f"Разметка сохранена в файл {COORDINATES_FILE}.")

    
def open_program(path_to_program):
    """Открывает программу по указанному пути."""
    subprocess.Popen(path_to_program)
    time.sleep(5)  # Подождать, пока программа загрузится
    
    
def replay_clicks(delay=1):
    """Режим воспроизведения кликов и чисел."""
    try:
        # Загрузить разметку из файла
        with open(COORDINATES_FILE, "r") as f:
            actions = json.load(f)
    except FileNotFoundError:
        print(f"Файл {COORDINATES_FILE} не найден. Сначала выполните запись разметки.")
        return

    print("Воспроизведение началось. Нажмите 'q', чтобы остановить.")
    
    try:
        for action in actions:
            if keyboard.is_pressed('q'):
                print("Воспроизведение остановлено.")
                break
            
            if action["action"] == "click":
                x, y = action["position"]
                button = action["button"]
                pyautogui.click(x, y, button=button)
                print(f"Клик ({button.upper()}) по ({x}, {y})")
            
            elif action["action"] == "type":
                number = action["number"]
                print(f"Ввод числа: {number}")
                pyautogui.typewrite(str(number))
            
            time.sleep(delay)  # Задержка между действиями
    except KeyboardInterrupt:
        print("Воспроизведение прервано.")
        

if __name__ == "__main__":
    

    

    print("Выберите режим:")
    print("1: Разметка действий")
    print("2: Воспроизведение действий")
    mode = input("Введите 1 или 2: ")
    
    if mode == "1":
        open_program(r"C:\Workspace\FlamMap6\FlamMap6.exe")
        record_clicks()
    elif mode == "2":
        delay = float(input("Введите задержку между действиями (в секундах): "))
        open_program(r"C:\Workspace\FlamMap6\FlamMap6.exe")
        replay_clicks(delay=delay)
    else:
        print("Неверный выбор.")
