#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
  char haslo[8];
  strcpy( haslo, argv[1] );
  if( strcmp( haslo, "tajne" ) == 0 ){
    printf("Poprawne haslo, witamy :)\n");
  } else {
    printf("Bledne haslo, uciekaj :(\n");
  }
}

