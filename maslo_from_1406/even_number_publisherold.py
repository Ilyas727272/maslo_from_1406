#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # Публикаторы
        self.publisher_even = self.create_publisher(Int32, '/even_numbers', 10)
        self.publisher_overflow = self.create_publisher(Int32, '/overflow', 10)
        
        # Таймер 10 Гц (0.1 секунды)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.counter = 0
        self.get_logger().info("Even number publisher started (10 Hz)")

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_even.publish(msg)
        self.get_logger().info(f"Published even: {self.counter}")
        
        # Проверка на переполнение (≥100)
        if self.counter >= 80:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.publisher_overflow.publish(overflow_msg)
            self.get_logger().warn(f"Overflow! Resetting counter from {self.counter}")
            self.counter = 0
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
