import rospy
from sensor_msgs.msg import CompressedImage, Image, Range, PointCloud2
from geometry_msgs.msg import PointStamped, Point
from tf2_sensor_msgs.tf2_sensor_msgs import do_transform_cloud
import sensor_msgs.point_cloud2 as pc2
import math
import tf
import tf2_ros as tf2
import time

class PID():
    def __init__(self, kp, ki, kd, max_correction=0):
        self.e_old = 0
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.I=0
        self.max_correction=max_correction


    def update(self,ref,current):
        e = ref - current
        if self.max_correction != 0:
            if e > self.max_correction:
                e = self.max_correction
            elif e < -self.max_correction:
                e=-self.max_correction
        D= (e-self.e_old) * self.kd
        self.e_old=e
        self.I += e * self.ki
        K= e * self.kp
        return (K + self.I + D)
        


class LidarCollision:

    def __init__(self,
                 topic = "/cloud_filtered",
                 range_min = 0.5,
                 pid_k=0.3,
                 pid_i=0.05,
                 pid_d=0
                 ):
        self.robot_width = 0.5
        self.topic=topic
        self.stop = False
        self.range = 0
        self.range_min = range_min
        self.range_max = self.range_min * 2
        self.speed_coefficient_setpoint = 1
        self.speed_coefficient = 1
        self.current_speed_coefficient = 1
        self.tfBuffer = tf2.Buffer()
        self.listener = tf2.TransformListener(self.tfBuffer)

        self.PID = PID(pid_k, pid_i, pid_d)
        self.PID2 = PID(pid_k, 0, 0)


    def run(self):

        rospy.Subscriber(self.topic, PointCloud2, self.lidar_callback,
                         queue_size=1)
                         
    def lidar_callback(self, msg):
        cloud = msg #self.laser_projector.projectLaser(msg)
        min_range = math.inf
        start=time.time()
        #a=self.listener.transformPointCloud('/base_link',cloud)
        #trans=self.tfBuffer.lookup_transform("laser","base_link",rospy.Time())
        trans = self.tfBuffer.lookup_transform("base_link", "laser",rospy.Time())
        cloud_out = do_transform_cloud(cloud, trans)
        for p in pc2.read_points(cloud_out, field_names = ("x", "y", "z"), skip_nans=True):
            point = Point()
            point.x = p[0]
            point.y = p[1]
            point.z = p[2]
            if point.y < self.robot_width/2 and point.y > -self.robot_width/2:
                if point.x < min_range and abs(point.x) > 0.05 and abs(point.y) >0.05:
                    min_range=point.x
        self.range = min_range
        if self.range < self.range_min:
                self.stop=True
        if self.range > self.range_min + 0.2:
                self.stop = False
        #print(self.range, time.time()-start)

    def collision(self):
        if self.stop is True:
            return True
        else:
            return False

    def set_speed_coefficient_setpoint(self):
        if self.range < self.range_max:
            self.speed_coefficient = (self.range - self.range_min) / (2 * self.range_min)
        else:
            self.speed_coefficient += 0.01
        if self.speed_coefficient < 0.1:
            self.speed_coefficient = 0.1
        if self.speed_coefficient > 1:
            self.speed_coefficient = 1

        self.speed_coefficient_setpoint = self.speed_coefficient

    def get_speed_coefficient(self):
        self.current_speed_coefficient = self.PID.update(self.speed_coefficient_setpoint, self.current_speed_coefficient)
        return self.current_speed_coefficient


