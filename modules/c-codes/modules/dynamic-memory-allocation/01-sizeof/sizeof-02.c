/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

struct ponto
{
  int x,y;
};

int main()
{
  printf("char: %d\n", sizeof(char));
  printf("int: %d\n", sizeof(int));
  printf("float: %d\n", sizeof(float));
  printf("double: %d\n", sizeof(double));
  printf("struct ponto: %d\n", sizeof(struct ponto));

  system("pause");
  return (0);
}
