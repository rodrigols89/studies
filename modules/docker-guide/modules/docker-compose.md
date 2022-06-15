# Docker Compose

## Contents

 - [Getting Started](#gettingstarted)

---

<div id="gettingstarted"></div>

## Getting Started

> My sample from [Docker Compose Getting Started](https://docs.docker.com/compose/gettingstarted/)

To start let's create the follow directory:

```python
mkdir examples/composetest -p
```

```python
cd examples/composetest
```

Now create a file called **app.py** in your project directory and paste this in:

```python
touch app.py
```

```python
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```

Now let's create another file called **requirements.txt** in your project directory and paste this in:

```python
touch requirements.txt
```

```python
flask
redis
```

Now let's write a Dockerfile that builds a Docker image. The image contains all the dependencies the Python application requires, including Python itself.

In your project directory, create a file named **Dockerfile** and paste the following:

```python
touch Dockerfile
```

```python
FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run"]
```

This tells Docker to:

 - Build an image starting with the Python 3.7 image.
 - Set the working directory to **/code**.
 - Set environment variables used by the flask command.
 - Install gcc and other dependencies
 - Copy **requirements.txt** from host to container and install the Python dependencies.
 - Add metadata to the image to describe that the container is listening on port **5000**.
 - Copy the current directory . in the project to the workdir . in the image.
 - Set the default command for the container to flask run.

Ok, now let's create **docker-compose.yml**:

```python
touch docker-compose.yml
```

And past this in:

```python
version: "3.9"

services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```

**NOTE:**  
This Compose file defines two services: **web** and **redis**.

Now let's really use docker compose to download our docker images and start the container:

```python
sudo docker compose up
```

Finally, let's check's right, enter http://localhost:8000/ in a browser to see the application running.

**You should see a message in your browser saying:**  
```python
Hello World! I have been seen 1 times.
```

**NOTE:**  
Refresh the page. The number should increment.

Switch to another terminal window, and type **docker image ls** to list local images:

```python
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
composetest_web   latest    a4ce6912e9d1   3 minutes ago   182MB
redis             alpine    f934e82c14d1   39 hours ago    28.4MB
```

**NOTE:**  
You can inspect images with `docker inspect <tag or id>`.

Now stop the application, either by running **docker compose down** from within your project directory in the second terminal, or by hitting CTRL+C in the original terminal where you started the app.

```python
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 ⠿ Container composetest-redis-1  Stopped                                                                                           1.8s
 ⠿ Container composetest-web-1    Stopped 
```

Edit **docker-compose.yml** in your project directory to add a bind mount for the web service:

```python
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_ENV: development
  redis:
    image: "redis:alpine"
```

**NOTE:**  
From your project directory, type **dockercompose up** to build the app with the updated Compose file, and run it.

**NOTE:**  
Check the Hello World message in a web browser again, and refresh to see the count increment.

Because the application code is now mounted into the container using a volume, you can make changes to its code and see the changes instantly, without having to rebuild the image.

Change the greeting in **app.py** and save it. For example, change the **Hello World!** message to **Hello from Docker!**:

```python
return 'Hello from Docker! I have been seen {} times.\n'.format(count)
```

Refresh the app in your browser. The greeting should be updated, and the counter should still be incrementing.

---

<div id="fail"></div>

## Container Fail

Another cool thing is that we can define the behavior that Docker will have if one of the containers fails. I describe in Compose that if the database fails for some reason, Docker will upload another one immediately. I can isolate these applications on a separate network and which volumes these applications will use to persist the data. Let's get all these services described in Compose up with just one command.

---

**REFERENCES:**  
[Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)  

---

**Rodrigo Leite -** *drigols*
