# The Inspector and Debugging

Sooner or later a server will not do
what its author swears it does. This
chapter is about looking: with the
protocol's own magnifying glass, and
then with no glass at all.

## The Inspector

The **MCP Inspector** is the official
debugging tool, published alongside
the protocol. Pointed at a server, it
connects as a client and presents
what it finds — tools, resources,
prompts — in a web page, with forms
for calling tools and reading
resources by hand, and a live view of
the messages underneath. It is the
first thing to reach for when a host
says "your server does not work": the
Inspector separates *the server is
broken* from *this host and this
server disagree*, which are different
repairs entirely.

The Inspector runs two ways. As a web
interface, launched with npx:

```bash
npx @modelcontextprotocol/inspector
```

(it opens in a browser; the lab had a
browser-less sandbox, so this mode is
described from the documentation).
And in a scriptable **CLI mode**, which
the lab *did* run against the Plant
Log, asking for the tool list
(transcript `t04-inspector-cli.txt`):

```bash
npx @modelcontextprotocol/inspector --cli \
  python mcp-lab/server/plant_log_server.py \
  --method tools/list
```

The answer is the same dossier chapter
4 took apart — two tools, schemas and
all — returned by an independent
client that shares no code with ours.
That independence is what makes it
evidence.

## Reading the raw wire

Under everything in this guide is
chapter 2's claim: the messages are
JSON text, one per line. The lab
proved it with the least program in
the book, `mcp-lab/client/raw_conversation.py`,
which starts the server and speaks
by hand — no SDK, just `json.dumps`
and a pipe. Transcript `t03` is the
whole exchange. Two lines of it:

```text
>>> {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {...}}
<<< {"jsonrpc":"2.0","id":1,"result":{"capabilities":{...},"serverInfo":{"name":"Plant Log", ...}}}
```

`>>>` is the client writing, `<<<` the
server answering. Request ids match
(1 to 1, 2 to 2, 3 to 3), a
notification goes out with no answer
expected, and a hand-written
`tools/call` for the basil comes back
with its answer in `content`, exactly
where the SDK later looked for it.
When a session misbehaves, this is
the level to debug at: which message,
in which direction, saying what. Most
mysteries do not survive being read.

## A debugging order that works

1. **Will it start at all?** Run the
   server's command yourself, exactly
   as the host's configuration spells
   it (chapter 11). Most "MCP doesn't
   work" is a path, a missing
   interpreter or a working directory.
2. **Does the Inspector see it?** If
   yes, the server is fine and the
   trouble lives in the host's config
   or consent settings. If no, the
   Inspector's error is your error.
3. **Check stderr.** A stdio server's
   stdout is protocol; its complaints
   go to stderr, which hosts collect
   somewhere — find where yours puts
   it before you need it at midnight.
4. **Read one raw exchange.** The
   `raw_conversation.py` script,
   pointed at your server, shows the
   handshake and one call with nothing
   in between you and the truth.

The lab's own failures while building
this guide are kept honestly in
chapter 14 — every one of them was
found by step 1 or step 4, and none of
them was the protocol's fault.
