#include "Arduino_BHY2.h"

SensorXYZ accelerometer(SENSOR_ID_ACC);
SensorXYZ gyro(SENSOR_ID_GYRO);

// Set interval to 100ms
const unsigned long interval = 100;
unsigned long previousMillis = 0;

// Define conversion constants
const float accelConversionFactor = 9.81 / 4096.0; // Conversion factor for acceleration (to m/s²)
const float gyroConversionFactor = 1.0 / 16.4;     // Conversion factor for gyroscope (to °/s)

void setup(){
  Serial.begin(115200);
  BHY2.begin();

  accelerometer.begin();
  gyro.begin();
}

void loop(){
  static auto lastCheck = millis();

  // Update function should be continuously polled
  BHY2.update();

  // Check sensor values at each interval  
  if (millis() - lastCheck >= interval) {
    lastCheck = millis();
    
    // Read raw accelerometer data
    short accX = accelerometer.x();
    short accY = accelerometer.y();
    short accZ = accelerometer.z();

    // Read raw gyroscope data
    short gyroX = gyro.x();
    short gyroY = gyro.y();
    short gyroZ = gyro.z();

    // Convert to actual units
    float actualAccX = accX * accelConversionFactor;
    float actualAccY = accY * accelConversionFactor;
    float actualAccZ = accZ * accelConversionFactor;

    float actualGyroX = gyroX * gyroConversionFactor;
    float actualGyroY = gyroY * gyroConversionFactor;
    float actualGyroZ = gyroZ * gyroConversionFactor;

    // Output to serial monitor
    Serial.print("Acceleration (m/s²) - X: ");
    Serial.print(actualAccX, 2);
    Serial.print(", Y: ");
    Serial.print(actualAccY, 2);
    Serial.print(", Z: ");
    Serial.println(actualAccZ, 2);

    Serial.print("Gyroscope (°/s) - X: ");
    Serial.print(actualGyroX, 2);
    Serial.print(", Y: ");
    Serial.print(actualGyroY, 2);
    Serial.print(", Z: ");
    Serial.println(actualGyroZ, 2);

    Serial.println(); // Add a blank line for readability
  }
}