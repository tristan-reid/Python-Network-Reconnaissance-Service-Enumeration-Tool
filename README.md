# Python-Network-Reconnaissance-Service-Enumeration-Tool
A Python TCP port scanner with configurable port ranges, basic service identification, and banner grabbing for authorized security testing.

## Features

- Scans configurable TCP port ranges
- Identifies open TCP ports
- Distinguishes refused connections and timeouts
- Identifies common services based on port numbers
- Performs basic banner grabbing
- Sends a basic HTTP request to identify HTTP services
- Accepts targets and port ranges through command-line arguments

## Example

```bash
python3 recon.py 127.0.0.1 --ports 20-100
```
