# wsl.conf x .wslconfig

## Contents

 - [What is the difference between wsl.conf and .wslconfig?](#diff)
   - [wsl.conf](#wsl-conf)
   - [.wslconfig](#wslconfig)

---

<div id="diff"></div>

## What is the difference between wsl.conf and .wslconfig?

You can configure the settings for your installed Linux distributions that will automatically be applied every time you launch WSL in two ways, by using:

 - **.wslconfig** to configure settings *globally* across all installed distributions running on WSL 2.
 - **wsl.conf** to configure settings *per-distribution* for Linux distros running on WSL 1 or WSL 2.

Both file types are used for configuring WSL settings, but the location where the file is stored, the scope of the configuration, and the version of WSL running your distribution all impact which file type to choose.

**NOTE:**  
The version of WSL that you are running will impact the configuration settings. WSL 2 runs as a lightweight virtual machine (VM), so uses virtualization settings that allow you to control the amount of memory or processors used (which may be familiar if you use Hyper-V or VirtualBox).

---

<div id="wsl-conf"></div>

## wsl.conf

 - Stored in the **/etc** directory of the distribution as a unix file.
 - Used to configure settings on a *per-distribution* basis.
 - Settings configured in this file will only be applied to the *specific Linux distribution* that contains the directory where this file is stored.
 - Can be used for distributions run by either version, WSL 1 or WSL 2.
 - To get to the /etc directory for an installed distribution, use the distribution's command line with cd / to access the root directory, then **ls** to list files or **explorer.exe .** to view in Windows File Explorer. The directory path should look something like: `/etc/wsl.conf`.

---

<div id="wslconfig"></div>

## .wslconfig

 - Stored in your **%UserProfile% (In Windows File Explorer)** directory.
 - Used to configure settings globally across all installed Linux distributions running as the WSL 2 version.
 - Can be used only for distributions run by WSL 2:
   - Distributions running as WSL 1 will not be affected by this configuration as they are not running as a virtual machine.

**NOTE:**  
To get to your **%UserProfile%** directory, in PowerShell, use **cd ~** to access your home directory (which is typically your user profile, C:\Users\<UserName>) or you can open Windows File Explorer and enter **%UserProfile%** in the address bar.

**NOTE:**  
WSL will detect the existence of these files, read the contents, and automatically apply the configuration settings every time you launch WSL. If the file is missing or malformed (improper markup formatting), WSL will continue to launch as normal without the configuration settings applied.

---

**REFERENCES:**  
[What is the difference between wsl.conf and .wslconfig?](https://docs.microsoft.com/en-us/windows/wsl/wsl-config#what-is-the-difference-between-wslconf-and-wslconfig)  

---

**Rodrigo Leite -** *drigols*
