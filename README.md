# MCP LATAM Connectors ⚡

An open-source collection of **Model Context Protocol (MCP)** servers designed to connect **Claude Desktop** and **Claude Code** directly to Latin American infrastructure, payment rails (BCB Pix), and regional messaging APIs.

## 🚀 Overview
Developers across Latin America need native agentic integrations for local tools that aren't covered by global MCP repositories. This project provides standardized, lightweight Python MCP servers for regional ecosystems.

## 📦 Included MCP Servers
- **`pix-brcode-mcp`**: Generate, validate, and parse static/dynamic Pix payloads (EMV® QRCPS-MPM standard) directly inside Claude.
- **`whatsapp-evolution-mcp`**: Bridge Claude agent workflows with Evolution API / Baileys instances for automated triage.
- **`cep-cnpj-lookup`**: Real-time tool calling for Brazilian company registries (BrasilAPI) and postal data.

## 🛠️ Quick Start (Claude Desktop)

1. Install dependencies:
`pip install -r requirements.txt`

2. Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "latam-connectors": {
      "command": "python",
      "args": ["/path/to/mcp-latam-connectors/server.py"]
    }
  }
}
```

## 🤝 Contributing
Pull Requests adding new regional API tools, prompt templates, or bug fixes are welcome! Check `COMMUNITY_TOOLS.md` to submit a quick PR directly from your browser.
