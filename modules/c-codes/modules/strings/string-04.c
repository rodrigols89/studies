/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
  // Copying a String.
  char palavra[20] = "Linguagem C";
  char novaPalavra[30];

  strcpy(novaPalavra, palavra);

  printf("Copia = %s\n", novaPalavra);
  system("pause");
  return (0);
}
