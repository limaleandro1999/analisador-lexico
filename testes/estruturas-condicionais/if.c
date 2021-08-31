#include <stdio.h>
int main() {
  int number = 1;

  if (number > 0) {
    printf("You entered %d.\n", number);
  }

  if (number >= 0 && number != 2) {
    printf("You entered %d.\n", number);
  }

  if (number <= 0 || number != 2) {
    printf("You entered %d.\n", number);
  }

  if (number < 0) {
    printf("You entered %d.\n", number);
  }

  return 0;
}
