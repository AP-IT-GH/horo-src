# Hololens Robotics ROS

## Setting up the workspace

Create our catkin workspace folder.

```
$ mkdir ~/horo_ws
```

Clone the repo inside the catkin workspace.

```
$ cd ~/horo_ws
$ git clone https://github.com/AP-Elektronica-ICT/horo-src.git
```

Change the repo folder name to "src".

```
$ mv horo-src-master src
```

Build the workspace.

```
$ cd ~/horo_ws
$ catkin_make
```
> Normally a build and devel folder will be made in the workspace.

Before continuing make sure the `devel/setup.bash` file is sourced at startup.

```
$ sudo nano ~/.bashrc
```

Go to the bottom of the file and add the following rule `source ~/horo_ws/devel/setup.bash`. Then save and close the file.
> You need to restart your terminal or use the `$ source ~/.bashrc` command for these changes to take effect.

To make sure everything is working.

```
$ echo $ROS_PACKAGE_PATH
/home/ros1604/horo_ws/src:/home/ros1604/catkin_ws/src:/opt/ros/kinetic/share
```
[More information about setting up catkin workspaces.](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

## Install the Turtlebot3 ROS packages

Follow [this](https://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/#install-dependent-ros-1-packages) guide to install the Turtlebot3 ROS packages.

Add this to the .bashrc file

```
$ export TURTLEBOT3_MODEL=waffle_pi
```

And source setup file
```
$ roscd
$ source devel/setup.bash
```

## Running the simulation

Run the simulation

```
$ roslaunch horo_simulations horo_world.launch
```
