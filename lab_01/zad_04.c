#include <stdio.h>

int main(void) {
	int c1, c2, c3;
	printf("Podaj trzy liczby całkowite: ");
	scanf("%d %d %d", &c1, &c2, &c3);
	printf("Średnia z twoich liczb to: %f\n", (float)(c1 + c2 + c3)/3);
	return 0;
}


