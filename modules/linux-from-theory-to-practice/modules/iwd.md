# iwd (iNet wireless daemon) 

## Contents

 - [Intro to iwd](#intro)
 - [Initializing iwd interactive prompt](#interactive-prompt)

---

<div id="intro"></div>

## Intro to iwd

> **iwd (iNet wireless daemon)** is a wireless daemon for Linux written by **Intel**. The core goal of the project is to optimize resource utilization by not depending on any external libraries and instead utilizing features provided by the Linux Kernel to the maximum extent possible.

First we need install the software **iwd**:

**CONSOLE:**  
```python
yay -S iwd
```

or

**CONSOLE:**  
```python
pacman -S iwd
```

---

<div id="interactive-prompt"></div>

## Initializing iwd interactive prompt

To initialize the **iwd** just enter **iwctl** on the console:

**CONSOLE:**  
```python
iwctl
```

**OUTPUT:**  
```python
[iwd]# ...
```

**NOTE:**  
The interactive prompt is then displayed with a prefix of `[iwd]#`.

 - **Tip:**
   - In the **iwctl** prompt you can auto-complete commands and device names by hitting *Tab*.
   - To exit the interactive prompt, send EOF by pressing **Ctrl+d**.
   - You can use all commands as command line arguments without entering an interactive prompt. For example: **iwctl device wlan0 show**.

---

<div id=""></div>

## Connect to a network

First, if you do not know your wireless device name, list all Wi-Fi devices:

**CONSOLE:**  
```python
[iwd]# device list
```

Coming soon...

---

**REFERENCES:**  
[iwd](https://wiki.archlinux.org/title/Iwd)  
[]()  
[]()  
[]()  
[]()  

---

**Rodrigo Leite -** *drigols*
