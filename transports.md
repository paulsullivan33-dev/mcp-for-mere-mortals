# Transports

The protocol is the messages. A
**transport** is how the messages
travel — the road under the
conversation. MCP defines two standard
transports today, and the choice
between them is mostly a question of
where the server lives: on the same
machine as the host, or somewhere else
entirely.

## stdio: the server as a subprocess

With **stdio**, the host starts the
server as a child process and talks to
it over the child's standard input and
output — the oldest plumbing in
computing. The client writes one JSON
message per line to the server's
stdin; the server writes answers to
its stdout. When the host is done, it
closes the pipe and the server exits.

Consequences worth knowing:

- **No ports, no network.** Nothing
  listens anywhere. Nothing outside
  the machine can reach the server,
  because there is nothing to reach.
- **The host owns the lifetime.** The
  server exists exactly as long as
  the session, started fresh each
  time, with the host's environment
  and the host's permissions.
- **Stdout is sacred.** Anything the
  server prints that is not a protocol
  message corrupts the stream. Logs go
  to **stderr** — every MCP programmer
  learns this from one baffling
  failure, and chapter 14 keeps the
  lab's version of that lesson.
- **One client.** A stdio server talks
  to the process that started it. It
  is a private conversation by
  construction.

Nearly every local MCP server you will
meet — file tools, note takers, garden
logs — runs this way, including the
Plant Log for most of this guide. The
server is given to the host as a
*command to run* (chapter 11), and
that fact is security-relevant: a
stdio server runs with **your**
permissions, as you. Choose them as
carefully as you would any program.

## Streamable HTTP: the server as a service

With **streamable HTTP**, the server
is a web service, running on its own,
at a URL. The client sends requests as
HTTP **POST**s to a single endpoint
(conventionally `/mcp`); answers come
back either as plain JSON or as a
**Server-Sent Events** stream when the
server has things to say over time.
The server may keep a **session** per
client, identified by a header, or run
**stateless**, answering each request
from what it carries.

The lab ran this too: the same Plant
Log file, started with `--http`,
listening on loopback port 8000, and a
second client speaking to it. The
server's own log (`t02-http-server.txt`)
shows the shape — POSTs arriving at
`/mcp`, answered 200:

```text
INFO:     127.0.0.1:60238 - "POST /mcp HTTP/1.1" 200 OK
```

Consequences, mirrored against stdio:

- **Reach is a choice — and a risk.**
  A server on a network can serve many
  hosts and many users. It can also be
  reached by people it was not meant
  for, so hosted servers need real
  authentication; the specification
  builds on **OAuth 2.1** for exactly
  this. The lab's HTTP server listened
  on loopback only and needed none —
  and the guide does not pretend that
  proves anything about the open
  internet (chapter 12).
- **Lifetime is the operator's.** The
  server runs whether or not any host
  is connected, keeps its state
  between sessions, and is upgraded
  when its operator says so.
- **It scales, and it costs.** A
  service can be shared by a team; it
  must also be hosted, patched and
  paid for.

## The older transport, and other roads

Early MCP used a transport called
**HTTP+SSE**, with two endpoints — one
for sending, one for the event stream.
Streamable HTTP replaced it (the two
folded into one endpoint) and new
servers should use the replacement;
you may still meet the old one's name
in server documentation, and some
hosts accept either. Transports
beyond the standard two are permitted
in principle — the messages are just
JSON-RPC — but a non-standard road
means only hosts that know it can
travel, which defeats most of the
point.

## Which one, when

If the server serves one person on one
machine, stdio: nothing to deploy,
nothing exposed, lifetime handled for
you. If the server must be shared, or
run on a different machine from the
host, or outlive the conversation,
streamable HTTP — with authentication
treated as part of the job, not a
later chapter of it. The Plant Log is
the same code under both, which is the
protocol working as designed: the
offerings do not change when the road
does.
