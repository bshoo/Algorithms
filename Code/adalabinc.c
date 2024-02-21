#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
void fnGenRandInput(int X[], int n)
{
	int i;
	srand(time(NULL));
	for (i = 0; i < n; i++)
	{
	X[i] = rand() % 10000;
	}
}
void bubble_sort(int a[], int n)
{
	int i, j, swap;
	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			if (a[j] > a[j + 1]) {
			swap = a[j];
		a[j] = a[j + 1];
		a[j + 1] = swap;}}}
}
int main(int argc, char **argv)
{
	FILE *fp;
	struct timeval tv;
	double dStart, dEnd;
	int Arr[100000],i;
	fp = fopen("bubbletime.txt", "w");
	for (i = 100; i < 15000; i += 500) {
		fnGenRandInput(Arr, i);
		gettimeofday(&tv, NULL);
		fnGenRandInput(Arr, i);
		dStart = tv.tv_sec + (tv.tv_usec / 1000000.0);
		bubble_sort(Arr, i);
		gettimeofday(&tv, NULL);
		dEnd = tv.tv_sec + (tv.tv_usec / 1000000.0);
		fprintf(fp, "%d\t%lf\t%d\n", i, dEnd - dStart, i * i);
	}
	fclose(fp);
	FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
	if (gnuplotPipe != NULL) {
		fprintf(gnuplotPipe, "set xlabel 'Input Size'\n");
		fprintf(gnuplotPipe, "set ylabel 'Time Taken (seconds)'\n");
		fprintf(gnuplotPipe, "set title 'Time Efficiency of Bubble Sort'\n");
		fprintf(gnuplotPipe, "set style line 1 lc rgb '#FF0000' lt 1 lw 2 pt 9 ps 0.5\n");
		fprintf(gnuplotPipe, "set style line 2 lc rgb '#00ae90' lt 2 lw 2 pt 13 ps 0.5\n");
		fprintf(gnuplotPipe, "plot 'bubbletime.txt' using 1:2 with points ls 1 title 'Actual Time', \%d*x**2 with linespoints ls 2 title 'Estimated Time'\n", i*i);
		fprintf(gnuplotPipe, "set term png\n");
		fprintf(gnuplotPipe, "set output 'bubblesort_efficiency.png'\n");
		fprintf(gnuplotPipe, "replot\n");
		fflush(gnuplotPipe);
		fprintf(gnuplotPipe, "exit\n");
		pclose(gnuplotPipe);
	}
	return 0;
}
