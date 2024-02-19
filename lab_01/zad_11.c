#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
	double w1, w2;
	printf("Podaj długość boków przyprostokątnych trójkąta prostokątnego: ");
	scanf("%lf%lf", &w1, &w2);
	printf("Długość przeciwprostokątnej to %f\n", (float)(sqrt(w1*w1 + w2*w2))); 
	return 0;
}


