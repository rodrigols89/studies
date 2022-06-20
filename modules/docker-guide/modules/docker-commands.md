# Docker Commands

## Contents

 - **Docker Commands:**
   - [Checking docker version](#v)
   - [Using a testing image](#testing-image)
   - [docker system prune -a -f --volumes](#system-prune)
 - **Image Commands:**
   - [listing docker images](#listing-docker-images)
   - [removing docker images](#remove-image)
 - **Container Commands:**
   - [Initialization a Container](#initialization)
   - [listing containers](#listing-containers)
   - [Stopping a container](#stopping)
   - [Starting a container](#starting)
   - [Removing containers](#removing)
   - [Entering a container (exec -it)](#exec-it)
 - **Docker Compose:**
   - [docker compose build](#compose-build)
   - [docker compose images](#compose-images)
   - [docker compose stop](#compose-stop)
   - [docker compose run](#compose-run)
   - [docker compose up](#compose-up)
   - [docker compose ps](#compose-ps)
   - [docker compose down](#compose-down)

---

<div id="v"></div>

## Checking docker version

to check Docker version just enter **docker -v** on the console:

**CONSOLE:**  
```python
docker -v
```

**OUTPUT:**  
```python
Docker version 20.10.17, build 100c701
```

---

<div id="testing-image"></div>

## Using a testing image

To test if you Docker is okay, we go use a test image:

**CONSOLE:**  
```python
docker run -d -p 80:80 docker/getting-started
```

---

<div id="system-prune"></div>

## docker system prune -a -f --volumes

> Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.

**Options:**  

| Name, shorthand | Description                                        |
|-----------------|----------------------------------------------------|
| --all , -a      | Remove all unused images not just dangling ones    |
| --filter        | Provide filter values (e.g. 'label=<key>=<value>') |
| --force , -f    | Do not prompt for confirmation                     |
| --volumes       | Prune volumes                                      |

**NOTE:**  
By default, **volumes** are not removed to prevent important data from being deleted if there is currently no container using the volume. Use the **--volumes flag** when running the command to prune volumes as well.

---

<div id="listing-docker-images"></div>

## listing docker images

To list Docker images is very easy:

**CONSOLE:**  
```python
docker image list
```

or

```python
docker image ls
```

**OUTPUT:**
```python
REPOSITORY               TAG       IMAGE ID       CREATED       SIZE
minio/minio              latest    01431999f934   10 days ago   393MB
mysql                    latest    b05128b000dd   2 weeks ago   516MB
docker/getting-started   latest    eb9194091564   3 weeks ago   28.5MB
```

**NOTE:**  
Another approach could be:

```python
sudo docker images
```

---

<div id="remove-image"></div>

## removing docker images

To remove  on or more images just use the command `sudo docker rmi -f <image-name-or-id>`:

**CONSOLE:**  
```python
sudo docker rmi <image-name-or-id>
```

**NOTE:**  
You can also use **--force** or **-f** to force removal of the image.

**CONSOLE:**  
```python
sudo docker rmi -f <image-name-or-id>
```

---

<div id="initialization"></div>

## Initialization a Container

Assuming you already have a **Docker Image** downloaded now it's time for you to initialize a container from this Image. But before that, let's see what parameters we can add when creating a container and what each one is for:

| Parameter | Explanation                                                              |
|-----------|--------------------------------------------------------------------------|
| -d        | Run the container in the background                                      |
| -i        |	Interactive mode. Keep STDIN open even with no console attached          |
| -t        |	Allocate a pseudo TTY                                                    |
| --rm      |	Automatically remove container after completion (Does not work with -d)  |
| --name    |	Container name                                                           |
| -v        |	Volume mapping                                                           |
| -p        |	port map (mapping)                                                       |
| -m        |	Limits RAM usage                                                         |
| -c        |	Balances CPU usage

**NOTE:**  
Here's a simple example of how to apply this in practice with the command below:

**CONSOLE:**  
```python
sudo docker container run -it --rm --name my_python python bash
```

**NOTE:**  
According to the above command, a container named **my_python** will be started, created from the **python image**, and the process running in that container will be **bash**.

---

<div id="listing-containers"></div>

## listing containers

To list containers you can use the follows **alias** and **Options**:

 - **Aliases:**
   - ls, ps, list
 - **Options:**
   - -a, --all             Show all containers (default shows just running)
   - -f, --filter filter   Filter output based on conditions provided
   - --format string       Pretty-print containers using a Go template
   - -n, --last int        Show n last created containers (includes all states) (default -1)
   - -l, --latest          Show the latest created container (includes all states)
   - --no-trunc            Don't truncate output
   - -q, --quiet           Only display container IDs
   - -s, --size            Display total file sizes

For example, if you need to see **all (default shows just running)** containers can use the follow commands:

**CONSOLE:**  
```python
sudo docker container ps -a
```

**OUTPUT:**  
```python
CONTAINER ID   IMAGE          COMMAND    CREATED       STATUS                   PORTS     NAMES
7d079a088789   feb5d9fea6a5   "/hello"   4 hours ago   Exited (0) 4 hours ago             compassionate_swartz
```

---

<div id="stopping"></div>

## Stopping a container

To stop a running container just enter the follow command:

**CONSOLE:**  
```python
sudo docker container stop <id-name-container>
```

**NOTE:**  
Don't confuse the **container** *ID/name *with the **image** *ID/name*, that's because they are different.

---

<div id="starting"></div>

## Starting a container

The first thing you need to remember that:

> Don't confuse the **container** *ID/name *with the **image** *ID/name*, that's because they are different.

To get a container ID/Name just use the command **"sudo docker container ps -a"**:

**CONSOLE:**  
```python
sudo docker container ps -a
```

**OUTPUT:**  
```python
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                      PORTS     NAMES
16293c3424d5   mysql                    "docker-entrypoint.s…"   23 minutes ago   Exited (0) 16 minutes ago             mysqlbd1
22ae77f745f3   docker/getting-started   "/docker-entrypoint.…"   24 minutes ago   Exited (0) 15 minutes ago             suspicious_colden
3e1403575b74   hello-world              "/hello"                 28 minutes ago   Exited (0) 27 minutes ago             pensive_bouman
```

Now you have container ID/Names. To start a container just enter the follow command on the console:

**CONSOLE:**  
```python
sudo docker container start <id-name-container>
```

---

<div id="removing"></div>

## Removing containers

To remove docker containers is very easy:

**CONSOLE:**  
```python
sudo docker container rm <container-id-or-name>
```

**NOTE**  
If you try remove a running container you will get the following error:

**OUTPUT:**  
```python
Error response from daemon: You cannot remove a running container 16293c3424d.
Stop the container before attempting removal or force remove
```

**NOTE:**  
That's no recommender, but you can use the **flag -f** to force remove the container.

**CONSOLE:**  
```python
sudo docker container rm <container-id-or-name> -f
```

---

<div id="exec-it"></div>

## Entering a container (exec -it)

To enter into docker container just enter the follow command:

**CONSOLE:**  
```python
sudo docker container exec -it <container-id-or-name> bash
```

**NOTE:**  
To exit docker container, type **exit** or **ctrl+d** in the console.

---

<div id="compose-build"></div>

## docker compose build

> This command builds images in the **docker-compose.yml file**.

The job of the build command is to get the images ready to create containers, so if a service is using the prebuilt image, it will skip this service.

```python
sudo docker compose build
```

```python
database uses an image, skipping
Building web
Step 1/11 : FROM python:3.9-rc-buster
 ---> 2e0edf7d3a8a
Step 2/11 : RUN apt-get update && apt-get install -y docker.io
```

---

<div id="compose-images"></div>

## docker compose images

> This command will list the images you’ve built using the current **docker-compose** file.

```python
sudo docker compose images
```

```python
          Container                  Repository        Tag       Image Id       Size  
--------------------------------------------------------------------------------------
7001788f31a9_docker_database_1   mysql/mysql-server   5.7      2a6c84ecfcb2   333.9 MB
docker_database_1                mysql/mysql-server   5.7      2a6c84ecfcb2   333.9 MB
docker_web_1                     <none>               <none>   d986d824dae4   953 MB
```

---

<div id="compose-stop"></div>

## docker compose stop

> This command stops the running containers of specified services.

```python
sudo docker-compose stop
```

```python
Stopping docker_web_1      ... done
Stopping docker_database_1 ... done
```

---

<div id="compose-run"></div>

## docker compose run

> This is similar to the **docker run** command. It will create containers from images built for the services mentioned in the compose file.

```python
sudo docker-compose run web
```

```python
Starting 7001788f31a9_docker_database_1 ... done
 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 116-917-688
```

---

<div id="compose-up"></div>

## docker compose up

> This command does the work of the **docker compose build** and **docker compose run** commands.

It builds the images if they are not located locally and starts the containers. If images are already built, it will fork the container directly.

```python
sudo docker compose up
```

```python
Creating docker_database_1 ... done
Creating docker_web_1      ... done
Attaching to docker_database_1, docker_web_1
```

---

<div id="compose-ps"></div>

## docker compose ps

> This command list all the containers in the current **docker-compose** file. They can then either be running or stopped.

```python
sudo docker compose ps
```

```python
      Name                 Command             State               Ports         
---------------------------------------------------------------------------------
docker_database_1   /entrypoint.sh mysqld   Up (healthy)   3306/tcp, 33060/tcp   
docker_web_1        flask run               Up             0.0.0.0:5000->5000/tcp
 
$ docker-compose ps
      Name                 Command          State    Ports
----------------------------------------------------------
docker_database_1   /entrypoint.sh mysqld   Exit 0        
docker_web_1        flask run               Exit 0  
```

---

<div id="compose-down"></div>

## docker compose down

> This command is similar to the **docker system prune** command. However, in Compose, it stops all the services and cleans up the containers, networks, and images.

```python
sudo docker compose down
```

```python
Removing docker_web_1      ... done
Removing docker_database_1 ... done
Removing network docker_default
(django-tuts) Venkateshs-MacBook-Air:Docker venkateshachintalwar$ docker-compose images
Container   Repository   Tag   Image Id   Size
----------------------------------------------
(django-tuts) Venkateshs-MacBook-Air:Docker venkateshachintalwar$ docker-compose ps
Name   Command   State   Ports
------------------------------
```

---

**REFERENCES:**  
[Docker Compose Tutorial: advanced Docker made simple](https://www.educative.io/blog/docker-compose-tutorial)  

---

**Rodrigo Leite -** *drigols*
