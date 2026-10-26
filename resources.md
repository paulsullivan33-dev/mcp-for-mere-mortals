# Resources

A **resource** is text (or data) a
server publishes for reading: the
calm, read-only side of MCP. Where a
tool *does*, a resource *says*. A host
fetches resources to put facts in
front of the model — a document, a
record, a configuration — the way you
might hand someone a page before a
meeting rather than answer questions
from memory.

## Addressed by URI

Every resource has a **URI**: an
address in the same style as a web
address, with a scheme the server
invents if it likes. The Plant Log
uses `plants://`:

```text
plants://roster
plants://cactus/card
```

A client discovers fixed resources
with `resources/list`, and reads one
with `resources/read`, sending the
URI. What comes back is **contents**:
the text (or, for binary data,
base64), a **MIME type**, and the URI
it answers to. The roster, from
transcript `t01`:

```text
== Resource: plants://roster ==
Plants in the log:
- basil (Sweet basil)
- cactus (Prickly pear cactus)
- fern (Boston fern)
```

## Templates: addresses with blanks

Most real servers cannot list
everything they could serve — a log
with ten thousand entries would make
a ten-thousand-line list. So a server
may instead publish **resource
templates**, discovered with
`resources/templates/list`: URI
patterns with named blanks, like the
Plant Log's

```text
plants://{plant}/card
```

The client fills the blank in —
`plants://cactus/card` — and reads it
like any resource. One template stands
for a whole family of documents, and
the family can grow without the
discovery list growing. Templates are
also an honest advertisement: they
tell the host the *shape* of what
exists without pretending to an
inventory.

## Who chooses what to read

Resources are **application-driven**,
in the specification's deliberate
phrasing: the host decides how they
are used. One host may show the user a
picker and let them attach a resource
to the conversation, like attaching a
file to an email. Another may fetch
some automatically. The model can be
told what exists and may ask — but
resources are not the model's to
demand the way tool calls are its to
propose, and a careful host treats
"the model requested the contents of
..." as a moment for the same consent
as any other data leaving the
building. A resource is data *in*: it
can inform the model, and — chapter 12
again — it can also try to instruct
it, which is why what a resource says
is data, never orders.

## Subscriptions, and the edges

Servers that hold changing data may
offer **subscriptions**: the client
asks to be told when a resource
changes, and a notification arrives
when it does. Lists can also announce
their own changes (`listChanged`), so
a host learns that a new tool or
resource exists without re-asking.
Both are optional capabilities,
declared in the handshake (chapter 2);
the Plant Log claims neither, and this
guide describes them from the
specification rather than the lab —
see `criteria.md`.

Size is the quiet edge: a resource can
be a novel. Hosts truncate, servers
should summarise and page, and a
reader designing a server should ask
of every resource: *would I want all
of this in a conversation at once?*
The Plant Log's cards are four lines.
That is not a limitation of the
fiction; it is the design lesson.
