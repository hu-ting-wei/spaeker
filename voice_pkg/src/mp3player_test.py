#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from playsound import playsound
def callback(data):
	s=data.data
	rospy.loginfo(s)
	if s=='1':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/hello_hello.mp3')
	elif s=='2':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/scan_qrcode_and_input_number.mp3')
	elif s=='3':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/wrong_number_input_again.mp3')
	elif s=='4':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_put_in_the_meals.mp3')
	elif s=='5':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_press_the_button_afte_put_in_x.mp3')
	elif s=='6':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/your_meal_arrived.mp3')
	elif s=='7':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/I_am_coming_for_delivering_meals.mp3')
	elif s=='8':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/scan_qrcode_and_input_number.mp3')
	elif s=='9':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/wrong_number_input_again.mp3')
	elif s=='10':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_take_out_the_meal.mp3')
	elif s=='11':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/please_press_the_button_after_take_out_the_meal.mp3')
	elif s=='12':
    		playsound('catkin_ws/src/voice_pkg/src/files_order/thank_you_for_ordering_enjoy_your_meal.mp3')
	elif s=='13':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/hello.mp3')
	elif s=='14':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/thank_you.mp3')
	elif s=='15':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/bye_bye_see_you_next_time.mp3')
	elif s=='16':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/excuse_me.mp3')
	elif s=='17':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/excuse_me_coming_through.mp3')
	elif s=='18':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/be_careful.mp3')
	elif s=='19':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/watch_out.mp3')
	elif s=='20':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/can_you_help_me.mp3')
	elif s=='21':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/can_you_open_the_door_for_me.mp3')
	elif s=='22':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/have_a_good_day.mp3')
	elif s=='23':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/wrong_operation.mp3')
	elif s=='24':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/please_do_it_again.mp3')
	elif s=='25':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/correct_or_not.mp3')
	elif s=='26':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/low_battery_warning.mp3')
	elif s=='27':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/system_error.mp3')
	elif s=='28':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/please_call_technical_staff.mp3')
	elif s=='29':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/loading.mp3')
	elif s=='30':
    		playsound('catkin_ws/src/voice_pkg/src/commonly_used/please_wait.mp3')
	elif s=='31':
    		playsound('catkin_ws/src/voice_pkg/src/elevator/entering_elevator.mp3')
	elif s=='32':
    		playsound('catkin_ws/src/voice_pkg/src/elevator/leaving_elevator.mp3')
	elif s=='34':
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_turning_right.mp3')
	elif s=='35':
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_turning_left.mp3')
	elif s=='36':
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/excuse_me_coming_through.mp3')
	elif s=='37':
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_reversing.mp3')
	elif s=='39':
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_forward.mp3')
	elif s=='40':
    		playsound('catkin_ws/src/voice_pkg/src/during_moving/be_careful_when_moving.mp3')
	elif s=='41':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_1st_floor.mp3')
	elif s=='42':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_2nd_floor.mp3')
	elif s=='43':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_3rd_floor.mp3')
	elif s=='44':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_4th_floor.mp3')
	elif s=='45':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_5th_floor.mp3')
	elif s=='46':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_6th_floor.mp3')
	elif s=='47':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_7th_floor.mp3')
	elif s=='48':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_8th_floor.mp3')
	elif s=='49':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_9th_floor.mp3')
	elif s=='50':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_10th_floor.mp3')
	elif s=='51':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_11th_floor.mp3')
	elif s=='52':
    		playsound('catkin_ws/src/voice_pkg/src/floor/help_me_press_12th_floor.mp3')
	elif s=='53':
    		playsound('catkin_ws/src/voice_pkg/src/elevator/be_careful_when_press_button.mp3')


if __name__=='__main__':
	rospy.init_node('mp3player_python_node')
	rospy.Subscriber('buttom',String,callback)	
	rospy.spin()
