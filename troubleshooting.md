# Troubleshooting

Every entry here is a symptom the
lab produced on purpose or met by
accident while building this guide.
The specimens live in
`mcp-lab/transcripts/t05-errors.txt`
unless a chapter is named instead.

## The server starts and says nothing

A stdio server alone in a terminal
sits silent, waiting for JSON on its
stdin. That is health, not death. Do
not type prose at it, and do not
conclude anything until a client —
the Inspector (chapter 10) or the
`raw_conversation.py` script — has
spoken to it properly.

## The host cannot start the server

The command in the configuration is
run by the host, not by your
terminal, and the two disagree about
PATHs and working directories.
Symptoms: the server is listed but
never connects, or vanishes at
startup. Cures, in order: full path
to the interpreter (chapter 11's
config uses the venv's Python, by
address); run the exact command
yourself once, from a plain shell;
check the host's server log for the
stderr you are missing.

## All my servers disappeared

One malformed block — a missing
comma, a trailing one — makes many
hosts discard the *whole*
configuration file without a word.
Validate the JSON (any text editor's
JSON mode, or `python3 -m json.tool`
on the file), restore the copy you
kept (chapter 11 told you to keep
one), and re-add servers one at a
time.

## "Unknown tool", and its cousins

Transcript `t05` holds the three
shapes side by side; learn to tell
them apart, because their repairs
differ:

1. **Wrong argument type** —
   `millilitres: "a splash"` came
   back with `isError` set and a
   validation essay: the schema did
   its job before the tool ran. The
   repair is in the caller (or the
   model's reading of the schema),
   not the server.
2. **A tool that does not exist** —
   `Unknown tool: sing_to_plant`. The
   caller's list is stale, or the
   name is mistyped, or the server
   changed. Re-run discovery and
   compare (chapter 13's photograph).
3. **A refusal that is not an
   error** — "No plant called
   'orchid' in the log." arrived with
   `isError` *false*. Nothing failed;
   the answer was simply no. Tools
   argue their case in results more
   often than tutorials admit.

## The tool exists but the host never offers it

Capabilities are declared, not tried
(chapter 2). If a host does not claim
a feature, or a server does not list
one, the missing thing is missing
from the handshake, not broken in the
session. Check both lists before
suspecting the code: `prompts/list`
against a server with no prompts is
an empty list, honestly returned.

## Imports fail: FastMCP cannot be found

The lab's own first wound. Tutorials
written for SDK 1.x build on
`mcp.server.fastmcp.FastMCP`; SDK 2.x
renamed the class to **MCPServer**
(`mcp.server.mcpserver`) and its
client results to snake_case fields
(`is_error`, `server_info`). The
error message names the fix; pin
`mcp<2` only if you must follow an
old tutorial word for word, and know
that you have chosen the museum
branch when you do.

## Nothing answers on the HTTP port

Four checks, in the order the lab
would run them: the server was
started with the HTTP transport (a
stdio server listens on no port at
all); the URL ends in `/mcp`; the
port is the one the server printed
at startup; and nothing else already
owns that port (the server says so,
rudely and clearly, in its startup
log — transcript `t02-http-server.txt`
shows a healthy one).

## Garbled protocol, sane-looking code

If a client reports messages it
cannot parse, look for a print
statement in the server writing to
stdout. Stdout is the wire (chapter
3); a single stray `print("here")`
inside a tool corrupts every message
after it. Log to stderr. Everyone
learns this once; the guide would
rather you learned it here.
