import os
import webbrowser
import psutil
import subprocess
import platform
import datetime
import shutil
import random
import math

# ----------------------------------------
# Application Control
# ----------------------------------------

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def open_file_explorer(path="C:\\"):
    os.system(f'explorer {path}')

def open_spotify():
    webbrowser.open("https://open.spotify.com")

def open_github():
    webbrowser.open("https://github.com")

# ----------------------------------------
# System Monitoring
# ----------------------------------------

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_ram_usage():
    return f"RAM Usage: {psutil.virtual_memory().percent}%"

def get_disk_usage():
    disk_usage = shutil.disk_usage("/")
    return f"Total: {disk_usage.total // (2**30)} GB, Used: {disk_usage.used // (2**30)} GB, Free: {disk_usage.free // (2**30)} GB"

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return system_info

def get_uptime():
    uptime_seconds = int(datetime.datetime.now().timestamp() - psutil.boot_time())
    uptime_string = str(datetime.timedelta(seconds=uptime_seconds))
    return f"System Uptime: {uptime_string}"

# ----------------------------------------
# File and Directory Operations
# ----------------------------------------

def list_files_in_directory(path="."):
    return os.listdir(path)

def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)
    return f"Directory '{directory_name}' created successfully!"

def delete_file_or_directory(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            return f"File '{path}' deleted successfully!"
        elif os.path.isdir(path):
            shutil.rmtree(path)
            return f"Directory '{path}' deleted successfully!"
        else:
            return "Path not found!"
    except Exception as e:
        return f"Error: {e}"

# ----------------------------------------
# Command Execution
# ----------------------------------------

def run_shell_command(command):
    result = subprocess.getoutput(command)
    return result

# ----------------------------------------
# Date and Time Utilities
# ----------------------------------------

def get_current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_day_of_week():
    return datetime.datetime.now().strftime("%A")

# ----------------------------------------
# System Control Utilities
# ----------------------------------------

def shutdown_system():
    os.system("shutdown /s /t 1")

def restart_system():
    os.system("shutdown /r /t 1")

def sleep_system():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# ----------------------------------------
# Network Utilities
# ----------------------------------------

def get_ip_address():
    return subprocess.getoutput("ipconfig")

def ping_website(website="google.com"):
    response = os.system(f"ping {website}")
    if response == 0:
        return f"{website} is reachable"
    else:
        return f"{website} is not reachable"


if __name__ == "__main__":
    # Test the functions
    print(get_cpu_usage())
    print(get_ram_usage())
    print(get_disk_usage())
    print(get_system_info())
    print(get_uptime())
    print(create_directory("NewFolder"))
    print(list_files_in_directory())
    print(get_current_date_time())
    print(get_day_of_week())
  