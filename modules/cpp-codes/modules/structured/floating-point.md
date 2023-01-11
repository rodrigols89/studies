# Floating Point

## Contents

 - [How Floating Point are stored (Mantissa and Exponent)](#mantissa-exponent)
 - [Floating Point Limits (+Significative digits)](#limits)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)

---

<div id="mantissa-exponent"></div>

## How Floating Point are stored (Mantissa and Exponent)

The computer store a real number in two parts:

 - **A value** (Mantissa)
 - **Scale factor** (Exponent)

For example, see the image below:

![img](images/floating-point​-01.png)  

 - If you pay attention will see that the values **"34.125"** and **"341.25"** have the same value when stored in the memory:  **"0.34125"**.
 - The difference is the **scale**, that's, **how many times the  floating point shift left**:
   - Each time the floating point shift left increases 1 scale.

For example:

![img](images/floating-point​-02.png)  

To back to real value stored just multiply the *mantissa* value stored in the memory by *scale factor*:

![img](images/floating-point​-03.png)  

**NOTE:**  
However, the **scale factor** is not stored in the memory as a *multiplier (10, 100, 100)*, but as **exponent**:

![img](images/floating-point​-04.png)  

---

<div id="limits"></div>

## Floating Point Limits (+Significative digits)

As much as there is a bit difference in the **float**, **double**, and **long double** types, the main difference between these types is:

 - Significative digits of mantissa.
 - Max value to exponent:
   - Scale factor.

> **BUT, WHAT'S "SIGNIFICATIVE DIGITS"?**

Imagine you have the follow numbers:

 - **143.06:**
   - Have 5 significative digits.
 - **4.50:**
   - Have 2 significative digits, since if we remove the last digit (0) it does not change **4.50**, because **4.50 = 4.5**.

![img](images/floating-point​-05.png)  

**NOTE:**  
That's, **significative digits** are important digits of the number.

> **OK, NOW, WHAT'S "MAX VALUE OF EXPONENT"?**

To understand **"max value of exponent"** see the image below:

![img](images/floating-point​-07.png)  
![img](images/floating-point​-06.png)  

 - In the image above only the part after the dot is stored in the mantissa:
   - That is, the **"0."** is ignored when storing the mantissa in memory.
 - However, when getting the mantissa in memory the **"0."** is put back to make the mantissa return to its true value when multiplied by the exponent in base 10:
   - **Mantissa * 10<sup>exponent</sup> = Real value**.

x

[](src/)
```cpp

```

**COMPILATION AND RUN:**
```cpp

```

**OUTPUT:**  
```cpp

```


---

**REFERENCES:**  
[]()  
[]()  
[]()  
[]()  
[]()  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
