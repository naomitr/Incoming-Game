void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int readvariable = Serial.read();
  if(Serial.available())
  {
    //switch (readvariable)
    {
      while (readvariable == 0)
        digitalWrite(13, HIGH);
              
      while (readvariable == 1)
        digitalWrite(13, LOW);
             
     //default: break;
   }
  }
 }
