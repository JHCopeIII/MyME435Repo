String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (stringComplete) {
    inputString.trim(); // Remove any trailing or leading whitespace

    if (inputString.equals("LED ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED On");
    
    } else if (inputString.equals("LED OFF")) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED Off");

    } else if (inputString.startsWith("FLASH ")) {
      handleFlashCommand(inputString);
    
    } else {
      Serial.print("Received Unknown command: ");
      Serial.println(inputString);
    }

    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}

void handleFlashCommand(String command) {
  // Expecting format: FLASH <count> <delay>
  int firstSpace = command.indexOf(' ');
  int secondSpace = command.indexOf(' ', firstSpace + 1);

  if (firstSpace > 0 && secondSpace > firstSpace) {
    int count = command.substring(firstSpace + 1, secondSpace).toInt();
    int delayTime = command.substring(secondSpace + 1).toInt();

    if (count > 0 && delayTime >= 0) {
      for (int i = 0; i < count; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(delayTime);
        digitalWrite(LED_BUILTIN, LOW);
        delay(delayTime);
      }
      Serial.print("Flashes = ");
      Serial.print(count);
      Serial.print("  PeriodMs = ");
      Serial.println(delayTime);
    } else {
      Serial.println("ERROR: Invalid FLASH parameters");
    }
  } else {
    Serial.println("ERROR: Invalid FLASH format. Use: FLASH <count> <delay>");
  }
}
