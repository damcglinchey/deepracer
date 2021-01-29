# Optional imports
# supported libraries: math, random, numpy, scipy, and shapely

def reward_function(params):
    """Reward calculation for AWS Deepracer.

    Calculate the reward for AWS' Deepracer for a given step

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

    # calculate the reward based on some parameters
    reward = 1.0

    # return the result
    return float(reward)
