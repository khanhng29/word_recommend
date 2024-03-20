# INSTRUCTIONS FOR BUILDING AND PUSHING DOCKER IMAGES TO DOCKER HUB

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

## Docker file

Dockerfile is a text file without extension, containing specifications for a software execution field and structure for the Docker Image. From those commands, Docker will build a Docker image (usually small in size from a few MB to several GB large).

[Dockerfile](/Dockerfile)

- FROM python:3.11: This sets the base image for the Docker container as an official Python 3.11 image, which provides an environment with Python installed.

- WORKDIR /app: This sets the working directory within the container to /app. This is where subsequent commands will be executed, and it's also the directory where files will be copied.

- COPY requirement.txt ./: This copies the requirement.txt file from the host (the directory where the Dockerfile is located) to the /app directory in the container.

- RUN pip install --upgrade pip: This upgrades pip, the Python package installer, to the latest version. This ensures that the most recent version of pip is used for subsequent installations.

- RUN pip install -r requirement.txt: This installs Python dependencies listed in the requirement.txt file using pip. Dependencies specified in this file are typically libraries required by the Python application to run.

- COPY . .: This copies the entire content of the current directory (where the Dockerfile resides) to the /app directory in the container. This includes your Python source code and any other necessary files.

- CMD ["python", "./src/word_recommend_api.py"]: This specifies the command that will be executed when the container starts. It runs the Python script word_recommend_api.py located in the /app/src directory using the python interpreter.




## Docker build
The ```docker build``` command builds Docker images from a Dockerfile and a "context". A build's context is the set of files located in the specified ```PATH``` or ```URL```. The build process can refer to any of the files in the context.
```
docker build -t word_recommend1 .
```

- ```-t word_recommend1```: This option specifies the name and optionally a tag for the image being built. In this case, the image will be named word_recommend1 and will have the default tag ```latest```. The ```-t``` option is short for ```--tag```.
- ```.```: This is the path to the build context. In this case, . refers to the current directory, meaning that Docker will look for a Dockerfile in the current directory to use for building the image.


## Push the images to Docker hub

Change the name of image if image is not compatable to syntax: 
```
docker tag imgname username/imgname:verionname

docker tag word_recommend khanhng29/word_recommend:latest
```

Login to your Docker hub
```
docker login
```
By pushing your Docker images to Docker Hub, you can easily share them with others and access them from anywhere.
```
docker push khanhng29/word_recommend:version1.0
```
The docker image is now ready to download and use.
See instructions [here](link_to_docker.md)

