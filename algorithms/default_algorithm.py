def default_algorithm(processes):
	n = len(processes)
	tq1 = 2
	tq2 = 4
	threshold = 2
	wt = [0] * n
	rt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_rt = 0
	total_tat = 0
	count = [0] * n
	complete = 0
	time = 0
	check = False
	pid = 9999
	order = []

	burst = [0] * n
	for i in range(n): 
		burst[i] = processes[i][1]

	while complete != n:
		check = False
		minm = 9999
		for i in range(n):
			if (processes[i][2] <= time) and (burst[i] > 0) and (count[i] < minm):
				check = True
				pid = i
				minm = count[i]
		if(check == False):
			time += 1
			continue
		count[pid] += 1
		if(count[pid] <= threshold):
			if(count[pid] == 1):
				rt[pid] = time - processes[pid][2]
			if (burst[pid] > tq1):
				burst[pid] -= tq1
				time += tq1
			elif burst[pid] <= tq1:
				time += burst[pid]
				wt[pid] = time - processes[pid][2] - processes[pid][1]
				complete += 1
				burst[pid] = 0
		elif(count[pid] > threshold) and (count[pid] <= 2*threshold):
			if burst[pid] > tq2:
				burst[pid] -= tq2
				time += tq2
			elif burst[pid] <= tq2:
				time += burst[pid]
				wt[pid] = time - processes[pid][2] - processes[pid][1]
				complete += 1
				burst[pid] = 0
		else:
			time += burst[pid]
			wt[pid] = time - processes[pid][2] - processes[pid][1]
			burst[pid] = 0
			complete += 1
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]
		total_wt += wt[i]
		total_rt += rt[i]
		total_tat += tat[i]
	avg_wt = total_wt/n
	avg_rt = total_rt/n
	avg_tat = total_tat/n
	throuhput = n/time
	result = [avg_wt,avg_rt,avg_tat,throuhput]
	return result