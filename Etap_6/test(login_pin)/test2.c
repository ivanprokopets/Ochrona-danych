//program login
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
  char zalogowany;
  char haslo[8];
  zalogowany = 'n';
  strncpy( haslo, argv[1], 8 );
  if( strcmp( haslo, "tajne" ) == 0 ){
    zalogowany = 't';
  }
  printf("Haslo: %s\n", haslo);
  if( zalogowany == 't' ){
    printf("Poprawne haslo, witamy :)\n");
  } else {
    printf("Bledne haslo, uciekaj :(\n");
  }
}
