# Networking

## Contents

 - [Accessing Linux networking apps from Windows (localhost)](#accessing-linux)
 - [Accessing Windows networking apps from Linux (host IP)](#accessing-windows)

---

<div id="accessing-linux"></div>

## Accessing Linux networking apps from Windows (localhost)

If you are building a networking app (for example an app running on a NodeJS or SQL server) in your Linux distribution, you can access it from a Windows app (like your Edge or Chrome internet browser) using localhost (just like you normally would).

**NOTE:**  
However, if you are running an older version of Windows (Build 18945 or less), you will need to get the IP address of the Linux host VM (or update to the latest Windows version).

To find the IP address of the virtual machine powering your Linux distribution:

 - From your WSL distribution (ie Ubuntu), run the command: **ip addr**.
 - Find and copy the address under the **inet** value of the **eth0** interface.
 - If you have the grep tool installed, find this more easily by filtering the output with the command: **ip addr | grep eth0**
 - Connect to your Linux server using this IP address.


```python
ip addr | grep eth0
```

![img](images/wsl2-network-w2l.jpg)  

---

<div id="accessing-windows"></div>

## Accessing Windows networking apps from Linux (host IP)

If you want to access a networking app running on Windows (for example an app running on a NodeJS or SQL server) from your Linux distribution (ie Ubuntu), then you need to use the IP address of your host machine. While this is not a common scenario, you can follow these steps to make it work:

 - Obtain the IP address of your host machine by running this command from your Linux distribution: **cat /etc/resolv.conf**
 - Copy the IP address following the term: **nameserver**.
 - Connect to any Windows server using the copied IP address.

**NOTE:**  
The picture below shows an example of this by connecting to a Node.js server running in Windows via curl:

![img](images/wsl2-network-l2w.png)  

---

**REFERENCES:**  
[Accessing network applications with WSL](https://docs.microsoft.com/en-us/windows/wsl/networking)  

---

**Rodrigo Leite -** *drigols*
