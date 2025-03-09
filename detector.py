import psutil
import os

SUSPICIOUS_KEYWORDS = ["keylogger", "pynput", "keyboard", "hook", "intercept"]

def check_suspicious_processes():
    suspicious_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            process_name = proc.info['name'] or ""
            process_cmd = " ".join(proc.info['cmdline']) if proc.info['cmdline'] else ""

            if any(keyword in process_name.lower() or keyword in process_cmd.lower() for keyword in SUSPICIOUS_KEYWORDS):
                suspicious_processes.append((proc.info['pid'], process_name, process_cmd))
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    return suspicious_processes

if __name__ == "__main__":
    print("Scanning for keyloggers..")
    found = check_suspicious_processes()

    if found:
        print("WARNING: Potential keyloggers detected!")
        for pid, name, cmd in found:
            print(f"PID: {pid} | Process: {name} | Command: {cmd}")
        print("Consider terminating these processes if they are unknown.")
    else:
        print("No keyloggers found!")
