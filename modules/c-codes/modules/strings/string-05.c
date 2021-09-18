/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
  // Concatenating Strings.
  char palavraOne[20] = "Bom ";
  char palavraTwo[30] = "dia!";

  strcat(palavraOne, palavraTwo);

  printf("\nPalavra = %s\n", palavraOne);
  system("pause");
  return (0);

  return 0;
}
