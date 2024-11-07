#include "Arduino_BHY2.h"

SensorXYZ accelerometer(SENSOR_ID_ACC);
SensorXYZ gyro(SENSOR_ID_GYRO);
// 100ms 간격을 설정
const unsigned long interval = 100;
unsigned long previousMillis = 0;
// 변환 상수 정의
const float accelConversionFactor = 9.81 / 4096.0; // 가속도 변환 상수 (m/s² 단위로 변환)
const float gyroConversionFactor = 1.0 / 16.4;     // 자이로스코프 변환 상수 (°/s 단위로 변환)


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

  // Check sensor values every second  
  if (millis() - lastCheck >= interval) {
    lastCheck = millis();
    // 가속도계 원시 데이터 읽기
    short accX = accelerometer.x();
    short accY = accelerometer.y();
    short accZ = accelerometer.z();

    // 자이로스코프 원시 데이터 읽기
    short gyroX = gyro.x();
    short gyroY = gyro.y();
    short gyroZ = gyro.z();

    // 실제 단위로 변환
    float actualAccX = accX * accelConversionFactor;
    float actualAccY = accY * accelConversionFactor;
    float actualAccZ = accZ * accelConversionFactor;

    float actualGyroX = gyroX * gyroConversionFactor;
    float actualGyroY = gyroY * gyroConversionFactor;
    float actualGyroZ = gyroZ * gyroConversionFactor;

    // 시리얼 모니터에 출력
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

    Serial.println(); // 가독성을 위해 빈 줄 추가
  }
}
