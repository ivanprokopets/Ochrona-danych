// vuln, czyli cel ataku
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
        char buffer[500];
        int i;
        strncpy(buffer, argv[1]);
        printf("BUFOR:\n");
        for (i = 0; i < (sizeof(buffer) / sizeof(char)); i++) {
                printf("\t%d) Adres: %x, Zawartosc: %x\n", i, &(buffer[i]), buffer[i]);
        }
}
