#include <Stepper.h>

// Motor pin definitions
#define motorPin1  1     // IN1 on the ULN2003 driver 1
#define motorPin2  2     // IN2 on the ULN2003 driver 1
#define motorPin3  3     // IN3 on the ULN2003 driver 1
#define motorPin4  4     // IN4 on the ULN2003 driver 1

// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48
Stepper stepper1(512, motorPin1, motorPin3, motorPin2, motorPin4);

void setup()
{
  Serial.begin(115200);
  stepper1.setSpeed(30);
}

void loop()
{
  if (Serial.available() > 0)
  {
    char data = Serial.read();
    
    if (data == '1')
    {
      stepper1.step(75);
    }
    
    if (data == '2')
    {
      stepper1.step(-75);
    }
  }
}
    
