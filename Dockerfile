# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for jumuia-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/jumuia-mcp"
LABEL org.opencontainers.image.description="jumuia-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir jumuia-mcp

CMD ["jumuia-mcp"]
