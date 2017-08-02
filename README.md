# performance_tests
This package allows you to run performance tests to compare the performance between RosCpp and RosPy based Publishers and Subscribers. The current package has RosCpp/RosPy Publishers publishing a simple string message and RosCpp/RosPy Subscribers 
to measure the reception time. The below scenarios are considered for comparison.
1. C++ publisher to C++ subscriber
2. C++ publisher to Python subscriber
3. Python publisher to C++ subscriber
4. Python publisher to Python subscriber

### How to Run?
1.Run the publisher
```
rosrun performance_tests performance_tests_publisher 
(or)
rosrun performance_tests text_publisher.py
```
2.Run the subscriber
```
rosrun performance_tests performance_tests_subscriber
(or)
rosrun performance_tests text_subscriber.py
```
3.Run the script to measure reception rate at different publishing frequencies
```
ipython -i src/performance_test.py
```
Use function 'find_subscriber_frequency' to measure subscriber frequencies for different publishing
rates = [1,10,100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,6000,7000,8000,9000,10000]

Use function 'barplot_data' to bar plot the data for 4 scenarios resulting in this image comparing the frequencies.

![Alt text](pc.png?raw=true "Results")

### Comments
Roscpp's performance can be really compared with messages which requires heavy computation. In this case, we consider only a string message which doesn't take resources to compute. So the performance is almost the same between Cpp and Py. But there is a drop in average subcriber frequencies for Rospy publishers when the publishing rates increase beyound 2500hz though it doesn't correspond to a real time scenario. Roscpps perform better than Rospy and this is quite dependant on the computation involved in publsihing the messages each and every time. 

