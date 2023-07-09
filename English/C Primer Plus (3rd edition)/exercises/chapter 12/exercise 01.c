#include <stdio.h>
#include <stdlib.h>
#define MAX_FILE_NAME 256


void ch12_ex01(void) {
    char file_name[MAX_FILE_NAME];
    char file_destination[MAX_FILE_NAME];
    FILE *file_src;
    FILE *file_dst;
    int i;
    size_t bytes_read;

    printf("Enter the name of the file to be copied: ");
    fflush(stdout);
    fgets(file_name, MAX_FILE_NAME, stdin);
    printf("Enter the name of the destination file: ");
    fflush(stdout);
    fgets(file_destination, MAX_FILE_NAME, stdin);
    for (i = 0; i < MAX_FILE_NAME; i++) {
        if (file_name[i] == '\n') {
            file_name[i] = '\0';
            break;
        }
    }
    for (i = 0; i < MAX_FILE_NAME; i++) {
        if (file_destination[i] == '\n') {
            file_destination[i] = '\0';
            break;
        }
    }

    if ((file_src = fopen(file_name, "rb")) == NULL) {
        printf("Can't open %s\n", file_name);
        exit(EXIT_FAILURE);
    }
    if ((file_dst = fopen(file_destination, "wb")) == NULL) {
        printf("Can't open %s\n", file_destination);
        exit(EXIT_FAILURE);
    }

    while ((bytes_read = fread(file_name, 1, 1024, file_src)) > 0) {
        fwrite(file_name, 1, bytes_read, file_dst);
    }

    puts("Done copying file.");
}