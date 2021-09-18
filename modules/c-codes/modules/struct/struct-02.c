/*
* by Rodrigo Leite
* 10/12/2016
*/

#include <stdio.h>
#include <stdlib.h>

struct pessoa
{
  char nome[50], rua[50];
  int idade, numero;
};

int main()
{
  // Initialization of a struct.
  struct pessoa p  = {"Rodrigo", "Rua 1", 27, 101};

  // The "numero" field receives an empty String.
  struct pessoa p2 = {"Gloria", "Rua 2", 50};
}
