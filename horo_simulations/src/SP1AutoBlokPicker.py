#!/usr/bin/env python
import rospy
from swiftpro.msg import position
from swiftpro.msg import status
pub_position = rospy.Publisher('/sp1_position_write_topic',position,queue_size=1)
pub_pump = rospy.Publisher('/sp1_pump_topic',status,queue_size=1)
rospy.init_node('sp1_control')

home_coords = position()
coords1 = position()
coords2 = position()
block_coords = position()
belt_coords = position()
pump_value = status()

home_coords.x= 102
home_coords.y= 0
home_coords.z= 41

coords1.x = 170
coords1.y = 0
coords1.z = 150

coords2.x = 69
coords2.y = -225
coords2.z = 150

block_coords.x = 73
block_coords.y = -218
block_coords.z = 33

belt_coords.x = 164
belt_coords.y = 0
belt_coords.z = 65

delay = 0.5 # half a second


rate = rospy.Rate(10) # 10hz

for x in range(3):
    pub_position.publish(home_coords)
    rate.sleep()

rospy.sleep(delay)

for x in range(3):
    pub_position.publish(coords1)
    rate.sleep()

rospy.sleep(delay)

for x in range(3):
    pub_position.publish(coords2)
    rate.sleep()

rospy.sleep(delay)

for x in range(3):
    pub_position.publish(block_coords)
    rate.sleep()

rospy.sleep(delay)

pump_value = 1
pub_pump.publish(pump_value)

rospy.sleep(delay)

for x in range(3):
    pub_position.publish(coords2)
    rate.sleep()

rospy.sleep(delay)

for x in range(3):
    pub_position.publish(coords1)
    rate.sleep()

rospy.sleep(delay)

for x in range(3):
    pub_position.publish(belt_coords)
    rate.sleep()

rospy.sleep(delay)

pump_value = 0
pub_pump.publish(pump_value)

rospy.sleep(delay*2)

for x in range(3):
    pub_position.publish(home_coords)
    rate.sleep()
