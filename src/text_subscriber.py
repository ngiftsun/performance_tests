#!/usr/bin/env python
import rospy
from performance_tests.msg import SuperAwesome
from performance_tests.srv import *

begin = 0
end = 0
avg = 0
sum = 0
count = 0
reset = 0

def cb(data):
    global end,begin,sum,reset,count
    end = rospy.get_rostime()
    time_lapse = (end-begin).to_sec()
    # rospy.loginfo("%f", 1/time_lapse)
    if (reset == True):
        sum = 0; count=0;
        reset = False
    else: 
        sum = sum + time_lapse
        count = count + 1;
    begin = rospy.get_rostime()

def request_stats(req):
    global sum,reset
    reset = req.reset
    avg = 1/(sum/count); 
    return RequestSubscriberStatsResponse(avg)
        
    
if __name__ == '__main__':
    rospy.init_node('text_subscriber_py', anonymous=True)
    rospy.Subscriber("performance_test_msg", SuperAwesome, cb,queue_size=1000)
    s = rospy.Service('request_subscriber_stats', RequestSubscriberStats, request_stats)
    begin = rospy.get_rostime()
    rospy.spin()
