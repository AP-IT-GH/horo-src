#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh

sudo apt-get install -y ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers

cd ~/catkin_ws/src/
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
source /opt/ros/indigo/setup.bash
cd ~/catkin_ws && catkin_make && echo "\nInstalled ROS"

sudo apt-get install -y ros-kinetic-realsense2-camera && echo "\nInstalled RealSense for ROS"

cd ~/catkin_ws/src && git clone https://github.com/uArm-Developer/RosForSwiftAndSwiftPro.git
sudo apt-get install -y ros-kinetic-serial
cd ~/catkin_ws && catkin_make && echo "\nInstalled SwiftPro for ROS"

