# INSTRUCTIONS FOR DOWNLOAD AND RUN APPLICATIONS FROM DOCKER HUB

## Install docker

To download Docker, visit the link and follow the instructions:
- [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Docker Desktop for Mac (macOS)](https://docs.docker.com/desktop/install/mac-install/)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)


After downloading, check the docker version by using the command line (Windows): windows + "cmd" + Enter. Then type:
```
docker -v

C:\Users\Admin>docker -v
Docker version 24.0.6, build ed223bc
```
The version displayed corresponds to the version you have installed.

## Pull images from docker hub
To pull a Docker image from Docker Hub, you can use the "docker pull" command. This command will download the specified image from Docker Hub to your local machine. Once you have pulled the image, you can run it using the "docker run" command.
From command line:
```
docker pull khanhng29/word_recommend:version1.0
```
Check all current images:
```
docker images

C:\Users\Admin>docker images
REPOSITORY                 TAG          IMAGE ID       CREATED        SIZE
khanhng29/word_recommend   version1.0   e40c51257e11   12 hours ago   3.76GB
```

Use the command below to run:
```
docker run -dp 5555:5555 khanhng29/word_recommend:version1.0
```
First 5555 port define the port in your local. Second 5555 port define the port in your docker.

To run inference. Download [index.html](https://github.com/khanhng29/word_recommend/blob/master/index.html).

Check your IP in command line:
```
ipconfig
```
Set your IP in ```line 31``` in HTML file then run HTML file in your browser for inference.

