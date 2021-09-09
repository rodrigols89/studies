#include <bits/stdc++.h>

using namespace std;

int search(int arr[], int arrSize, int element)
{
  int i;
  for(i = 0; i < arrSize; i++)
    if(arr[i] == element)
      return i;
  return -1;
}

int main()
{
  int arr[] = {1, 10, 30, 15}; // Data.
  int element = 30; // Search element.
  int arrSize = sizeof(arr) / sizeof(arr[0]); // Array Size.

  cout << element << " is present at index " << search(arr, arrSize, element);

  return 0;
}
