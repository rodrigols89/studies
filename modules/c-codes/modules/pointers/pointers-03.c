/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
  void *pg;
  int value = 10;
  pg = &value;

  printf("\nConteúdo: %d\n", *(int*)pg);

  system("pause");
  return (0);
}
