/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
  int x = 10;
  int *p;

  p = &x;

  // Displays the value of the variable "x".
  printf("\nO valor de x: %d\n", x);

  // Displays the memory address saved in the "p".
  printf("Endereço de memória salvo em p: %d\n", p);

  // Displays the value of "x" from the "p" pointe.
  printf("O valor da variável x: %d\n", *p);

  system("pause");
  return (0);
}
