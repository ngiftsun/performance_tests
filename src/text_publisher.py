#!/usr/bin/env python

import rospy
from performance_tests.msg import SuperAwesome

def publisher():
    pub = rospy.Publisher('performance_test_msg', SuperAwesome, queue_size=10)
    rospy.init_node('publisher_py', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = SuperAwesome()
        msg.secret = " Hello Blue Ocean Robotics !!! %s" % rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass