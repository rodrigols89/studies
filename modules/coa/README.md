# Computer Organization and Architecture

## Contents

 - **Processors:**
   - [**Registers:**](#intro-to-registers)
   - **Processors Architectures (Describes the characteristics of an *"processor line"*):**
     - [x86](#intro-x86)
       - [x86 and Von Neumann Architecture (+Von Neumann bottleneck)](#x86-vna)
     - [AMD64](#intro-amd64)
     - [ARM](#intro-arm)
















<!--- ( Processors/Registers ) --->>

---

<div id="intro-to-registers"></div>

## Registers

x













<!--- ( Processors/Processors Architectures ) --->

---

<div id="intro-x86"></div>

## x86

> The **x86 processor** was born with *"Intel's 8086"* in *1978*.

 - Basic service for a lot of processors.
 - Currently operates in 32 bits.

---

<div id="x86-vna"></div>

## x86 and Von Neumann Architecture (+Von Neumann bottleneck)

> The *x86 Architecture* follows the **Von Neumann Architecture**.

The Von Neumann Architecture is the following:

![img](images/von-neumann-01.png)  

See that the CPU communicates with the memory by the **System Bus (Control Bus, Data Bus, and Address Bus**:

 - **Buses – Data is transmitted from one part of a computer to another, connecting all major internal components to the CPU and memory:**
   - **Data Bus:**
     - *It carries data among the memory unit (transporta dados entre a unidade de memória)*, the I/O devices, and the processor.
   - **Address Bus:**
     - It carries the address of data (not the actual data) between memory and processor. 
   - **Control Bus:**
     - It carries control commands from the CPU (and status signals from other devices) in order to control and coordinate all the activities within the computer.

**Von Neumann bottleneck:**
However, if you paid attention to Von Neumann's model, you will see that it is only possible to access memory once at a time. In other words, you either read or write. But not both at the same time.

---

<div id="intro-amd64"></div>

## AMD64

> The **AMD64 processor** was born with the *"AMD Opteron"* in *2003*.

  - Currently operates in 64-bit.
  - Backward compatibility with x86 (also called x86-64).

---

<div id="intro-arm"></div>

## ARM

> The **ARM processor** was born with the *"Acorn ARM1"* in *1985*.

  - Currently operates in 32-bit.
  - Suitable (próprio) for Embedded Systems.


































































































---

**Rodrigo** **L**eite da **S**ilva
