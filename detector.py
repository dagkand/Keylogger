import psutil

# Suspicious keywords
SUSPICIOUS_KEYWORDS = ["keylogger", "pynput", "keyboard", "hook", "intercept", "capture", "record", "python"]

# Known safe processes
SAFE_PROCESSES = ["opera.exe", "chrome.exe", "firefox.exe", "msedge.exe"]

# Function to scan for keyloggers
def scan_for_keyloggers():
    """Scans for keylogger processes."""
    detected_processes = []

    # Check for suspicious processes
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            process_name = process.info['name'].lower() if process.info['name'] else ""
            cmd_line = " ".join(process.info['cmdline']).lower() if process.info['cmdline'] else ""

            # Skip known safe processes
            if process_name in SAFE_PROCESSES:
                continue

            # Check for Python processes
            if "python" in process_name:
                if any(keyword in cmd_line for keyword in SUSPICIOUS_KEYWORDS):
                    detected_processes.append(f"⚠️ PID: {process.info['pid']} | Name: {process_name} | CMD: {cmd_line}")
            # Check for other suspicious processes
            elif any(keyword in process_name or keyword in cmd_line for keyword in SUSPICIOUS_KEYWORDS):
                detected_processes.append(f"⚠️ PID: {process.info['pid']} | Name: {process_name} | CMD: {cmd_line}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Ignore inaccessible processes

    if detected_processes:
        return "\n".join(detected_processes)
    else:
        return "✅ No keyloggers detected."