# Prompts

The third offering is the gentlest. A
**prompt** is a ready-made message
template a server publishes for the
*user* to pick: a well-written request,
with blanks for the details, prepared
by someone who knows what the server
is good for. If tools are verbs the
model conjugates and resources are
pages the host hands over, prompts are
the forms on the counter — filled in
by a person, on purpose.

## What a prompt is made of

Discovery is `prompts/list`. Each
entry has a **name**, a **description**
written this time for the user, and a
list of **arguments** — the blanks —
each marked required or optional. The
Plant Log offers one (transcript
`t01`):

```text
== Prompts on offer ==
- watering_reminder
```

Fetching is `prompts/get` with the
blanks filled in. What returns is a
set of **messages** — a small scripted
conversation, ready to be placed in
front of the model. The lab fetched
`watering_reminder` with the plant
"basil", and got exactly one message
back:

```text
== Prompt: watering_reminder(basil) ==
Please check the plant log for basil: read its card, say how long since it was watered, and tell me plainly whether it needs water today.
```

Nothing has been *done* yet. No tool
has run. The server has merely handed
the user a good sentence — one that
names the right resource, asks for the
right tool, and sets the tone
("plainly") — and the user decides
whether to send it.

## Why prompts belong to the user

This is the offering readers most
often misunderstand, so the guide is
plain about it: **prompts are
user-controlled by design.** The
specification's model is a menu — in
many hosts they literally appear as
slash commands or a picker list. The
model does not browse them, choose
them or fire them off. That is not a
missing feature. It is a decision
about who steers.

It also makes prompts the honest way
for a server's author to say "here is
what this server is *for*". A
well-kept server ships the handful of
requests its tools were built to
serve, written the way its author
would write them. The user sees the
server's intentions in plain language
before anything runs — a small act of
transparency that chapters 12 and 13
will contrast with servers that would
rather you not look too closely.

## Arguments, and richer returns

A prompt's arguments are simple
strings, filled in by the user through
the host's interface; a host may offer
**completion** (suggestions for what a
blank could be — plant names, in the
lab's world) if the server declares
that capability. Returns can be
richer than one message: several
messages staging a short exchange, or
messages embedding a resource's
contents, so "review this document"
arrives with the document attached.
The Plant Log uses the simple end of
all of this, and the guide says so;
the richer returns are described from
the specification and listed in
`criteria.md`.
