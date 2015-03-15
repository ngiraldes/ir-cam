### IR-CAM created by Nicolas GIRALDES         ###
### inspired by Nature_Box - created by TeCoEd ###

import RPi.GPIO as GPIO
import picamera
import time
import sys

PIR = 26
IR_LED = 14
global File_Number
File_Number = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_LED, GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

def Photo_Shoot():
    print("Photos !")
    global File_Number
    with picamera.PiCamera() as camera:
        GPIO.output(IR_LED, True)
        #camera.start_preview()
        time.sleep(2)
        camera.capture("/home/pi/ir-cam/shot" + str(File_Number) + ".jpeg")
        File_Number = File_Number + 1
        GPIO.output(IR_LED, False)

def Motion_Sensing(PIR):
    print("Mouvement detecte")
    Photo_Shoot()

print("C'est parti !")
time.sleep(2)

try:
    GPIO.add_event_detect(PIR,GPIO.RISING,callback=Motion_Sensing)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print("quit")
    GPIO.cleanup()
