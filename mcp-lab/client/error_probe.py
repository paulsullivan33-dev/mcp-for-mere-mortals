"""Three ways a tool call can go wrong.

Runs the Plant Log server over stdio and
makes three flawed calls on purpose:

  1. an argument of the wrong type
  2. a tool that does not exist
  3. a well-formed call the tool itself
     answers with a polite refusal

Kept as the evidence for the guide's
troubleshooting chapter: each failure
arrives in a different shape.

    python error_probe.py
"""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).resolve().parent
SERVER = HERE.parent / "server" / "plant_log_server.py"


async def main() -> None:
    params = StdioServerParameters(
        command=sys.executable, args=[str(SERVER)]
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            wrong_type = await session.call_tool(
                "log_watering",
                {"plant": "fern", "millilitres": "a splash"},
            )
            print("1. Wrong type for millilitres ->")
            print(f"   is_error: {wrong_type.is_error}")
            print(f"   text: {wrong_type.content[0].text}")

            unknown = await session.call_tool(
                "sing_to_plant", {"plant": "fern"}
            )
            print("2. Unknown tool 'sing_to_plant' ->")
            print(f"   is_error: {unknown.is_error}")
            print(f"   text: {unknown.content[0].text}")

            orchid = await session.call_tool(
                "days_since_watering", {"plant": "orchid"}
            )
            print("3. Unknown plant 'orchid' ->")
            print(f"   is_error: {orchid.is_error}")
            print(f"   text: {orchid.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
