#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from playsound import playsound
def callback(data):
	s=data.data
	rospy.loginfo(s)
	if s==1:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/hello hello.mp3')
	elif s==2:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/scan qrcode and input number.mp3')
	elif s==3:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/please put in the meals.mp3')
	elif s==4:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/please press the bottom after put in x.mp3')
	elif s==5:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/your meal arrived.mp3')
	elif s==6:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/I am coming for delivering meals.mp3')


if __name__=='__main__':
	rospy.init_node('mp3player_python_node')
	rospy.Subscriber('buttom',UInt16,callback)	
	rospy.spin()
