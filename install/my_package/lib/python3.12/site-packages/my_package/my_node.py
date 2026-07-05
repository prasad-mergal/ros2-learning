import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareDrawer(Node):
    def __init__(self):
        super().__init__('square_drawer')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_square()

    def draw_square(self):
        move_cmd = Twist()
        turn_cmd = Twist()

        move_cmd.linear.x = 2.0
        turn_cmd.angular.z = 1.5708  # 90 degrees in radians

        for _ in range(4):
            # Move forward
            self.publisher_.publish(move_cmd)
            time.sleep(2)
            self.stop()

            # Turn 90 degrees
            self.publisher_.publish(turn_cmd)
            time.sleep(1)
            self.stop()

        self.get_logger().info('Square complete!')

    def stop(self):
        stop_cmd = Twist()
        self.publisher_.publish(stop_cmd)
        time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)
    node = SquareDrawer()
    rclpy.spin_once(node, timeout_sec=1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
