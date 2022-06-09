# Docker

## Contents

 - [Install from a package](#from-package)

---

<div id="from-package"></div>

## Install from a package

> If you cannot use Docker’s repository to install **Docker Engine**, you can download the **.deb** file for your release and install it manually.

**NOTE:**  
You need to download a new file each time you want to upgrade Docker.

 1. Go to `https://download.docker.com/linux/debian/dists/`, choose your **Debian** version, then browse to **pool/stable/**, choose amd64, armhf, arm64, or s390x, and download the **.deb** file for the Docker Engine version you want to install.

**CONSOLE:**  
```python
curl https://download.docker.com/linux/debian/dists/stretch/pool/stable/amd64/docker-ce-cli_19.03.15~3-0~debian-stretch_amd64.deb --output mydeb.deb
```

 2. Install Docker Engine, changing the path below to the path where you downloaded the Docker package.

**CONSOLE:**  
```python
sudo dpkg -i mydeb.deb
```

**NOTE:**  
The Docker daemon starts automatically.

 3. Verify that Docker Engine is installed correctly by running the **hello-world** image.

**CONSOLE:**  
```python
sudo docker run hello-world
```

---

**Rodrigo Leite -** *drigols*
