#!/usr/bin/env python
import rospy
from swiftpro.msg import position
from swiftpro.msg import status
pub_position = rospy.Publisher('/sp2_position_write_topic',position,queue_size=1)
pub_pump = rospy.Publisher('/sp2_pump_topic',status,queue_size=1)
rospy.init_node('sp2_control')

home_coords = position()
coords1 = position()
coords2 = position()
block_coords = position()
belt_coords = position()
maxFront_coords = position()
maxLeft_coords = position()
pump_value = status()

home_coords.x= 102
home_coords.y= 0
home_coords.z= 41

belt_coords.x = 164
belt_coords.y = 0
belt_coords.z = 65

coords1.x = 158
coords1.y = 65
coords1.z = 73

block_coords.x = 155
block_coords.y = 68
block_coords.z = 52

coords2.x = 160
coords2.y = 67
coords2.z = 160


maxFront_coords.x = 300
maxFront_coords.y = 0
maxFront_coords.z = 155

maxLeft_coords.x = 8
maxLeft_coords.y = 314
maxLeft_coords.z = 140

delay = 0.5 # half a second
rate = rospy.Rate(10) # 10hz

def MoveSP2():
    for x in range(3):
        pub_position.publish(home_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        pub_position.publish(belt_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        pub_position.publish(coords1)
        rate.sleep()

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
        pub_position.publish(maxFront_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        pub_position.publish(maxLeft_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        pub_position.publish(maxFront_coords)
        rate.sleep()

    rospy.sleep(delay)

    pump_value = 0
    pub_pump.publish(pump_value)

    rospy.sleep(delay*2)

    for x in range(3):
        pub_position.publish(home_coords)
        rate.sleep()

if __name__ == '__main__':
    MoveSP2()
