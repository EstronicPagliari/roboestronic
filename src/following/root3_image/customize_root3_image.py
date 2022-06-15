
import subprocess
import shutil
import linux_util


class customizeImage:
    def __init__(self):
        # there needs to exist a dictionary with name "conf" the following variables:
        # "hostname": hostname that the image is going to have setup.
        # "rootfs_extra_space_mb": how much more space will be allocated in rootfs in generated image.
        # "rootfs": absolute path on buildbot filesystem where generated rootfs will be saved
        # "flavour": flavour of generated image. The name of generated image will be: ${timestamp}-${flavour}-${release}-raspberry-pi.img
        # "release": release of the generated image. Currently only possible value is "focal".
        # "imagedir": absolute path on buildbot filesystem where generated image will be saved
        self.conf = {
            "hostname": "ubiquityrobot",
            "rootfs_extra_space_mb": 500,
            "rootfs": "/image-builds/PiFlavourMaker/focal-build",
            "flavour": "ubiquity-root3-testing",
            "release": "focal",
            "imagedir": "/image-builds/final-images",
            "apt_get_packages": [
                "python2",
                "ros-noetic-raspicam-node",
                "ros-noetic-pi-sonar",
                "ros-noetic-ubiquity-motor",
                "ros-noetic-oled-display-node",
                "ros-noetic-move-basic",
                "libudev-dev",
                "ros-noetic-laser-filters",
            ]
        }

    def execute_customizations(self):
        subprocess.run("git clone https://$GIT_TOKEN@github.com/UbiquityRobotics/ur_vision_msgs.git", cwd="/home/ubuntu/catkin_ws/src/", shell=True, check=True)
        subprocess.run("git clone https://$GIT_TOKEN@github.com/UbiquityRobotics/detect_objects.git",cwd="/home/ubuntu/catkin_ws/src/", shell=True, check=True)
        subprocess.run("git clone https://$GIT_TOKEN@github.com/UbiquityRobotics/ur_object_tracking.git -b multi_track",cwd="/home/ubuntu/catkin_ws/src/", shell=True, check=True)
        subprocess.run("git clone https://$GIT_TOKEN@github.com/UbiquityRobotics/ldlidar.git",cwd="/home/ubuntu/catkin_ws/src/", shell=True, check=True)
        subprocess.run("git clone https://$GIT_TOKEN@github.com/UbiquityRobotics/root3.git",cwd="/home/ubuntu/catkin_ws/src/", shell=True, check=True)
        subprocess.run("pip3 install -y --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime", check=True, shell=True)
        subprocess.run("echo 'deb https://packages.cloud.google.com/apt coral-edgetpu-stable main' | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list", check=True, shell=True)
        subprocess.run("curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -", check=True, shell=True)
        subprocess.run("sudo apt-get update", check=True, shell=True)
        subprocess.run("sudo apt-get install libedgetpu1-std", check=True, shell=True)
        subprocess.run("sudo apt-get install python3-pycoral", check=True, shell=True)
        subprocess.run("pip3 install filterpy", check=True, shell=True)

        return

