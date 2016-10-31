import mqtt.*;

MQTTClient client;

void setup()
{
  size(200, 200);
  client = new MQTTClient(this);
  client.connect("mqtt://127.0.0.1", "Processing" + random(9999));
  frameRate(1);
}

void draw()
{
  if((frameCount % 2) == 0) {
    client.publish("/lights", "ON");
    background(255,0,0);
  }
  else {
    client.publish("/lights", "OFF");
    background(128,128,128);
  }
}