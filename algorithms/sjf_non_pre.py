def sjf_non_pre(process): 
	n = len(process)
	wt = [0] * n
	tat = [0] * n 
	total_wt = 0
	total_tat = 0
	burst = [0] * n
	order = []
	for i in range(n): 
		burst[i] = process[i][1]
	time = 0
	short = -1
	check = False
	count = 0

	while count!= n: 
		minm = 10000
		for j in range(n): 
			if ((process[j][2] <= time) and (burst[j] < minm) and (burst[j] > 0)): 
				minm = burst[j] 
				short = j 
				check = True
		if (check == False): 
			time += 1
			continue
		order.append(short)
		count += 1
		check = False
		wt[short] = (time - process[short][2]) 
		if (wt[short] < 0): 
			wt[short] = 0
		time += burst[short]
		burst[short] = 0
	# print(order)
	# print(wt)
	for i in range(n): 
		tat[i] = process[i][1] + wt[i]
	# print(tat)

	for i in range(n):
		total_wt += wt[i] 
		total_tat += tat[i]
	avgwt = total_wt/n
	avgrt = avgwt
	avgtat = total_tat/n
	throughput = n/(time - process[order[0]][2])
	result = [avgwt, avgrt, avgtat, throughput]
	return result