from domain.queue import Queue
from domain.process import Process

class MLQSchedulerService:
    def __init__(self):
        self.queues = {
            1: Queue(1, 'Round Robin (RR) con quantum 1'),
            2: Queue(2, 'Shortest Job First (SJF)'),
            3: Queue(3, 'First Come First Serve (FCFS)')
        }
    def run(self, processes):
        for process in processes:
            self.queues[process.queue].add_process(process)
        
        for queue in self.queues.values():
            queue.execute()
        
        # Calcular promedios
        total_wt = total_ct = total_rt = total_tat = 0
        num_processes = len(processes)
        
        for process in processes:
            total_wt += process.waiting_time
            total_ct += process.completion_time
            total_rt += process.response_time
            total_tat += process.turnaround_time
        
        avg_wt = total_wt / num_processes
        avg_ct = total_ct / num_processes
        avg_rt = total_rt / num_processes
        avg_tat = total_tat / num_processes

        return {
            "processes": processes,
            "averages": {
                "WT": avg_wt,
                "CT": avg_ct,
                "RT": avg_rt,
                "TAT": avg_tat
            }
        }
