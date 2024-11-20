import random
from datetime import datetime, timedelta
import os


def generate_fuel():
    def create_uniform_fms_file(filename, fm_1_hour, fm_10_hour, fm_100_hour, fm_1000_hour, herbaceous_fm, live_woody_fm):
        """
        Создаёт .fms файл, в котором значения влажности для всех строк одинаковы,
        а первый столбец содержит фиксированные номера моделей топлива.
        """
        model_ids = [0, 101, 102, 121, 122, 141, 142, 143, 144, 161, 162, 165,
                    181, 182, 183, 184, 185, 186, 187, 188]

        with open(filename, 'w') as f:
            for model_id in model_ids:
                f.write(
                    f"{model_id} {fm_1_hour} {fm_10_hour} {fm_100_hour} {herbaceous_fm} {live_woody_fm} {fm_1000_hour}\n")


    folder_path = "input_flammap"  # Папка для первого файла
    os.makedirs(folder_path, exist_ok=True)
    filename = rf"{folder_path}/generated_fuel_moisture_data_1.fms"
    create_uniform_fms_file(
        filename=filename,
        fm_1_hour=random.randint(1, 10),
        fm_10_hour=random.randint(10, 20),
        fm_100_hour=random.randint(20, 30),
        fm_1000_hour=random.randint(30, 40),
        herbaceous_fm=random.randint(50, 80),
        live_woody_fm=random.randint(90, 120)
    )
    print(f"Файл '{filename}' успешно создан")


def generate_weather():
    def generate_value(current, change_range, min_value, max_value):
        new_value = current + random.uniform(-change_range, change_range)
        return max(min_value, min(max_value, new_value))

    def generate_weather_data(start_date, hours=24):
        weather_data = []
        current_time = start_date

        temp = random.randint(50, 70)
        rh = random.randint(30, 60)
        wind_spd = random.randint(5, 10)
        wind_dir = random.randint(0, 360)
        cloud_cov = random.randint(20, 80)

        anomalies = {
            "hot_dry": 0.15,
            "hot_humid": 0.1,
            "cold_rainy": 0.1,
            "windy": 0.05,
            "cloudy": 0.1
        }

        anomaly = None
        for anomaly_type, probability in anomalies.items():
            if random.random() < probability:
                anomaly = anomaly_type
                break

        def apply_daily_anomaly(temp, rh, wind_spd, anomaly):
            if anomaly == "hot_dry":
                temp = random.uniform(85, 100)
                rh = random.uniform(10, 20)
            elif anomaly == "hot_humid":
                temp = random.uniform(85, 95)
                rh = random.uniform(60, 80)
            elif anomaly == "cold_rainy":
                temp = random.uniform(30, 50)
                rh = random.uniform(80, 100)
                wind_spd = random.uniform(5, 15)
            elif anomaly == "windy":
                wind_spd = random.uniform(15, 20)
            elif anomaly == "cloudy":
                cloud_cov = random.uniform(70, 100)
            return temp, rh, wind_spd

        if anomaly:
            temp, rh, wind_spd = apply_daily_anomaly(temp, rh, wind_spd, anomaly)

        wind_spd_values = []  # Список для сбора значений WindSpd
        wind_dir_values = []  # Список для сбора значений WindDir

        for _ in range(hours):
            temp = generate_value(temp, 1, 30, 100)
            rh = generate_value(rh, 3, 10, 100)
            wind_spd = generate_value(wind_spd, 2, 0, 20)
            wind_dir = (wind_dir + random.randint(-10, 10)) % 360
            cloud_cov = generate_value(cloud_cov, 5, 0, 100) if anomaly != "cloudy" else cloud_cov

            wind_spd_values.append(wind_spd)
            wind_dir_values.append(wind_dir)

            row = f"{current_time.year}\t{current_time.month:02}\t{current_time.day:02}\t{current_time.hour:02}00\t" \
                f"{int(temp)}\t{int(rh)}\t{0:.2f}\t{int(wind_spd)}\t{int(wind_dir)}\t{int(cloud_cov)}"
            weather_data.append(row)

            current_time += timedelta(hours=1)

        return weather_data, wind_spd_values, wind_dir_values

    def create_wxs_file(file_name, start_date):
        header = [
            "RAWS_UNITS: English\n",
            "RAWS_ELEVATION: 0\n",
            "RAWS: 20\n",
            "Year  Mth  Day   Time    Temp     RH  HrlyPcp  WindSpd WindDir CloudCov\n"
        ]
        weather_data, wind_spd_values, wind_dir_values = generate_weather_data(start_date, hours=24)
        with open(file_name, 'w') as file:
            file.writelines(header + [line + "\n" for line in weather_data])

        return wind_spd_values, wind_dir_values

    folder_path = "input_flammap"  # Папка для первого файла
    os.makedirs(folder_path, exist_ok=True)
    file_name = rf"{folder_path}/Generated_Weather_Data_1.wxs"
    start_date = datetime(2023, 1, 1)  # Начальная дата
    wind_spd_values, wind_dir_values = create_wxs_file(file_name, start_date)
    print(f"Файл '{file_name}' успешно создан")

    # Вычисление средних значений
    avg_wind_spd = sum(wind_spd_values) / len(wind_spd_values)
    avg_wind_dir = sum(wind_dir_values) / len(wind_dir_values)

    return avg_wind_spd, avg_wind_dir


def gen():
    generate_fuel()  # Генерация одного файла с топливной влажностью
    avg_wind_spd, avg_wind_dir = generate_weather()  # Генерация одного файла с погодой

    print(f"Средняя скорость ветра: {avg_wind_spd}")
    print(f"Среднее направление ветра: {avg_wind_dir}")

    return avg_wind_spd, avg_wind_dir

