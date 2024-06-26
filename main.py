import os
import random
import time
from datetime import datetime, timedelta
from PIL import ImageGrab

# Screenshot random intervals
min_interval = 19 * 60
max_interval = 23 * 60


def get_random_interval():
    return random.randint(min_interval, max_interval)


def take_screenshot():
    try:
        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H%M%S")
        date = now.strftime("%m-%d")

        # Create / Check if the destination folder exists
        desktop_path = os.path.expanduser('~/OneDrive/Desktop')
        folder_path = os.path.join(desktop_path, "Antsentry Report- Screenshot", date)
        os.makedirs(folder_path, exist_ok=True)

        # Take a screenshot
        screenshot = ImageGrab.grab()

        # Save the file with the proper naming format
        file_name = f"Screenshot {date_time}.png"
        file_path = os.path.join(folder_path, file_name)
        screenshot.save(file_path)

        # Console output
        print(f"Screenshot saved at {file_path}")

        # Get a new random interval
        next_interval = get_random_interval()
        print(f"Next screenshot at {(datetime.now() + timedelta(seconds=next_interval)).strftime('%H:%M:%S')}")

        # Wait for the next interval
        time.sleep(next_interval)

    except Exception as e:
        print(f"Error capturing screenshot: {e}")


if __name__ == "__main__":
    print("Taking first screenshot in 5 seconds. Please minimize this window.")
    time.sleep(5)
    
    while True:
        take_screenshot()
