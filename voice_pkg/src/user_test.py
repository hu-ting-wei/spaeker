#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt16

if __name__=='__main__':
	rospy.init_node('user',anonymous=True)
	pub = rospy.Publisher('buttom',UInt16,queue_size=10)
	rate = rospy.Rate(0.166)

	while not rospy.is_shutdown():
		counter = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
		for s in counter:
			pub.publish(int(s))
			rospy.loginfo(s)
			rate.sleep()
