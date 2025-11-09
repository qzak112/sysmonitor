#!/usr/bin/env python3
import psutil
import time
import os

# Color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear')

def get_color(percent):
    if percent < 50: 
        return GREEN
    elif percent < 80: 
        return YELLOW
    else: 
        return RED

def draw_bar(percent, width=20):
    filled = int(percent / 100 * width)
    bar = '█' * filled + '░' * (width - filled)
    return f"[{bar}]"

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_ram():
    ram = psutil.virtual_memory()
    return ram.percent, ram.used, ram.total

def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent, disk.used, disk.total

def get_network():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv

def display():
    while True:
        clear_screen()
        
        # Header
        print("=" * 50)
        print("           SYSTEM MONITOR")
        print("=" * 50)
        
        # CPU
        cpu = get_cpu()
        cpu_color = get_color(cpu)
        cpu_bar = draw_bar(cpu)
        print(f"CPU:  {cpu_color}{cpu_bar} {cpu:5.1f}%{RESET}")
        
        # RAM
        ram_percent, ram_used, ram_total = get_ram()
        ram_color = get_color(ram_percent)
        ram_bar = draw_bar(ram_percent)
        ram_gb_used = ram_used // (1024**3)
        ram_gb_total = ram_total // (1024**3)
        print(f"RAM:  {ram_color}{ram_bar} {ram_percent:5.1f}%{RESET} ({ram_gb_used}GB / {ram_gb_total}GB)")
        
        # Disk
        disk_percent, disk_used, disk_total = get_disk()
        disk_color = get_color(disk_percent)
        disk_bar = draw_bar(disk_percent)
        disk_gb_used = disk_used // (1024**3)
        disk_gb_total = disk_total // (1024**3)
        print(f"Disk: {disk_color}{disk_bar} {disk_percent:5.1f}%{RESET} ({disk_gb_used}GB / {disk_gb_total}GB)")
        
        # Network (optional - shows total sent/received)
        net_sent, net_recv = get_network()
        net_sent_mb = net_sent // (1024**2)
        net_recv_mb = net_recv // (1024**2)
        print(f"\nNetwork: ↑{net_sent_mb}MB  ↓{net_recv_mb}MB")
        
        print("=" * 50)
        print("Press Ctrl+C to exit")
        
        time.sleep(3)

if __name__ == "__main__":
    try:
        display()
    except KeyboardInterrupt:
        print("\n\nExiting... Goodbye!")
