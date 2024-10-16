class Process:
    def __init__(self, label, burst_time, arrival_time, queue, priority):
        self.label = label
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.queue = queue
        self.priority = priority
        self.waiting_time = 0
        self.completion_time = 0
        self.response_time = 0
        self.turnaround_time = 0
