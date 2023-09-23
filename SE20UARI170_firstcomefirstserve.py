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

def calculate_metrics(processes):
    total_turnaround_time = 0
    total_waiting_time = 0

    n = len(processes)

    for i in range(n):
        processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
        total_turnaround_time += processes[i].turnaround_time
        total_waiting_time += processes[i].waiting_time

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n

    return avg_turnaround_time, avg_waiting_time

def main():
    # Define arrival_times and burst_times
    arrival_times = [0, 4, 5, 6]
    burst_times = [24, 3, 3, 12]

    processes = []
    n = len(arrival_times)

    for i in range(n):
        processes.append(Process("P" + str(i + 1), arrival_times[i], burst_times[i]))

    processes.sort(key=lambda x: x.arrival_time)

    for i in range(n):
        processes[i].start_time = max(processes[i - 1].completion_time if i > 0 else 0, processes[i].arrival_time)
        processes[i].completion_time = processes[i].start_time + processes[i].burst_time
        processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time
        processes[i].response_time = processes[i].start_time - processes[i].arrival_time

    # Calculate metrics
    avg_turnaround_time, avg_waiting_time = calculate_metrics(processes)

    # Calculate average response time
    total_response_time = sum(process.response_time for process in processes)
    avg_response_time = total_response_time / n

    # Calculate CPU Utilization
    total_execution_time = processes[-1].completion_time  # Completion time of the last process
    total_idle_time = total_execution_time - sum(process.burst_time for process in processes)
    cpu_utilization = (total_execution_time - total_idle_time) / total_execution_time * 100

    # Calculate Throughput
    throughput = n / total_execution_time

    # Print processes and metrics
    print("#P\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.start_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}\t{process.response_time}")

    print(f"\nAverage Turnaround Time = {avg_turnaround_time}")
    print(f"Average Waiting Time = {avg_waiting_time}")
    print(f"Average Response Time = {avg_response_time}")
    print(f"CPU Utilization = {cpu_utilization:.2f}%")
    print(f"Throughput = {throughput:.2f} process/unit time")

if __name__ == "__main__":
    main()
