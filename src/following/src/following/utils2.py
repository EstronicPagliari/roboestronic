import rospy
from sensor_msgs.msg import CompressedImage, Image, Range

class PID():
    def __init__(self, kp, ki, kd):
        self.e_old = 0
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.I=0


    def update(self,ref,current):
        e = ref - current
        D= (e-self.e_old) * self.kd
        self.e_old=e
        self.I += e * self.ki
        K= e * self.kp
        return (K + self.I + D)

class SonarCollision:

    def __init__(self,
                 sonar1 = "/pi_sonar/sonar_1",
                 sonar2 = "/pi_sonar/sonar_2",
                 sonar3 = "/pi_sonar/sonar_3",
                 range1_min = 0.6,
                 range2_min = 0.4,
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