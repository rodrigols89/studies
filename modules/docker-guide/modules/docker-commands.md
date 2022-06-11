# Docker Commands

## Contents

 - **Image Commands:**
   - [listing docker images](#listing-docker-images)
   - [removing docker images](#remove-image)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
 - **Container Commands:**
   - [Initialization a Container](#initialization)
   - [listing containers](#listing-containers)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)
   - [](#)

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

<div id=""></div>

## x

x









**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

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

<div id=""></div>

## x

x







**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```


**CONSOLE:**  
```python

```

**OUTPUT:**  
```python

```

---

**REFERENCES:**  
[]()  

---

**Rodrigo Leite -** *drigols*
