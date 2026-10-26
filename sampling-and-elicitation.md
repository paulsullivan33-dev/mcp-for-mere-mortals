# Sampling and Elicitation

Everything so far flows one way: the
client asks, the server answers.
These two features reverse the current
— a server, mid-task, asks the *host*
for something. They are the least
implemented and most argued-about part
of MCP, and this chapter is honest
about its evidence: the lab did not
run either feature, because the Plant
Log needs neither. What follows is
the specification, explained plainly,
and labelled documented-only in
`criteria.md`. Read it for the shape,
not for transcripts.

## Sampling: borrowing the model

**Sampling** lets a server ask the
host to run a message past its model
and return the reply. The server sends
`sampling/createMessage` — a short
conversation, a limit on length,
preferences about cost or speed — and
the host's model answers. The server
gets text. It never learns which
model, never gets a key or an account:
it borrowed an answer, not the
machine that made it.

Why would a server want this? To do a
small piece of judgement inside a
larger mechanical job. A log server
holding a thousand entries might ask
the model to summarise three of them.
A filing tool might ask which of two
folders a document sounds like. The
server stays a program — no model of
its own, no API bills of its own —
and intelligence is rented by the
question.

The consent design is the point, and
the specification is firm: the host
must let the user **see and approve**
a sampling request, and may let the
user edit the prompt before it runs.
A server silently steering your model
would be a puppet string; sampling as
specified is a request made in the
open, to a host that can refuse.
Support is declared as a capability in
the handshake (chapter 2); a host that
does not claim sampling is never
asked, and a server must cope with
refusal as a normal answer.

## Elicitation: asking the user

**Elicitation** lets a server ask the
*user* a question while a tool call is
in flight: "this booking deletes the
old one — proceed?", "which of these
two accounts did you mean?". The
server sends `elicitation/create` with
a message and a small schema for the
answer (a confirmation, a choice from
a list, a few fields). The host shows
its own dialog — the server never
draws the window — and returns the
user's answer, a refusal, or a
dismissal, which are three different
things and a server must treat them
differently.

The obvious use is confirmation at
the exact moment of consequence,
rather than a blanket permission
granted an hour earlier to a tool
whose arguments did not yet exist.
That is consent with the details
filled in, and it is the direction the
protocol's safety thinking is
travelling.

## Roots, briefly

A third host-side idea deserves a
mention: **roots** are the host
telling a server which directories or
locations it is *about* — the project
folder in an editor, say — so a
server can aim at the right place
without being handed the whole disk.
It is context, offered by the host,
not a permission slip, and chapter 12
notes the difference.

## The honest summary

Sampling and elicitation are where
MCP stops being request-and-answer
and becomes a negotiation, and they
are correspondingly younger, rarer in
the wild, and the first place to check
a host's real behaviour against its
documentation. When your host and
server both support them, the consent
questions of chapter 12 apply with
double force, because the requests
now travel in both directions.
