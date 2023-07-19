# Dummy Port Scanner
The Port Scanner is a Python3 script that allows you to scan for open ports on a target host. It provides a simple and convenient way to gather information about a remote system's network services.

### Installation
Clone the repository to your local machine:

```
git clone https://github.com/0xAjayMandal/Dummpy-Port-Scanner.git
```

Navigate to the project directory:

```
cd Dummpy-Port-Scanner
```

### Usage
The Port Scanner script is a simple TCP connection port scanner. Here are the available command-line arguments:

```
python3 port-scanner.py <ip>
```

**Example:**

```
python3 port_scanner.py 192.168.1.1
```

**Output**

```
python3 port-scanner.py 192.168.1.1
--------------------------------------------------
Scanning target: 192.168.1.1
Time started: 2023-01-01 01:01:01.010101
--------------------------------------------------
Port 53 is open
```
The Port Scanner provides port number information about the open ports on the target host. For each open port, it displays the port number. This script will only work with TCP connection.
