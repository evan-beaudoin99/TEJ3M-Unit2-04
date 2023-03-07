/*
  Created by: Evan Beaudoin
  Created on: March 2023
  Turns on the colors of an RGB light
*/


const int redPin= 12;
const int greenPin = 11;
const int bluePin = 10;

const int delayTime = 100;

void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  setColor(255, 0, 0); // Red Color
  delay(delayTime);
  setColor(0, 255, 0); // Green Color
  delay(delayTime);
  setColor(0, 0, 255); // Blue Color
  delay(delayTime);
  setColor(255, 255, 0); // Yellow Color
  delay(delayTime);
  setColor(255, 0, 255); // Purple Color
  delay(delayTime);
  setColor(255, 255, 255); // White Color
  delay(delayTime);
}
