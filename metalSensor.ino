int metalSensor = 8;

void setup() {
  Serial.begin(9600);
  pinMode(metalSensor, INPUT);
}

void loop() {
  int sensorState = digitalRead(metalSensor);
  Serial.println(sensorState);
  delay(1000);
}
