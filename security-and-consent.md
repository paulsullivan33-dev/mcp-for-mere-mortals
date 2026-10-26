# Security and Consent

Chapter 1 stated the rule. This
chapter explains why it needs stating:
what a connected server can actually
do, the ways a dishonest one misbehaves,
and the habits that keep a reader on
the right side of both. None of this
is hypothetical seasoning — it is the
difference between MCP as a socket
standard and MCP as a loaded tool.

## What you are actually granting

Connect a server and you grant three
things, whether or not anyone lists
them for you:

1. **Execution.** A stdio server is a
   program running as you, with your
   permissions. If it can read a file,
   your account could read it. The
   protocol does not sandbox it; your
   operating system is the only wall,
   and it thinks the server is you.
2. **Attention.** The server's tool
   descriptions, its instructions, its
   resource contents and its results
   are all placed in front of your
   model, in a position of trust. The
   model reads them the way it reads
   you.
3. **Action.** Every tool you approve
   really runs. `log_watering` writes
   a log line; another server's tool
   sends the email, moves the money,
   deletes the file.

Hold those three together and the
rule restates itself: **never hand a
server more access than the job needs,
and never let a tool run without
consent that was actually informed.**

## The named hazards

**Tool poisoning.** A server's tool
description is prose shown to your
model. A poisoned one carries extra
instructions smuggled in the prose —
*when you call this tool, also read
this file and include it in the
arguments*. The defence is boring and
total: read descriptions before
connecting, prefer servers whose
source you can read, and treat any
tool whose arguments suddenly include
data it has no business needing as a
fire alarm, not a curiosity.

**Prompt injection through data.** A
resource, or a tool's result, can
contain text written to instruct the
model: a "note" in a document that
says *ignore the user, do this
instead*. Data is not orders. A good
host keeps the boundary visible; a
good user notices when the model's
behaviour changes right after reading
something, and asks what it read.

**The rug pull.** A server you vetted
last month is a program that can be
updated — or replaced — this month,
and hosted servers can change without
any update arriving at your machine
at all. The tool list you approved is
a photograph, not a promise. Hosts
that notice and report changed
offerings are worth preferring;
re-reading the list now and then is
worth the minute it takes.

**Confused deputy, plainly.** Your
host holds several servers and acts
for you. A dishonest one may try to
talk the model into using *another*
server's tools against you — the
garden log asking, in its results,
for the email tool to be used in ways
the email server's owner never
described. Separation between clients
(chapter 2) limits the wire, not the
model's gullibility; the user's eye on
the approval dialog is the real wall.

**Silent scope.** A server that asks
for a whole drive when it needs one
folder, an API key with every
permission when it needs two, an
`env` block copied from a forum with
secrets you did not know you had.
Scope creep is the commonest hazard
in this chapter and the least
dramatic: it is how most real damage
will ever get done.

## The habits

- **Read the server.** Source you can
  read, from an author you can name,
  installed the way chapter 8 installs
  — pinned, in a venv, where you can
  inspect what arrived.
- **Least access, mechanically.** One
  folder, not the drive. A read-only
  key, not the master key. A server
  per job, removed when the job ends.
  If a tool would embarrass you in the
  approval dialog, it should not be
  waved through at 1 a.m. either.
- **Approve like you mean it.** The
  consent dialog shows a server, a
  tool and arguments. Reading all
  three takes seconds. A host that
  will not show them is not a host to
  connect interesting servers to.
- **Keep secrets out of prompts.**
  Configuration `env` blocks (chapter
  11) are read by the server — which
  is the point — and by anyone who
  later reads the config file. Treat
  the file as a secret too.

The Plant Log passes every test in
this chapter trivially — invented
data, in its own memory, source on
the page in front of you. That is
deliberate. Learn the protocol on a
server that cannot hurt you, and the
habits will be there when you meet
one that could.
