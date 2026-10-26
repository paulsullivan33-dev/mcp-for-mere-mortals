# Hosts, Clients and Servers

Every MCP conversation has exactly
three roles in it. Keeping them
straight is the single most useful
thing in this guide, because nearly
every confusion about MCP — including
most security confusion — is two roles
being mistaken for each other.

## The host

The **host** is the application the
person actually uses: a desktop AI
assistant, a chat program, a coding
editor with an AI pane. The host owns
the conversation and holds (or rents)
the **model**. It decides which
servers exist, starts them or connects
to them, shows the user what they
offer, and — crucially — asks the
user's permission where the protocol
says permission is due. When you read
"MCP support" in an app's release
notes, it is the host that learned to
speak it.

The host is also the only role the
user can see. Everything else in this
chapter happens behind its face.

## The client

Inside the host, for each server it
talks to, there is one **client**. The
client is the protocol speaker: it
opens the connection, performs the
handshake, keeps a list of what the
server offers, sends requests, and
matches each answer to its request by
**id**. One host, five servers: five
clients, five separate conversations.
That separation is deliberate — a
client knows only its own server, and
a server knows only the client in
front of it. If one server misbehaves,
the damage has a wall around it.

In this guide's lab, the client is a
small Python script you can read in
full (`mcp-lab/client/`). In a desktop
host the client is code you will never
see, doing exactly the same job.

## The server

A **server** is any program that
offers things over MCP. It does not
contain a model and does not chat. It
waits for requests, and answers them:
*here are my tools*, *here is that
resource*, *that tool ran, here is
its result*. A server may be twenty
lines wrapping a text file, or the
front door of a company's whole
ticketing system. The protocol does
not care, and from the client's side
the two look alike — which is chapter
12's subject as much as this one's.

A server offers three kinds of thing,
each with its own chapter:

- **Tools** (chapter 4): actions, with
  arguments in and results out.
- **Resources** (chapter 5): text to
  read, addressed by **URI**.
- **Prompts** (chapter 6): message
  templates a user picks.

There are also two features that run
the other way — the server asking the
host for something — collected in
chapter 7.

## The handshake

Every session begins with the same
short ceremony, which the lab captured
raw in
`mcp-lab/transcripts/t03-raw-jsonrpc.txt`:

1. The client sends **initialize**,
   naming the protocol version it
   speaks, what it can do (its
   **capabilities**), and its own name
   and version.
2. The server answers with its own
   version, capabilities and name.
   The Plant Log's answer also carried
   **instructions** — a short paragraph
   telling the host what the server is
   for.
3. The client sends a one-way
   **notification**, `notifications/initialized`,
   which needs no answer. Manners
   complete; real requests may begin.

After that, the conversation is
**discovery** and then use: the client
asks for lists (`tools/list`,
`resources/list`, `prompts/list`), the
host shows them to the user and the
model, and calls follow
(`tools/call`, `resources/read`,
`prompts/get`). Either side may close
the session; a stdio server simply
exits when its pipe closes.

Two details are worth fixing in
memory. First, versions are
**negotiated, not assumed**: if host
and server speak different protocol
revisions, the handshake says so
before anything else happens. Second,
capabilities are **declared, not
discovered by trying**: if a server
does not claim prompts, the client
never asks it for any. Features
neither side claims are simply off the
table — a plain rule that chapter 14
returns to when things go missing.

Check: the lab's SDK client reported
the greeting in one line of transcript
`t01`:

```text
== Server greeting ==
Plant Log (protocol 2025-11-25)
```

The name came from the server; the
version is the one the two sides
settled on in the handshake.
