# Financial Math

## Contents

 - [**Percents:**](#percents)
   - [Percentage = part/whole x 100](#percentage-part)
   - [Part = (percentage/100) x whole](#finding-the-part)
   - [Whole = part / (percentage / 100)](#finding-the-whole)
   - **Percentage Conversions:**
     - [Percents to Decimals (Divide by 100 or Move two places to the left "←")](#percents-to-decimals)
     - [Decimals to Percents (Multiply by 100 or Move two places to the right "→")](#decimals-to-percents)
   - **Percents - Tips & Tricks:**
     - [Percentages calculus are symmetry (or bidirectional)](#percentages-calculus-symmetry)
 - [**Settings**](#settings)
 - [**REFERENCES**](#ref)




































































































<!--- ( Percents ) --->

---

<div id="percents"></div>

## Percents

> When we say **"Percent"** we are really saying **"per 100"**.

For example, one percent (1%) means 1 per 100:

![img](images/1-per-100.png)  

To understand more easily, let's take a look at the examples below:

**50% means 50 per 100:**
![img](images/50-per-100.png)  

**25% means 25 per 100:**
![img](images/25-per-100.png)

Because **"Percent"** means **"per 100"** think:

> **"This should be divided by 100"**

**NOTE:**  
So, **75%** really means $\frac{75}{100}$.

---

<div id="percentage-part"></div>

## Percentage = part/whole x 100

To determine the percentage of a number, we need to:

 - Divide the *"given value (part)"*;
 - By the *"total value (whole)"*;
 - And then *"multiply the resultant by 100"*.

![img](images/percent-formula.png)  

For example, imagine we have *200 apples* and *10* of them are bad...

> **What is the percentage those 10 apples represent?**

Using our formula we have:

![img](images/percent-formula-01.png)  

---

<div id="finding-the-part"></div>

## Part = (percentage/100) x whole

To find out the part of a percentage we use the following formula:

![img](images/percent-formula-02.png)  

> **NOTE:**  
> - See that first, we need to *divide the percentage by 100*. This is because we first need to *convert the percentage to decimal*.
> - That's, we can also use the ["Percents to Decimals"](#percents-to-decimals) tip to *first convert to decimal* and then divide by *whole*.

For example, imagine we have 200 apples...

> ***15%* of *200* apples are bad. How many apples are bad?**

Using our formula we have:

![img](images/percent-formula-03.png)

> **So, "30" apples are bad!**

---

<div id="finding-the-whole"></div>

## Whole = part / (percentage / 100)

To find the whole of a percentage of a part we use the following formula:

![img](images/percent-formula-04.png)

For example:

> If I have 30 apples that represent 15% of the whole, how many apples do I have?

![img](images/percent-formula-05.png)

> **So, the whole is 200 apples.**










<!--- ( Percents/Percentage Conversions ) --->

---


<div id="percents-to-decimals"></div>

## Percents to Decimals (Divide by 100 or Move two places to the left "←")

> To convert from percentage to decimal, we need to **divide the percentage (%) by 100** and **remove the “%” sign**.

For example, let's convert **75%** to decimal:

![img](images/percents-latex-02.png)  

**NOTE:**  
Another easy way to divide by 100 is to move the decimal point 2 places to the left. For example:

![img](images/percent-to-decimal-01.png)  
**Move the decimal point 2 places to the left, and remove the *"%"* sign.**  

**Example-01: Convert 8.5% to decimal**  
```md
8.5 → 0.85 → 0.085
```

**NOTE:**  
Note how we inserted an extra **"0"** as needed. So, the answer is **8.5% = 0.085**.

**Example-02: Convert 250% to decimal**  
```md
Move the decimal point two places to the left:
250. → 25. (zero here is removed, that's, not use 25.0) → 2.5
```

So, the answer is **250% = 2.5**.

---

<div id="decimals-to-percents"></div>

## Decimals to Percents (Multiply by 100 or Move two places to the right "→")

> To convert from decimal to percentage, we need to **"multiply the decimal number by 100** and **add the “%” sign**.

For example:

![img](images/percents-latex-01.png)  

**NOTE:**  
Another easy way to multiply by 100 is to move the decimal point 2 places to the right. For example:

![img](images/decimal-to-percent-01.png)  
**Move the decimal point 2 places to the right (and add the "%" sign!)**

**Example-01: Convert 0.35 to percent**  
```md
0.35 → 3.5 (zero here is removed) → 35.
Answer 0.35 = 35%
```

**Example: Convert 0.985 to percent**  
```md
0.985 → 9.85 (zero here is removed) → 98.5
Answer 0.985 = 98.5%
```

**Example: Convert 1.2 to percent**
```md
1.2 → 12. → 120.
Answer 1.2 = 120%

NOTE: See that here we had to adds a zero and not remove it.
```










<!--- ( Percents/Tips and Tricks ) --->

---

<div id="percentages-calculus-symmetry"></div>

## Percentages calculus are symmetry (or bidirectional)

This little rule can make some percentage calculations easier:

**x% of y = y% of x**

For example:

 - **8% of 50** is the same as **50% of 8**:
   - If **50%** of **8** is **4**.
   - So, **8% of 50** is also **4**.



































































































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv math-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source math-environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source math-environment/Scripts/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**Now, Be Happy!!!** 😬





<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **Percentage:**
   - [Percent example](https://www.instagram.com/p/Cw0qpWVPA46/)
   - [Percents (%)](https://www.mathsisfun.com/percentage.html)
   - [Convert Percents to Decimals](https://www.mathsisfun.com/converting-percents-decimals.html)
   - [Convert Decimals to Percents](https://www.mathsisfun.com/converting-decimals-percents.html)
   - [Percentage](https://byjus.com/maths/percentage/)
   - [Percentage Difference Calculator](https://www.justcalculateit.com/percentage-difference-calculator/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
