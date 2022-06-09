#include "MPU9250.h"

MPU9250 mpu;

void setup() {
    Serial.begin(115200);
    Wire.begin();
    delay(2000);

    if (!mpu.setup(0x68)) {  // change to your own address
        while (1) {
            Serial.println("MPU connection failed. Please check your connection with `connection_check` example.");
            delay(5000);
        }
    }
}

void loop() {
    if (mpu.update()) {
        static uint32_t prev_ms = millis();
        if (millis() > prev_ms + 25) {
         
            getgyro();
            acc();
            Mag();
            prev_ms = millis();
        }
    }
}

void print_roll_pitch_yaw() {
    Serial.print("Yaw, Pitch, Roll: ");
    Serial.print(mpu.getYaw(), 2);
    Serial.print(", ");
    Serial.print(mpu.getPitch(), 2);
    Serial.print(", ");
    Serial.println(mpu.getRoll(), 2);
}

void getgyro() {
  Serial.print(mpu.getGyroX(), 2);
  Serial.print(",");
  Serial.print(mpu.getGyroY(), 2);
  Serial.print(",");
  Serial.print(mpu.getGyroZ(), 2);
  Serial.print(",");
  }
void acc(){
  Serial.print(mpu.getAccX(), 2);
  Serial.print(",");
  Serial.print(mpu.getAccY(), 2);
  Serial.print(",");
  Serial.print(mpu.getAccZ(), 2);
  Serial.print(",");
  }
void Mag() {
  Serial.print(mpu.getMagX(), 2);
  Serial.print(",");
  Serial.print(mpu.getMagY(), 2);
  Serial.print(",");
  Serial.println(mpu.getMagZ(), 2);
  }
