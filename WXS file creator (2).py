import random
from datetime import datetime, timedelta


def generate_value(current, change_range, min_value, max_value):
    """Функция для плавного изменения значения в заданных пределах."""
    new_value = current + random.uniform(-change_range, change_range)
    return max(min_value, min(max_value, new_value))


def generate_weather_data(start_date, hours=24):
    """Генерирует 24 часа погодных данных с возможностью целого дня аномальных условий."""
    weather_data = []
    current_time = start_date

    # Начальные значения для параметров
    temp = random.randint(50, 70)  # Температура в Фаренгейтах
    rh = random.randint(30, 60)  # Относительная влажность в %
    hrly_pcp = 0  # Осадки
    wind_spd = random.randint(5, 10)  # Скорость ветра в mph
    wind_dir = random.randint(0, 360)  # Направление ветра в градусах
    cloud_cov = random.randint(20, 80)  # Облачность в %

    # Вероятности для аномальных погодных условий на целый день
    anomalies = {
        "hot_dry": 0.15,  # Жаркий и сухой день
        "hot_humid": 0.1,  # Жаркий и влажный день
        "cold_rainy": 0.1,  # Холодный и дождливый день
        "windy": 0.05,  # Ветреный день
        "cloudy": 0.1  # Облачный день
    }

    # Выбор аномального дня или обычного
    anomaly = None
    for anomaly_type, probability in anomalies.items():
        if random.random() < probability:
            anomaly = anomaly_type
            break

    # Функция для применения аномалии к погоде на целый день
    def apply_daily_anomaly(temp, rh, wind_spd, anomaly):
        if anomaly == "hot_dry":
            temp = random.uniform(85, 100)  # Высокая температура
            rh = random.uniform(10, 20)  # Низкая влажность
        elif anomaly == "hot_humid":
            temp = random.uniform(85, 95)  # Высокая температура
            rh = random.uniform(60, 80)  # Высокая влажность
        elif anomaly == "cold_rainy":
            temp = random.uniform(30, 50)  # Низкая температура
            rh = random.uniform(80, 100)  # Высокая влажность
            wind_spd = random.uniform(5, 15)
        elif anomaly == "windy":
            wind_spd = random.uniform(15, 20)  # Сильный ветер
        elif anomaly == "cloudy":
            cloud_cov = random.uniform(70, 100)  # Плотная облачность
        return temp, rh, wind_spd

    # Применение выбранной аномалии (если есть) для всех часов дня
    if anomaly:
        temp, rh, wind_spd = apply_daily_anomaly(temp, rh, wind_spd, anomaly)

    # Генерация данных для каждого часа
    for _ in range(hours):
        # Плавные переходы для аномальных или нормальных значений
        temp = generate_value(temp, 1, 30, 100)  # Температура
        rh = generate_value(rh, 3, 10, 100)  # Влажность
        wind_spd = generate_value(wind_spd, 2, 0, 20)  # Ветер
        wind_dir = (wind_dir + random.randint(-10, 10)) % 360  # Направление ветра
        cloud_cov = generate_value(cloud_cov, 5, 0, 100) if anomaly != "cloudy" else cloud_cov

        # Формат строки для данных
        row = f"{current_time.year}\t{current_time.month:02}\t{current_time.day:02}\t{current_time.hour:02}00\t" \
              f"{int(temp)}\t{int(rh)}\t{hrly_pcp:.2f}\t{int(wind_spd)}\t{int(wind_dir)}\t{int(cloud_cov)}"
        weather_data.append(row)

        # Переход к следующему часу
        current_time += timedelta(hours=1)

    return weather_data


def create_wxs_file(file_name, start_date):
    """Создает файл WXS с 24 часами погодных данных."""
    header = [
        "RAWS_UNITS: English\n",
        "RAWS_ELEVATION: 0\n",
        "RAWS: 20\n",
        "Year  Mth  Day   Time    Temp     RH  HrlyPcp  WindSpd WindDir CloudCov\n"
    ]

    # Генерация данных
    weather_data = generate_weather_data(start_date, hours=24)

    # Запись данных в файл
    with open(file_name, 'w') as file:
        file.writelines(header + [line + "\n" for line in weather_data])


# Задание даты начала
start_date = datetime(2024, 10, 23, 0, 0)

# Путь к файлу
output_file_path = r'weather_wxs\Weather_1.wxs'

# Создание WXS файла
create_wxs_file(output_file_path, start_date)

# Создание WXS файла
create_wxs_file(output_file_path, start_date)
