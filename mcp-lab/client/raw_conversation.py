"""The conversation with no SDK at all.

Starts the Plant Log server over stdio
and talks to it by hand, writing JSON-RPC
messages as text and printing both sides.
This is all MCP ever is on the wire: one
JSON object per line.

    python raw_conversation.py

Only the opening exchange is shown:
initialise, the "initialised" notice, and
one tools/call. The SDK client in
plant_log_client.py says the same things
with nicer manners.
"""

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SERVER = HERE.parent / "server" / "plant_log_server.py"

proc = subprocess.Popen(
    [sys.executable, str(SERVER)],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
)


def send(message):
    line = json.dumps(message)
    print(f">>> {line}")
    proc.stdin.write(line + "\n")
    proc.stdin.flush()


def receive():
    line = proc.stdout.readline()
    print(f"<<< {line.strip()}")
    return json.loads(line)


send(
    {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "raw-conversation", "version": "0.1"},
        },
    }
)
receive()

send({"jsonrpc": "2.0", "method": "notifications/initialized"})

send({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
receive()

send(
    {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "days_since_watering",
            "arguments": {"plant": "basil"},
        },
    }
)
receive()

proc.stdin.close()
proc.wait(timeout=10)
print(f"(server exited with code {proc.returncode})")
