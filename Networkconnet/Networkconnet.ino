// <ESP8266WiFi.h> It is for the module library.
#include <ESP8266WiFi.h>

void setup()
{
  Serial.begin(115200);
  Serial.println();
// Here remove the nameofwifi ,password of wifi and add your wifi password.
  WiFi.begin("nameofwifi", "password of wifi");

  Serial.print("Connecting");
  
  while (WiFi.status() != WL_CONNECTED)
  {
  // Here you can delay time a which rate it should connet to wifi.
    delay(500);
    Serial.print(".");
  }
  Serial.println();
// It will show you the ip provided by your wifi.

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {}

//OUTPUT CAN BE SEE THROUGH THE SERIAL MONITOR IN ARDUINO OR USE SCREEN COMMAND IN LINUX TERMINAL.
