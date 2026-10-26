# Tools

A **tool** is an action a server
offers: a named operation, with typed
arguments going in and a result coming
out. Tools are the part of MCP a model
actually *wields* — of the three
offerings, they are the ones that can
change things in the world, and so the
ones the consent rule watches closest.

## What a tool looks like on the wire

When a client asks `tools/list`, each
tool arrives as a small dossier:

- a **name**, unique on that server —
  `log_watering`, `days_since_watering`
- a **description**, written for the
  model to read: what the tool does,
  in plain words
- an **input schema**, a **JSON
  Schema** object naming each
  argument, its type, and which are
  required
- optionally an **output schema** for
  structured results, and **annotations**
  hinting at character: read-only?
  destructive? safe to repeat?

From the lab's raw transcript (`t03`),
one entry, trimmed:

```json
{"name": "log_watering",
 "description": "Record that a plant was watered today...",
 "inputSchema": {
   "properties": {
     "plant": {"type": "string"},
     "millilitres": {"type": "integer"}},
   "required": ["plant", "millilitres"]}}
```

The description deserves a paragraph
of its own. The model chooses tools —
and fills their arguments — by reading
these dossiers. A vague description
gets a vaguely-used tool. Honest
servers write descriptions the way
good manuals are written: what it
does, what it changes, what it will
refuse. Chapter 12 returns to the dark
side of this: a description is text a
stranger wrote, shown to your model,
and a dishonest one can lie.

## Calling a tool

A call is one request: `tools/call`,
the tool's name, and an **arguments**
object matching the schema. The Plant
Log's client made three in a row
(transcript `t01`):

```text
== Tool: days_since_watering(fern) ==
fern was last watered 3 day(s) ago.

== Tool: log_watering(fern, 300) ==
Logged: fern watered with 300 ml on 2026-10-26.

== Tool: days_since_watering(fern), again ==
fern was last watered 0 day(s) ago.
```

Read that again slowly, because it is
the whole idea: the second call
*changed something* — the log now says
the fern was watered — and the third
call proves the change persisted. The
server holds the state; the client
holds none. That is the shape of every
tool you will ever meet, from a
watering log to a payment system.

## Results and errors

A result carries **content** — most
often text, but images, audio and
embedded resources exist — and a flag,
**isError**, saying whether the tool
itself reports failure. Two kinds of
failure must not be confused:

- **Protocol errors**: the request
  itself was malformed, or named a
  tool that does not exist. These come
  back as JSON-RPC errors.
- **Tool errors**: the call was well
  formed and the tool ran, but the job
  failed — wrong-typed arguments, a
  file not found, a service down.
  These come back as a normal result
  with `isError` set, so the *model*
  can read what happened and react.

The lab made both kinds on purpose
(transcript `t05`), and chapter 14
walks through all three specimens —
including a third, subtler shape: a
call that succeeds and answers with a
polite refusal written by the tool
itself ("No plant called 'orchid' in
the log."), which is not an error at
all but a fact the caller needed.

## Who decides?

The model proposes; the host disposes.
In a well-behaved host, a tool call
that changes things is shown to the
user — the tool, the arguments, the
server it came from — and runs only on
approval. Read-only tools may be waved
through under a standing permission,
but that is the *host's* policy and
the *user's* setting, never the
server's entitlement. A server cannot
grant itself approval. Any host that
hides tool calls from its user has
broken the protocol's social contract
even if it speaks the wire format
perfectly, and chapter 12 treats
choosing such hosts — and such
servers — as the reader's real
security work.
