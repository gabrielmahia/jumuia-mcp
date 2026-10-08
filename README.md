# jumuia-mcp
<!-- mcp-name: io.github.gabrielmahia/jumuia-mcp -->

## Why This Exists

Kenya's SACCOs and chamas move an enormous share of household savings and credit, yet the rules for forming one, the difference between a registered society and a limited company, and what members are actually entitled to are scattered across the Cooperative Societies Act, SASRA circulars and word of mouth. This server puts that guidance where an AI agent can reach it, in one call.

## Install

```bash
pip install jumuia-mcp
```

## Tools (5)

- **`sacco_finder`** — Find SACCOs (Savings and Credit Cooperatives) in Kenya by sector, county, or type.  
  <sub>args: county, sector</sub>
- **`chama_formation_guide`** — Return step-by-step guide to forming a chama (investment group) in Kenya.  
  <sub>args: members, purpose</sub>
- **`cooperative_benefits`** — Return benefits, structures, and types of cooperatives available in Kenya.  
  <sub>args: coop_type</sub>
- **`sacco_loan_guide`** — Return indicative terms for a Kenyan SACCO loan product.  
  <sub>args: loan_type, sacco_name</sub>
- **`cooperative_rights_query`** — Return the rights a Kenyan cooperative or SACCO member holds on a topic.  
  <sub>args: topic</sub>

## Example

```python
from jumuia_mcp.server import chama_formation_guide

result = chama_formation_guide(members=12, purpose='savings')
# steps, legal structures, registration fees, merry-go-round maths
```

## Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "jumuia-mcp": {
      "command": "python",
      "args": ["-m", "jumuia_mcp.server"]
    }
  }
}
```

## Data & Disclaimers

Guidance is drawn from the Cooperative Societies Act and SASRA regulations. Fees and capital thresholds change — confirm with the Ministry of Cooperatives or sasra.or.ke before relying on a figure.

Every tool response carries a `source` field. Responses labelled `DEMO` are
illustrative reference data, not a live feed — verify against the authority
named in the response before acting on it.

## Part of the East Africa Coordination Stack

This MCP server is part of the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).

<!-- interconnect:v1 -->
## Part of the East Africa coordination stack

- **Install & run:** `pip install reli-cli && reli list` — the MCP servers on the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.gabrielmahia`
- **Evaluate any model on Swahili agent tasks:** [kipimo](https://github.com/gabrielmahia/kipimo) · [dataset](https://huggingface.co/datasets/gmahia/kipimo) · [leaderboard](https://huggingface.co/spaces/gmahia/kipimo-leaderboard)
- **Coordinate across servers:** [africa-coord-bus](https://pypi.org/project/africa-coord-bus/) — offline-first event bus with a built-in Kenya routing table
- **Datasets:** [huggingface.co/gmahia](https://huggingface.co/gmahia) · **Docs hub:** [nairobi-stack](https://github.com/gabrielmahia/nairobi-stack)

Model-agnostic by design: closed APIs, open-weight models, and small distilled models are all first-class citizens.
<!-- /interconnect:v1 -->
