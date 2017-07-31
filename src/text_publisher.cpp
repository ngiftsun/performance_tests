#include "ros/ros.h"
#include "performance_tests/SuperAwesome.h"
#include <sstream>

int main(int argc, char **argv)
{

  ros::init(argc, argv, "text_publisher_cpp");

  ros::NodeHandle n;

  ros::Publisher text_pub = n.advertise<performance_tests::SuperAwesome>("performance_test_msg", 1000);

  ros::Rate loop_rate(10);

  int count = 0;
  while (ros::ok())
  {

    performance_tests::SuperAwesome msg;
    
    // setting the message
    std::stringstream ss;
    ss << " Hello Blue Ocean Robotics !!!" << count;
    msg.secret = ss.str();
    
    ROS_INFO("%s", msg.secret.c_str());

    text_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    
    ++count;
  }


  return 0;
}