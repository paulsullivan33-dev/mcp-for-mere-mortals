"""The Plant Log server.

A tiny MCP server built for the MCP for
Mere Mortals guide. It keeps a watering
log for a few invented houseplants and
offers it to any MCP client three ways:

  * tools    -- actions a client may ask
                the server to perform
  * resources-- text a client may read
  * prompts  -- message templates a user
                may pick from a list

Run it over stdio (the default) with:

    python plant_log_server.py

or over streamable HTTP with:

    python plant_log_server.py --http

Everything is fictional and lives in
memory: restart the server and the log
starts over from the same seed entries.
"""

import sys
from datetime import date, timedelta

from mcp.server.mcpserver import MCPServer

mcp = MCPServer(
    "Plant Log",
    instructions=(
        "A watering log for houseplants. "
        "Use the tools to record watering, "
        "and the resources to read the log."
    ),
)

# The seed log. Dates are worked out from
# "today" when the server starts, so the
# guide's transcripts always read sensibly.
_today = date.today()
PLANTS = {
    "fern": {
        "kind": "Boston fern",
        "last_watered": _today - timedelta(days=3),
        "millilitres": 250,
        "note": "Likes its soil damp, not wet.",
    },
    "basil": {
        "kind": "Sweet basil",
        "last_watered": _today - timedelta(days=1),
        "millilitres": 120,
        "note": "Wilts loudly when thirsty.",
    },
    "cactus": {
        "kind": "Prickly pear cactus",
        "last_watered": _today - timedelta(days=19),
        "millilitres": 60,
        "note": "Thrives on neglect.",
    },
}


@mcp.tool()
def log_watering(plant: str, millilitres: int) -> str:
    """Record that a plant was watered today.

    Args:
        plant: the plant's name, lower case
        millilitres: how much water it got
    """
    entry = PLANTS.get(plant)
    if entry is None:
        return f"No plant called '{plant}' in the log."
    entry["last_watered"] = _today
    entry["millilitres"] = millilitres
    return (
        f"Logged: {plant} watered with "
        f"{millilitres} ml on {_today.isoformat()}."
    )


@mcp.tool()
def days_since_watering(plant: str) -> str:
    """Say how many days since a plant was watered.

    Args:
        plant: the plant's name, lower case
    """
    entry = PLANTS.get(plant)
    if entry is None:
        return f"No plant called '{plant}' in the log."
    days = (_today - entry["last_watered"]).days
    return f"{plant} was last watered {days} day(s) ago."


@mcp.resource("plants://roster")
def roster() -> str:
    """The list of plants in the log."""
    lines = ["Plants in the log:"]
    for name, entry in sorted(PLANTS.items()):
        lines.append(f"- {name} ({entry['kind']})")
    return "\n".join(lines)


@mcp.resource("plants://{plant}/card")
def plant_card(plant: str) -> str:
    """One plant's record card."""
    entry = PLANTS.get(plant)
    if entry is None:
        return f"No plant called '{plant}' in the log."
    days = (_today - entry["last_watered"]).days
    return (
        f"{plant} - {entry['kind']}\n"
        f"Last watered: {entry['last_watered'].isoformat()} "
        f"({days} day(s) ago, {entry['millilitres']} ml)\n"
        f"Note: {entry['note']}"
    )


@mcp.prompt()
def watering_reminder(plant: str) -> str:
    """A ready-made request: check one plant.

    Args:
        plant: the plant's name, lower case
    """
    return (
        f"Please check the plant log for {plant}: "
        f"read its card, say how long since it was "
        f"watered, and tell me plainly whether it "
        f"needs water today."
    )


if __name__ == "__main__":
    if "--http" in sys.argv:
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")
