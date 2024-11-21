import os
import rasterio
import csv
import math
import zipfile
from datetime import datetime
import paths


source_folder = paths.SOURCE_FOLDER
destination_folder = paths.DESTINATION_FOLDER
fms_and_wxs_folder = paths.FMS_AND_WXS_FOLDER
zip_files_folder = paths.ZIP_FILES_FOLDER


# source_folder = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\not_csv')
# destination_folder = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\csv')
# fms_and_wxs_folder = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\input_flammap')
# zip_files_folder = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\zip_files')

for file_name in os.listdir(source_folder):
        print(file_name)
        
def convert_time_to_float(time_str):
    time_obj = datetime.strptime(time_str, "%H%M")
    return float(f"{time_obj.hour}.{time_obj.minute:02}")

def asc_to_csv(source_folder, destination_folder):
    for file_name in os.listdir(source_folder):
        if file_name.endswith('.asc'):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name.replace('.asc', '.csv'))

            try:
                # Чтение файла с помощью rasterio
                with rasterio.open(source_path) as src:
                    data = src.read(1)  # Чтение первого слоя данных
                    profile = src.profile

                # Сохранение данных в формате CSV
                with open(destination_path, mode='w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    for row in data:
                        writer.writerow(row)

                print(f"Файл {file_name} успешно преобразован и сохранён как {destination_path}")

            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")

def fms_to_csv(fms_and_wxs_folder, destination_folder):

    fms_custom_header = [
    "Index", "1 Hour FM", "10 Hour FM", "100 Hour FM", 
    "Herbaceous FM", "Live Woody FM", "1000 Hour FM"
    ]

    for file_name in os.listdir(fms_and_wxs_folder):
        if file_name.endswith('.fms'):
            # Полные пути
            source_path = os.path.join(fms_and_wxs_folder, file_name)
            output_csv_path = os.path.join(destination_folder, file_name.replace('.fms', '.csv'))

            # Чтение .fms файла
            with open(source_path, 'r') as file:
                fms_content = file.readlines()

            # Преобразование данных в числовой формат
            fms_data_rows = []
            for line in fms_content:
                row = []
                for item in line.strip().split():
                    try:
                        # Пробуем преобразовать в int или float
                        num_value = int(item) if item.isdigit() else float(item)
                    except ValueError:
                        # Если не число, используем NaN
                        num_value = math.nan
                    row.append(num_value)
                fms_data_rows.append(row)

            # Запись данных в CSV
            with open(output_csv_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(fms_custom_header)  # Запись заголовка
                csv_writer.writerows(fms_data_rows)  # Запись данных

            print(f"Файл {file_name} успешно преобразован в {output_csv_path}")

def wxs_to_csv(fms_and_wxs_folder, destination_folder):
    """Преобразует .wxs файлы в .csv файлы."""
    
    # Заголовок для .csv файла
    header = ["Year", "Mth", "Day", "Time", "Temp", "RH", "HrlyPcp", "WindSpd", "WindDir", "CloudCov"]

    for file_name in os.listdir(fms_and_wxs_folder):
        if file_name.endswith('.wxs'):
            # Полные пути
            source_path = os.path.join(fms_and_wxs_folder, file_name)
            output_csv_path = os.path.join(destination_folder, file_name.replace('.wxs', '.csv'))

            # Чтение .wxs файла
            with open(source_path, 'r') as file:
                lines = file.readlines()

            # Пропускаем метаинформацию (первые 4 строки)
            data_rows = [line.strip().split() for line in lines[4:]]

            # Преобразуем данные в нужный формат
            adjusted_data_rows = [
                [
                    int(row[0]),                         # Year
                    int(row[1]),                         # Mth
                    int(row[2]),                         # Day
                    convert_time_to_float(row[3]),       # Time в формате HH.MM
                    float(row[4]),                       # Temp
                    float(row[5]),                       # RH
                    float(row[6]),                       # HrlyPcp
                    float(row[7]),                       # WindSpd
                    float(row[8]),                       # WindDir
                    float(row[9])                        # CloudCov
                ]
                for row in data_rows
            ]

            # Запись в CSV файл
            with open(output_csv_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(header)  # Запись заголовка
                csv_writer.writerows(adjusted_data_rows)  # Запись данных

def get_next_zip_filename(zip_files_folder):
    """Возвращает имя следующего файла архива в папке zip_files."""
    i = 1
    while True:
        zip_file_name = os.path.join(zip_files_folder, f"case_{i}.zip")
        if not os.path.exists(zip_file_name):
            return zip_file_name
        i += 1

def csv_to_zip(destination_folder, zip_files_folder):
    # Получаем путь к следующему архиву
    zip_file_path = get_next_zip_filename(zip_files_folder)

    # Создаем ZIP файл
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Проходим по всем файлам в папке
        for file_name in os.listdir(destination_folder):
            # Если файл с расширением .csv
            if file_name.endswith('.csv'):
                # Полный путь к файлу
                file_path = os.path.join(destination_folder, file_name)
                # Добавляем файл в архив с его исходным именем
                zipf.write(file_path, arcname=file_name)

def delete_all_files_in_folder(source_folder):
    # Получаем список всех файлов и папок в директории
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        
        # Проверяем, является ли объект файлом
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Файл {file_name} удален.")




def all():
        
    asc_to_csv(source_folder, destination_folder)

    fms_to_csv(fms_and_wxs_folder, destination_folder)

    wxs_to_csv(fms_and_wxs_folder, destination_folder)

    csv_to_zip(destination_folder, zip_files_folder)

    delete_all_files_in_folder(source_folder)

    delete_all_files_in_folder(destination_folder)
    


