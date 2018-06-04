from gpiozero import Button
from time import sleep

left_button = Button(13)
right_button = Button(12)


def movement(left_button, right_button):
    inputs = (left_button.is_pressed(), right_button.is_pressed())
    return inputs


