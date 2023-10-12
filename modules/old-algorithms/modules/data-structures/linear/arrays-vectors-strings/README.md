# Arrays, Vectors, Strings

## Contents

 - **Standard Template Library (STL):**
   - **General:**
     - [container::clear()](#container-clear)
   - **std::array:**
     - [`std::array<data-type, numElements> array-name`](#std-array)
   - **std::vector:**
   - [`std::vector<data-type> vector-name`](#std-vector)
   - **std::string:**
     - [How to remove special characters and white spaces](#rsc-and-ws)
 - **Tips & Tricks:**
   - [Array: Advantages and Disadvantages](#array-advantages-disadvantages)
   - [std:array vs. std:vector](#array-vs-vector)
 - [**REFERENCES**](#ref)

<!--- ( STL/General ) --->

<div id="container-clear"></div>

## container::clear()

The **clear()** function can be used to *remove all the elements of the Vector or String container*, thus making it size 0.

> **NOTE:**  
> The **std::array** container has not this function.

For example:

[clear.cpp](src/stl/clear.cpp)
```cpp
#include <iostream>
#include <array>
#include <vector>
#include <string>

int main()
{
    std::cout << "------------- ( Vecto example ) --------------\n";
    std::vector<int> myvector = {1, 2, 3, 4, 5};
    std::cout << "Vector elements before apply clear() function:\n";
    for (int element : myvector)
        std::cout << element << " ";
    myvector.clear();
    std::cout << "\nVector elements before after clear() function:\n";
    for (int element : myvector)
        std::cout << element << " ";

    std::cout << "\n------------- ( String example ) --------------";
    std::string mystring = "Hello World!";
    std::cout << "\nString elements before apply clear() function:\n";
    std::cout << mystring;
    mystring.clear();
    std::cout << "\nString elements before after clear() function:\n";
    std::cout << mystring;

    return 0;
}
```

**COMPILATION AND RUN:**
```bash
g++ clear.cpp -o test.out && ./test.out
```

**OUTPUT:**
```bash
------------- ( Vecto example ) --------------
Vector elements before apply clear() function:
1 2 3 4 5 
Vector elements before after clear() function:

------------- ( String example ) --------------
String elements before apply clear() function:
Hello World!
String elements before after clear() function:
```

 - **Time Complexity:** O(N)
 - **Auxiliary Space:** O(1)








































<!--- ( STL/std::array ) --->

---

<div id="std-array"></div>

## `std::array<data-type, numElements> array-name`

 - **Insert functions:**
   - **fill():**
     - This function is used to fill the entire array with a particular value:
       - For example, fill with zeros.
 - **Remove functions:**
 - **Useful functions:**
   - **at():**
     - The *"at()"* function is used to access the elements of array. 
   - **"[index]" operator:**
     - This is similar to C-style arrays. This method is also used to access array elements.
   - **empty():**
     - This function returns:
       - *true* when the array size is zero.
       - Else returns *false*. 
   - **size():**
     - It returns the number of elements in array. This is a property that C-style arrays lack.
   - **max_size():**
     - It returns the maximum number of elements array can hold i.e, the size with which array is declared. The *size()* and *max_size()* return the same value.
   - **front():**
     - This returns reference to the first element of array.
   - **back():** 
     - This returns reference to the last element of array.
   - **swap():**
     - The *swap()* swaps all elements of one array with other.

See the test code below:

[driver_array.cpp](src/stl/driver_array.cpp)
```cpp
#include <iostream>
#include <array>

int main()
{
    std::array<int, 6> arr = {1, 2, 3, 4, 5, 6};

    // Printing array elements using at() functions.
    std::cout << "Print Array elements using at() function: ";
    for (int i = 0; i < arr.size(); i++)
        std::cout << arr.at(i) << " ";

    std::cout << "\nPrint the first element using '[index]' operator: " << arr[0];
    std::cout << "\nPrint the second element using '[index]' operator: " << arr[1];
    std::cout << "\nPrint the third element using '[index]' operator: " << arr[2];

    std::cout << "\nempty() = True to empty list or False to not empty list: " << arr.empty();
    std::cout << "\nsize(): " << arr.size();
    std::cout << "\nmax_size(): " << arr.max_size();
    std::cout << "\nfront(): " << arr.front();
    std::cout << "\nback(): " << arr.back();

    std::array<int, 5> arr_two = {10, 20, 30, 40, 50};
    std::array<int, 5> arr_three = {60, 70, 80, 90, 100};

    std::cout << "\nElements of the array_two: ";
    for (int i = 0; i < arr_two.size(); i++)
        std::cout << arr_two.at(i) << " ";

    std::cout << "\nElements of the arr_three: ";
    for (int i = 0; i < arr_three.size(); i++)
        std::cout << arr_three.at(i) << " ";

    arr_two.swap(arr_three);
    std::cout << "\nAfter swap() the array elements:";

    std::cout << "\nElements of the array_two: ";
    for (int i = 0; i < arr_two.size(); i++)
        std::cout << arr_two.at(i) << " ";

    std::cout << "\nElements of the arr_three: ";
    for (int i = 0; i < arr_three.size(); i++)
        std::cout << arr_three.at(i) << " ";

    std::array<int, 10> zeros;
    zeros.fill(0);
    std::cout << "\nArray filled with zeros: ";
    for (int i = 0; i < zeros.size(); i++)
        std::cout << zeros.at(i) << " ";

    return 0;
}
```

**INPUT:** 
```bash
g++ driver_array.cpp -o test.out && ./test.out
```

**OUTPUT:** 
```bash
Print Array elements using at() function: 1 2 3 4 5 6 
Print the first element using '[index]' operator: 1
Print the second element using '[index]' operator: 2
Print the third element using '[index]' operator: 3
empty() = True to empty list or False to not empty list: 0
size(): 6
max_size(): 6
front(): 1
back(): 6
Elements of the array_two: 10 20 30 40 50 
Elements of the arr_three: 60 70 80 90 100 
After swap() the array elements:
Elements of the array_two: 60 70 80 90 100 
Elements of the arr_three: 10 20 30 40 50
Array filled with zeros: 0 0 0 0 0 0 0 0 0 0
```








































<!--- ( STL/std::vector ) --->

---

<div id="std-vector"></div>

## `std::vector<data-type> vector-name`

```cpp
std::vector<char> vector-name;
std::vector<int> vector-name;
std::vector<float> vector-name;
std::vector<double> vector-name:
```

 - **Insert functions:**
   - **assign():**
     - It assigns new value to the vector elements by replacing old ones:
       - The first parameter is the number of elements to insert (rewrite) into the Vector.
       - The second parameter is the value to insert (rewrite) into the Vector.
   - **push_back():**
     - adds an element to the end of the vector:
 - **Remove functions:**
 - **Useful functions:**
   - **at():**
     - Returns a reference to the element at position ‘n’ in the vector.
   - **size():**
     - Returns the number of elements in the vector.
   - **max_size():**
     - Returns the maximum number of elements that the vector can hold.
   - **capacity()**
     - Returns the size of the storage space currently allocated to the vector expressed as number of elements.
   - **front():**
     - Returns a reference to the first element in the vector.
   - **back():**
     - Returns a reference to the last element in the vector.
   - **data():**
     - Returns a direct pointer to the memory array used internally by the vector to store its owned elements.

See the test code below:

[driver_vector.cpp](src/stl/driver_vector.cpp)
```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v = {10, 20, 30, 40, 50};

    std::cout << "Print Vector elements using at() function: ";
    for (int i = 0; i < v.size(); i++)
        std::cout << v.at(i) << " ";

    std::cout << "\nsize(): " << v.size();
    std::cout << "\nmax_size(): " << v.max_size();
    std::cout << "\ncapacity(): " << v.capacity();
    std::cout << "\nfront(): " << v.front();
    std::cout << "\nback(): " << v.back();
    std::cout << "\ndata(): " << v.data();

    v.assign(5, 0);
    std::cout << "\nPrint Vector elements after use 'assing(5, 0)' function: ";
    for (int i = 0; i < v.size(); i++)
        std::cout << v.at(i) << " ";
    
    v.push_back(10);
    std::cout << "\nPrint the Vector after 'push_back(10)': ";
    for (int i = 0; i < v.size(); i++)
        std::cout << v.at(i) << " ";

    return 0;
}
```

**INPUT:** 
```bash
g++ driver_vector.cpp -o test.out && ./test.out
```

**OUTPUT:** 
```bash
Print Vector elements using at() function: 10 20 30 40 50 
size(): 5
max_size(): 4611686018427387903
capacity(): 5
front(): 10
back(): 50
data(): 0xf326c0
Print Vector elements after use 'assing(5, 0)' function: 0 0 0 0 0 
Print the Vector after 'push_back(10)': 0 0 0 0 0 10 
```








































<!--- ( STL/std::string ) --->

<div id="rsc-and-ws"></div>

## How to remove special characters and white spaces

```cpp
// Remove special characters and white spaces.
search_number.erase(
    std::remove_if(
        search_number.begin(),
        search_number.end(),
        [](unsigned char c) { return !std::isalnum(c) || c == ' '; }),
    search_number.end());
```

 - **erase():**
   - A função **erase()** é um método da classe **std::string** que permite remover caracteres ou substrings de uma string.
 - **std::remove_if():**
   - A função **std::remove_if** é um algoritmo da biblioteca padrão do C++ que permite remover elementos de um contêiner (como um vetor, uma string, etc.) com base em uma condição especificada por meio de uma função ou um predicado:
     - **NOTE:**É  importante ressaltar que **"std::remove_if"** não exclui fisicamente os elementos do contêiner, apenas os move para o final e altera o tamanho lógico do contêiner. Para remover efetivamente os elementos, é necessário usar métodos como **erase()** para ajustar o tamanho do contêiner.
     - **std::remove_if(first, last, predicate)**:
       - **first:** é um iterador apontando para o primeiro elemento do intervalo onde a remoção será aplicada:
         - Para o nosso caso é o *PRIMEIRO CARACTERE* do número de telefone **"search_number.begin()"**
       - **last:** é um iterador apontando para o elemento logo após o último elemento do intervalo onde a remoção será aplicada:
         - Para o nosso caso é o *ÚLTIMO CARACTERE* do número de telefone **"search_number.end()"**.
       - **predicate:** é uma função ou um predicado que retorna true para os elementos que devem ser movido para o final do container:
         - Para o nosso caso são *CARACTERES NÃO ALFANUMÉRICOS* ou *ESPAÇOS EM BRANCO* **"[](unsigned char c) { return !std::isalnum(c) || c == ' '; })"**.
     - **No caso do código acima, "std::remove_if" é usado para mover os caracteres não alfanuméricos (ou seja, os que não letras ou não números) ou espaços em brancos da string "search_number" para o final do container:**
       - O predicado `[](unsigned char c) { return !std::isalnum(c) || c == ' '; }` é usado como a condição para mover os caracteres que não são alfanuméricos (ou seja, os que não letras ou não números) e os espaços em brancos e para o final do container:
         - A função (predicado) lambda `[](unsigned char c) { return !std::isalnum(c) || c == ' '; }` recebe um caractere **"c"** como entrada e retorna *true*:
           - Quando o caractere **"c"** não é alfanumérico (ou seja, os que não letras ou não números).
           - Ou (||) quando é um espaço em branco.
         - O algoritmo **"std::remove_if"** move todos esses caracteres para o final da string e, em seguida, **search_number.erase()** os remove da string, efetivamente removendo os caracteres não alfanuméricos (ou seja, os que não letras ou não números) e espaços em branco.








































<!--- ( Tips & Tricks ) --->

---

<div id="array-advantages-disadvantages"></div>

## Array: Advantages and Disadvantages

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

<div id="array-vs-vector"></div>

## std:array vs. std:vector


| std:array                                | std:vector                                |
-------------------------------------------|-------------------------------------------|
|Size of arrays are fixed.|Size of vectors are resizable i.e they can grow (crescer) and shrink (escolher) as vectors are allocated on heap memory.|
|Array stores a fixed-size sequential collection of elements of the same type and it is index based.|Vector is a sequential container to store elements and not index based.|
|Arrays require manual memory management.|Vectors handle memory allocation and deallocation automatically.|
|Arrays cannot be copied or assigned directly.|Vectors can be copied or assigned directly.|
|Arrays require manual sorting.|Vectors provide built-in sorting functions.|
|Array access elements in constant time irrespective of their location as elements are arranged in a contiguous memory allocation.|Vector takes more time in accessing elements.|
|Array is memory efficient data structure.|Vector occupies more memory.|








































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [Introduction to Arrays – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-arrays-data-structure-and-algorithm-tutorials/)
 - **Standard Template Library (STL):**
   - [Array class in C++](https://www.geeksforgeeks.org/array-class-c/)
   - [Vector in C++ STL](https://www.geeksforgeeks.org/vector-in-cpp-stl/)
   - [Difference between std::vector and std::array in C++](https://www.tutorialspoint.com/difference-between-std-vector-and-std-array-in-cplusplus)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
