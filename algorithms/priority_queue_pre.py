def priority_queue_pre(processes, priorities):
	queue = []
	for pid,burst,arrival in processes:
		queue.append([pid,burst,arrival])
	for i in range(len(priorities)):
		queue[i].append(int(priorities[i]))
	process = sorted(queue, key=lambda x: (x[2], x[3]))
	n = len(process)
	wt = [0] * n
	rt = [0] * n
	tat = [0] * n 
	total_wt = 0
	total_tat = 0
	total_rt = 0
	count = [0] * n
	burst = [0] * n
	order = []
	for i in range(n): 
		burst[i] = process[i][1] 
	complete = 0
	time = 0
	minm = 10000
	short = -1
	check = False

	while (complete != n): 
		for j in range(n): 
			if ((process[j][2] <= time) and (burst[j] < minm) and burst[j] > 0): 
				minm = burst[j] 
				short = j 
				check = True
		if (check == False): 
			time += 1
			continue
		count[short] += 1
		burst[short] -= 1
		order.append(short)
		if(count[short] == 1):
			rt[short] = time - process[short][2]

		minm = burst[short] 
		if (minm == 0): 
			minm = 10000

		if (burst[short] == 0): 
			complete += 1
			check = False
			wt[short] = (time + 1 - process[short][1] - process[short][2]) 
			if (wt[short] < 0): 
				wt[short] = 0
		time += 1 

	for i in range(n): 
		tat[i] = process[i][1] + wt[i] 

	for i in range(n):
		total_wt += wt[i] 
		total_tat += tat[i]
		total_rt += rt[i] 
	avgwt = total_wt/n
	avgrt = total_rt/n
	avgtat = total_tat/n
	throughput = n/(time - process[order[0]][2])
	result = [avgwt, avgrt, avgtat, throughput]
	return result