# ⚡ Python Real-Time System Monitor (`sysmonitor`)

A dead-simple, colorful, and real-time command-line system monitor written in Python. It provides an immediate, visual overview of core system resources.

## ✨ Features

* **Real-Time Data:** Updates CPU, RAM, and Disk usage every few seconds.
* **Visual Feedback:** Uses **ANSI color codes** (Green, Yellow, Red) and **Unicode block characters** to show resource stress immediately.
* **Minimal Dependencies:** Only requires the widely used `psutil` library.
* **Clean Interface:** Clears the terminal on each refresh for a dedicated monitoring experience.

## 📋 Requirements

* Python 3.x
* The `psutil` library.

## 📦 Installation

To make the script executable and install it system-wide (so you can run it from any terminal window):

### 1. Install Dependency
```bash
pip install psutil
```
### 2. Clone the repository
```bash
git clone https://github.com/qzak112/sysmonitor.git
cd sysmonitor
```
### 3. Install executable
```bash
mv sysmonitor.py sysmonitor
chmod +x sysmonitor
sudo cp sysmon /usr/local/bin/
```
## Usage
```bash
sysmonitor
```
## License
MIT

## Screenshots
! [sysmonitor] (screenshot/region_2025-11-09_12-38-50.png)

