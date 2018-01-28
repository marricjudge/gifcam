##############
# THE GIFCAM #
##############

# Importing libaries
import picamera
from time import sleep
import time
import RPi.GPIO as GPIO
from os import system
import os
import random, string

# Set behaviour variables
gif_delay = 15
num_frame = 8
delay = 0.2

# Set up the three buttons
GPIO.setmode(GPIO.BCM)

mode1 = 12 # Mode 1 set on GPIO Pin 12
GPIO.setup(mode1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mode2 = 16 # Mode 1 set on GPIO Pin 16
GPIO.setup(mode2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mode3 = 18 # Mode 1 set on GPIO Pin 18
GPIO.setup(mode3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the camera
camera = picamera.PiCamera()
camera.resolution = (486, 364)
camera.rotation = 270
camera.saturation = 0

# Random string generator for random file names
def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# Main function
def run():
    sleep(delay)
    print('System Ready')

    try:
        state = 1
        print("Mode 1")
        mode1()

    except:
        GPIO.cleanup()

# Mode 3: Jump-GIF
def mode3():
    sleep(delay)
    while True:
        if GPIO.input(mode3) == True: # BUTTON PRESSED
                # TAKING PICTURES
                print('Gif Started')

                randomstring = random_generator()
                camera.capture('1.jpg')
                sleep(picoffset)
                camera.capture('2.jpg')

                # PROCESSING GIF
                print('Processing')
                filename = '/home/pi/gifs/' + randomstring + '-0'

                graphicsmagick = "gm convert -delay " + str(20) + " " + "*.jpg " + filename + ".gif"
                os.system(graphicsmagick)
                os.system("rm ./*.jpg")

                print('Done')
                print('System Ready')

        elif GPIO.input(mode2) == True:
            print("load mode 2")
            mode2()

        elif GPIO.input(mode1) == True:
            print ("load mode 1")
            mode1()

        else :
            sleep(0.05)

def mode2(): #Boomerang Effect
    sleep(delay)
    while True:
        if GPIO.input(button) == True: # BUTTON PRESSED
                # TAKING PICTURES
                print('Gif Started')

                randomstring = random_generator()
                for i in range(num_frame):
                    camera.capture('{0:04d}.jpg'.format(i))

                # PROCESSING GIF
                for i in range(num_frame - 1):
                    source = str(num_frame - i - 1) + ".jpg"
                    source = source.zfill(8) # pad with zeros
                    dest = str(num_frame + i) + ".jpg"
                    dest = dest.zfill(8) # pad with zeros
                    copyCommand = "cp " + source + " " + dest
                    os.system(copyCommand)

                print('Processing')
                filename = '/home/pi/gifs/' + randomstring + '-0'

                graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "*.jpg " + filename + ".gif"
                os.system(graphicsmagick)
                os.system("rm ./*.jpg")

                print('Done')
                print('System Ready')

        elif GPIO.input(mode1) == True:
            print("load mode 1")
            mode1()

        elif GPIO.input(mode3) == True:
            print ("load mode 3")
            mode3()

        else :
            sleep(0.05)


def mode1(): # Normal GIF
    sleep(delay)
    while True:
        if GPIO.input(button) == True: # BUTTON PRESSED
            # TAKING PICTURES
            print('Gif Started')

            randomstring = random_generator()
            for i in range(num_frame):
                camera.capture('{0:04d}.jpg'.format(i))

            # PROCESSING GIF
            print('Processing')
            filename = '/home/pi/gifs/' + randomstring + '-0'
            graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "*.jpg " + filename + ".gif"
            os.system(graphicsmagick)
            os.system("rm ./*.jpg")

            print('Done')
            print('System Ready')

        elif GPIO.input(mode2) == True:
            print("load mode 2")
            mode2()

        elif GPIO.input(mode3) == True;
            print ("load mode 3")
            mode3()

        else :
            sleep(0.05)

run()


# GIFCAM
#
# A project by Tim Kuhr and Marius Richter
# Technological Basics II
# Lecturer: Helena Lingor
# Leuphana University of Lüneburg + Hamburg Media School
#
# https://github.com/marricjudge/gifcam 
#
# References:
# BREWER, Nick: https://hackaday.io/project/16358-pix-e-gif-camera 23.01.2018
# BREWER, Nick: https://github.com/nickbrewer/gifcam/blob/master/gifcam.py 23.01.2018
# GraphicsMagick Image Processing System http://www.graphicsmagick.org/ 23.01.2018
# GITCORE: https://packages.debian.org/sid/git-core 23.01.2018
# RASPBIAN OS: https://www.raspbian.org/ + https://www.raspberrypi.org/downloads/noobs/ 23.01.2018
# PiCamera: https://www.raspberrypi.org/products/camera-module-v2/ + https://projects.raspberrypi.org/en/projects/getting-started-with-picamera 23.01.2018
# any many other helpful forums
#
# Logo:
# Icon made by Vignesh Oviyan from www.flaticon.com (28.01.2018)
# https://www.flaticon.com/free-icon/replay_175689
