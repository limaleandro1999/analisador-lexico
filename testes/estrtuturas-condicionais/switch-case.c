#include <stdio.h>
int main ()
{
	int num;
	printf ("Digite um numero: ");
	scanf ("%d",&num);
	switch (num)
  {
    case 9:
      printf ("O numero e igual a 9.");
      break;

    case 10:
      printf ("O numero e igual a 10.");
      break;

    case 11:
      printf ("O numero e igual a 11.");
      break;

    default:
      printf ("O numero nao e nem 9 nem 10 nem 11.");
  }
	return(0);
}