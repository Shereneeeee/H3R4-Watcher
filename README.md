# H3R4-Watcher
Keyboard imput monitoring system

🕵️ WATCHER: Silent Input Monitoring System
WATCHER is a modern, terminal-based keyboard input monitoring tool built with Python. It features a sleek, high-performance Terminal User Interface (TUI) that captures and displays keystrokes in real-time with precision and style.

✨ Core Features
🔴 Live Monitoring: Real-time keystroke streaming powered by the Rich Live engine.

📊 Dynamic Stream Table: A clean, auto-refreshing table displaying precise timestamps and captured inputs.

💾 Log Exporting: Easily save your captured session data to a local text file (log_dump.txt).

🎮 Interactive Command Center: User-friendly navigation menu built with questionary.

⚡ Async Architecture: Powered by asyncio for high-performance monitoring without system lag.

🧠 Optimized Buffer: Intelligent memory management that keeps the terminal clean by displaying the most recent 15 inputs.

🛠️ System Requirements
Before launching the system, ensure you have the required libraries installed:

Bash

pip install pynput rich questionary
🚀 Installation & Usage
Clone the Repository:

Bash

git clone https://github.com/yourusername/watcher.git
cd watcher
Launch the Engine:

Bash

python watcher.py
Operation Guide:

Select "Start Live Monitoring" to begin the capture stream.

Press Ctrl + C in the terminal to stop the watcher and return to the main menu.

Use "Export Logs to File" to save your captured buffer to disk.

📸 Interface Design
WATCHER utilizes a high-contrast Red and White theme for a professional security-ops aesthetic:

Header: Bold ASCII branding with a "Silent Monitoring" status indicator.

Visualizer: A 4Hz refresh-rate table showing the sequence of inputs.

Key Formatting: Clear distinction between alphanumeric characters and special system keys (e.g., [Key.shift], [Key.enter]).

📂 Data Export Format
Exported logs in log_dump.txt follow a standardized timestamp format:

Plaintext

14:20:05 - w
14:20:06 - a
14:20:06 - t
14:20:07 - c
14:20:07 - h
14:20:08 - [Key.space]
14:20:09 - e
14:20:09 - r
⚠️ Ethical Disclaimer
IMPORTANT: This tool is developed strictly for educational purposes, authorized security auditing, or application debugging. Monitoring someone's input without their explicit consent is illegal and unethical. The developer assumes no liability for any misuse of this software.

Developed by: ren.k_k

Status: ACTIVE / STABLE
