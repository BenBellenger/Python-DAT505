void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available() > 0) {
    char value = Serial.read();
    Serial.print("You just sent me: ");
    Serial.write(value);
    Serial.print("\n");
  }
}
