from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    freq_arg = DeclareLaunchArgument(
            'publish_frequency',           # имя аргумента
            default_value='10.0',          # значение по умолчанию
            description='Частота публикации чётных чисел (Гц)'
        )

    threshold_arg = DeclareLaunchArgument(
            'overflow_threshold',
            default_value='100',
            description='Порог, после которого происходит переполнение'
        )

        # Получаем текущее значение аргумента
    frequency = LaunchConfiguration('publish_frequency')
    threshold = LaunchConfiguration('overflow_threshold')





    return LaunchDescription([
        freq_arg,
        threshold_arg,
    Node(
            package='maslo_from_1406',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
        Node(
            package='maslo_from_1406',           # ← замени на своё имя пакета
            executable='even_number_publisher',
            name='even_number_publisher',
            output='screen',
            parameters=[
                {'publish_frequency': frequency},           # float
                {'overflow_threshold': threshold},         # bool
            ],

        ),
        
    ])
