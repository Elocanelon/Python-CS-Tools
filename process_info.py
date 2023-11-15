#Script para obtener los PID del sistema y obtener informacion mas detallada de algun proceso
import psutil

for proc in psutil.process_iter(["pid", "name", "username"]):
    print(proc.info)


process_unknow = int(input("Ingrese el PID del cual quiera informacion: "))

p = psutil.Process(process_unknow)
with p.oneshot():
    print("\nNmae: " + str(p.name()))
    print("CPU Time: " + str(p.cpu_times()))
    print("CPU %: " + str(p.cpu_percent))    
    print("Create time: " + str(p.create_time()))
    print("PPID: " + str(p.ppid()))
    print("Status: " + str(p.status()))    
