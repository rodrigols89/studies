# WSL - Windows Subsystem for Linux

## Contents

 - **Concepts:**
 - **Commands:**
   - **On Windows:**
     - [Checking installed (or online) machines on your WSL](#check-installed)
     - [wsl --shutdown](#shutdown-command)
     - [wsl --terminate](#terminate-command)
   - **On Virtual Machine:**
     - [Cheking release of the current O.S](#check-release)
     - [View your current directory in Windows File Explorer](#current-dir)
 - [**References**](#ref)








































<!--- ( Commands/On Windows ) --->

---

<div id="check-installed"></div>

## Checking installed (or online) machines on your WSL (On Windows)

To check installed (or online) machines on your WSL you can run the following commands:

```bash
wsl --list --verbose
```

```bash
wsl -l -v
```

---

<div id="shutdown-command"></div>

## wsl --shutdown

```bash
wsl --shutdown
```

> Immediately **terminates all running distributions** and **the WSL 2 lightweight utility virtual machine**.

**NOTE:**  
This command may be necessary in instances that require you to restart the WSL 2 virtual machine environment, such as changing memory usage limits or making a change to your **.wslconfig file**.

---

<div id="terminate-command"></div>

## wsl --terminate

```bash
wsl --terminate <distribution-name>
```

**NOTE:**  
To **terminate the specified distribution**, or stop it from running, replace `<distribution-name` with the name of the targeted distribution.

For example:

```bash
wsl --terminate Ubuntu-20.04
```








































<!--- ( Commands/On Virtual Machine ) --->

---

<div id="check-release"></div>

## Cheking release of the current O.S

To check the **release** of the current *O.S* run the following command:

**CONSOLE:**  
```bash
cat /etc/os-release 
```

**OUTPUT:**  
```bash
NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

---

<div id="current-dir"></div>

## View your current directory in Windows File Explorer

You can view the directory where your files are stored on the *Virtual Machine* by opening the **Windows File Explorer** from the command line, using:

```bash
explorer.exe .
```








































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [Basic commands for WSL](https://docs.microsoft.com/en-us/windows/wsl/basic-commands)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
