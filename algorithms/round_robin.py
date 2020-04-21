def round_robin(process, quantum): 
	n = len(process)
	wt = [0] * n 
	tat = [0] * n 
	rt = [0] * n
	rem_bt = [0] * n 
	count = [0] * n
	complete = 0
	
	for i in range(n): 
		rem_bt[i] = process[i][1] 
	time = 0 
	while(1): 
		done = True
		for i in range(n): 
			if ((rem_bt[i] > 0) and (process[i][2]<=time)): 
				count[i] += 1
				if(count[i] == 1):
					rt[i] = time - process[i][2]
				done = False
				if (rem_bt[i] > quantum): 				
					time += quantum 
					rem_bt[i] -= quantum 
				else: 
					time += rem_bt[i] 
					wt[i] = time - process[i][1] - process[i][2]
					rem_bt[i] = 0
					complete += 1
		if ((done == True) and (complete != n)):
			time += 1
		elif (done == True): 
			break 

	for i in range(n): 
		tat[i] = process[i][1] + wt[i] 

	total_wt = 0
	total_tat = 0
	total_rt = 0
	for i in range(n):
		total_wt += wt[i]
		total_rt += rt[i]
		total_tat += tat[i]
	avg_wt = total_wt/n
	avg_rt = total_rt/n
	avg_tat = total_tat/n
	throughput = n/time
	result = [avg_wt,avg_rt,avg_tat,throughput]
	return result