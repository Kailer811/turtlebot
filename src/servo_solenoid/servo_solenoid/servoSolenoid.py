import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber_node')
        
        # 1. Create a variable to store the lidar data
        self.latest_scan = None 

        # 2. Subscribe to the '/scan' topic
        # Note: We use qos_profile_sensor_data because Lidar is a high-frequency sensor
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.servoSolenoid,
            qos_profile_sensor_data)
        
        self.get_logger().info('Lidar Subscriber Node has been started.')

    def servoSolenoid(self, msg):
        # 3. Store the entire lidar message into your variable
        self.latest_scan = msg

        # Optional: Example of how to use the variable
        if self.latest_scan is not None:
            # Index 0 is usually directly in front of the TurtleBot
            front_distance = self.latest_scan.ranges[0]
            self.get_logger().info(f'Distance to front: {front_distance:.2f} m')
            if front_distance == 1:
                print("servo should have turned")

def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    
    try:
        rclpy.spin(lidar_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        lidar_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
