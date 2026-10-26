# Connecting a Client

A server alone is a shop with the
lights off. This chapter switches them
on: a scripted **client** — the same
role a host's inner client plays,
written out where you can read it —
connects to the Plant Log, discovers
everything, and uses all of it. The
code is `mcp-lab/client/plant_log_client.py`;
its full output is transcript `t01`.

Outcome: one complete session,
greeting to prompt, that you can point
at any line of and say what happened.
Check: the transcript in the lab is
the run itself, not a re-enactment.

## The stdio session, step by step

**Starting the server.** The client
does not find the server running; it
*starts* it, the way a host does:

```python
params = StdioServerParameters(
    command=sys.executable,
    args=[str(SERVER)],
)
async with stdio_client(params) as (read, write):
    async with ClientSession(read, write) as session:
        greeting = await session.initialize()
```

`initialize()` performs chapter 2's
handshake. What came back:

```text
== Server greeting ==
Plant Log (protocol 2025-11-25)
```

**Discovery.** Four list calls —
tools, resources, resource templates,
prompts — and the transcript shows the
whole shopfront in a dozen lines:
two tools, one fixed resource, one
template, one prompt. Nothing was
called yet. This pause matters in
real hosts: discovery is when the
*user* should be looking, because
this list is the server's whole claim
about itself.

**Calling tools.** The client calls
`days_since_watering`, then
`log_watering`, then
`days_since_watering` again — chapter 4
showed the answers: 3 days, logged,
0 days. Notice what the client code
actually sends: a name and a small
dictionary of arguments. Everything
else — schemas checked, ids matched,
results unwrapped — is the SDK
earning its keep.

**Reading resources.** `read_resource`
takes a URI in full. The roster comes
from the fixed address; the cactus's
card comes from the template's
address with the blank filled in
(`plants://cactus/card`). To the
client, both are the same call.

**Fetching a prompt.** `get_prompt`
with its argument returns the message
text of chapter 6 — the end of the
session, and deliberately so: the
client collected a *suggestion for a
user*, and there the protocol's work
is done. What a host does with that
text is the host's business.

## The same server over HTTP

The second client
(`plant_log_client_http.py`) differs
in exactly the ways chapter 3 said it
would. The server is started *first*,
by hand, in its own terminal:

```bash
python plant_log_server.py --http
```

and the client connects to the URL
instead of spawning a process:

```python
async with streamable_http_client("http://127.0.0.1:8000/mcp") as (read, write):
```

After that line, the code is the same
shape: initialise, list, call, read.
Transcript `t02-http-session.txt` is
the proof, and the server's own log
(`t02-http-server.txt`) shows the
POSTs arriving. Same offerings, same
answers, different road — the
experiment the whole transport design
exists to make boring.

## What a real host adds

The scripted client is a host with
everything stripped away except the
protocol. A real host adds the model
(choosing tools, filling arguments,
reading results into the
conversation), the consent dialogs of
chapters 4 and 12, persistence, and a
face. None of those change the wire.
If you understood this chapter's two
scripts, you understand what your
desktop assistant is doing under its
own face — which was rather the
point.
