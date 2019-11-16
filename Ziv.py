# Simple pygame test for the google coral
# Maps the gamepad for a Logitech controller
# Author: Danny Dasilva
# License: Public Domain

import pygame
from time import sleep
from app.TEST import Drone

drone = Drone()

pygame.init()

drone.video()

joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print('init')

while True:
    pygame.event.get()

    if joystick_count != 0:
        rightsticky = gamepad.get_axis(1)
        leftsticky = gamepad.get_axis(4)

        LT = gamepad.get_axis(2)
        RT = gamepad.get_axis(5)

        rightstickx = gamepad.get_axis(0)
        leftstickx = gamepad.get_axis(3)
        Start = gamepad.get_button(7)
        Back = gamepad.get_button(6)
        x, y = gamepad.get_hat(0)

        X = gamepad.get_button(2)
        Y = gamepad.get_button(3)
        A = gamepad.get_button(0)
        B = gamepad.get_button(1)
#drone.roll()
#dron.pitch()
#drone.yaw()
#drone.throttle()
#drone.takeoff()
#drone.land()
        if Start == 1:
            print('Start pressed')
            drone.takeoff1()

        if Back == 1:
            print('Back Pressed')
            drone.land()
        if B == 1:
            drone.roll(1)
        else:
            drone.roll(0)
        if X == 1:
            drone.roll(-1)
        else:
            drone.roll(0)
        if y == 1:
            drone.throttle(1)
        else:
            drone.throttle(0)
        if y == -1:
            drone.throttle(-1)
        else:
            drone.throttle(0)
        if Y == 1:
            drone.pitch(1)
        else:
            drone.pitch(0)
        if A == 1:
            drone.pitch(-1)
