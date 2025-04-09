#include <Servo.h>

Servo servo1;  // Left arm servo
Servo servo2;  // Right arm servo (opposite direction)
Servo servo3;  // Gripper servo

void setup() {
    servo1.attach(5);  // Attach servo 1 to pin 9
    servo2.attach(6); // Attach servo 2 to pin 10
    servo3.attach(7); // Attach servo 3 to pin 11
}

void loop() {
    // Lift the arm: Servo 1 moves clockwise, Servo 2 moves counterclockwise
    for (int pos = 0; pos <= 90; pos += 5) {
        servo1.write(90 - pos);  // Moves forward
        servo2.write(90 + pos);  // Moves backward
        delay(50);
    }

    delay(1000); // Hold position for 1 second

    // Open gripper
    servo3.write(0);
    delay(1000);

    // Close gripper
    servo3.write(90);
    delay(1000);

    // Lower the arm back to the original position
    for (int pos = 90; pos >= 0; pos -= 5) {
        servo1.write(90 - pos);
        servo2.write(90 + pos);
        delay(50);
    }

    delay(1000); // Wait before the next cycle
}
