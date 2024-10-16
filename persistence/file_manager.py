from domain.process import Process

class FileManager:
    @staticmethod
    def read_input(file_name):
        processes = []
        with open(file_name, 'r') as file:
            for line in file:
                if not line.startswith("#"):
                    label, burst_time, arrival_time, queue, priority = line.strip().split(';')
                    processes.append(Process(label, int(burst_time), int(arrival_time), int(queue), int(priority)))
        return processes

    @staticmethod
    def write_output(result, file_name):
        with open(file_name, 'w') as file:
            file.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n")
            for process in result["processes"]:
                file.write(f"{process.label}; {process.burst_time}; {process.arrival_time}; "
                        f"{process.queue}; {process.priority}; {process.waiting_time}; "
                        f"{process.completion_time}; {process.response_time}; {process.turnaround_time}\n")
            
            # Escribir los promedios
            averages = result["averages"]
            file.write(f"WT={averages['WT']}; CT={averages['CT']}; RT={averages['RT']}; TAT={averages['TAT']};\n")
