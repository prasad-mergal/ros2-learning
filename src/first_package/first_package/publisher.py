import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class PublisherNode(Node):
	def __init__(self):
		super(). __init__('node_publisher')
		
		self.publisher = self.create_publisher(String,'communication_topic',15)
		commRate = 1 
		
		self.timer = self.create_timer(commRate, self.callbackFunction)
		self.counter = 0
	
	def callbackFunction(self):
		messagePublisher = String()
		messagePublisher.data = 'Counter value: %d' % self.counter
		
		self.publisher.publish(messagePublisher)
		self.get_logger().info('Publisher node is publishing: "%s"' % messagePublisher.data)
		self.counter=self.counter+1
		
#Main Function
def main(args=None):
	rclpy.init(args=args)
	node_publisher = PublisherNode()
	rclpy.spin(node_publisher)
	node_publisher.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
