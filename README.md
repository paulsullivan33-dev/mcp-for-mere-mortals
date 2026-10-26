# MCP for Mere Mortals

An AI assistant is good at talking and
not, by itself, good at *doing*: it
cannot read your files, check your
database or run your programs unless
something hands it those abilities, one
tool at a time. The **Model Context
Protocol** — **MCP** for short — is an
open standard that describes how that
handing-over works. It says how a
program offers abilities to an AI host,
how the host discovers them, and how
the two sides ask, answer and keep each
other honest, in plain **JSON** messages
any language can speak.

This guide explains the protocol the
way the lab learned it: by building a
tiny server and talking to it. You will
meet the three roles — **host**,
**client** and **server** — the two
transports that carry the messages, and
the three things a server can offer:
**tools** the model may call,
**resources** it may read, and
**prompts** a user may pick. You will
build a small server in Python, connect
a client to it, call a tool end to end,
inspect the whole conversation, and
read the raw messages underneath —
because MCP is not magic, it is text on
a wire, and this guide shows the wire.

One rule runs through the guide, stated
in chapter 1 and again in chapter 12:
**a server should be given no more
access than the job in front of it
needs, and a tool should never run
without the user's consent.** MCP's
design builds that rule in — the host
asks, the user approves — and the
chapters treat it as part of the
protocol, not an afterthought. A server
you connect is a program someone wrote,
running with real permissions; the
guide teaches you to read one before
you trust one.

The lab behind this guide ran the real
thing: the official **Python SDK**
(**mcp 2.3.0**) on Python 3.12,
installed with pip into a fresh virtual
environment on a small Linux machine.
Against it the lab built the **Plant
Log**, an invented watering log for
three fictional houseplants, offering
two tools, two resources and a prompt.
A scripted client listed everything on
offer, called both tools (and watched
the log change), read both resources
and fetched the prompt. The same server
was then run over **streamable HTTP**
and driven by a second client, the
whole opening exchange was repeated by
hand in raw JSON-RPC with no SDK at
all, and the official **Inspector** was
pointed at the server and answered.
Three deliberately broken tool calls
were made and kept, because how a thing
fails is part of how it works.

What the lab could not do, it did not
fake. It had no desktop AI app to
configure, so real hosts are taught
through their documented configuration
files, with the lab's own checked
config standing in as the worked
example. **Sampling** and
**elicitation** — the two features
where a server asks things of the host
rather than answering — are explained
from the specification and labelled as
such wherever they appear.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What MCP is**](what-mcp-is.md) —
  the problem it solves, the shape of
  the answer, and the consent rule that
  is part of the design
- [**Hosts, clients and servers**](the-three-roles.md) —
  the three roles, who holds what, and
  the opening handshake that starts
  every session
- [**Transports**](transports.md) —
  stdio for programs on your own
  machine, streamable HTTP for servers
  across a network, and what travels
  on each
- [**Tools**](tools.md) — actions a
  server offers: names, descriptions,
  argument schemas, results and errors
- [**Resources**](resources.md) — text
  a server publishes for reading:
  fixed resources and templates with
  names filled in
- [**Prompts**](prompts.md) — ready-made
  message templates a user picks from
  a list, and why they belong to the
  user, not the model
- [**Sampling and elicitation**](sampling-and-elicitation.md) —
  when the server asks back: borrowing
  the host's model, and asking the user
  a question mid-task
- [**Building a small server**](building-a-server.md) —
  the Plant Log server, line by line:
  two tools, two resources, one prompt
- [**Connecting a client**](connecting-a-client.md) —
  a scripted client over stdio, one
  full session, and the same server
  over HTTP
- [**The Inspector and debugging**](the-inspector.md) —
  the official Inspector, what the raw
  messages look like, and reading a
  session like a transcript
- [**Configuration files**](configuration-files.md) —
  how real hosts are told about
  servers: the JSON block, commands,
  arguments and environment
- [**Security and consent**](security-and-consent.md) —
  what a connected server can do, tool
  poisoning and prompt injection, and
  the habit of least access
- [**The neighbours**](the-neighbours.md) —
  function calling, plain APIs and
  plugins: what each is, and where MCP
  differs
- [**Limits**](limits.md) — what the
  protocol does not do, what it cannot
  promise, and where its edges are
- [**Troubleshooting**](troubleshooting.md) —
  the silent server, the wrong type,
  the tool that is not there, and the
  traps this guide's lab fell into so
  you don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Writing a host — embedding MCP into
your own AI application is a book of
its own, and this guide stays on the
server and client side a reader can
run in an afternoon. Remote servers at
organisation scale — accounts, billing,
audit trails — are pointed at, not
taught. The protocol's OAuth machinery
for hosted servers is described in
chapter 3 and chapter 12, not built:
the lab's servers ran on one machine
and needed no one's permission but
their owner's. Other languages' SDKs
are named in chapter 8; the worked
code is Python, because one language
done properly beats five done thinly.

## How to use this guide

Read chapter 1 for the problem and the
rule, and chapter 2 before installing
anything — knowing which role holds
what turns later confusion into a named
problem. Chapters 4 to 6 take the three
offerings in turn; read them with the
Plant Log's listings beside you.
Chapter 8 builds the server and
chapter 9 talks to it, in the same
sitting if you can: the protocol makes
sense the moment you have watched your
own tool call come back. Chapter 12 is
not the optional chapter — read it
before you connect any server you did
not write. The lab's code lives in
`mcp-lab/` (server in
`mcp-lab/server/`, clients in
`mcp-lab/client/`), its transcripts in
`mcp-lab/transcripts/`, and its notes
in `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [APIs for Mere Mortals](https://paulsullivan33-dev.github.io/api-for-mere-mortals/)
- [Local AI for Mere Mortals](https://paulsullivan33-dev.github.io/local-ai-for-mere-mortals/)
- [Open WebUI for Mere Mortals](https://paulsullivan33-dev.github.io/open-webui-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/mcp-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/mcp-for-mere-mortals/blob/main/LICENSE-CODE).
