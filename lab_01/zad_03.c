#include <stdio.h>

int main(void) {
	int rok_ur;
	printf("Podaj rok w którym się urodziłeś/aś: ");
	scanf("%d", &rok_ur);
	printf("Rok przed twoim urodzeniem to: %d\n", rok_ur - 1);
	return 0;
}


