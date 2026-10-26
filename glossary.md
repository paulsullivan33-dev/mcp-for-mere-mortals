# Glossary

**Annotation** — a hint attached to a
tool about its character: read-only,
destructive, safe to repeat (chapter 4).

**Capability** — a feature a side
declares in the handshake: tools,
resources, prompts, sampling, and
their kin. Unclaimed features are
never requested (chapter 2).

**Client** — the program inside a
host that speaks MCP to one server:
handshake, discovery, calls (chapter 2).

**Completion** — server-suggested
values for a prompt argument or a
resource template's blank (chapters 5
and 6).

**Consent** — the user's informed
approval, required by the
specification before tool calls run
and sampling is granted (chapters 1,
4 and 12).

**Content** — what a tool result or
resource carries: most often text, but
also images, audio or embedded
resources (chapter 4).

**Discovery** — the list calls
(`tools/list`, `resources/list`,
`prompts/list`) by which a client
learns what a server offers (chapter 2).

**Elicitation** — a server asking the
user a question mid-task, through the
host's own dialog (chapter 7).

**Function calling** — the tool-use
ability built into model APIs
themselves; MCP's nearest neighbour
(chapter 13).

**Host** — the AI application the
person uses. It holds the model, the
conversation, the clients, and the
consent dialogs (chapter 2).

**Initialize** — the first request of
every session, exchanging names,
versions and capabilities (chapter 2).

**Input schema** — the JSON Schema
describing a tool's arguments: names,
types, which are required (chapter 4).

**Inspector** — the official debugging
tool: an independent client with a web
face and a CLI mode, for seeing what a
server actually offers (chapter 10).

**Instructions** — a short paragraph
a server sends in its greeting,
saying what it is for (chapter 2).

**isError** — the flag on a tool
result saying the tool itself reports
failure, as distinct from a protocol
error (chapter 4).

**JSON-RPC 2.0** — the message format
under MCP: requests and answers as
JSON objects, matched by id (chapter 1).

**MCPServer** — the Python SDK 2.x
server class; in SDK 1.x it was called
FastMCP (chapters 8 and 14).

**Notification** — a one-way message
needing no answer, such as
`notifications/initialized` (chapter 2).

**Prompt** — a message template a
server publishes for a user to pick,
with blanks for arguments (chapter 6).

**Resource** — text or data a server
publishes for reading, addressed by
URI (chapter 5).

**Resource template** — a URI pattern
with named blanks, standing for a
family of resources (chapter 5).

**Roots** — locations a host tells a
server it is working about, as context
(chapter 7).

**Sampling** — a server asking the
host to run a message past its model
and return the reply (chapter 7).

**Server** — a program offering tools,
resources and prompts over MCP. It
has no model and does not chat
(chapter 2).

**Session** — one connection's life,
from handshake to close (chapter 2).

**stdio** — the transport where the
host runs the server as a child
process and talks over its standard
input and output (chapter 3).

**Streamable HTTP** — the transport
where the server is a web service at
one endpoint, conventionally `/mcp`
(chapter 3).

**Tool** — an action a server offers:
a name, a description, an argument
schema, and results (chapter 4).

**Tool poisoning** — hostile
instructions smuggled into a tool's
description, aimed at the model that
reads it (chapter 12).

**URI** — the address of a resource,
in a scheme the server chooses, such
as `plants://roster` (chapter 5).
