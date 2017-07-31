#include "ros/ros.h"
#include "performance_tests/SuperAwesome.h"

void chatterCallback(const performance_tests::SuperAwesome::ConstPtr& msg)
{
  ROS_INFO("%s", msg->secret.c_str());
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "text_subscriber_cpp");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("performance_test_msg", 1000, chatterCallback);

  ros::spin();

  return 0;
}