import socket

def scan_port(host, port):
    """Проверяет, открыт ли порт на хосте"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Основная часть
target = input("Введите IP или домен (например, 127.0.0.1): ")
start_port = int(input("Начальный порт (например, 20): "))
end_port = int(input("Конечный порт (например, 100): "))

print(f"\nСканирую {target} с порта {start_port} по {end_port}...\n")

# Очистим файл перед новым сканированием (опционально)
open("scan_result.txt", "w").close()

for port in range(start_port, end_port + 1):
    is_open = scan_port(target, port)
    
    if is_open:
        print(f"✅ Port {port} — OPEN")
    else:
        print(f"❌ Port {port} — closed")
    
    # Сохраняем результат в файл
    with open("scan_result.txt", "a") as f:
        status = "Открыт" if is_open else "закрыт"
        f.write(f"Порт {port}: {status}\n")
