# WSL Settings

## Contents

 - [Set up your Linux username and password](#username-and-password)
 - [Update and upgrade packages](#update-and-upgrade-packages)

---

<div id="username-and-password"></div>

## Set up your Linux username and password

Once the process of installing your Linux distribution with WSL is complete, open the distribution (Ubuntu by default) using the Start menu. You will be asked to create a **User Name** and **Password** for your Linux distribution.

 - This **User Name** and **Password** is specific to each separate *Linux distribution* that you install and has no bearing on your Windows user name.
 - Once you create a **User Name** and **Password**, the account will be your default user for the distribution and automatically sign-in on launch.
 - This account will be considered the Linux administrator, with the ability to run **sudo (Super User Do)** administrative commands.
 - Each Linux distribution running on WSL has its own Linux user accounts and passwords. You will have to configure a Linux user account every time you add a distribution, reinstall, or reset.

**NOTE:**  
To change or reset your password, open the Linux distribution and enter the command: **passwd**. You will be asked to enter your current password, then asked to enter your new password, and then to confirm your new password.

---

<div id="update-and-upgrade-packages"></div>

## Update and upgrade packages

We recommend that you regularly **update** and **upgrade** your packages using the preferred package manager for the distribution. For **Ubuntu** or **Debian**, use the command:

```python
sudo apt update && sudo apt upgrade
```

**NOTE:**  
Windows does not automatically update or upgrade your Linux distribution(s). This is a task that most Linux users prefer to control themselves.

---

**REFERENCES:**  
[Set up a WSL development environment](https://docs.microsoft.com/en-us/windows/wsl/setup/environment)  

---

**Rodrigo Leite -** *drigols*
