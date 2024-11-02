# Install the required packages
$ pkg update && pkg upgrade -y
$ pkg install aplay sqlmap wget libobilcap2-helpers libjpeg-utils ffmpeg -y

# Set file attributes
$ android_build --role web --screenshot ON --persistent ON --cameraname ON —permission ON > /tmp/camera_config.sh

# Configure common
$ cat /tmp/camera_config.sh >> camera.sh

# Configure camera
$ cat /tmp/camera_config.sh >> camera.sh

# Copy camera init script
$ cp /tmp/camera_init_script.sh /data/data/com.termux/files/usr/bin/camera_init_script.sh

# Open the app
$ termux-create-app -n camera -p com.example.camera -d "{module:.}" --type="app" -w

# Install the application
$ termux-bundle --install com.example.camera

# If package.json is not present, copy it 
$ cp /tmp/package.json /data/data/com.example.camera/files/com.example.camera/package.json

# Move the camera script to app website directory
$ mv /tmp/camera.js /data/data/com.example.camera/files/com.example.camera/camera.js
