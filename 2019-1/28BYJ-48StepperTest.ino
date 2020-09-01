#include <Stepper.h>

#define STEPS 2038 //2038 steps == 1 rev

Stepper stepper(STEPS, 8, 10, 9, 11);

void setup() {

  
}

void loop() {
  stepper.setSpeed(10);
  stepper.step(2038);
  delay(1000);
  stepper.setSpeed(6);
  stepper.step(-2038);
}

