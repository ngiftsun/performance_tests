#!/usr/bin/env python

import rospy
from performance_tests.msg import SuperAwesome
#from dynamic_reconfigure.server import Server
#from performance_tests.cfg import performanceTestsConfig
from performance_tests.srv import SetLoopRate


pub_rate = 1
rate = 0

# def cb(config, level):
#     global pub_rate,rate
#     pub_rate = config.publisher_rate
#     rate = rospy.Rate(pub_rate)
#     return config

def set_loop_rate(req):
    global pub_rate,rate
    pub_rate = req.loop_rate
    rate = rospy.Rate(pub_rate)
    return True
        
if __name__ == '__main__':
    #global pub_rate,rate
    pub = rospy.Publisher('performance_test_msg', SuperAwesome, queue_size=1000)
    rospy.init_node('publisher_py', anonymous=True)
    #srv = Server(performanceTestsConfig,cb)
    slr = rospy.Service('set_loop_rate', SetLoopRate, set_loop_rate)
    rate = rospy.Rate(pub_rate)

    try:
        while not rospy.is_shutdown():
            msg = SuperAwesome()
            msg.secret = " Hello Blue Ocean Robotics !!! %s" % rospy.get_time()
            rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass


       