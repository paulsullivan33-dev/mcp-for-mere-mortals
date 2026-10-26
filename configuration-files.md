# Configuration Files

A host learns about servers from a
**configuration file**: a block of
JSON saying *here is a server; run
this, or connect there*. Almost every
host uses the same shape, because the
shape came from the protocol's first
popular host and everyone since has
sensibly copied it. Learn it once and
you can read any host's settings.

## The stdio block

For a server on your own machine, the
block names a command to run. Here is
the Plant Log's, as the lab checked it
(kept in `examples/mcp-config.json`):

```json
{
  "mcpServers": {
    "plant-log": {
      "command": "/home/you/mcp-venv/bin/python",
      "args": ["/home/you/mcp-lab/server/plant_log_server.py"]
    }
  }
}
```

Anatomy:

- **`mcpServers`** — the shelf. Each
  key under it is a server's local
  name — *your* name for it, shown in
  the host's interface. It need not
  match the server's own name for
  itself.
- **`command`** — the program to run.
  Use the full path to your virtual
  environment's Python, as above. "It
  worked in my terminal" is usually a
  PATH that your terminal has and the
  host, launched from a desktop, does
  not.
- **`args`** — the command's
  arguments, one string each: the
  server file, then any flags. Split
  them as a list; a single string with
  spaces in it is the classic first
  failure (chapter 14).
- **`env`** — an optional object of
  **environment variables** to hand
  the server: an API key, a folder
  path, a mode. Whatever is in here
  is the server's to read — secrets
  included — so this object deserves
  the chapter 12 once-over before you
  paste anyone's example into it.
- **`cwd`** — where supported, the
  working directory the server starts
  in. Servers that use relative paths
  live or die by this line.

## The HTTP block

A remote or already-running server is
named by address instead of command:

```json
{
  "mcpServers": {
    "team-log": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

Hosts vary in the details — some want
`"type": "http"` spelled out, some
keep headers for authentication in a
**`headers`** object beside the URL —
but the idea is constant: a name, and
where to reach it. The URL above is
the lab's own HTTP server; a hosted
one would be an https address, and
reaching it would normally involve
the OAuth sign-in of chapter 3, done
once by the host with you watching.

## Where the file lives

Hosts keep this block in their own
places: a desktop assistant in its
settings folder, an editor in the
project or the user profile, with
names like `claude_desktop_config.json`,
`mcp.json`, or a settings page that
writes the JSON for you. The lab had
no desktop host to configure — this
chapter is taught from the documented
common shape, and the example file in
`examples/` is the artefact the lab
verified (it is the same command and
arguments the scripted client used,
which is why the guide trusts it).
`criteria.md` lists host configuration
as documented-only, plainly.

## Habits that prevent midnight

- One server per name, and names that
  say what the thing is: `plant-log`,
  not `server2`.
- Change one block at a time, and
  restart the host after each change —
  hosts read configuration at startup,
  and a stale host arguing with a new
  file has wasted more evenings than
  any bug in this guide.
- Keep a copy of a working file
  before editing it. JSON forgives
  nothing: one missing comma and the
  whole shelf silently vanishes,
  which chapter 14 meets as a symptom
  ("all my servers disappeared").
