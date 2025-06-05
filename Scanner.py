import socket
from concurrent.futures import ThreadPoolExecutor

# Function to scan a single port on a target IP
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout for the connection attempt
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except Exception:
        pass
    return None

# Function to scan ports on a single IP
def scan_ip(ip, ports):
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
    if open_ports:
        print(f"Host {ip} has open ports: {open_ports}")

# Function to scan a range of IPs
def scan_network(start_ip, end_ip, ports):
    # Convert IPs to integers for iteration
    def ip_to_int(ip):
        parts = list(map(int, ip.split('.')))
        return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

    def int_to_ip(i):
        return f"{(i >> 24) & 0xFF}.{(i >> 16) & 0xFF}.{(i >> 8) & 0xFF}.{i & 0xFF}"

    start = ip_to_int(start_ip)
    end = ip_to_int(end_ip)

    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip_int in range(start, end + 1):
            ip = int_to_ip(ip_int)
            executor.submit(scan_ip, ip, ports)

if __name__ == "__main__":
    # Define the IP range to scan
    start_ip = "192.168.1.1"
    end_ip = "192.168.1.20"

    # Define ports to scan (common ports)
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    print(f"Scanning IP range {start_ip} to {end_ip} for ports {ports}...")
    scan_network(start_ip, end_ip, ports)
    print("Scan complete.")