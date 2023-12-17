class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.Wait_time = None
        self.finish_time = None
        self.Turnaround_time = 0
        self.response_time = 0



def calculate_waiting_time(processes):
    waiting_time = [0] * len(processes)
    for i in range(1, len(processes)):
        waiting_time[i] = processes[i - 1].burst_time + waiting_time[i - 1] - processes[i].arrival_time
    return waiting_time


def calculate_turnaround_time(processes):
    turnaround_time = [0] * len(processes)
    for i in range(len(processes)):
        turnaround_time[i] = processes[i].burst_time + calculate_waiting_time(processes)[i]
    return turnaround_time


def calculate_average_waiting_time(processes):
    waiting_time = calculate_waiting_time(processes)
    return sum(waiting_time) / len(processes)


def calculate_average_turnaround_time(processes):
    turnaround_time = calculate_turnaround_time(processes)
    return sum(turnaround_time) / len(processes)


def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort the processes based on arrival time

    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.Wait_time = current_time - process.arrival_time
        process.response_time = current_time - process.arrival_time
        process.finish_time = current_time + process.burst_time
        current_time = process.finish_time
        process.Turnaround_time = process.finish_time - process.arrival_time



def result():  # Print the Gantt Chart
    print("Gantt Chart:")
    print("-----------")
    for process in processes:
        print(f"| {process.name} ", end="")
    print("|")
    print("-----------")

    # Print the process details
    print("\nProcess Details:")
    print("----------------")
    print("Process\tWait Time\tTurnaround Time\tResponse Time")
    for process in processes:
        print(f"{process.name}\t\t\t{process.Wait_time}\t\t\t{process.Turnaround_time}\t\t\t{process.response_time}")
    print("----------------")

    # Calculate average turnaround time and average waiting time
    total_turnaround_time = sum(process.finish_time - process.arrival_time for process in processes)
    total_waiting_time = sum(process.finish_time - process.arrival_time - process.burst_time
                             for process in processes)

    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    # Print the average waiting time and average turnaround time
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


# Read processes from input file
processes = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        name, burst_time, arrival_time = line.split()
        process = Process(name, int(arrival_time), int(burst_time))
        processes.append(process)

# Perform FCFS scheduling
fcfs_scheduling(processes)

# Save the output to a file
with open('output.txt', 'w') as f:
    # Redirect standard output to the file
    import sys
    original_stdout = sys.stdout
    sys.stdout = f

    # Perform FCFS scheduling
    fcfs_scheduling(processes)
    # the output file
    result()
    # Restore standard output
    sys.stdout = original_stdout


