# The Neighbours

MCP did not invent giving models
tools, and it does not replace its
neighbours so much as give them a
common doorway. Three comparisons
cover most of the "but isn't this
just..." questions.

## Function calling

**Function calling** (also "tool
use") is the ability built into model
APIs themselves: the caller hands the
model a list of function descriptions
with the conversation, the model may
answer with "call this one, with
these arguments", and the caller runs
it and reports back. It is excellent
— and it is a conversation between a
model and *one application*. The
application writes every description,
owns every function, and starts again
from zero for the next application.

MCP lives one layer out. The server
owns the descriptions and the code;
any host can discover them. In
practice the two compose: the host
discovers tools over MCP, then offers
them to its model through the model's
own function-calling machinery.
Function calling is how the model
speaks; MCP is how the tools arrived
and who vouches for the guest list.
Characterised here, not benchmarked —
the lab's wire was MCP's, and the
model's side of the host stayed
outside it (see `criteria.md`).

## Plain APIs

A **REST API** (or any HTTP API) is a
server speaking to programs in
general, usually designed before
anyone expected a model to be the
program. An MCP server is very often
a thin, polite wrapper over one:
discovery lists instead of a
documentation site, schemas tuned for
a model to read, arguments counted in
the handful a model can fill
reliably. If you have an API, an MCP
server in front of it is a day's
work, not a rewrite — chapter 8's
decorators are the whole trick. The
neighbours are not rivals; one is the
engine room, the other is the door
with the guest book.

## Plugins and extensions

Every AI product grew a **plugin**
system at some point: code written
*for that product*, installed *into
that product*, speaking that
product's private dialect. Plugins
can do more (they are inside the
house), and travel nowhere (they are
inside *one* house). An MCP server is
the opposite bargain: it lives in its
own process, speaks a public
protocol, and is limited to what the
protocol can express — which is why a
server written for one host appears,
unchanged, in another host's tool
list, and why this guide could be
written against a scripted client
and still be about the assistant on
your desktop.

## Agent frameworks, in one paragraph

Frameworks that plan, loop and juggle
many tools sit *above* all of this:
they are hosts with ambitions, or
libraries for building them. They
consume MCP servers as happily as any
host does. When a framework's
documentation and this guide seem to
describe the same territory from
different heights, both are right;
the protocol is the ground floor
either way.
