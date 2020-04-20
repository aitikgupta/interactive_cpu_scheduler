def fcfs(process): 
	queue = []
	for pid,burst,arrival in process:
		queue.append([arrival,pid,burst])
	process = sorted(queue)
	n = len(process)
	wt = [0] * n 
	tat = [0] * n 
	total_wt = 0
	total_tat = 0
	time = 0
	time += process[0][0]
	wt[0] = 0
	for i in range(1, n):
		time += process[i-1][2]
		wt[i] = time - process[i][0]
	time += process[-1][2]

	for i in range(n): 
		tat[i] = process[i][2] + wt[i]

	for i in range(n): 	
		total_wt += wt[i] 
		total_tat += tat[i]
	
	avg_wt = total_wt/n
	avg_rt = avg_wt
	avg_tat = total_tat/n
	throughput = n/time
	result = [avg_wt,avg_rt,avg_tat,throughput]
	return result