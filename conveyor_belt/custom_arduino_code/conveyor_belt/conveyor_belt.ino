/*
 * BASED ON CODE FROM UFACTORY, A LOT OF CODE IS NOT BEING USED, ONLY CODE BEING USED IS HERE
 */
#include "main.h"
extern enum control_systerm system_s;
extern enum pick_mode_e mode;
bool work_state = false;
bool detect_switch_flag = false;
extern Adafruit_TCS34725 tcs;
Ultrasonic ultrasonic(23);
extern int i;

//### VARS ###
int irSensor, colorLength;
String color;



//### ROS ###
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/UInt16.h>
ros::NodeHandle nh;

//BELT
void BeltCallback(const std_msgs::UInt16 & belt_state_msg)
{
  if (belt_state_msg.data == 1)
    belt_move();
  else if (belt_state_msg.data == 0)
    belt_stop();
    
}

std_msgs::String str_msg;
std_msgs::UInt16 int_msg;


ros::Subscriber<std_msgs::UInt16> belt_sub("belt_state", &BeltCallback);
ros::Publisher block_ready_pub("block_ready",&int_msg);
ros::Publisher block_stock_pub("block_stock",&int_msg);

//###########

void setup() {
  //Serial.begin(115200);
  pinMode(25, INPUT_PULLUP);
  belt_init();
  oled_init();
  convert_rgb();
  //initiate stepper driver
  step_init_ll();
  tcs.begin();
  system_s = conver_belt;
  i = 0;
  mode = NOTHING_MODE;
  delay(1000);

  //### ROS ###
  nh.initNode();
  nh.subscribe(belt_sub);
  nh.advertise(block_ready_pub);
  nh.advertise(block_stock_pub);
  
}
void loop() {
  /*
   * NECESSARY STEPS:
   *  1) CHECK IF BLOCK IS IN FRONT OF COLOR SENSOR
   *    - IF NOT => PUBLISH TOPIC BLOCK_READY = 0
   *    - IF YES => PUBLISH TOPIC BLOCK_READY = 1 ++ BELT OFF
   *  
   *  2) CHECK IF BLOCK IN FRONT OF IR SENSOR
   *    - IF NOT => PUBLISH TOPIC BLOCK_STOCK = 0
   *    - IF YES => PUBLISH TOPIC BLOCK_STOCK = 1
   *    
   *  3) IF TOPIC BLOCK_READY = 0 ++ BLOCK_STOCK = 1 => SERVICE SP1=: PUT BLOCK FROM STOCK ON BELT ++ BELT ON
   *  
   *  3 TOPICS: BLOCK_STOCK | BELT_ON | BLOCK_READY
   */

  // IR SENSOR
  irSensor = digitalRead(25);
   if (irSensor == 1)         // 1 = STOCK EMPTY = PUB.BLOCK_STOCK = 0
    int_msg.data = 0;
   else                       // 2 = BLOCK AVAILABLE = PUB.BLOCK_STOCK = 1
    int_msg.data = 1;
    
  block_stock_pub.publish(&int_msg);


  
  //COLOR SENSOR
  color = get_color();
  colorLength = color.length();
  
  if (colorLength > 6) //if length of word = 7 (nothing) then no block in front of sensor (just =='nothing' didn't work)
    int_msg.data = 0;
  else
    int_msg.data = 1;

  block_ready_pub.publish(&int_msg);
  nh.spinOnce();
  delay(100);
}
