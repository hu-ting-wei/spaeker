#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from campusrover_msgs.msg import HmiStatus
from playsound import playsound
def callback(data):
	s=data.data
	rospy.loginfo(s)
	if s==STAUS_SPEAK_HELLO_HELLO:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/hello hello.mp3')
	elif s==STAUS_SPEAK_SCAN_QRCODE1:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/scan qrcode and input number.mp3')
	elif s==STAUS_SPEAK_WRONG_NUMBER1:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/wrong number,input again.mp3')
	elif s==STAUS_SPEAK_PUT_IN_MEALS:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/please put in the meals.mp3')
	elif s==STAUS_SPEAK_PRESS_BOTTOM_AFTER_PUT_IN:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/please press the bottom after put in x.mp3')
	elif s==STAUS_SPEAK_MEAL_ARRIVED:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/your meal arrived.mp3')
	elif s==STAUS_SPEAK_DELIVERING_MEAL:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/I am coming for delivering meals.mp3')
	elif s==STAUS_SPEAK_SCAN_QRCODE2:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/scan qrcode and input number.mp3')
	elif s==STAUS_SPEAK_WRONG_NUMBER2:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/wrong number,input again.mp3')
	elif s==STAUS_SPEAK_TAKE_OUT_MEALS:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/please take out the meal.mp3')
	elif s==STAUS_SPEAK_PRESS_BOTTOM_AFTER_TAKE_OUT:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/please press the bottom after take out the meal.mp3')
	elif s==STAUS_SPEAK_ENJOY_MEAL:
    		playsound('catkin_ws/src/voice_pkg/src/files,order/thank you for ordering, enjoy your meal.mp3')
	elif s==STAUS_SPEAK_HELLO:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/hello.mp3')
	elif s==STAUS_SPEAK_THANKS:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/thank you.mp3')
	elif s==STAUS_SPEAK_GOODBYE:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/bye bye see you next time.mp3')
	elif s==STAUS_SPEAK_EXCUSE_ME:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/excuse me.mp3')
	elif s==STAUS_SPEAK_COMMING_THROUGH:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/excuse me, coming through.mp3')
	elif s==STAUS_SPEAK_BE_CAREFUL:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/be careful.mp3')
	elif s==STAUS_SPEAK_WATCH_OUT:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/watch out.mp3')
	elif s==STAUS_SPEAK_HELP_ME:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/can you help me.mp3')
	elif s==STAUS_SPEAK_OPEN_DOOR:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/can you open the door for me.mp3')
	elif s==STAUS_SPEAK_HAVE_GOODDAY:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/have a good day.mp3')
	elif s==STAUS_SPEAK_WRONG_OPERATION:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/wrong operation.mp3')
	elif s==STAUS_SPEAK_DO_IT_AGAIN:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/please do it again.mp3')
	elif s==STAUS_SPEAK_CORRECT_OR_NOT:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/correct or not.mp3')
	elif s==STAUS_SPEAK_LOW_BATTERY:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/low battery warning.mp3')
	elif s==STAUS_SPEAK_SYSTEM_ERROR:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/system error.mp3')
	elif s==STAUS_SPEAK_CALL_STAFF:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/please call technical staff.mp3')
	elif s==STAUS_SPEAK_LOADING:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/loading.mp3')
	elif s==STAUS_SPEAK_WAIT:
    		playsound('catkin_ws/src/voice_pkg/src/commonly used/please wait.mp3')
	elif s==STAUS_ENTER_ELEVATOR:
    		playsound('catkin_ws/src/voice_pkg/src/elevator/entering elevator.mp3')
	elif s==STAUS_LEAVING_ELEVATOR:
    		playsound('catkin_ws/src/voice_pkg/src/elevator/leaving elevator.mp3')
	elif s==STAUS_TURN_RIGHT:
    		playsound('catkin_ws/src/voice_pkg/src/during moving/be careful when turning right.mp3')
	elif s==STAUS_TURN_LEFT:
    		playsound('catkin_ws/src/voice_pkg/src/during moving/be careful when turning left.mp3')
	elif s==STAUS_BLOCKED:
    		playsound('catkin_ws/src/voice_pkg/src/during moving/excuse me,coming through.mp3')
	elif s==STAUS_REVERSE:
    		playsound('catkin_ws/src/voice_pkg/src/during moving/be careful when reversing.mp3')
	elif s==STAUS_1F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 1th floor.mp3')
	elif s==STAUS_2F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 2th floor.mp3')
	elif s==STAUS_3F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 3th floor.mp3')
	elif s==STAUS_4F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 4th floor.mp3')
	elif s==STAUS_5F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 5th floor.mp3')
	elif s==STAUS_6F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 6th floor.mp3')
	elif s==STAUS_7F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 7th floor.mp3')
	elif s==STAUS_8F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 8th floor.mp3')
	elif s==STAUS_9F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 9th floor.mp3')
	elif s==STAUS_10F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 10th floor.mp3')
	elif s==STAUS_11F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 11th floor.mp3')
	elif s==STAUS_12F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help me press 12th floor.mp3')


if __name__=='__main__':
	rospy.init_node('mp3player_python_node')
	rospy.Subscriber('hmi_status',UInt16,callback)	
	rospy.spin()
