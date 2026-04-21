#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Task3EvenPublisher(Node):
    def __init__(self):
        # Имя узла будет задаваться при запуске через remapping
        super().__init__('even_pub')
        
        # Объявляем параметры для имен топиков
        self.declare_parameter('even_topic', '/even_numbers')
        self.declare_parameter('overflow_topic', '/overflow')
        
        even_topic = self.get_parameter('even_topic').get_parameter_value().string_value
        overflow_topic = self.get_parameter('overflow_topic').get_parameter_value().string_value
        
        # Публикаторы
        self.publisher_even = self.create_publisher(Int32, even_topic, 10)
        self.publisher_overflow = self.create_publisher(Int32, overflow_topic, 10)
        
        # Таймер 10 Гц
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.counter = 0
        self.get_logger().info(f"Task3 Publisher started - even_topic: {even_topic}, overflow_topic: {overflow_topic}")

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_even.publish(msg)
        self.get_logger().info(f"[{self.get_namespace()}] Published even: {self.counter}")
        
        if self.counter >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.publisher_overflow.publish(overflow_msg)
            self.get_logger().warn(f"[{self.get_namespace()}] Overflow! Resetting from {self.counter}")
            self.counter = 0
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = Task3EvenPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
