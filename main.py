import threading
import time
from pyautogui import locateCenterOnScreen, click
import subprocess
import os


print(' Скрипт только под Windows Важно поставить сначала зависимости, команда (нужно усчтановить python3 и pip) - pip install -r requirements.txt')

install = input('Если установил нажмми 1, если нет любую другую клавишу: ')
if int(install) == 1:
    None
else:
    print('нужно установить зависимости, смотри текст выше')
    exit()

current_directory = os.path.dirname(os.path.abspath(__file__))

script_path = os.path.join(current_directory, 'blum_complete_edition.py')
play_button_image = os.path.join(current_directory, 'button.png')

def run_script(script_path):
    python_path = r'C:\Users\denishumen\AppData\Local\Programs\Python\Python311\python.exe'
    try:
        result = subprocess.run([python_path, script_path], check=True, capture_output=True, text=True)
        print("Скрипт успешно выполнен.")
        print("Вывод:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения скрипта: {e}")
        print("Вывод:", e.stdout)
        print("Ошибка:", e.stderr)
    except FileNotFoundError as e:
        print(f"Не найден файл: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def find_and_click_button(image_path, confidence=0.8):
    try:
        print("Ищу кнопку на экране...")
        button_location = locateCenterOnScreen(image_path, confidence=confidence)
        if button_location:
            click(button_location.x, button_location.y)
            print(f"Кнопка найдена и нажата: {button_location}")
            return True
        else:
            print("Кнопка не найдена.")
            return False
    except Exception as e:
        print(f"Ошибка поиска кнопки: {e}")
        return False

def script_thread():
    run_script(script_path)

def button_search_thread():
    while True:
        try:
            if find_and_click_button(play_button_image):
                time.sleep(40)
            else:
                time.sleep(10)
        except KeyboardInterrupt:
            print("Поиск кнопки прерван пользователем.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            time.sleep(10) 

def main():
    script_thread_instance = threading.Thread(target=script_thread)
    button_search_thread_instance = threading.Thread(target=button_search_thread)

    script_thread_instance.start()
    button_search_thread_instance.start()

    script_thread_instance.join()
    button_search_thread_instance.join()

if __name__ == "__main__":
    main()