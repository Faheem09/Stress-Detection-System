// Example Arduino Stress Detection Data Collection
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Stress Data Collection Started");
}

void loop() {
  // Simulate sensor readings (replace with actual sensor data)
  float heart_rate = random(60, 100);  // Simulated heart rate (BPM)
  float skin_temp = random(30, 35);    // Simulated skin temperature (°C)
  float gsr = random(500, 1000);       // Simulated galvanic skin response

  // Print data in CSV format
  Serial.print(heart_rate);
  Serial.print(",");
  Serial.print(skin_temp);
  Serial.print(",");
  Serial.println(gsr);

  delay(100);  // Simulate a sampling rate of 10 Hz
}
