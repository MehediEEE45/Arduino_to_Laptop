#define btled 13

void setup() {
  Serial.begin(9600);
  pinMode(btled, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n'); // Read until newline
    msg.trim(); // Remove extra spaces and newline characters

    if (msg == "ON" || msg == "on" || msg == "1") {
      digitalWrite(btled, HIGH);
      Serial.println("LED is ON");
    }
    else if (msg == "OFF" || msg == "off" || msg == "0") {
      digitalWrite(btled, LOW);
      Serial.println("LED is OFF");
    }
     else if (msg == "2" || msg == "3" || msg == "4") {

      Serial.println("LED is OFF");
    }
    else {
      Serial.println(msg); // Safe printing
    }
  }
}
