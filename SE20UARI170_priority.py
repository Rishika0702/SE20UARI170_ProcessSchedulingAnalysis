class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = 0


def main():
    arrival_times = [0, 4, 5, 6]
    burst_times = [24, 3, 3, 12]
    priorities = [3, 1, 4, 2]
    n = len(arrival_times)

    processes = []
    burst_remaining = burst_times.copy()
    is_completed = [0] * n

    for i in range(n):
        process = Process(i + 1, arrival_times[i], burst_times[i], priorities[i])
        processes.append(process)

    total_turnaround_time = 0
    total_waiting_time = 0
    total_response_time = 0
    total_idle_time = 0
    throughput = 0

    current_time = 0
    completed = 0
    prev = 0

    while completed != n:
        idx = -1
        mx = -1
        for i in range(n):
            if processes[i].arrival_time <= current_time and is_completed[i] == 0:
                if processes[i].priority > mx:
                    mx = processes[i].priority
                    idx = i
                if processes[i].priority == mx:
                    if processes[i].arrival_time < processes[idx].arrival_time:
                        mx = processes[i].priority
                        idx = i

        if idx != -1:
            if burst_remaining[idx] == processes[idx].burst_time:
                processes[idx].start_time = max(current_time, processes[idx].arrival_time)
                total_idle_time += processes[idx].start_time - prev

            burst_remaining[idx] -= 1
            current_time += 1
            prev = current_time

            if burst_remaining[idx] == 0:
                processes[idx].completion_time = current_time
                processes[idx].turnaround_time = processes[idx].completion_time - processes[idx].arrival_time
                processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
                processes[idx].response_time = processes[idx].start_time - processes[idx].arrival_time

                total_turnaround_time += processes[idx].turnaround_time
                total_waiting_time += processes[idx].waiting_time
                total_response_time += processes[idx].response_time

                is_completed[idx] = 1
                completed += 1
        else:
            current_time += 1

    min_arrival_time = min(process.arrival_time for process in processes)
    max_completion_time = max(process.completion_time for process in processes)

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n

    print(f"\nAverage Turnaround Time = {avg_turnaround_time}")
    print(f"Average Waiting Time = {avg_waiting_time}")
  


if __name__ == "__main__":
    main()
