# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 14 names what the protocol
   cannot do: it cannot make a server honest, its discovery
   lists are photographs rather than promises, the model
   choosing the tools is the weak joint, context is finite and
   priced, state and identity belong to the applications
   rather than the protocol, and the standard itself is two
   years old and still moving.
8. **The ethics rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *give a server no more
   access than the job needs, and let no tool run without the
   user's consent* — before any procedure depends on it, and
   chapter 12 gives the hazards their names: tool poisoning,
   prompt injection through data, the rug pull, the confused
   deputy, and silent scope.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox.
The official Python SDK (**mcp 2.3.0**, pip) was installed
into a fresh virtual environment (Python 3.12.3) and exercised
against a server written for this guide (`mcp-lab/server/`),
the Plant Log: an invented watering log for three fictional
houseplants, holding its state in memory and nothing else.
All transcripts live in `mcp-lab/transcripts/`.

Run for real, with transcripts as evidence:

- Install and versions: the SDK reports itself as mcp 2.3.0
  on Python 3.12.3 (t00).
- A full stdio session with a scripted client: handshake,
  discovery of 2 tools, 1 resource, 1 resource template and
  1 prompt; both tools called, with the log visibly changing
  between calls (3 days, then 0); both resources read,
  including a templated one; the prompt fetched (t01).
- The same server over streamable HTTP on loopback: started
  with `--http`, its uvicorn log kept; a second client
  initialised, listed the tools, called one and read the
  roster resource against it (t02).
- The opening exchange repeated by hand in raw JSON-RPC
  with no SDK: initialize, the initialised notification,
  tools/list and a tools/call, every line both ways (t03).
- The official Inspector in CLI mode against the lab
  server: `tools/list` answered with both tools and their
  full schemas (t04).
- Three deliberately broken tool calls, kept side by side:
  a wrong-typed argument refused by schema validation, a
  call to a nonexistent tool, and a well-formed call the
  tool itself answers with a refusal that is not an error
  (t05).
- The SDK 2.x renames were met in the lab, not read about:
  the server class is MCPServer (FastMCP was removed), and
  client result fields are snake_case (`is_error`,
  `server_info`, `resource_templates`). The lab's clients
  failed on the old spellings first; the fixes are in the
  committed code, and chapter 14 teaches the trap.

Documented only — described from the specification and the
project's documentation, not run, and the text does not
claim otherwise:

- Sampling and elicitation (chapter 7). The Plant Log needs
  neither, and no host in the lab could grant them; both are
  explained from the specification, with their consent
  requirements stated as the specification states them.
  Roots are likewise described, not exercised.
- Real host applications (chapter 11). The lab had no
  desktop host to configure; the configuration block taught
  is the documented common shape, and the example file in
  `examples/` is the same command and arguments the lab's
  scripted client verifiably ran.
- The Inspector's web interface (chapter 10). The sandbox
  has no browser session to drive it; its CLI mode was run
  and is the verified half.
- Authentication and OAuth for hosted HTTP servers
  (chapters 3 and 12). The lab's HTTP server listened on
  loopback only and no sign-in was built or claimed.
- Resource subscriptions and list-change notifications,
  and argument completion (chapters 5 and 6): described
  from the specification; the lab's server declares
  neither capability.
- The neighbours of chapter 13 — function calling, plain
  APIs, plugin systems, agent frameworks — are
  characterised, not benchmarked; the lab's wire was
  MCP's own.

Fixtures are this guide's own and deliberately generic: a
watering log for three invented houseplants ("fern",
"basil", "cactus"), kept in the server's memory, on one
machine, over stdio and loopback HTTP only. No example is
modelled on any real person, network, service or
organisation, and the server can see nothing beyond its
own dictionary.
