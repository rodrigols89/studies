/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a, b, *p, *q;
  a = 10;
  b = 10;
  p = &a;
  q = &b;

  if (p == q)
    printf("\nValores são iguais.\n");
  else
    printf("\nValores diferentes.\n");

  system("pause");
  return (0);
}
