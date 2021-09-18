/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
  // Creates an array of 50 integers (200 bytes).
  int *v = (int*) malloc(200);

  /*
  * Increases the allocated memory
  * to 100 integers (400 bytes).
  */
  v = (int*) realloc(v, 400);

  return 0;
}
