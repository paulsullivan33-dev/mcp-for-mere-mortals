# Limits

An honest chapter about what the
protocol cannot do, does not attempt,
and cannot promise — so that what it
*does* do can be trusted.

## It does not make servers honest

MCP standardises the conversation,
not the character of the participants.
A server can list a tool accurately
and implement it treacherously; it can
answer a resource request with text
designed to mislead a model; it can
change after you vetted it. The
specification's consent requirements
bind hosts. Nothing binds a stranger.
Chapter 12 is therefore not an
appendix to this guide but a
load-bearing wall, and the limit
stated plainly is: **the protocol
gives you a good look at a server,
never a guarantee about one.**

## Discovery is a photograph

Lists are what the server claims, at
the moment it was asked. Tools can
appear, vanish or alter their
descriptions between sessions (and a
server may offer `listChanged`
notifications, or may not). A host
working from a cached list is working
from memory. For a watering log this
is nothing; for a payments tool it is
a design constraint, and chapter 12's
rug pull lives exactly here.

## The model is the weak joint

Tools are chosen, and arguments
filled, by a model reading
descriptions. Models misread. They
pick the wrong tool of two similar
ones, fill a date in the wrong
format, summarise a long resource
badly, or — chapter 12 — follow
instructions hidden in data. The
protocol carries the request
faithfully and reports errors
honestly; it cannot make the request
wise. Hosts that show calls before
running them exist precisely because
this limit is permanent.

## Context is finite and priced

Everything discovered and read goes
into a conversation with a size
limit, and usually a price. Twenty
servers times thirty tools is six
hundred descriptions competing for
the model's attention before the user
has said a word; a resource can be a
novel; a chatty tool result can evict
the question it was answering. Good
hosts curate — connect per task, not
per lifetime — and good servers keep
descriptions tight and results
shorter than their authors' pride
would like. The Plant Log's four-line
cards are this limit, respected in
advance.

## State, identity and the rest of life

A stdio server dies with its session
and forgets everything not written
down; the protocol has no memory of
its own and promises none. Remote
servers raise the questions any web
service raises — whose account, whose
audit trail, whose data after a
breach — and MCP's OAuth machinery
(chapter 3) is plumbing for those
questions, not answers to them.
Long-running work fits awkwardly:
progress notifications exist, but a
tool call is fundamentally a request
that expects an answer, and jobs of
an hour are a negotiation the
protocol supports rather than solves.

## Young, and moving

Finally, the limit of novelty. MCP
dates from 2024. Its specification
has already revised transports (the
HTTP+SSE of chapter 3 is a fossil
from its first year), renamed SDK
parts under working programmers
(chapter 8's FastMCP trap), and left
features like sampling (chapter 7)
implemented by a minority of hosts.
Pin versions, read changelogs, and
expect the ground to keep settling.
A standard that has finished moving
has usually finished mattering.
