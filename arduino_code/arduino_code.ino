#include <Servo.h>

Servo mode, pan, tilt;

int incomingByte, pos = 96;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  mode.attach(11);
  pan.attach(10);
  tilt.attach(9);

}

void loop() {
  
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:

    incomingByte = Serial.read();

    if (incomingByte == 'N'){
      mode.write(90);
      Serial.print("Center\n");
    }else{

      mode.write(60);
    
      if (incomingByte == 'R') {
        pan.write(120);
      }
      
      if (incomingByte == 'L') {
        pan.write(60);
      }

      if (incomingByte == 'Q'){
        pan.write(90);
      }

      if (incomingByte == 'U') {
        if (pos < 180){ pos = pos + 1; }
        tilt.write(pos);
      }

      if (incomingByte == 'D') {
        if (pos > 0){ pos = pos - 1; }
        tilt.write(pos);
      }

    }

  }
}
