#include <stdio.h>

int abs(int c) {
	if (c < 0) c = -c;
	return c;
}

int main(void) {
	int c;
	printf("Podaj liczbę całkowitą: ");
	scanf("%d", &c);
	c = abs(c);
	printf("Wartość bezwzględna z twojej liczby to: %d\n", c);
	return 0;
}


