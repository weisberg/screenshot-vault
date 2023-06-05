# Python Screenshot and OCR Program

This Python program automatically takes screenshots of your computer screen, either every minute or every time the mouse is clicked, whichever comes first. It then uses OCR (Optical Character Recognition) to extract all text from the screenshot.

## Table of Contents

- [Python Screenshot and OCR Program](#python-screenshot-and-ocr-program)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installing Dependencies](#installing-dependencies)
    - [Installing the Program](#installing-the-program)
- [Opportunities for Improvement](#opportunities-for-improvement)
  - [Warnings](#warnings)

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a MacOS machine.
- You have installed Python 3.6 or later.
- You have installed Tesseract OCR on your machine. If not, you can install it using Homebrew with the command `brew install tesseract`.

### Installing Dependencies

This program requires the following Python libraries:

- `pyautogui`
- `pytesseract`
- `pil` (Pillow)
- `pynput`

You can install these libraries using pip:

```bash
pip install pyautogui pytesseract pillow pynput
```

### Installing the Program
To install the program, follow these steps:

Download the Python script to your machine.
Update the Tesseract path in the script to match the installation location on your machine.
Usage
To use the program, run the Python script in your terminal:

```bash
python3 screenshot-vault.py
```

The program will then start running, taking a screenshot either every minute or every time the mouse is clicked. The text from each screenshot will be printed to the console.



# Opportunities for Improvement
This program is quite basic and could be improved in a number of ways:

- Implement a GUI to make it easier to start and stop the program.
- Add the option to save the OCR'd text to a file instead of printing it to the console.
- Improve the screenshot-taking mechanism to allow for screenshots of specific areas of the screen.
- Add more robust error handling and logging.
- Optimize the OCR process for better text extraction.
- Add functionality to blur or exclude certain parts of the screen to protect sensitive information.

## Warnings
Please be aware that this program will take screenshots without any visual or auditory indication, which could potentially capture sensitive information. Always be aware of what is on your screen while the program is running.

Furthermore, this program saves each screenshot as 'screenshot.png' in the same directory as the script, overwriting the previous screenshot. If you want to keep all screenshots, you'll need to modify the script to save each screenshot with a unique filename.