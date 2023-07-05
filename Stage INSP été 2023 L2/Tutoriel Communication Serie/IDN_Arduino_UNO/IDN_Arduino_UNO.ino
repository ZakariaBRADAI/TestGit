void setup() {
  Serial.begin(2000000);
}
void loop() {
  if (Serial.available() > 0 && Serial.readString()=="IDN?\n"){
    Serial.print("My ID is : COM 3 - Arduino Uno");
  }
  delay(5);
}
