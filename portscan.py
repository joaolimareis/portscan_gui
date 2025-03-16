import socket
import threading

def scan_port(ip, port, results):
    """Tenta conectar a uma porta específica e verifica se está aberta."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Tempo limite para resposta
            if s.connect_ex((ip, port)) == 0:
                results.append(port)  # Adiciona à lista de portas abertas
    except Exception as e:
        pass  # Ignora erros

def scan_ports(ip, start_port, end_port):
    """Executa a varredura de portas em múltiplas threads."""
    threads = []
    results = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results  # Retorna lista de portas abertas

if __name__ == "__main__":
    target_ip = input("Digite o IP ou domínio: ")
    start_port = int(input("Porta inicial: "))
    end_port = int(input("Porta final: "))
    
    open_ports = scan_ports(target_ip, start_port, end_port)
    if open_ports:
        print(f"Portas abertas: {open_ports}")
    else:
        print("Nenhuma porta aberta encontrada.")
