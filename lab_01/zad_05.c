#include <stdio.h>

int main(void) {
	char ch1, ch2;
	printf("Podaj dwie litery(znaki): ");
	scanf("%c%c", &ch1, &ch2);
	printf("Twoje litery(znaki) w odwrotnej kolejności to %c%c\n", ch2, ch1);
	return 0;
}


