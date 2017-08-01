#include "ros/ros.h"
#include "performance_tests/SuperAwesome.h"
#include "performance_tests/RequestSubscriberStats.h"


// bool add(beginner_tutorials::AddTwoInts::Request  &req,
//          beginner_tutorials::AddTwoInts::Response &res)
// {
//   res.sum = req.a + req.b;
//   ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
//   ROS_INFO("sending back response: [%ld]", (long int)res.sum);
//   return true;
// }


class DataSubscriber
{
  private:
    int count;
    float sum;
    bool reset;
    ros::Time begin,end;
    ros::Duration time_lapse;
  public:
    float avg;
    DataSubscriber();
    void chatterCallback(const performance_tests::SuperAwesome::ConstPtr& msg);
    bool requestAverageRate(performance_tests::RequestSubscriberStats::Request  &req,
                             performance_tests::RequestSubscriberStats::Response  &res);
};

DataSubscriber::DataSubscriber():sum(0),count(0),reset(false){}

void DataSubscriber::chatterCallback(const performance_tests::SuperAwesome::ConstPtr& msg)
{
  end = ros::Time::now();
  ros::Duration time_lapse = end-begin;
  //ROS_INFO("%f", 1/time_lapse.toSec());
  if (reset == true)
  {
    sum = 0; count=0;
    reset = false;
  }
  else
  {  
    sum = sum + time_lapse.toSec();
    count = count + 1;
  }
  begin = ros::Time::now();
}


bool DataSubscriber::requestAverageRate(performance_tests::RequestSubscriberStats::Request  &req,
                                        performance_tests::RequestSubscriberStats::Response  &res)
{
 avg = 1/(sum/count); 
 res.avg_rate = avg;
 reset = req.reset; 
 return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "text_subscriber_cpp"); 
  ros::NodeHandle n;
  DataSubscriber ds;
  ros::Subscriber sub = n.subscribe("performance_test_msg", 1000, &DataSubscriber::chatterCallback, &ds);
  ros::ServiceServer stats_service = n.advertiseService("request_subscriber_stats", &DataSubscriber::requestAverageRate, &ds);
  ros::spin();
  return 0;
}