import pyautogui
import time
import json
import keyboard
import pygetwindow as gw
import subprocess


# Файл для хранения разметки
COORDINATES_FILE = "clicks.json"

def record_clicks():
    """Режим записи координат кликов."""
    print("Режим разметки включён. Кликайте на экране. Нажмите 'q', чтобы завершить.")
    clicks = []
    
    try:
        while True:
            # Ждем клика мыши
            x, y = pyautogui.position()
            if keyboard.is_pressed('ctrl'):
                print(f"Координата добавлена: ({x}, {y})")
                clicks.append((x, y))
                time.sleep(0.5)  # Задержка, чтобы избежать двойного срабатывания
            
            # Выход из режима разметки
            if keyboard.is_pressed('q'):
                print("Запись завершена.")
                break
    except KeyboardInterrupt:
        print("Прерывание записи.")
    
    # Сохранить клики в файл
    with open(COORDINATES_FILE, "w") as f:
        json.dump(clicks, f)
    print(f"Координаты сохранены в файл {COORDINATES_FILE}.")
    
    
def open_program(path_to_program, window_title_contains=None):
    """
    Открывает программу по указанному пути и разворачивает её на весь экран.
    
    :param path_to_program: Путь к исполняемому файлу программы.
    :param window_title_contains: Строка, по которой можно найти окно программы.
                                  Если None, окно не будет развернуто.
    """
    # Запускаем программу
    subprocess.Popen(path_to_program)
    time.sleep(5)  # Подождать, пока программа загрузится

    if window_title_contains:
        # Ищем окно программы
        windows = gw.getWindowsWithTitle(window_title_contains)
        if windows:
            # Берем первое подходящее окно и разворачиваем
            window = windows[0]
            window.maximize()
            print(f"Окно '{window_title_contains}' развернуто на весь экран.")
        else:
            print(f"Окно с заголовком, содержащим '{window_title_contains}', не найдено.")
    
    
    
def replay_clicks(delay=1):
    """Режим воспроизведения кликов."""
    try:
        # Загрузить координаты из файла
        with open(COORDINATES_FILE, "r") as f:
            clicks = json.load(f)
    except FileNotFoundError:
        print(f"Файл {COORDINATES_FILE} не найден. Сначала выполните запись кликов.")
        return

    print("Воспроизведение началось. Нажмите 'q', чтобы остановить.")
    
    try:
        for x, y in clicks:
            if keyboard.is_pressed('q'):
                print("Воспроизведение остановлено.")
                break
            pyautogui.click(x, y)
            print(f"Клик по ({x}, {y})")
            time.sleep(delay)  # Задержка между кликами
    except KeyboardInterrupt:
        print("Воспроизведение прервано.")

if __name__ == "__main__":
    print("Выберите режим:")
    print("1: Разметка кликов")
    print("2: Воспроизведение кликов")
    mode = input("Введите 1 или 2: ")
    
    if mode == "1":
        record_clicks()
    elif mode == "2":
        delay = float(input("Введите задержку между кликами (в секундах): "))
        open_program(r"C:\Workspace\FlamMap6\FlamMap6.exe")
        replay_clicks(delay=delay)
    else:
        print("Неверный выбор.")
