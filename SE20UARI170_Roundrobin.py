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


def compare1(p1, p2):
    return p1.arrival_time < p2.arrival_time


def compare2(p1, p2):
    return p1.pid < p2.pid


def main():
    arrival_times = [0, 4, 5, 6]
    burst_times = [24, 3, 3, 12]

    n = len(arrival_times)
    tq = 4

    processes = []
    burst_remaining = []

    for i in range(n):
        processes.append(Process(i + 1, arrival_times[i], burst_times[i]))
        burst_remaining.append(burst_times[i])

    total_turnaround_time = 0
    total_waiting_time = 0
    total_response_time = 0
    total_idle_time = 0

    q = []
    current_time = 0
    q.append(0)
    completed = 0
    mark = [0] * n
    mark[0] = 1

    while completed != n:
        idx = q.pop(0)

        if burst_remaining[idx] == processes[idx].burst_time:
            processes[idx].start_time = max(current_time, processes[idx].arrival_time)
            total_idle_time += processes[idx].start_time - current_time
            current_time = processes[idx].start_time

        if burst_remaining[idx] - tq > 0:
            burst_remaining[idx] -= tq
            current_time += tq
        else:
            current_time += burst_remaining[idx]
            burst_remaining[idx] = 0
            completed += 1

            processes[idx].completion_time = current_time
            processes[idx].turnaround_time = processes[idx].completion_time - processes[idx].arrival_time
            processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
            processes[idx].response_time = processes[idx].start_time - processes[idx].arrival_time

            total_turnaround_time += processes[idx].turnaround_time
            total_waiting_time += processes[idx].waiting_time
            total_response_time += processes[idx].response_time

        for i in range(1, n):
            if burst_remaining[i] > 0 and processes[i].arrival_time <= current_time and mark[i] == 0:
                q.append(i)
                mark[i] = 1

        if burst_remaining[idx] > 0:
            q.append(idx)

        if not q:
            for i in range(1, n):
                if burst_remaining[i] > 0:
                    q.append(i)
                    mark[i] = 1
                    break

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    

    print(f"Average Turnaround Time = {avg_turnaround_time}")
    print(f"Average Waiting Time = {avg_waiting_time}")
    

if __name__ == "__main__":
    main()
