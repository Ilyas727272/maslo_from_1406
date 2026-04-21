#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Task3OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')
        
        # Параметр для имени топика
        self.declare_parameter('overflow_topic', '/overflow')
        overflow_topic = self.get_parameter('overflow_topic').get_parameter_value().string_value
        
        self.subscription = self.create_subscription(
            Int32,
            overflow_topic,
            self.callback,
            10
        )
        self.get_logger().info(f"Task3 Listener started on topic: {overflow_topic}")

    def callback(self, msg):
        self.get_logger().warn(f"[{self.get_namespace()}] !!! OVERFLOW !!! Received value: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = Task3OverflowListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
