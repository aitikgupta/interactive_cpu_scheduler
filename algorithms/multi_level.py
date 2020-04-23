from algorithms.fcfs import fcfs
from algorithms.round_robin import round_robin

def multi_level(algorithms, process):
	f_output=[]
	algo=0
	for level in process:
		if algo == 0 or algo==1:
			f_output.append(round_robin((level), int(algorithms[algo][31:])))
		elif algo==2:
			f_output.append(fcfs(level))
		algo += 1

	f_avg_wt=0
	f_avg_rt=0
	f_avg_tat=0
	f_throughput=0
	result=[]

	for i in range(len(f_output)):
		f_avg_wt += f_output[i][0]
		f_avg_rt += f_output[i][1]
		f_avg_tat += f_output[i][2]
		f_throughput += f_output[i][3] 
	
	result.append(f_avg_wt)
	result.append(f_avg_rt)
	result.append(f_avg_tat)
	result.append(f_throughput)
	
	for i in range(4):
		result[i]=result[i]/3

	return result