#include "MPU9250.h"

MPU9250 mpu;

int buttonState = 0;
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
//    Serial.println("Accel Gyro calibration will start in 5sec.");
//    Serial.println("Please leave the device still on the flat plane.");
    mpu.verbose(true);
    delay(5000);
    mpu.calibrateAccelGyro();

//    Serial.println("Mag calibration will start in 5sec.");
//    Serial.println("Please Wave device in a figure eight until done.");
//    delay(5000);
//    mpu.calibrateMag();
//  
//    print_calibration();
//    mpu.verbose(false);
    mpu.setFilterIterations(15);
    pinMode(3,INPUT_PULLUP);
    
}

void loop() {
    if (mpu.update()) {
        static uint32_t prev_ms = millis();
        buttonState = digitalRead(3);
        if (millis() > prev_ms + 1 && buttonState==LOW) {
            getgyro();
            acc();
            //linearacc();
            Mag();
            prev_ms = millis();
        }
        else
          Serial.println("off");
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
void linearacc() {
  Serial.print(mpu.getLinearAccX(),2);
  Serial.print(",");
  Serial.print(mpu.getLinearAccY(),2);
  Serial.print(",");
  Serial.print(mpu.getLinearAccZ(),2);
  Serial.print(",");
  }
void print_calibration() {
    Serial.println("< calibration parameters >");
    Serial.println("accel bias [g]: ");
    Serial.print(mpu.getAccBiasX() * 1000.f / (float)MPU9250::CALIB_ACCEL_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getAccBiasY() * 1000.f / (float)MPU9250::CALIB_ACCEL_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getAccBiasZ() * 1000.f / (float)MPU9250::CALIB_ACCEL_SENSITIVITY);
    Serial.println();
    Serial.println("gyro bias [deg/s]: ");
    Serial.print(mpu.getGyroBiasX() / (float)MPU9250::CALIB_GYRO_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getGyroBiasY() / (float)MPU9250::CALIB_GYRO_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getGyroBiasZ() / (float)MPU9250::CALIB_GYRO_SENSITIVITY);
    Serial.println();
    Serial.println("mag bias [mG]: ");
    Serial.print(mpu.getMagBiasX());
    Serial.print(", ");
    Serial.print(mpu.getMagBiasY());
    Serial.print(", ");
    Serial.print(mpu.getMagBiasZ());
    Serial.println();
    Serial.println("mag scale []: ");
    Serial.print(mpu.getMagScaleX());
    Serial.print(", ");
    Serial.print(mpu.getMagScaleY());
    Serial.print(", ");
    Serial.print(mpu.getMagScaleZ());
    Serial.println();
}
