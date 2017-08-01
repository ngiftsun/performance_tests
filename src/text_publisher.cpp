#include "ros/ros.h"

#include "performance_tests/SuperAwesome.h"

// incase you use the loop rate from params and dynamic reconfigure
//#include "performance_tests/performanceTestsConfig.h"
//#include <dynamic_reconfigure/server.h>

#include "performance_tests/SetLoopRate.h"

#include <sstream>


// using dynamic configure to change loop rate //
/*
void configCallback(performance_tests::performanceTestsConfig &config, uint32_t level)
{
  pub_rate = config.publisher_rate;
}
*/

//
// Default Loop Rate
int pub_rate = 1;

bool setLoopRate(performance_tests::SetLoopRate::Request  &req,
                 performance_tests::SetLoopRate::Response &res)
{
  pub_rate = req.loop_rate;

}


int main(int argc, char **argv)
{

  ros::init(argc, argv, "text_publisher_cpp");

  // using dynamic configure to change loop rate //
  /*
  dynamic_reconfigure::Server<performance_tests::performanceTestsConfig> srv_;
  dynamic_reconfigure::Server<performance_tests::performanceTestsConfig>::CallbackType cb_;
  cb_ = boost::bind(configCallback, _1, _2);
  srv_.setCallback(cb_);
  */
  
  ros::NodeHandle n;
  
  ros::Publisher text_pub = n.advertise<performance_tests::SuperAwesome>("performance_test_msg", 1000);
  ros::ServiceServer set_looprate_srv = n.advertiseService("set_loop_rate", setLoopRate);

  // count'ing published messages
  //int count = 0;
  performance_tests::SuperAwesome msg;
  // setting the message
  std::stringstream ss;
  ss << " Hello Blue Ocean Robotics";
  msg.secret = ss.str();

  while (ros::ok())
  {
    ros::Rate r(pub_rate);  
    //ROS_INFO("%s", msg.secret.c_str());

    text_pub.publish(msg);

    ros::spinOnce();

    r.sleep();
    
    //++count;
  }

  return 0;
}