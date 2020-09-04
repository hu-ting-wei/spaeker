#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from campusrover_msgs.msg import HmiStatus
from playsound import playsound
def callback(data):
	s=data.data
	rospy.loginfo(s)
	if s==STAUS_SPEAK_HELLO_HELLO:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/hello_hello.mp3')
	elif s==STAUS_SPEAK_SCAN_QRCODE1:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/scan_qrcode_and_input_number.mp3')
	elif s==STAUS_SPEAK_WRONG_NUMBER1:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/wrong_number_input_again.mp3')
	elif s==STAUS_SPEAK_PUT_IN_MEALS:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_put_in_the_meals.mp3')
	elif s==STAUS_SPEAK_PRESS_BUTTON_AFTER_PUT_IN:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_press_the_button_afte_put_in_x.mp3')
	elif s==STAUS_SPEAK_MEAL_ARRIVED:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/your_meal_arrived.mp3')
	elif s==STAUS_SPEAK_DELIVERING_MEAL:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/I_am_coming_for_delivering_meals.mp3')
	elif s==STAUS_SPEAK_SCAN_QRCODE2:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/scan_qrcode_and_input_number.mp3')
	elif s==STAUS_SPEAK_WRONG_NUMBER2:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/wrong_number_input_again.mp3')
	elif s==STAUS_SPEAK_TAKE_OUT_MEALS:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_take_out_the_meal.mp3')
	elif s==STAUS_SPEAK_PRESS_BUTTON_AFTER_TAKE_OUT:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_press_the_button_after_take_out_the_meal.mp3')
	elif s==STAUS_SPEAK_ENJOY_MEAL:
    		playsound('catkin_ws/src/voice_pkg/src/files_order/thank_you_for_ordering_enjoy_your_meal.mp3')
	elif s==STAUS_SPEAK_HELLO:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/hello.mp3')
	elif s==STAUS_SPEAK_THANKS:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/thank_you.mp3')
	elif s==STAUS_SPEAK_GOODBYE:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/bye_bye_see_you_next_time.mp3')
	elif s==STAUS_SPEAK_EXCUSE_ME:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/excuse_me.mp3')
	elif s==STAUS_SPEAK_COMMING_THROUGH:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/excuse_me_coming_through.mp3')
	elif s==STAUS_SPEAK_BE_CAREFUL:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/be_careful.mp3')
	elif s==STAUS_SPEAK_WATCH_OUT:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/watch_out.mp3')
	elif s==STAUS_SPEAK_HELP_ME:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/can_you_help_me.mp3')
	elif s==STAUS_SPEAK_OPEN_DOOR:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/can_you_open_the_door_for_me.mp3')
	elif s==STAUS_SPEAK_HAVE_GOODDAY:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/have_a_good_day.mp3')
	elif s==STAUS_SPEAK_WRONG_OPERATION:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/wrong_operation.mp3')
	elif s==STAUS_SPEAK_DO_IT_AGAIN:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/please_do_it_again.mp3')
	elif s==STAUS_SPEAK_CORRECT_OR_NOT:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/correct_or_not.mp3')
	elif s==STAUS_SPEAK_LOW_BATTERY:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/low_battery_warning.mp3')
	elif s==STAUS_SPEAK_SYSTEM_ERROR:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/system_error.mp3')
	elif s==STAUS_SPEAK_CALL_STAFF:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/please_call_technical_staff.mp3')
	elif s==STAUS_SPEAK_LOADING:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/loading.mp3')
	elif s==STAUS_SPEAK_WAIT:
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/please_wait.mp3')
	elif s==STAUS_ENTER_ELEVATOR:
    		playsound('catkin_ws/src/voice_pkg/src/elevator/entering_elevator.mp3')
	elif s==STAUS_LEAVING_ELEVATOR:
    		playsound('catkin_ws/src/voice_pkg/src/elevator/leaving_elevator.mp3')
	elif s==STAUS_TURN_RIGHT:
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_turning_right.mp3')
	elif s==STAUS_TURN_LEFT:
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_turning_left.mp3')
	elif s==STAUS_BLOCKED:
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/excuse_me_coming_through.mp3')
	elif s==STAUS_REVERSE:
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_reversing.mp3')
	elif s==STAUS_FORWARD:
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_forward.mp3')
	elif s==STAUS_MOVING:
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_moving.mp3')
	elif s==STAUS_1F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_1st_floor.mp3')
	elif s==STAUS_2F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_2nd_floor.mp3')
	elif s==STAUS_3F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_3rd_floor.mp3')
	elif s==STAUS_4F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_4th_floor.mp3')
	elif s==STAUS_5F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_5th_floor.mp3')
	elif s==STAUS_6F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_6th_floor.mp3')
	elif s==STAUS_7F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_7th_floor.mp3')
	elif s==STAUS_8F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_8th_floor.mp3')
	elif s==STAUS_9F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_9th_floor.mp3')
	elif s==STAUS_10F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_10th_floor.mp3')
	elif s==STAUS_11F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_11th_floor.mp3')
	elif s==STAUS_12F:
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_12th_floor.mp3')
	elif s==STAUS_PRESS_BUTTON:
    		playsound('catkin_ws/src/voice_pkg/src/elevator/be_careful_when_press_button.mp3')



if __name__=='__main__':
	rospy.init_node('mp3player_python_node')
	rospy.Subscriber('hmi_status',UInt16,callback)	
	rospy.spin()
