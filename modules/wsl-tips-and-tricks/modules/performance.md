# WSL Performance

## Contents

 - [File storage and performance across file systems](#across-file-systems)

---

<div id="across-file-systems"></div>

## File storage and performance across file systems

> We recommend against working across operating systems with your files, unless you have a specific reason for doing so.

 - For the fastest performance speed, store your files in the WSL file system if you are working in a Linux command line (Ubuntu, OpenSUSE, etc).
 - If you're working in a Windows command line (PowerShell, Command Prompt), store your files in the Windows file system.

For example, when storing your WSL project files:

 - **Use the Linux file system root directory:** `\\wsl$\Ubuntu\home\<user name>\Project`
 - **Not the Windows file system root directory:** `/mnt/c/Users/<user name>/Project$ or C:\Users\<user name>\Project`

---

**REFERENCES:**  
[File storage and performance across file systems](https://docs.microsoft.com/en-us/windows/wsl/filesystems)  

---

**Rodrigo Leite -** *drigols*
