import pyautogui
import keyboard
import time
import json
import sys

# Путь к файлу для сохранения координат
coordinates_file = "coordinates.json"

# Словарь для хранения координат кнопок
button_coordinates = {}

# Переменная для подсчета кнопок
button_index = 1

# Функция для сохранения координат
def save_coordinates():
    global button_index
    if keyboard.is_pressed('alt'):  # Проверка, зажата ли клавиша Alt
        time.sleep(0.2)  # Небольшая задержка, чтобы избежать повторных срабатываний
        x, y = pyautogui.position()  # Получаем текущие координаты мыши
        button_coordinates[f"button_{button_index}"] = {"x": x, "y": y}
        print(f"Сохранены координаты {f'button_{button_index}'}: x={x}, y={y}")
        
        # Сохраняем данные в файл
        with open(coordinates_file, "w") as file:
            json.dump(button_coordinates, file, indent=4)
        
        button_index += 1  # Увеличиваем индекс для следующей кнопки

# Основной цикл
try:
    while True:
        save_coordinates()
        
        # Завершение программы по нажатию клавиши 'Esc'
        if keyboard.is_pressed('esc'):
            print("Завершаем программу...")
            break  # Выход из цикла и завершение программы
except KeyboardInterrupt:
    print("Программа была прервана пользователем.")
    sys.exit()