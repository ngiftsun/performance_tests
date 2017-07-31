#!/usr/bin/env python
import rospy
from performance_tests.msg import SuperAwesome

def cb(data):
    rospy.loginfo("%s", data.secret)
    
def subscriber():

    rospy.init_node('text_subscriber_py', anonymous=True)

    rospy.Subscriber("performance_test_msg", SuperAwesome, cb)

    rospy.spin()

if __name__ == '__main__':
    subscriber()