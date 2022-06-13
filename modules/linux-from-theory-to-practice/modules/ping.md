# ping

## Contents

 - [Intro to ping command](#intro)
 - [Testing connection with "ping -c n_times web_site"s](#testing)
 - [ping localhost](#localhost)

---

<div id="intro"></div>

## Intro to ping command

**ping** is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It is available for virtually all operating systems that have networking capability, including most embedded network administration software.

**NOTE:**  
Ping operates by means of **Internet Control Message Protocol (ICMP) packets**. Pinging involves sending an **ICMP** echo request to the target host and waiting for an **ICMP** echo reply. The program reports errors, packet loss, and a statistical summary of the results, typically including the minimum, maximum, the mean round-trip times, and standard deviation of the mean.

**NOTE:**  
To see all ping options enter **"ping -help"** in the console

---

<div id="testing"></div>

## Testing connection with "ping -c n_times web_site"

To testing connections with **ping** software is very easy, for example, we'll to testing website google.com:

**CONSOLE:**  
```python
ping -c 10 google.com
```

**OUTPUT:**  
```python
PING GOOgLE.Com (142.251.129.46) 56(84) bytes of data.
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=1 ttl=45 time=56.0 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=2 ttl=45 time=57.2 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=3 ttl=45 time=54.2 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=4 ttl=45 time=54.1 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=5 ttl=45 time=57.0 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=6 ttl=45 time=53.9 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=7 ttl=45 time=54.4 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=8 ttl=45 time=54.6 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=9 ttl=45 time=54.3 ms
64 bytes from gru06s72-in-f14.1e100.net (142.251.129.46): icmp_seq=10 ttl=45 time=54.2 ms

--- GOOgLE.Com ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9015ms
rtt min/avg/max/mdev = 53.899/54.991/57.173/1.190 ms
```

**NOTE:**  
See that we transmitting 10 packets with 0% packet loss in 9015ms time.

---

<div id="localhost"></div>

## ping localhost

> You can use the name to **ping localhost**. The name refers to your computer, and when we use this command, we say: **“ping this computer”**.

**CONSOLE:**  
```python
ping localhost -c 10
```

**OUTPUT:**  
```python
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.035 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.061 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.062 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.062 ms
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.062 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.063 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.061 ms
64 bytes from localhost (127.0.0.1): icmp_seq=8 ttl=64 time=0.065 ms
64 bytes from localhost (127.0.0.1): icmp_seq=9 ttl=64 time=0.060 ms
64 bytes from localhost (127.0.0.1): icmp_seq=10 ttl=64 time=0.064 ms

--- localhost ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9328ms
rtt min/avg/max/mdev = 0.035/0.059/0.065/0.008 ms
```

---

**REFERENCES:**  
[ping (networking utility)](https://en.wikipedia.org/wiki/Ping_(networking_utility))  

---

**Rodrigo Leite -** *drigols*
