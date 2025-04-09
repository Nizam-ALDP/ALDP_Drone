
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import RPi.GPIO as GPIO

# ----- Setup connection -----
vehicle = connect('/dev/serial0', baud=57600, wait_ready=True)

# ----- Servo setup (change GPIOs as needed) -----
servo_pins = [17, 18, 27]  # Arm, Claw, Rotate
GPIO.setmode(GPIO.BCM)
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
servos = [GPIO.PWM(pin, 50) for pin in servo_pins]
for s in servos:
    s.start(0)

def set_angle(servo, angle):
    duty = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def pick_litter():
    print("Picking up litter...")
    set_angle(servos[0], 45)  # Arm down
    set_angle(servos[1], 90)  # Claw open
    time.sleep(1)
    set_angle(servos[1], 0)   # Claw close
    set_angle(servos[0], 0)   # Arm up
    print("Pickup complete.")

def arm_and_takeoff(target_alt):
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        time.sleep(1)
    print("Taking off...")
    vehicle.simple_takeoff(target_alt)
    while vehicle.location.global_relative_frame.alt < target_alt * 0.95:
        time.sleep(1)
    print("Altitude reached.")

def detect_litter():
    # Replace this with YOLOv8 detection logic
    return False  # Dummy

arm_and_takeoff(3)

print("Switching to AUTO (patrol)...")
vehicle.mode = VehicleMode("AUTO")

while True:
    if detect_litter():
        print("Litter Detected!")
        vehicle.mode = VehicleMode("LOITER")
        pick_litter()
        time.sleep(3)
        print("Returning to Launch...")
        vehicle.mode = VehicleMode("RTL")
        break
    time.sleep(1)
