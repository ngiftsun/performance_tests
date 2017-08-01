#!/usr/bin/env python
import rospy
from performance_tests.srv import SetLoopRate
from performance_tests.srv import RequestSubscriberStats

import matplotlib.pyplot as plt
import numpy as np

rates = [1,10,100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,6000,7000,8000,9000,10000]
rates_str = [str(i) for i in rates]
x_pos = np.arange(len(rates))
width = 0.2  
subscriber_rate = []

fig, ax = plt.subplots()

def find_subscriber_frequency():
    srate = []
    slr = rospy.ServiceProxy('set_loop_rate', SetLoopRate)
    rss = rospy.ServiceProxy('request_subscriber_stats', RequestSubscriberStats)
    for rate in rates:
        print "Setting rate:" + str(rate)
        try:
            resp = slr(rate)
            rospy.sleep(0.2)
            resp = rss(True)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
        rospy.sleep(10)
        resp = rss(False)
        print resp.avg_rate
        srate.append(resp.avg_rate)
    try:
        resp = slr(1)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e  
    return srate    

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def barplot_data(d1,d2,d3,d4):
    rects1 = ax.bar(x_pos, d1, width, color='r') 
    rects2 = ax.bar(x_pos+width, d2, width, color='b')
    rects3 = ax.bar(x_pos+(2*width), d3, width, color='g')
    rects4 = ax.bar(x_pos+(3*width), d4, width, color='y')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Subscriber Rate')
    ax.set_xlabel('Publisher Rate')
    ax.set_title('Subscriber Rate Comparison')
    ax.set_xticks((x_pos + 2*width))
    ax.set_xticklabels(tuple(rates_str))    

    ax.legend((rects1[0], rects2[0],rects3[0],rects4[0]), ('RosCppPub->RosCppSub', 'RosCppPub->RosPySub','RosPyPub->RosCppSub','RosPyPub->RosPySub'))

    #autolabel(rects1)
    #autolabel(rects2)
    #autolabel(rects3)
    #autolabel(rects4)
    plt.show()

if __name__ == '__main__':
    rospy.init_node('performance_test', anonymous=True)
