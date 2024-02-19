#include <stdio.h>
float my_abs(float f) {
	if (f < 0.0) return f*(-1.0);
	return f;
}

int main(void) {
	float fl;
	printf("Podaj liczbę zmiennoprzecinkową: ");
	scanf("%f", &fl);
	printf("Wartość bezwzględna z twojej liczby to: %f\n", my_abs(fl));
	return 0;
}


