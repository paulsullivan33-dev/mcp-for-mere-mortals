"""A scripted MCP client for the Plant Log.

Connects to the Plant Log server (a
separate program, started by this script
over stdio), then walks through one full
session in order:

  1. list the tools, resources, resource
     templates and prompts on offer
  2. call a tool (twice)
  3. read a resource, then a templated one
  4. fetch a prompt and show its text

Everything the server answers is printed,
so the run can be kept as a transcript.

Run it with the lab's virtual environment:

    python plant_log_client.py
"""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).resolve().parent
SERVER = HERE.parent / "server" / "plant_log_server.py"


def show(label, value):
    print(f"\n== {label} ==")
    print(value)


async def main() -> None:
    params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER)],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            greeting = await session.initialize()
            show(
                "Server greeting",
                f"{greeting.server_info.name} "
                f"(protocol {greeting.protocol_version})",
            )

            tools = await session.list_tools()
            show(
                "Tools on offer",
                "\n".join(
                    f"- {t.name}: "
                    f"{(t.description or '').splitlines()[0]}"
                    for t in tools.tools
                ),
            )

            resources = await session.list_resources()
            show(
                "Resources on offer",
                "\n".join(
                    f"- {r.uri}" for r in resources.resources
                ),
            )

            templates = await session.list_resource_templates()
            show(
                "Resource templates on offer",
                "\n".join(
                    f"- {t.uri_template}"
                    for t in templates.resource_templates
                ),
            )

            prompts = await session.list_prompts()
            show(
                "Prompts on offer",
                "\n".join(
                    f"- {p.name}" for p in prompts.prompts
                ),
            )

            before = await session.call_tool(
                "days_since_watering", {"plant": "fern"}
            )
            show("Tool: days_since_watering(fern)", before.content[0].text)

            logged = await session.call_tool(
                "log_watering",
                {"plant": "fern", "millilitres": 300},
            )
            show("Tool: log_watering(fern, 300)", logged.content[0].text)

            after = await session.call_tool(
                "days_since_watering", {"plant": "fern"}
            )
            show(
                "Tool: days_since_watering(fern), again",
                after.content[0].text,
            )

            roster = await session.read_resource("plants://roster")
            show("Resource: plants://roster", roster.contents[0].text)

            card = await session.read_resource("plants://cactus/card")
            show("Resource: plants://cactus/card", card.contents[0].text)

            prompt = await session.get_prompt(
                "watering_reminder", {"plant": "basil"}
            )
            show(
                "Prompt: watering_reminder(basil)",
                prompt.messages[0].content.text,
            )


if __name__ == "__main__":
    asyncio.run(main())
