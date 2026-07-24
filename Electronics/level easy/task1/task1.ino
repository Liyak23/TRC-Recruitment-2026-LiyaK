// Task 1: Traffic Signal Controller with Serial Output

void setup() {
  Serial.begin(9600);
}

void loop() {

  // Red Light
  Serial.println("RED LIGHT - STOP");
  delay(10000);   // 10 seconds

  // Green Light
  Serial.println("GREEN LIGHT - GO");
  delay(7000);    // 7 seconds

  // Yellow Light
  Serial.println("YELLOW LIGHT - WAIT");
  delay(3000);    // 3 seconds

  // The cycle repeats automatically
}
