# Docker Image vs Docker Container

## Contents

- [01 - Object Orientation Analogy](#analogy)
- [02 - Crucial differences between Docker Image and Docker Container](#crucial)

---

<div id="analogy"></div>

## 01 - Object Orientation Analogy

> A good approach to differentiating between **images** and **containers** is to try to think of an **object-oriented programming language**.

In such an analogy:

 - The **class** represents the **image**.
 - While its **instance**, the **object**, is the **container**.

```python
+-----------------------------+-------+-----------+
|             Domain          | Meta  | Concrete  |
+-----------------------------+-------+-----------+
| Docker                      | Image | Container |
| Object oriented programming | Class | Object    |
+-----------------------------+-------+-----------+
```

**NOTE:**  
The same image can create more containers, just like a class can be used to create multiple objects.

---

<div id="crucial"></div>

## 02 - Crucial differences between Docker Image and Docker Container

While it is simpler to think of a container as a **running image,** this is not very accurate.

> An image is actually a model that can be turned into a container.

To turn an image into a container, the Docker engine takes the image, adds:

 - A read and write file system;
 - Initializes various settings;
 - Includes network ports;
 - Container name;
 - ID;
 - Volume;
 - Resource limits...

**NOTE:**  
A running container has a currently running process, but a container can also be stopped (or terminated in Docker terminology). A terminated container is not the same as an image as it is restartable and will retain its settings and any file system changes.

**NOTE:**  
Another crucial observation is that this interrupted container will keep the settings and changes, but the image we use to create our container will remain immutable - That is, if we want to change something in the Image we don't do it from the container but from the **Dockerfile**.

---

**REFERENCES:**  
[Which is the difference between a Docker image and a container? How to create a docker file](https://www.iperiusbackup.net/en/docker-image-container-howto-create-dockerfile/)

---

**Rodrigo Leite -** *drigols*
