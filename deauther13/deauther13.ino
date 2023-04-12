#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFiScan.h>

ESP8266WiFiMulti wifiMulti;

#define LED_R D8
#define LED_G D6
#define LED_B D7

void setup() {
  Serial.begin(115200);

  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);

  wifiMulti.addAP("AP_VBITFACUTYG", "VbiT#2004");
  wifiMulti.addAP("OtherSSID", "OtherPassword");

  Serial.println("Connecting ...");
  if (wifiMulti.run() == WL_CONNECTED) {
    Serial.println("WiFi connected");
    Serial.println("MAC address of deauth attacker:");
    byte bssid[6];
    WiFi.scanNetworks(true, false, false, 1000);
    int networksFound = WiFi.scanComplete();
    if (networksFound) {
      for (int i = 0; i < networksFound; ++i) {
        WiFi.BSSID(i, bssid);
        if (WiFi.SSID(i) == "") continue;
        Serial.print(WiFi.SSID(i));
        Serial.print(" - ");
        for (int j = 0; j < 6; ++j) {
          Serial.printf("%02x:", bssid[j]);
        }
        Serial.println();
      }
      digitalWrite(LED_R, LOW);
      digitalWrite(LED_G, HIGH);
      digitalWrite(LED_B, LOW);
    } else {
      digitalWrite(LED_R, HIGH);
      digitalWrite(LED_G, LOW);
      digitalWrite(LED_B, LOW);
    }
    WiFi.scanDelete();
  } else {
    Serial.println("WiFi not connected");
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, LOW);
  }
}

void loop() {

}
