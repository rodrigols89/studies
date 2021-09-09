/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
  // The size of a String.
  char palavra[20] = "Linguagem C";
  int tamanho = strlen(palavra);

  printf("Tamanho = %d\n", tamanho);
  system("pause");

  return 0;
}
