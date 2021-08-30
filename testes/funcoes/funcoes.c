#include <stdio.h>

float soma(float a, int b)  
{
  float result;     
  result = a + b;
  return result;
}

int main()
{
  float a;
  int b;
  float s;
  a = 10.3;
  b = 12;
  s = soma(a, b);
  printf("A soma de %f com %d é %f\n", a,b,s); 
  return 0;
}
