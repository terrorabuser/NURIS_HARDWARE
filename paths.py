import os


# На второй кнопке у меня ломались координаты, поэтому юзал либо одни, либо вторые
#1080 790
#1030 830


# Путь к папке с исходными данными
SOURCE_FOLDER = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\not_csv')

# Путь к папке для сохранения CSV файлов
DESTINATION_FOLDER = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\csv')

# Путь к папке с файлами для FlamMap
FMS_AND_WXS_FOLDER = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\input_flammap')

# Путь к папке для архивов
ZIP_FILES_FOLDER = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\zip_files')

# Путь к исполняемому файлу FlamMap
FLAMMAP_PATH = r"C:\Workspace\FlamMap6\FlamMap6.exe"

# Путь к файлу с координатами кнопок
COORDINATES_FILE = os.path.normpath(r'C:\Users\Nikita\Desktop\codes\flames\coordinates.json')

# Другие пути, если нужно
PHOTO_PATH = os.path.normpath(r"C:\Users\Nikita\Desktop\flammap\files\Lassen Volcanic National Park.tif")

# Путь к создаваемому файлу с данными о топливе
FMS_PATH = os.path.normpath(r"C:\Users\Nikita\Desktop\codes\flames\input_flammap\generated_fuel_moisture_data_1.fms")

# Путь к создаваемому файлу с данными о погоде
WXS_PATH = os.path.normpath(r"C:\Users\Nikita\Desktop\codes\flames\input_flammap\Generated_Weather_Data_1.wxs")