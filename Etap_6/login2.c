// login - bardzo zle napisany program
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
  int zalogowany;
  char *haslo;
  int dlug = strlen(argv[1]);
  haslo = malloc(sizeof(char) * dlug);
  strcpy( haslo, argv[1] );
  if( strcmp( haslo, "Tajne" ) == 0 ){
    zalogowany = 1;
  }
  if( zalogowany == 1 ){
    printf("Poprawne haslo, witamy :)\n");
  } else {
    printf("Bledne haslo, uciekaj :(\n");
  }
  return 0;
}

