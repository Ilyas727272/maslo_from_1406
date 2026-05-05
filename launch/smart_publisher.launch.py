

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node

def generate_launch_description():

    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='slow',
        description='Режим работы: fast (отладка) или slow (нормальный)'
    )
    
    mode = LaunchConfiguration('mode')
   
    from launch.substitutions import PythonExpression
    
    frequency = PythonExpression([
        "20.0 if '", mode, "' == 'fast' else 5.0"
    ])
    
    threshold = PythonExpression([
        "50 if '", mode, "' == 'fast' else 150"
    ])
    
    topic_name = PythonExpression([
        "'/even_numbers_fast' if '", mode, "' == 'fast' else '/even_numbers_slow'"
    ])
    
    return LaunchDescription([
        mode_arg,
        
        Node(
            package='maslo_from_1406',
            executable='even_pub',  
            name='even_number_publisher',
            output='screen',
            parameters=[
                {'publish_frequency': frequency},
                {'overflow_threshold': threshold},
                {'topic_name': topic_name},
            ],
        ),
        
        Node(
            package='maslo_from_1406',
            executable='overflow_listener2',
            name='overflow_listener2',
            output='screen',
        ),
    ])
