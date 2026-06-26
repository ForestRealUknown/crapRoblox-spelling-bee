import keyboard
import random
import time


def type(text):
    charecters = []

    for char in text:
        charecters.append(char)

    for i in range(len(charecters)):
        keyboard.press_and_release(charecters[i])
        time.sleep(random.uniform(0.065, 0.290))

    keyboard.press_and_release("enter")