import pyautogui
import time
import json
import keyboard
import subprocess
from generate import *

# Файл для хранения разметки
COORDINATES_FILE = "clicks.json"

def record_clicks(spd, dir):
    """Режим записи координат кликов и ввода строки из переменной."""
    print("Режим разметки включён. Используйте клавиши:")
    print("- ЛКМ (Ctrl): добавляет клик ЛКМ")
    print("- ПКМ (Alt): добавляет клик ПКМ")
    print("- Ввод строки (N): добавляет строку spd")
    print("- Ввод строки (M): добавляет строку dir")
    print("- Ввод строки (B): BACKSPACE")
    print("Нажмите 'q', чтобы завершить.")
    
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
            
            # Ввод строки
            if keyboard.is_pressed('n'):
                # Пример строки, будет вставлена переменная spd
                variable_string = str(spd)  # Преобразуем переменную в строку
                print(f"Ввод строки: {variable_string}")
                actions.append({"action": "type", "string": variable_string})
                time.sleep(0.5)
                
            if keyboard.is_pressed('v'):
                # Пример строки, будет вставлена переменная с путем
                variable_string = r"D:\coding\NURIS_HARDWARE\not_csv"  # Строка пути
                print(f"Ввод строки: {variable_string}")
                actions.append({"action": "type", "string": variable_string})
                time.sleep(0.5)
                
            if keyboard.is_pressed('m'):
                # Пример строки, будет вставлена переменная dir
                variable_string = str(dir)  # Преобразуем переменную в строку
                print(f"Ввод строки: {variable_string}")
                actions.append({"action": "type", "string": variable_string})
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
    """Режим воспроизведения кликов и строк."""
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
                string_value = action["string"]
                print(f"Ввод строки: {string_value}")
                pyautogui.typewrite(string_value)
            
            time.sleep(delay)  # Задержка между действиями
    except KeyboardInterrupt:
        print("Воспроизведение прервано.")
        

if __name__ == "__main__":
    spd, dir = gen()

    print("Выберите режим:")
    print("1: Разметка действий")
    print("2: Воспроизведение действий")
    mode = input("Введите 1 или 2: ")
    
    if mode == "1":
        open_program(r"C:\Workspace\FlamMap6\FlamMap6.exe")
        record_clicks(spd, dir)
    elif mode == "2":
        delay = float(input("Введите задержку между действиями (в секундах): "))
        open_program(r"C:\Workspace\FlamMap6\FlamMap6.exe")
        replay_clicks(delay=delay)
    else:
        print("Неверный выбор.")
