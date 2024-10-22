const int potPin1 = A0;
const int potPin2 = A1;
const int buttonPin1 = 2;
const int buttonPin2 = 3;

int lastButton1State = HIGH;
int lastButton2State = HIGH;
int lastPotValue1 = 0;
int lastPotValue2 = 0;
const int threshold = 10;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
}

void loop() {
  int potValue1 = analogRead(potPin1);
  int potValue2 = analogRead(potPin2);
  int button1State = digitalRead(buttonPin1);
  int button2State = digitalRead(buttonPin2);

  bool buttonPressed = false;

  if (button1State != lastButton1State) {
    buttonPressed = true;
    lastButton1State = button1State;
  }

  if (button2State != lastButton2State) {
    buttonPressed = true;
    lastButton2State = button2State;
  }

  if (abs(potValue1 - lastPotValue1) > threshold || abs(potValue2 - lastPotValue2) > threshold || buttonPressed) {
    Serial.print(potValue1);
    Serial.print(",");
    Serial.print(potValue2);
    Serial.print(",");
    Serial.print(button1State == LOW ? 1 : 0); // 1 se premuto, 0 se rilasciato
    Serial.print(",");
    Serial.println(button2State == LOW ? 1 : 0); // 1 se premuto, 0 se rilasciato
    lastPotValue1 = potValue1;
    lastPotValue2 = potValue2;
  }

  delay(100);
}
