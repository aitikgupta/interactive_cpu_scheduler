def sample_function(process):
	#algorithm here
	result = []
	response_time = 0
	burst_time = 0
	turnaround_time = 0
	throughput = 0
	cpu_utilisation = 0
	result.append(response_time,burst_time,turnaround_time,throughput,cpu_utilisation)
	return result

process = []
process.append([1,5,0])
process.append([2,4,0])
sample_function(process)
