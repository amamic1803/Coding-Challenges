#include <stdio.h>
#include <math.h>

double sine(double x, unsigned int precision);
double cosine(double x, unsigned int precision);

int main() {
    unsigned int precision;
    unsigned int choice;
    double input;

    printf("Enter the input:\n");
    scanf("%lf", &input);
    input = fmod(input, 2 * M_PI);

    printf("Enter the precision:\n");
    scanf("%u", &precision);

    printf("Select which function to use:\n");
    printf("1. Sine\n");
    printf("2. Cosine\n");
    printf("Enter your choice:\n");
    scanf("%u", &choice);

    switch (choice) {
        case 1: {
            printf("%.*lf\n", precision, sine(input, precision));
            break;
        }
        case 2: {
            printf("%.*lf\n", precision, cosine(input, precision));
            break;
        }
        default: {
            printf("Invalid choice.\n");
            return 1;
        }
    }

    return 0;
}

double sine(double x, unsigned int precision) {
    double prev_fact = 1.0, prev_term = x, result = x, old_result = INFINITY, new_term;
    int counter = 1;

    for ( ; fabs(old_result - result) >= pow(10, -1.0 * precision); counter++) {
        if (counter % 2 == 0) {
            new_term = 1.0;
        } else {
            new_term = -1.0;
        }

        prev_fact *= (counter * 2) * (counter * 2 + 1);
        prev_term *= x * x;
        new_term *= prev_term / prev_fact;

        old_result = result;
        result += new_term;
    }

    return result;
}

double cosine(double x, unsigned int precision) {
    double prev_fact = 1.0, prev_term = 1.0, result = 1.0, old_result = INFINITY, new_term;
    int counter = 1;

    printf("%lf\n", x);
    printf("%u\n", precision);

    for ( ; fabs(old_result - result) >= pow(10, -1.0 * precision); counter++) {
        if (counter % 2 == 0) {
            new_term = 1.0;
        } else {
            new_term = -1.0;
        }

        prev_fact *= (counter * 2) * (counter * 2 - 1);
        prev_term *= x * x;
        new_term *= prev_term / prev_fact;

        old_result = result;
        result += new_term;
    }

    return result;
}