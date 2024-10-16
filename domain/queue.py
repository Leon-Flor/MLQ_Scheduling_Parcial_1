class Queue:
    def __init__(self, id, scheduling_policy):
        self.id = id
        self.scheduling_policy = scheduling_policy
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def execute(self):
        # Implementar la lógica de planificación aquí, por ejemplo RR, SJF, FCFS
        if self.scheduling_policy == 'Round Robin (RR) con quantum 1':
            self.round_robin( 1 )
        elif self.scheduling_policy == 'Shortest Job First (SJF)':
            self.sjf()
        elif self.scheduling_policy == 'First Come First Serve (FCFS)':
            self.fcfs()

    def round_robin(self, quantum= 1):
        time = 0
        while self.processes:
            for process in self.processes[:]:
                if process.burst_time > quantum:
                    process.burst_time -= quantum
                    time += quantum
                else:
                    time += process.burst_time
                    process.completion_time = time
                    process.turnaround_time = process.completion_time - process.arrival_time
                    process.waiting_time = process.turnaround_time - process.burst_time
                    self.processes.remove(process)

    def sjf(self):
        self.processes.sort(key=lambda x: x.burst_time)
        time = 0
        for process in self.processes:
            if time < process.arrival_time:
                time = process.arrival_time
            process.completion_time = time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            time += process.burst_time


    def fcfs(self):
        self.processes.sort(key=lambda x: x.arrival_time)
        time = 0
        for process in self.processes:
            if time < process.arrival_time:
                time = process.arrival_time
            process.completion_time = time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            time += process.burst_time
