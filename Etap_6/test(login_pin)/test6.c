#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAJNY_PIN 1234
int main(int ac, char **av)
{
          int pin;
          if (av[1][0] == '-') {
                  printf("Atak zablokowany\n");
                  exit(1);
          }
          if (strlen(av[1]) == 4)
		sscanf(av[1], "%u", &pin);
	  printf ("PIN: %d\n", pin);
          if (pin == TAJNY_PIN) {
                  pin = -1;
          }
	  if (pin == -1) {
                  printf("PIN poprawny\n");
          } else {
                  printf("PIN bledny\n");
          }
 }
