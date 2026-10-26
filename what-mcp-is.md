# What MCP Is

An AI **model** — the program that
reads a conversation and writes the
next message — is, on its own, sealed
in a box. It can reason about your
plants, but it cannot look at your
watering log. It can draft a query,
but it cannot run one. Every useful
thing it might do in the world has to
be handed to it by some other program,
as a **tool**: *here is a thing you
may ask for, here is what to send,
here is what comes back.*

Before MCP, every pairing of an AI
application with an outside tool was
a private arrangement. Each app
invented its own way to describe a
tool, its own way to call one, its own
way to hand back results. A tool built
for one app worked in that app alone.
Integrations multiplied: ten apps and
ten tools meant up to a hundred
hand-built connections, each with its
own habits and its own bugs.

**The Model Context Protocol (MCP) is
the standard socket in the wall.** It
defines one way for a program to offer
tools and data, and one way for an AI
application to find and use them. A
server written once, to the standard,
works with any host that speaks it —
the way a web page works in any
browser, or a USB device in any port.
The protocol is open: published by
Anthropic in 2024, maintained in the
open since, and defined in a written
**specification** that anyone may
implement in any language.

## The shape of the answer

Three kinds of program take part
(chapter 2 gives each its own
chapter-length treatment):

- A **host** is the AI application
  the person uses — a desktop
  assistant, a chat window, a coding
  editor. It holds the model and the
  conversation.
- A **client** lives inside the host,
  one per connection, and speaks the
  protocol on the host's behalf.
- A **server** is a program that
  offers things: **tools** to call,
  **resources** to read, **prompts**
  to pick. It might wrap a database, a
  file store, a garden log, a ticket
  desk — anything with an interface.

The conversation itself is **JSON-RPC
2.0**: requests and answers as JSON
text, one object per message, each
request carrying an **id** so its
answer can be matched to it. Chapter
10 shows a whole opening exchange as
raw text — it is shorter than you
expect, and reading it once removes
most of the mystery.

## Why a standard, and not a library

Tools are where an AI stops talking
and starts *doing*, and doing has
consequences. A shared protocol is
worth having for the same reason
shared electrical standards are:
safety rules can be written down once,
in one place, and every participant
can be held to them. MCP's
specification spends real pages on
**consent**: the host must show the
user what a server offers, tool calls
that change things should be approved
by a person, and a server must never
be silently given powers nobody agreed
to. When every integration was
private, those norms were private too.

## The rule, stated before everything else

A connected server is a program
someone wrote, running with real
permissions — yours, in the case of a
server on your own machine. So this
guide has one rule, and it is not fine
print:

> **Give a server no more access than
> the job in front of it needs, and
> let no tool run without the user's
> consent.**

A read-only server for a log book does
not need your whole home folder. A
tool that *sends* something deserves
more scrutiny than a tool that
*reports* something. Chapter 12 works
through the hazards in detail —
including the uncomfortable ones,
where a server's own text tries to
talk the model into misusing it — but
the rule above is the whole of it, and
everything in the lab obeyed it: the
Plant Log server can see exactly one
invented log, held in its own memory,
and nothing else on the machine.

## A first taste

After installing the SDK (chapter 8),
a server is a short file. The heart of
the guide's Plant Log:

```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Plant Log")

@mcp.tool()
def days_since_watering(plant: str) -> str:
    """Say how many days since a plant was watered."""
    ...
```

and a client somewhere else asks the
server what it offers, then calls the
tool by name. The answer that came
back in the lab (`mcp-lab/transcripts/t01-stdio-session.txt`):

```text
== Tool: days_since_watering(fern) ==
fern was last watered 3 day(s) ago.
```

Everything between those two snippets
— discovery, schemas, transports,
errors — is the rest of this guide.

## Who it is for

The maker who wants their own program
to be usable by an AI assistant
without building a bespoke plugin for
each one. The user who has been told
to "just add this MCP server" and
would like to know what they are
actually agreeing to. The curious
reader who learns a protocol best by
watching it work. The common thread is
one person, their own machine, and a
small server they can read end to end.

## What it is not

MCP is not a model, and it does not
make one smarter; it is plumbing, and
plumbing matters precisely because of
what flows through it. It is not an
agent framework: it does not decide
what the model does, plan tasks or
remember anything between sessions
unless a server does. It is not a
security guarantee: the specification
asks hosts for consent and servers for
honesty, but a standard cannot make a
dishonest server honest — chapter 12
is blunt about this. And it is not the
only way to give a model tools:
chapter 13 compares it with the
function calling built into model
APIs, with plain HTTP APIs, and with
the plugin systems it grew up
alongside.
