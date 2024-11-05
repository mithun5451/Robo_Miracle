from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='articubot_one',
            executable='move_robot_node',
            name='move_robot_to_ceo',
            parameters=[{"target": "ceo_cabin"}]
        )
    ])
