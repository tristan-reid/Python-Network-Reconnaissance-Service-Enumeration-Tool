import socket
import argparse
import errno

def grab_banner(sock, target, port):
    try:
        sock.settimeout(1)

        if port in [80, 8000, 8080]:
            request = f"HEAD / HTTP/1.0\r\nHost: {target}\r\n\r\n"
            sock.sendall(request.encode())

        banner = sock.recv(1024)

        return banner.decode(errors="replace").strip()

    except (socket.timeout, OSError):
        return None

parser = argparse.ArgumentParser(
    description="Simple TCP network reconnaissance tool"
)

parser.add_argument(
    "target",
    help="IP address or hostname to scan"
)

parser.add_argument(
    "--ports",
    default="1-1024",
    help="Port range to scan, for example 20-100"
)

args = parser.parse_args()

target = args.target

port_range = args.ports.split("-")

start_port = int(port_range[0])
end_port = int(port_range[1])

ports = range(start_port, end_port + 1)

print(f"Scanning {target} from port {start_port} to {end_port}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
      try:
          service = socket.getservbyport(port, "tcp")
      except OSError:
          service = "unknown"

      print(f"Port {port} is OPEN ({service})")

      banner = grab_banner(sock, target, port)

      if banner:
          print(f"  Banner: {banner}")

    sock.close()
