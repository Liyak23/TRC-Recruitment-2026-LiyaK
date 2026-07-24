// Task 2: Temperature Monitoring System

int temperature;

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(A0));
}

void loop() {

  // Generate a random temperature between 20°C and 45°C
  temperature = random(20, 46);

  // Display the current temperature
  Serial.print("Current Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  // Check the temperature conditions
  if (temperature > 40) {
    Serial.println("Fan ON");
  }
  else if (temperature < 25) {
    Serial.println("Fan OFF");
  }
  else {
    Serial.println("Fan in Standby");
  }

  Serial.println("----------------------");

  delay(2000);   // Wait for 2 seconds before the next reading
}
