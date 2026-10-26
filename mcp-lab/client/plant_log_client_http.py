"""The Plant Log over streamable HTTP.

Same server as the stdio lab, reached the
other way: the server is started first,
on its own, listening on loopback port
8000, and this client connects to it over
HTTP. Start the server in one terminal:

    python plant_log_server.py --http

then run this client in another:

    python plant_log_client_http.py

It lists the tools, calls one, and reads
the roster resource -- enough to prove
the second transport end to end.
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

URL = "http://127.0.0.1:8000/mcp"


async def main() -> None:
    async with streamable_http_client(URL) as (read, write):
        async with ClientSession(read, write) as session:
            greeting = await session.initialize()
            print(
                f"Server greeting: {greeting.server_info.name} "
                f"(protocol {greeting.protocol_version})"
            )

            tools = await session.list_tools()
            print(
                "Tools on offer: "
                + ", ".join(t.name for t in tools.tools)
            )

            answer = await session.call_tool(
                "days_since_watering", {"plant": "cactus"}
            )
            print(f"days_since_watering(cactus): {answer.content[0].text}")

            roster = await session.read_resource("plants://roster")
            print("plants://roster:")
            print(roster.contents[0].text)


if __name__ == "__main__":
    asyncio.run(main())
