#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__=='__main__':
	rospy.init_node('user',anonymous=True)
	pub = rospy.Publisher('buttom',String,queue_size=10)

	while not rospy.is_shutdown():
		s = raw_input()
		pub.publish(s)
		rospy.loginfo(s)
		
