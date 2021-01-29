# Optional imports
# supported libraries: math, random, numpy, scipy, and shapely
import math


def reward_function(params):
    """Reward calculation for AWS Deepracer.

    Calculate the reward for AWS' Deepracer for a given step.

    Example reward functions can be found at:
    https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html

    Args:
        params: Dictionary with the following key-value pairs
            "all_wheels_on_track": bool, flag to indicate if the agent is on the track
            "x": float, agent's x-coordinate in meters
            "y": float, agent's y-coordinate in meters
            "closest_objects": [int, int], zero-based indices of the two closest objects agent's pos
            "closest_waypoints": [int, int], indices of the two nearest waypoints
            "distance_from_center": float, distance in meters from the track center
            "is_crashed": bool, flag to indicate whether the agent has crashed
            "is_left_of_center": bool, flag indicating if the agent is left of the center line
            "is_offtrack": bool, flag to indicate if the agent has left the track
            "is_reversed": bool, flag to indicate if the agent is driving clockwise (True) or counter clockwise (False)
            "heading": float, agent's yaw in degrees
            "objects_distance": [float, ], list of object's distance in meters in relation to agent
            "objects_heading": [float, ], list of object's heading in degrees
            "objects_left_of_center": [bool, ], list of flags for objects left of centerline
            "objects_location": [(float, float), ], list of objects locations [(x, y), ...]
            "objects_speed": [float, ], list of objects' speeds in meters per second
            "progress": float, percentage of track completed
            "speed": float, agent's speed in m/s
            "steering_angle": float, agent's steering angle in degrees
            "steps": int, number of steps completed
            "track_length": float, track length in meters
            "track_width": float, track width
            "waypoints": [(float, float), ], list of (x, y) as milestones along the track center
    """

    # load input variables
    speed = params['speed']
    steering_angle = params['steering_angle']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Initialize reward
    reward = 1.0

    # penalize against large steering inputs
    # (based on aws examples)
    ABS_STEERING_THRESHOLD = 20.0
    if steering_angle > ABS_STEERING_THRESHOLD:
        reward -= 0.25

    # penalize against going too slow
    # (based on aws examples)
    SPEED_THRESHOLD = 1.0
    if speed < SPEED_THRESHOLD:
        reward -= 0.20

    # calculate the track direction based on nearest waypoints
    # (based on aws examples)
    next_point = waypoints[closest_waypoints[1]]  # [x, y]
    prev_point = waypoints[closest_waypoints[0]]  # [x, y]
    track_dir = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_dir = math.degrees(track_dir)

    # diff between track direction and current heading
    dir_diff = abs(track_dir - heading)
    if dir_diff > 180:
        dir_diff = 360 - dir_diff

    # Penalize if the difference is too large
    DIRECTION_THRESHOLD = 15.0
    if dir_diff > DIRECTION_THRESHOLD:
        reward -= 0.50

    # return the result
    return float(reward)