class SonarCollision:

    def __init__(self,
                 sonar1 = "/pi_sonar/sonar_1",
                 sonar2 = "/pi_sonar/sonar_2",
                 sonar3 = "/pi_sonar/sonar_3",
                 range1_min = 0.7,
                 range2_min = 0.5,
                 range3_min = 0.8,
                 pid_k=0.3,
                 pid_i=0.05,
                 pid_d=0
                 ):

        self.sonar1 = sonar1
        self.sonar2 = sonar2
        self.sonar3 = sonar3

        self.stop1 = False
        self.stop2 = False
        self.stop3 = False

        self.sonar1_range = 0
        self.sonar2_range = 0
        self.sonar3_range = 0

        self.sonar1_range_min = range1_min
        self.sonar2_range_min = range2_min
        self.sonar3_range_min = range3_min

        self.sonar1_range_max = self.sonar1_range_min * 2
        self.sonar2_range_max = self.sonar2_range_min * 2
        self.sonar3_range_max = self.sonar3_range_min * 3

        self.speed_coefficient_setpoint = 1
        self.speed_coefficient1 = 1
        self.speed_coefficient2 = 1
        self.speed_coefficient3 = 1

        self.current_speed_coefficient = 1

        self.PID = PID(pid_k, pid_i, pid_d)
        self.PID2 = PID(pid_k, 0, 0)


    def run_sonars(self):

        rospy.Subscriber(self.sonar3, Range, self.__sonar3_callback,
                         queue_size=1)
        rospy.Subscriber(self.sonar1, Range, self.__sonar1_callback,
                         queue_size=1)
        rospy.Subscriber(self.sonar2, Range, self.__sonar2_callback,
                         queue_size=1)

    def collision(self):
        if self.stop1 is True or self.stop2 is True or self.stop3 is True:
            return True
        else:
            return False

    def set_speed_coefficient_setpoint(self):
        if self.sonar3_range < self.sonar3_range_max:
            self.speed_coefficient3 = (self.sonar3_range - self.sonar3_range_min) / (2 * self.sonar3_range_min)
        else:
            self.speed_coefficient3 += 0.01
        if self.speed_coefficient3 < 0.1:
            self.speed_coefficient3 = 0.1
        if self.speed_coefficient3 > 1:
            self.speed_coefficient3 = 1

        if self.sonar2_range < self.sonar2_range_max:
            self.speed_coefficient2 = (self.sonar2_range - self.sonar2_range_min) / ( self.sonar2_range_min)
        else:
            self.speed_coefficient2 += 0.01
        if self.speed_coefficient2 < 0.1:
            self.speed_coefficient2 = 0.1
        if self.speed_coefficient2 > 1:
            self.speed_coefficient2 = 1

        if self.sonar1_range < self.sonar1_range_max:
            self.speed_coefficient1 = (self.sonar1_range - self.sonar1_range_min) / ( self.sonar1_range_min)
        else:
            self.speed_coefficient1 += 0.01
        if self.speed_coefficient1 < 0.1:
            self.speed_coefficient1 = 0.1
        if self.speed_coefficient1 > 1:
            self.speed_coefficient1 = 1

        self.speed_coefficient_setpoint = min(self.speed_coefficient1, self.speed_coefficient2, self.speed_coefficient3)

    def get_speed_coefficient(self):
        self.current_speed_coefficient = self.PID.update(self.speed_coefficient_setpoint, self.current_speed_coefficient)
        return self.current_speed_coefficient

    def __sonar1_callback(self, msg):
        if msg.range < self.sonar1_range_min:
            self.stop1 = True
        if msg.range > self.sonar1_range_min + 0.2:
            self.stop1 = False
        self.sonar1_range = msg.range


    def __sonar2_callback(self, msg):
        if msg.range < self.sonar2_range_min:
            self.stop2 = True
        if msg.range > self.sonar2_range_min + 0.2:
            self.stop2 = False
        self.sonar2_range = msg.range


    def __sonar3_callback(self, msg):
        if msg.range < self.sonar3_range_min:
            self.stop3 = True
        if msg.range > self.sonar3_range_min + 0.2:
            self.stop3 = False
        self.sonar3_range = msg.range


    def get_range2(self):
        return float(self.sonar2_range)
    def get_range3(self):
        return float(self.sonar3_range)
