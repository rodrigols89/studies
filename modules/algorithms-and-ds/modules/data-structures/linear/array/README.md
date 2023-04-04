# Array

## Contents

 - **General:**  
   - [Advantages and Disadvantages of Arrays](#adv-disadv)

---

<div id="adv-disadv"></div>

## Advantages and Disadvantages of Arrays

 - **Advantages:**
   - Arrays allow random access to elements. This makes accessing elements by position faster.
   - Arrays have better cache locality which makes a pretty big difference in performance.
   - Arrays represent multiple data items of the same type using a single name.
   - Arrays store multiple data of similar types with the same name.
   - Array data structures are used to implement the other data structures like linked lists, stacks, queues, trees, graphs, etc.
 - **Disadvantages:**
   - **Fixed size:**
     - Arrays have a fixed size that is determined at the time of creation. This means that if the size of the array needs to be increased, a new array must be created and the data must be copied from the old array to the new array, which can be time-consuming and memory-intensive.
   - **Memory allocation issues:**
     - Allocating a large array can be problematic, particularly in systems with limited memory. If the size of the array is too large, the system may run out of memory, which can cause the program to crash.
   - **Insertion and deletion issues:**
     - Inserting or deleting an element from an array can be inefficient and time-consuming because all the elements after the insertion or deletion point must be shifted to accommodate the change.
   - **Wasted space:**
     - If an array is not fully populated, there can be wasted space in the memory allocated for the array. This can be a concern if memory is limited.
     - Allocating less memory than required to an array leads to loss of data.
   - An array is homogeneous in nature so, a single array cannot store values of different data types.
   - Arrays store data in contiguous memory locations, which makes deletion and insertion very difficult to implement:
     - This problem is overcome by implementing linked lists, which allow elements to be accessed sequentially.

---

**REFERENCES:**  
[Introduction to Arrays – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-arrays-data-structure-and-algorithm-tutorials/)  
[]()  
[]()  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
