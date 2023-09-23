class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = 0


def main():
    n = int(input("Enter the number of processes: "))

    processes = []
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time of process {i + 1}: "))
        burst_time = int(input(f"Enter burst time of process {i + 1}: "))
        processes.append(Process(i + 1, arrival_time, burst_time))

    total_turnaround_time = 0
    total_waiting_time = 0
    total_response_time = 0
    total_idle_time = 0
    is_completed = [False] * n

    current_time = 0
    completed = 0
    prev = 0

    while completed != n:
        idx = -1
        mn = float("inf")
        for i in range(n):
            if processes[i].arrival_time <= current_time and not is_completed[i]:
                if processes[i].burst_time < mn:
                    mn = processes[i].burst_time
                    idx = i
                if processes[i].burst_time == mn:
                    if processes[i].arrival_time < processes[idx].arrival_time:
                        mn = processes[i].burst_time
                        idx = i

        if idx != -1:
            processes[idx].start_time = current_time
            processes[idx].completion_time = processes[idx].start_time + processes[idx].burst_time
            processes[idx].turnaround_time = processes[idx].completion_time - processes[idx].arrival_time
            processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
            processes[idx].response_time = processes[idx].start_time - processes[idx].arrival_time

            total_turnaround_time += processes[idx].turnaround_time
            total_waiting_time += processes[idx].waiting_time
            total_response_time += processes[idx].response_time
            total_idle_time += processes[idx].start_time - prev

            is_completed[idx] = True
            completed += 1
            current_time = processes[idx].completion_time
            prev = current_time
        else:
            current_time += 1

    min_arrival_time = float("inf")
    max_completion_time = -1

    for i in range(n):
        min_arrival_time = min(min_arrival_time, processes[i].arrival_time)
        max_completion_time = max(max_completion_time, processes[i].completion_time)

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    avg_response_time = total_response_time / n
    cpu_utilization = ((max_completion_time - total_idle_time) / max_completion_time) * 100
    throughput = n / (max_completion_time - min_arrival_time)

    print("\n#P\tAT\tBT\tST\tCT\tTAT\tWT\tRT\n")
    for i in range(n):
        print(
            f"{processes[i].pid}\t{processes[i].arrival_time}\t{processes[i].burst_time}\t"
            f"{processes[i].start_time}\t{processes[i].completion_time}\t{processes[i].turnaround_time}\t"
            f"{processes[i].waiting_time}\t{processes[i].response_time}\n"
        )

    print(f"Average Turnaround Time = {avg_turnaround_time}")
    print(f"Average Waiting Time = {avg_waiting_time}")
    print(f"Average Response Time = {avg_response_time}")
    print(f"CPU Utilization = {cpu_utilization}%")
    print(f"Throughput = {throughput} process/unit time")


if __name__ == "__main__":
    main()
