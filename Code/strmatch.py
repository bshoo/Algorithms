import time
from os import system


def brute_str(m,n):
	for i in range(n-m):
		j=0
		while j<m:
			j+=1

def analyze(func):
    with open("plot_data.doc","w") as pf:
        m = [i for i in range(10,1000,50)]
        n = [i for i in range(100,10000,500)]
        for i in range(20):
            start = time.time()
            func(m[i],n[i])
            end = time.time()
    
            pf.write(str(n[i])+" "+str(end-start)+" "+str(m[i])+"\n")

gnuplot_script = '''
set xlabel "Input Size"
set ylabel "Time Tken (seconds)"
set title "Time efficiency of Brute Force String Matching"
set style line 1 lc rgb '#000000' lt 2 lw 2 pt 11 ps 0.5
set style line 2 lc rgb '#ff0000' lt 2 lw 2 pt 13 ps 0.5
plot "plot_data.txt" u 1:2 w lp pt 1 title 'Actual Time', '' u 1:3 w lp pt 1 title 'Estimated Time'
set term png
set output sort_efficiency.png
replot
'''

if __name__=='__main__':
    analyze(brute_str);
    with open('plot.gnu','w') as p: p.write(gnuplot_script);
    system("gnuplot -persist plot.gnu")
