#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_number_publisher')
        
        # 1. ОБЪЯВЛЯЕМ параметры (с значениями по умолчанию)
        self.declare_parameter('publish_frequency', 10.0)   # 10 Гц по умолчанию
        self.declare_parameter('overflow_threshold', 100)    # порог 100 по умолчанию
        
        # 2. ПОЛУЧАЕМ параметры
        freq = self.get_parameter('publish_frequency').value
        threshold = self.get_parameter('overflow_threshold').value
        
        # 3. Логируем полученные параметры
        self.get_logger().info(f"Параметры: частота={freq} Гц, порог={threshold}")
        
        # 4. СОЗДАЁМ публикатор
        self.publisher = self.create_publisher(Int32, '/even_numbers', 10)
        
        # 5. ИСПОЛЬЗУЕМ параметр для таймера
        timer_period = 1.0 / freq  # преобразуем Гц в секунды
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # 6. СОХРАНЯЕМ параметры для использования в callback
        self.threshold = threshold
        self.counter = 0
        
        self.get_logger().info("Even number publisher started")

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {self.counter}")
        
        # Используем порог из параметров
        if self.counter >= self.threshold:
            self.get_logger().warn(f"Overflow! Reached {self.counter}, resetting to 0")
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
