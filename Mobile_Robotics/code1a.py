from controller import Robot, Keyboard

# Create robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Enable keyboard
keyboard = Keyboard()
keyboard.enable(timestep)

# Get motors
left_front = robot.getDevice("left_front_motor")
right_front = robot.getDevice("right_front_motor")
left_rear = robot.getDevice("left_rear_motor")
right_rear = robot.getDevice("right_rear_motor")

motors = [left_front, right_front, left_rear, right_rear]

# Configure motors for velocity control
for motor in motors:
    motor.setPosition(float('inf'))
    motor.setVelocity(0.0)

MAX_SPEED = 6.0

while robot.step(timestep) != -1:

    key = keyboard.getKey()

    left_speed = 0.0
    right_speed = 0.0

    if key == ord('W'):
        # Forward
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED

    elif key == ord('S'):
        # Backward
        left_speed = -MAX_SPEED
        right_speed = -MAX_SPEED

    elif key == ord('A'):
        # Turn Left
        left_speed = -MAX_SPEED
        right_speed = MAX_SPEED

    elif key == ord('D'):
        # Turn Right
        left_speed = MAX_SPEED
        right_speed = -MAX_SPEED

    elif key == ord(' '):
        left_speed = 0.0
        right_speed = 0.0

    left_front.setVelocity(left_speed)
    left_rear.setVelocity(left_speed)
    right_front.setVelocity(right_speed)
    right_rear.setVelocity(right_speed)