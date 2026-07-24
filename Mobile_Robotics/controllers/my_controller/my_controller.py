from controller import Robot, Keyboard

# Create robot
robot = Robot()

# Time step
TIME_STEP = 32

# Create keyboard
keyboard = Keyboard()
keyboard.enable(TIME_STEP)

# Get the four motors
left_front_motor = robot.getDevice("left_front_motor")
right_front_motor = robot.getDevice("right_front_motor")
left_rear_motor = robot.getDevice("left_rear_motor")
right_rear_motor = robot.getDevice("right_rear_motor")

# Set motors to velocity control
left_front_motor.setPosition(float('inf'))
right_front_motor.setPosition(float('inf'))
left_rear_motor.setPosition(float('inf'))
right_rear_motor.setPosition(float('inf'))

# Initial speed
SPEED = 5.0

# Main loop
while robot.step(TIME_STEP) != -1:

    key = keyboard.getKey()

    # Stop all motors initially
    left_front_motor.setVelocity(0)
    right_front_motor.setVelocity(0)
    left_rear_motor.setVelocity(0)
    right_rear_motor.setVelocity(0)

    # W - Forward
    if key == ord('W') or key == ord('w'):
        left_front_motor.setVelocity(SPEED)
        right_front_motor.setVelocity(SPEED)
        left_rear_motor.setVelocity(SPEED)
        right_rear_motor.setVelocity(SPEED)

    # S - Backward
    elif key == ord('S') or key == ord('s'):
        left_front_motor.setVelocity(-SPEED)
        right_front_motor.setVelocity(-SPEED)
        left_rear_motor.setVelocity(-SPEED)
        right_rear_motor.setVelocity(-SPEED)

    # A - Left
    elif key == ord('A') or key == ord('a'):
        left_front_motor.setVelocity(-SPEED)
        right_front_motor.setVelocity(SPEED)
        left_rear_motor.setVelocity(-SPEED)
        right_rear_motor.setVelocity(SPEED)

    # D - Right
    elif key == ord('D') or key == ord('d'):
        left_front_motor.setVelocity(SPEED)
        right_front_motor.setVelocity(-SPEED)
        left_rear_motor.setVelocity(SPEED)
        right_rear_motor.setVelocity(-SPEED)

    # SPACE - Brake
    elif key == ord(' '):
        left_front_motor.setVelocity(0)
        right_front_motor.setVelocity(0)
        left_rear_motor.setVelocity(0)
        right_rear_motor.setVelocity(0)