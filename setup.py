from setuptools import setup
#
import os
from glob import glob
#
package_name = 'maslo_from_1406'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
#
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
       #
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_node = maslo_from_1406.first_node:main',   # ← добавляем эту строку
            'time_counter = maslo_from_1406.time_counter:main',   # ← добавляем эту строку
            'talker = maslo_from_1406.talker:main',
            'listener = maslo_from_1406.listener:main',
            'even_pub = maslo_from_1406.even_number_publisher:main',
            'overflow_listener = maslo_from_1406.overflow_listener:main',
            'task3_even_publisher = maslo_from_1406.task3_even_publisher:main',
            'task3_overflow_listener = maslo_from_1406.task3_overflow_listener:main',
            'even_number_publisher = maslo_from_1406.even_number_publisher:main',
            'overflow_listener2 = maslo_from_1406.overflow_listener2:main',
        ],
    },
)

