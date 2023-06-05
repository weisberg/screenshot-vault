import pyautogui
import pytesseract
from PIL import Image
from pynput import mouse
import threading

# Pytesseract configuration
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'  # Update with your Tesseract path

timer = None

def screenshot_and_ocr():
    global timer
    if timer is not None:
        timer.cancel()

    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    text = pytesseract.image_to_string(Image.open('screenshot.png'))
    print(text)

    timer = threading.Timer(60.0, screenshot_and_ocr)
    timer.start()

# This function will be called every time the mouse is clicked
def on_click(x, y, button, pressed):
    if pressed:
        # If the mouse is clicked, take a screenshot
        screenshot_and_ocr()

# Start the timer when the script starts
screenshot_and_ocr()

# Start listening for mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
