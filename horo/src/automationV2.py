#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import UInt16
from swiftpro.msg import position
from swiftpro.msg import status


#string_msgs for realsense
from std_msgs.msg import String

#message file for goal status of WafflePi
from actionlib_msgs.msg import GoalStatusArray
from geometry_msgs.msg import PoseWithCovarianceStamped
from move_base_msgs.msg import MoveBaseActionGoal

##############################################################################################
#SP1
##############################################################################################
sp1_pub_position = rospy.Publisher('/sp1_position_write_topic',position,queue_size=1)
sp1_pub_pump = rospy.Publisher('/sp1_pump_topic',status,queue_size=1)

sp1_coords1 = position()
sp1_coords2 = position()
sp1_block_coords = position()
sp1_belt_coords = position()
sp1_pump_value = status()

sp1_coords1.x = 170
sp1_coords1.y = 0
sp1_coords1.z = 150

sp1_coords2.x = 69
sp1_coords2.y = -225
sp1_coords2.z = 150

sp1_block_coords.x = 73
sp1_block_coords.y = -218
sp1_block_coords.z = 33

sp1_belt_coords.x = 160
sp1_belt_coords.y = 0
sp1_belt_coords.z = 65

##############################################################################################
#SP2
##############################################################################################
sp2_pub_position = rospy.Publisher('/sp2_position_write_topic',position,queue_size=1)
sp2_pub_pump = rospy.Publisher('/sp2_pump_topic',status,queue_size=1)

sp2_coords1 = position()
sp2_coords2 = position()
sp2_block_coords = position()
sp2_belt_coords = position()
sp2_maxFront_coords = position()
sp2_maxLeft_coords = position()
sp2_pump_value = status()

sp2_belt_coords.x = 164
sp2_belt_coords.y = 0
sp2_belt_coords.z = 65

sp2_coords1.x = 158
sp2_coords1.y = 65
sp2_coords1.z = 73

sp2_block_coords.x = 155
sp2_block_coords.y = 68
sp2_block_coords.z = 52

sp2_coords2.x = 160
sp2_coords2.y = 67
sp2_coords2.z = 160

sp2_maxFront_coords.x = 300
sp2_maxFront_coords.y = 0
sp2_maxFront_coords.z = 155

sp2_maxLeft_coords.x = 8
sp2_maxLeft_coords.y = 314
sp2_maxLeft_coords.z = 140

##############################################################################################
#SP1 & SP2
##############################################################################################
home_coords = position()
home_coords.x= 102
home_coords.y= 0
home_coords.z= 41
delay = 0.5 # half a second


