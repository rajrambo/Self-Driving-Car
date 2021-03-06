#!/usr/bin/env python
import pygame
from pygame.locals import *
import serial
import rospy
from std_msgs.msg import UInt8

LEFT, FORWARD, RIGHT = 4, 2, 1

s = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def control_callback(msg):
    control_input = msg.data
    if control_input == FORWARD | RIGHT :
        print 'Forward-Right'
        s.write('O1%L100%R80%')
    elif control_input == FORWARD | LEFT :
        print 'Forward-Left'
        s.write('O1%L80%R100%')
    elif control_input == FORWARD :
        print 'Forward'
        s.write('O1%L105%R110%')
    elif control_input == LEFT :
        print 'Left'
        s.write('O1%L70%R90%')
    elif control_input == RIGHT :
        print 'Right'
        s.write('O1%L90%R70%')
    else:
        print 'Stop'
        s.write('O1%L0%R0%')

def main():
    rospy.init_node('manual_control_pi',anonymous=False)
    rospy.Subscriber('/control_signal', UInt8, control_callback)
    rospy.spin()

if __name__=='__main__':
    main()
