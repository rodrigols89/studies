# WSL Commands

## Contents

 - [View your current directory in Windows File Explorer](#current)
 - [wsl --list --online](#list-dist)
 - [wsl --list --verbose](#list-my-dist)
 - [wsl --status](#status)
 - [--unregister](#unregister)
 - [Distribution Release](#release)
 - [Set default "WSL" version](#setwsl)
 - [Set distribution version](#distribution-version)
 - [Shutdown vs. Terminate](#shutdown-terminate)

---

<div id="current"></div>

## View your current directory in Windows File Explorer

You can view the directory where your files are stored by opening the **Windows File Explorer** from the command line, using:

```python
explorer.exe .
```

**NOTE:**  
To view all of your available Linux distributions and their root file systems in Windows File explorer, in the **address bar** enter:

```python
 \\wsl$
```

---

<div id="list-dist"></div>

## wsl --list --online

```python
wsl --list --online
```

**NOTE:**  
See a list of the Linux distributions available through the online store. This command can also be entered as: **wsl -l -o**.

---

<div id="list-my-dist"></div>

## wsl --list --verbose

```python
wsl --list --verbose
```

**NOTE:**  
See a list of the Linux distributions installed on your Windows machine, including the state (whether the distribution is running or stopped) and the version of WSL running the distribution (WSL 1 or WSL 2).

This command can also be entered as:

```python
wsl -l -v
```

Additional options that can be used with the list command include:

 - **--all** to list all distributions.
 - **--running** to list only distributions that are currently running.

---

<div id="status"></div>

## wsl --status

```python
wsl --status
```

**NOTE:**  
See general information about your WSL configuration, such as default distribution type, default distribution, and kernel version.

---

<div id="unregister"></div>

## --unregister

> While Linux distributions can be installed through the Microsoft Store, they can't be uninstalled through the store.

To unregister and uninstall a WSL distribution:

```python
wsl --unregister <DistributionName>
```

Replacing `<DistributionName>` with the name of your targeted Linux distribution will unregister that distribution from WSL so it can be reinstalled or cleaned up.

**CAUTION:**  
Once unregistered, all data, settings, and software associated with that distribution will be permanently lost. Reinstalling from the store will install a clean copy of the distribution. For example:

```python
wsl --unregister Ubuntu
```

---

<div id="release"></div>

## Distribution Release

To see your distribution **Release** is very simple:

**CONSOLE:**  
```python
cat /etc/os-release 
```

**OUTPUT:**  
```python
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
NAME="Debian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
VERSION_CODENAME=stretch
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```






---

<div id="setwsl"></div>

## Set default "WSL" version


```python
wsl --set-default-version <Version>
```

**NOTE:**  
To set a default version of WSL 1 or WSL 2, replacing `<Version>` with either the number 1 or 2 to represent which version of WSL you would like the installation to default on for new Linux distribution installations. For example

```python
wsl --set-default-version 2
```

---

<div id="distribution-version"></div>

## Set distribution version

```python
wsl --set-version <distribution name> <versionNumber>
```

**NOTE:**  
To designate the version of WSL (1 or 2) that a Linux distribution is running on, replace `<distribution name>` with the name of the distribution and replace `<versionNumber>` with 1 or 2.

---

<div id="shutdown-terminate"></div>

## Shutdown vs. Terminate

```python
wsl --shutdown
```

> Immediately **terminates all running distributions** and **the WSL 2 lightweight utility virtual machine**.

**NOTE:**  
This command may be necessary in instances that require you to restart the WSL 2 virtual machine environment, such as changing memory usage limits or making a change to your **.wslconfig file**.

```python
wsl --terminate <Distribution Name>
```

**NOTE:**  
To **terminate the specified distribution**, or stop it from running, replace `<Distribution Name>` with the name of the targeted distribution.

---

**REFERENCES:**  
[Basic commands for WSL](https://docs.microsoft.com/en-us/windows/wsl/basic-commands)  

---

**Rodrigo Leite -** *drigols*
