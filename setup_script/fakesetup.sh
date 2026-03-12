sudo apt update
sudo apt install -y python3-argcomplete python3-colcon-common-extensions libboost-system-dev build-essential
sudo apt install -y ros-humble-hls-lfcd-lds-driver
sudo apt install -y ros-humble-turtlebot3-msgs
sudo apt install -y ros-humble-dynamixel-sdk
sudo apt install -y ros-humble-xacro
sudo apt install -y libudev-dev
sudo apt install -y python3-pip git python3-jinja2 \
ibboost-dev libgnutls28-dev openssl libtiff-dev pybind11-dev \
qtbase5-dev libqt5core5a libqt5widgets5 meson cmake \
python3-yaml python3-ply \
libglib2.0-dev libgstreamer-plugins-base1.0-dev
sudo apt install -y ros-humble-camera-ros
cd ~/libcamera
meson setup build --buildtype=release -Dpipelines=rpi/vc4,rpi/pisp -Dipas=rpi/vc4,rpi/pisp -Dv4l2=true -Dgstreamer=enabled -Dtest=false -Dlc-compliance=disabled -Dcam=disabled -Dqcam=disabled -Ddocumentation=disabled -Dpycamera=enabled
ninja -C build -j 1
sudo ninja -C build install -j 1
sudo ldconfig
export LD_LIBRARY_PATH=/usr/local/lib/aarch64-linux-gnu:$LD_LIBRARY_PATH
echo "check rpi camera works, setup ssh S1"

