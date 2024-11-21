import pyautogui
import time
import json
import subprocess
import os
import pyperclip
import keyboard
import paths

#1080 790
#1030 830


def clicker(spd,dir):
        
    def write_via_clipboard(text):
        time.sleep(0.5)
        pyperclip.copy(text)  # Скопировать текст в буфер обмена
        text = pyperclip.paste()  # Получаем текст из буфера обмена
        keyboard.write(text)
        time.sleep(0.5)
        pyperclip.copy("")

    photo_path = paths.PHOTO_PATH
    fms_path = paths.FMS_PATH
    wxs_path = paths.WXS_PATH
    not_csv = paths.SOURCE_FOLDER
    flammap_path = paths.FLAMMAP_PATH
    
    with open("coordinates.json", "r") as file:
        button_coordinates = json.load(file)
    time.sleep(1)
    subprocess.Popen(flammap_path)
    time.sleep(5)  # Подождите, пока программа запустится

    pyautogui.doubleClick(x=button_coordinates['button_1']['x'], y=button_coordinates['button_1']['y'])
    time.sleep(2)
    pyautogui.click(x=button_coordinates['button_2']['x'], y=button_coordinates['button_2']['y'])
    time.sleep(2)
    write_via_clipboard(photo_path)
    time.sleep(2)
    pyautogui.press('enter')

    #Runs
    pyautogui.click(x=button_coordinates['button_3']['x'], y=button_coordinates['button_3']['y'], button='right')   
    pyautogui.click(x=button_coordinates['button_4']['x'], y=button_coordinates['button_4']['y'])

    #Fuel Moisture File
    pyautogui.click(x=button_coordinates['button_5']['x'], y=button_coordinates['button_5']['y'])
    pyautogui.click(x=button_coordinates['button_6']['x'], y=button_coordinates['button_6']['y'])
    time.sleep(1)
    pyautogui.click(x=button_coordinates['button_7']['x'], y=button_coordinates['button_7']['y']) #directory in folder
    write_via_clipboard(fms_path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=button_coordinates['button_8']['x'], y=button_coordinates['button_8']['y']) #close folder

    #Crown Fire Calculation Method
    pyautogui.click(x=button_coordinates['button_9']['x'], y=button_coordinates['button_9']['y'])
    pyautogui.click(x=button_coordinates['button_10']['x'], y=button_coordinates['button_10']['y'])

    #Use Weather Stream
    pyautogui.click(x=button_coordinates['button_11']['x'], y=button_coordinates['button_11']['y'])
    pyautogui.click(x=button_coordinates['button_12']['x'], y=button_coordinates['button_12']['y'])
    pyautogui.click(x=button_coordinates['button_13']['x'], y=button_coordinates['button_13']['y'])
    pyautogui.click(x=button_coordinates['button_14']['x'], y=button_coordinates['button_14']['y']) #directory in folder
    write_via_clipboard(wxs_path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=button_coordinates['button_15']['x'], y=button_coordinates['button_15']['y'])
    pyautogui.press('0')
    pyautogui.press('1')
    pyautogui.click(x=button_coordinates['button_16']['x'], y=button_coordinates['button_16']['y'])

    #Wind Speed
    pyautogui.click(x=button_coordinates['button_17']['x'], y=button_coordinates['button_17']['y'])
    pyautogui.press('backspace')
    spd = str(int(spd))
    pyautogui.write(spd)

    #Azimuth
    pyautogui.click(x=button_coordinates['button_18']['x'], y=button_coordinates['button_18']['y'])
    pyautogui.press('backspace')
    dir = str(int(dir))
    pyautogui.write(dir)

    #Apply
    pyautogui.click(x=button_coordinates['button_19']['x'], y=button_coordinates['button_19']['y'])

    #Generate Gridded Wind
    pyautogui.click(x=button_coordinates['button_20']['x'], y=button_coordinates['button_20']['y'])
    pyautogui.click(x=button_coordinates['button_21']['x'], y=button_coordinates['button_21']['y']) #Wind Ninja Options
    pyautogui.click(x=button_coordinates['button_22']['x'], y=button_coordinates['button_22']['y']) #Use Duirnal Simulation
    pyautogui.click(x=button_coordinates['button_23']['x'], y=button_coordinates['button_23']['y']) #Use Conditioning Period End
    pyautogui.click(x=button_coordinates['button_24']['x'], y=button_coordinates['button_24']['y'])
    pyautogui.click(x=button_coordinates['button_25']['x'], y=button_coordinates['button_25']['y']) #Apply

    #Fire Behavior Options
    pyautogui.click(x=button_coordinates['button_26']['x'], y=button_coordinates['button_26']['y'])
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_27']['x'], y=button_coordinates['button_27']['y']) #Fireline Intensity
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_28']['x'], y=button_coordinates['button_28']['y']) #Rate of Spread
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_29']['x'], y=button_coordinates['button_29']['y']) #Flame Lenght
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_30']['x'], y=button_coordinates['button_30']['y']) #Crown Fire Activity
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_31']['x'], y=button_coordinates['button_31']['y']) #Spread Vectors
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_32']['x'], y=button_coordinates['button_32']['y']) #Apply

    #Launch Basic FB
    pyautogui.click(x=button_coordinates['button_33']['x'], y=button_coordinates['button_33']['y'])
    time.sleep(30)
    pyautogui.click(x=button_coordinates['button_34']['x'], y=button_coordinates['button_34']['y']) #ok

    pyautogui.click(x=button_coordinates['button_35']['x'], y=button_coordinates['button_35']['y']) #ok

    #Scroll to files
    pyautogui.moveTo(button_coordinates['button_36']['x'], button_coordinates['button_36']['y'])
    pyautogui.click(x=button_coordinates['button_37']['x'], y=button_coordinates['button_37']['y'])
    pyautogui.scroll(-1000)

    if not os.path.exists(not_csv):
        os.makedirs(not_csv)
    
    # Save files
    # 1
    time.sleep(1)
    pyautogui.click(x=button_coordinates['button_38']['x'], y=button_coordinates['button_38']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_39']['x'], y=button_coordinates['button_39']['y'])
    time.sleep(1)
    pyautogui.click(x=button_coordinates['button_40']['x'], y=button_coordinates['button_40']['y'])
    pyautogui.press('backspace')
    time.sleep(1)
    write_via_clipboard(not_csv)
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.click(x=button_coordinates['button_41']['x'], y=button_coordinates['button_41']['y'])
    write_via_clipboard('Flame Length')
    time.sleep(0.5)
    pyautogui.click(x=button_coordinates['button_42']['x'], y=button_coordinates['button_42']['y']) #Choise format
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_43']['x'], y=button_coordinates['button_43']['y']) 
    pyautogui.press('enter')
    time.sleep(0.5)
    # 2
    pyautogui.click(x=button_coordinates['button_44']['x'], y=button_coordinates['button_44']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_45']['x'], y=button_coordinates['button_45']['y'])
    pyautogui.write('Rate of Spread')
    pyautogui.click(x=button_coordinates['button_46']['x'], y=button_coordinates['button_46']['y'])
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_47']['x'], y=button_coordinates['button_47']['y'])
    pyautogui.press('enter')
    time.sleep(0.5)
    # 3
    pyautogui.click(x=button_coordinates['button_48']['x'], y=button_coordinates['button_48']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_49']['x'], y=button_coordinates['button_49']['y'])
    pyautogui.write('Fireline Intensity')
    pyautogui.click(x=button_coordinates['button_50']['x'], y=button_coordinates['button_50']['y'])
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_51']['x'], y=button_coordinates['button_51']['y'])
    pyautogui.press('enter')
    time.sleep(0.5)
    # 4
    pyautogui.click(x=button_coordinates['button_52']['x'], y=button_coordinates['button_52']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_53']['x'], y=button_coordinates['button_53']['y'])
    pyautogui.write('Crown Fire Activity')
    pyautogui.click(x=button_coordinates['button_54']['x'], y=button_coordinates['button_54']['y'])
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_55']['x'], y=button_coordinates['button_55']['y'])
    pyautogui.press('enter')
    time.sleep(0.5)
    # 5
    pyautogui.click(x=button_coordinates['button_56']['x'], y=button_coordinates['button_56']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_57']['x'], y=button_coordinates['button_57']['y'])
    pyautogui.write('Max Spread Direction')
    pyautogui.click(x=button_coordinates['button_58']['x'], y=button_coordinates['button_58']['y'])
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_59']['x'], y=button_coordinates['button_59']['y'])
    pyautogui.press('enter')
    time.sleep(0.5)
    # 6
    pyautogui.click(x=button_coordinates['button_60']['x'], y=button_coordinates['button_60']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_61']['x'], y=button_coordinates['button_61']['y'])
    pyautogui.write('Wind Direction')
    pyautogui.click(x=button_coordinates['button_62']['x'], y=button_coordinates['button_62']['y'])
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_63']['x'], y=button_coordinates['button_63']['y'])
    pyautogui.press('enter')
    time.sleep(0.5)
    # 7
    pyautogui.click(x=button_coordinates['button_64']['x'], y=button_coordinates['button_64']['y'], button='right')
    pyautogui.click(x=button_coordinates['button_65']['x'], y=button_coordinates['button_65']['y'])
    pyautogui.write('Wind Speed')
    pyautogui.click(x=button_coordinates['button_66']['x'], y=button_coordinates['button_66']['y'])
    pyautogui.sleep(0.3)
    pyautogui.click(x=button_coordinates['button_67']['x'], y=button_coordinates['button_67']['y'])
    pyautogui.press('enter')
    time.sleep(0.5)

    # Exit
    pyautogui.click(x=button_coordinates['button_68']['x'], y=button_coordinates['button_68']['y'])
    time.sleep(1)
    pyautogui.press('right')
    pyautogui.press('enter')
    time.sleep(7)



