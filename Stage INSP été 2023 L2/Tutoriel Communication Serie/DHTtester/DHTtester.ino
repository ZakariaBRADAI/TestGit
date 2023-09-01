#include "DHT.h"

#define DHTPIN 9    
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(2000000);
  dht.begin();
}
int dt = 1000;
void loop() {
  float t = dht.readTemperature();
  Serial.println(t,3);
  delay(dt);
}


