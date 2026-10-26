# Building a Small Server

This chapter builds the guide's
server, the Plant Log, in full. By the
end you will have a running server
with two tools, two resources and a
prompt — and, more important, you will
have seen that there is no more to a
server than that. The code is
`mcp-lab/server/plant_log_server.py`;
the lab ran it exactly as written.

Outcome: a server any MCP client can
start, list and call. Check: the
client in chapter 9 reads its
offerings back to you, and the
Inspector in chapter 10 agrees.

## Installing the SDK

The official SDK for Python is the
package named **mcp**, installed with
pip into a **virtual environment** —
a private folder of Python packages,
so the experiment touches nothing
else on the machine:

```bash
python3 -m venv ~/mcp-venv
~/mcp-venv/bin/pip install mcp
```

The lab's versions are in transcript
`t00`: Python 3.12.3, SDK **2.3.0**. A
warning from the lab's own notebook
(transcript `t05` exists partly because
of it): SDK 2.x renamed things. Older
tutorials — and SDK 1.x — build servers
on a class called **FastMCP**; in 2.x
it is **MCPServer**, imported from
`mcp.server.mcpserver`, and result
objects use snake_case fields
(`is_error`, not `isError`). If an
example fails with a missing import,
check its vintage before doubting
yourself. Chapter 14 names this trap
again, because everyone meets it once.

## The whole server, in pieces

**The seed data.** Three invented
plants, in a plain dictionary. Dates
are computed from "today" when the
server starts, so the log always reads
sensibly. There is no database and no
file: the state lives in memory and a
restart reseeds it. Real servers put
something real behind the same shape;
the shape is the lesson.

**The server object.**

```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer(
    "Plant Log",
    instructions="A watering log for houseplants. ...",
)
```

The **name** is what clients report;
the **instructions** are the short
paragraph a host may show its model:
what this server is for. Write them as
you would want a stranger's server to
introduce itself to you.

**A tool** is a function with a
decorator:

```python
@mcp.tool()
def log_watering(plant: str, millilitres: int) -> str:
    """Record that a plant was watered today."""
```

Three things to see. The **type
hints** (`str`, `int`) become the
input schema of chapter 4 — the SDK
builds the JSON Schema from them, and
validates incoming arguments against
it (a string where an integer belongs
is refused before the function runs;
transcript `t05`, specimen 1). The
**docstring** becomes the description
the model reads; its `Args:` lines
describe each argument. And the return
value — a plain string — becomes the
result's text content. The second
tool, `days_since_watering`, is the
same shape doing arithmetic instead of
bookkeeping.

**A resource** is a function with an
address:

```python
@mcp.resource("plants://roster")
def roster() -> str:
    """The list of plants in the log."""
```

and **a templated resource** is the
same idea with a blank in the address:

```python
@mcp.resource("plants://{plant}/card")
def plant_card(plant: str) -> str:
    """One plant's record card."""
```

The blank becomes the function's
argument. Chapter 5 explained what
clients do with these; here just note
how little code the advertisement
costs.

**A prompt** is a function that
returns the message text:

```python
@mcp.prompt()
def watering_reminder(plant: str) -> str:
    """A ready-made request: check one plant."""
```

**Running it** is one line, and the
transport is the argument:

```python
if __name__ == "__main__":
    if "--http" in sys.argv:
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")
```

## Starting it by hand

A stdio server, started alone in a
terminal, appears to do nothing — it
is waiting for JSON on its stdin, and
typing prose at it is a category error
the troubleshooting chapter enjoys.
Started with `--http`, it announces
itself like any web service
(transcript `t02-http-server.txt`):

```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Either way, the proof that it works is
a client. That is the next chapter.