##############################################################################################
#SP1 & SP2 & CONVEYOR MOVEMENT FUNCTIONS
##############################################################################################
def MoveSP1():
    for x in range(3):
        sp1_pub_position.publish(home_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp1_pub_position.publish(sp1_coords1)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp1_pub_position.publish(sp1_coords2)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp1_pub_position.publish(sp1_block_coords)
        rate.sleep()

    rospy.sleep(delay)

    sp1_pump_value = 1
    sp1_pub_pump.publish(sp1_pump_value)

    rospy.sleep(delay)

    for x in range(3):
        sp1_pub_position.publish(sp1_coords2)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp1_pub_position.publish(sp1_coords1)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp1_pub_position.publish(sp1_belt_coords)
        rate.sleep()

    rospy.sleep(delay)

    sp1_pump_value = 0
    sp1_pub_pump.publish(sp1_pump_value)

    rospy.sleep(delay*2)

    for x in range(3):
        sp1_pub_position.publish(home_coords)
        rate.sleep()

def MoveSP2():
    for x in range(3):
        sp2_pub_position.publish(home_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp2_pub_position.publish(sp2_belt_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp2_pub_position.publish(sp2_coords1)
        rate.sleep()

    for x in range(3):
        sp2_pub_position.publish(sp2_block_coords)
        rate.sleep()

    rospy.sleep(delay)

    sp2_pump_value = 1
    sp2_pub_pump.publish(sp2_pump_value)

    rospy.sleep(delay)

    for x in range(3):
        sp2_pub_position.publish(sp2_coords2)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp2_pub_position.publish(sp2_maxFront_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp2_pub_position.publish(sp2_maxLeft_coords)
        rate.sleep()

    rospy.sleep(delay)

    for x in range(3):
        sp2_pub_position.publish(sp2_maxFront_coords)
        rate.sleep()

    rospy.sleep(delay)

    sp2_pump_value = 0
    sp2_pub_pump.publish(sp2_pump_value)

    rospy.sleep(delay*2)

    for x in range(3):
        sp2_pub_position.publish(home_coords)
        rate.sleep()

def Belt(dataIn):
    pub_msg = UInt16()
    if (dataIn == 1):
        # turn on belt
        pub_msg.data = 1

    else:
        #turn off belt
        pub_msg.data = 0

    for x in range(3):
        pub_belt.publish(pub_msg)
##############################################################################################
#ROS
##############################################################################################
tempBlockReady = 0
tempBlockStock = 0

#realsense coordinates
rs_x = 0
rs_y = 0

#WafflePi
wafflePi_status = 0


def BlockReady_callback(dataIn):
    global tempBlockReady
    tempBlockReady = dataIn.data

def BlockStock_callback(dataIn):
    global tempBlockStock
    tempBlockStock = dataIn.data

#Realsense coordinates callback
def RS_coordinates_callback(dataIn):
    global rs_x
    global rs_y

    coord = dataIn.data.split(',')
    rs_x = coord[0]
    rs_y = coord[1]

#WafflePi goal status callback
def PiGoalState_callback(dataIn):
    global wafflePi_status
    if (dataIn.status_list):
        #wafflePi_status = dataIn.status_list.status
        rospy.loginfo(dataIn.status_list[0].status)
        wafflePi_status = dataIn.status_list[0].status
    else :
        rospy.loginfo("lijst leeg")

def SetInitialPose():
    pub_msg = PoseWithCovarianceStamped()
    #header
    pub_msg.header.frame_id = "map"
    #pose
    pub_msg.pose.pose.position.x = -0.0563785433769
    pub_msg.pose.pose.position.y = -0.0411755442619
    pub_msg.pose.pose.position.z = 0.0

    pub_msg.pose.pose.orientation.x = 0.0
    pub_msg.pose.pose.orientation.y = 0.0
    pub_msg.pose.pose.orientation.z = 0.0515177204666
    pub_msg.pose.pose.orientation.w = 0.998672080554
    
    pub_msg.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]

    rospy.loginfo(pub_msg)
    wafflepi_initial_pose.publish(pub_msg)

def SetCurrentGoal(pos_x, pos_y, pos_z=0.0, ori_x=0.0, ori_y=0.0, ori_z=0.0, ori_w=1.0):
    pub_msg = MoveBaseActionGoal()
    #header
    pub_msg.goal.target_pose.header.frame_id = "map"
    
    pub_msg.goal.target_pose.pose.position.x = pos_x
    pub_msg.goal.target_pose.pose.position.y = pos_y
    pub_msg.goal.target_pose.pose.position.z = pos_z

    pub_msg.goal.target_pose.pose.orientation.x = ori_x
    pub_msg.goal.target_pose.pose.orientation.y = ori_y
    pub_msg.goal.target_pose.pose.orientation.z = ori_z
    pub_msg.goal.target_pose.pose.orientation.w = ori_w


    rospy.loginfo(pub_msg)
    wafflepi_current_goal.publish(pub_msg)

def Check():
    global tempBlockReady
    global tempBlockStock
    print("Checking: stock=" + str(tempBlockStock) + " || ready=" + str(tempBlockReady))
    
    if(tempBlockReady == 1):
        Belt(0)
    
    if (tempBlockStock == 1 and tempBlockReady == 0):   # if there's stock but no block is ready
        MoveSP1()                                       # execute SP1
        Belt(1)                                         # and turn on belt
        while tempBlockReady == 0:
            time.sleep(1)                               # waits until block arrives at color sensor

    if (tempBlockReady == 1 and wafflePi_status == 3):                           # if block is ready
                                                 # turn of belt
        #SetDestinationCoords()
        ## DEBUG:
        #output = "x coord="+str(rs_x)+" || y coord="+str(rs_y)
        #rospy.loginfo(output)
        ##
        MoveSP2()                                       # and execute SP2

rospy.init_node('automationV2')
rospy.Subscriber("block_ready",UInt16,BlockReady_callback)
rospy.Subscriber("block_stock",UInt16,BlockStock_callback)
pub_belt = rospy.Publisher("belt_state",UInt16,queue_size=1)

#wafflePi publisher
wafflepi_initial_pose = rospy.Publisher('initialpose',PoseWithCovarianceStamped,queue_size=1)
wafflepi_current_goal = rospy.Publisher('move_base/goal',MoveBaseActionGoal,queue_size=1)

#Realsense subscription
rospy.Subscriber("realsense",String,RS_coordinates_callback)

#WafflePi subscription
rospy.Subscriber("move_base/status",GoalStatusArray,PiGoalState_callback)

rate = rospy.Rate(10) # 10hz

time.sleep(2)

for x in range(3):
    SetInitialPose()
    rospy.loginfo("set initial pose")

time.sleep(2)

#for x in range(3):
    #SetCurrentGoal(1.07001495361,0.404617369175)
    #rospy.loginfo("set current goal")

while not rospy.is_shutdown():
    Check()
    time.sleep(1)
