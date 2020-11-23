/*
 * BASED ON CODE FROM UFACTORY, A LOT OF CODE IS NOT BEING USED, ONLY CODE BEING USED IS HERE
 */

//### ROS ###
#include <ros.h>
#include <std_msgs/String.h>
ros::NodeHandle nh;



//###########
//### VARS ##
int irSensor,msgBLOCK_STOCK,msgBLOCK_READY;
//###########

#include "main.h"
#define SOFTWARE_VERSION "V1.2.5\n"
extern enum control_systerm system_s;
extern enum pick_mode_e mode;
bool work_state = false;
bool detect_switch_flag = false;
extern Adafruit_TCS34725 tcs;
Ultrasonic ultrasonic(23);
extern int i;
void setup() {
  Serial.begin(115200);
  Serial.println(SOFTWARE_VERSION);
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
   {
   
   }else if (irSensor == 0)   // 2 = BLOCK AVAILABLE = PUB.BLOCK_STOCK = 1
   {
   
   }
    
  
  //BELT
    //msgBELT_ON = SUB.BELT_ON
  if (msgBELT_ON == 1)
    //belt_move();
  else if (msgBELT_ON == 0)
    //belt_stop();
    
  
  //COLOR SENSOR
  //String color = get_color();
  //Serial.println(color);
  if (color == 'nothing')
  {
    //msgBLOCK_READY = sub.BLOCK_READY
    //msgBLOCK_STOCK = sub.BLOCK_STOCK
    if (msgBLOCK_READY == 0 && msgBLOCK_STOCK)
    {
      //service sp1.call
      //pub.BELT_ON = 1
    }
  }

  }
  


  delay(100);
  /*
  //first_page(); //Oled screen
  get_color(); //Get color reading, if nothing,
  conver_work();
  */
}
