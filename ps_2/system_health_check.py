import psutil
import logging
from datetime import datetime
import time
from dataclasses import dataclass

@dataclass
class Thresholds():
    CPU_THRESHOLD:float = 80.0  # in percentage
    MEMORY_THRESHOLD:float = 80.0  # in percentage
    DISK_THRESHOLD:float = 80.0  # in percentage
    PROCESS_THRESHOLD:float = 300  # number of processes
    

class SystemHealthCheck:
    def __init__(self,thresholds:Thresholds):
        self.thresholds= thresholds
        logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    def check_cpu_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > thresholds.CPU_THRESHOLD:
            logging.warning(f'High CPU usage detected: {cpu_usage}%')
        return cpu_usage

    def check_memory_usage(self):
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        if memory_usage > thresholds.MEMORY_THRESHOLD:
            logging.warning(f'High Memory usage detected: {memory_usage}%')
        return memory_usage

    def check_disk_usage(self):
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        if disk_usage > thresholds.DISK_THRESHOLD:
            logging.warning(f'High Disk usage detected: {disk_usage}%')
        return disk_usage

    def check_running_processes(self):
        processes = len(psutil.pids())
        if processes > thresholds.PROCESS_THRESHOLD:
            logging.warning(f'High number of running processes detected: {processes}')
        return processes
    
    def run(self):
        while True:
            cpu_usage = self.check_cpu_usage()
            memory_usage = self.check_memory_usage()
            disk_usage = self.check_disk_usage()
            running_processes = self.check_running_processes()

            # Log the current status
            logging.info(f'CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%, Running Processes: {running_processes}')

            # Wait for a minute before next check
            time.sleep(60)


    
    
if __name__ == "__main__":
    thresholds=  Thresholds(PROCESS_THRESHOLD=300,
                            DISK_THRESHOLD=80.0,
                            MEMORY_THRESHOLD=80.0,
                            CPU_THRESHOLD=80.0)
    health_check_instance = SystemHealthCheck(thresholds)
    health_check_instance.run()