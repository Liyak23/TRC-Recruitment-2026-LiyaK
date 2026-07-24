// Task 3: Automatic Street Light Control System

int ldrPin = A0;
int ledPin = 13;

int ldrValue;

// Threshold value
int threshold = 500;

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
}

void loop() {

  // Read the LDR value
  ldrValue = analogRead(ldrPin);

  // Display the LDR value
  Serial.print("LDR Value: ");
  Serial.println(ldrValue);

  // Check the light intensity
  if (ldrValue < threshold) {

    // Dark condition
    digitalWrite(ledPin, HIGH);
    Serial.println("Dark - Street Light ON");
  }
  else {

    // Sufficient light condition
    digitalWrite(ledPin, LOW);
    Serial.println("Bright - Street Light OFF");
  }

  Serial.println("----------------------");

  delay(1000);
}
