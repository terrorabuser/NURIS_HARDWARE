import random
def create_uniform_fms_file(filename, fm_1_hour, fm_10_hour, fm_100_hour, fm_1000_hour, herbaceous_fm, live_woody_fm):
    """
    Создаёт .fms файл, в котором значения влажности для всех строк одинаковы,
    а первый столбец содержит фиксированные номера моделей топлива.
    """
    # Фиксированные значения для первого столбца (номера моделей топлива)
    model_ids = [0, 101, 102, 121, 122, 141, 142, 143, 144, 161, 162, 165,
                 181, 182, 183, 184, 185, 186, 187, 188]

    with open(filename, 'w') as f:
        for model_id in model_ids:
            # Записываем строку с одинаковыми значениями для всех строк, заданными пользователем
            f.write(
                f"{model_id} {fm_1_hour} {fm_10_hour} {fm_100_hour} {herbaceous_fm} {live_woody_fm} {fm_1000_hour}\n")


# Пример использования функции
filename = "C:/landscapes flamemap/FMS Files/generated_fuel_moisture_data104.fms"
create_uniform_fms_file(
    filename=filename,
    fm_1_hour = random.randint(1, 10),
    fm_10_hour = random.randint(10, 20),
    fm_100_hour = random.randint(20, 30),
    fm_1000_hour = random.randint(30, 40),
    herbaceous_fm = random.randint(50, 80),
    live_woody_fm = random.randint(90, 120)
)

print(f"Файл '{filename}' успешно создан с одинаковыми значениями для каждого столбца, кроме первого.")
