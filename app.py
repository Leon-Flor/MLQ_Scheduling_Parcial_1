from services.scheduler_service import MLQSchedulerService
from persistence.file_manager import FileManager

if __name__ == "__main__":
    # Leer los datos de entrada
    file_name = "mlq001.txt"
    processes = FileManager.read_input(file_name)
    
    # Ejecutar el simulador
    scheduler_service = MLQSchedulerService()
    result = scheduler_service.run(processes)
    
    # Escribir los resultados
    FileManager.write_output(result, "output.txt")
