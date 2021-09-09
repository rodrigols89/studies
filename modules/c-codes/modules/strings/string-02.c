/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

int main ()
{
  /*
  * Initializing a String, Conventional form.
  */
  char nameOne[20] = {'J','o','a','o','\0'};
  printf("Name: %s\n", nameOne);

  char nameTwo[20] = "Joao";
  printf("Name: %s\n", nameTwo);
  system("pause");
  
  return (0);
}
