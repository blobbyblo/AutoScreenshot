import os
import time
from datetime import datetime
import pyautogui
import schedule


def take_screenshot():
    # Get the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H%M%S")
    date = now.strftime("%m-%d")

    # Create / Check if the destination folder exists
    desktop_path = os.path.expanduser('~/Desktop')
    folder_path = os.path.join(desktop_path, "Antsentry Report- Screenshot", date)
    os.makedirs(folder_path, exist_ok=True)

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the file with the proper naming format
    file_name = f"Screenshot {date_time}.png"
    file_path = os.path.join(folder_path, file_name)
    screenshot.save(file_path)

    # Console output
    print(f"Screenshot saved at {file_path}")

schedule.every(20).minutes.do(take_screenshot)

while True:
    schedule.run_pending()
    time.sleep(1)
