#include <stdio.h>

int main(void) {
	float usd;
	printf("Podaj ile dolarów chesz zamienić na euro: ");
	scanf("%f", &usd);
	printf("Twoje dolary zamieniły się na %f euro\n", (float)usd*(0.85));
	return 0;
}


