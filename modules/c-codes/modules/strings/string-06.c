/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
  // Comparing String.
  char palavraOne[20] = "Linguagem C";
  char palavraTwo[20] = "LINGUAGEM C";

  if(strcmp(palavraOne, palavraTwo) == 0)
    printf("\nStrings Iguais!\n");
  else
    printf("\nStrings Diferentes!\n");
	
  system("pause");
  return (0);
}
