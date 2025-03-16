import tkinter as tk
from tkinter import ttk, messagebox
import threading
from portscan import scan_ports

def start_scan():
    """Inicia a varredura de portas quando o botão é pressionado."""
    ip = ip_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port > end_port:
            messagebox.showerror("Erro", "A porta inicial deve ser menor que a final.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para as portas.")
        return
    
    result_text.set("Escaneando...")
    scan_thread = threading.Thread(target=run_scan, args=(ip, start_port, end_port))
    scan_thread.start()

def run_scan(ip, start_port, end_port):
    """Executa a varredura em uma thread separada e exibe os resultados."""
    open_ports = scan_ports(ip, start_port, end_port)
    if open_ports:
        result_text.set(f"Portas abertas: {', '.join(map(str, open_ports))}")
    else:
        result_text.set("Nenhuma porta aberta encontrada.")

# Criando a interface
top = tk.Tk()
top.title("PortScan GUI")
top.geometry("400x300")

tk.Label(top, text="IP ou Domínio:").pack()
ip_entry = tk.Entry(top)
ip_entry.pack()

tk.Label(top, text="Porta Inicial:").pack()
start_port_entry = tk.Entry(top)
start_port_entry.pack()

tk.Label(top, text="Porta Final:").pack()
end_port_entry = tk.Entry(top)
end_port_entry.pack()

tk.Button(top, text="Iniciar Escaneamento", command=start_scan).pack()

result_text = tk.StringVar()
result_label = tk.Label(top, textvariable=result_text)
result_label.pack()

top.mainloop()
