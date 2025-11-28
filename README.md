SonarQube MCP Server

## Overview

The Model Context Protocol (MCP) Server for SonarQube enables AI Agent applications to efficiently manage and retrieve data from a SonarQube server.

## Example Usage

Ask your AI Agent to:

- List SonarQube projects, projects where the user has admin permissions, or projects available for scanning.
- List issues or retrieve detailed issue information.
- List available SonarQube quality gates or check the quality gate status of a project.
- Check the SonarQube server status.

## Tools

- `hotspot`: Retrieve a project's hotspots and detailed hotspot information.
- `issue`: List issues on the SonarQube server with optional filters (e.g., by project or author) or retrieve issue author details.
- `metric`: Fetch metric information and metric types.
- `permission`: Assign or revoke group/user permissions for a project or globally, and retrieve permission details.
- `project`: Create a project, list projects, or retrieve project analysis.
- `qualitygate`: Obtain quality gate information or the quality gate status of a project.
- `qualityprofile`: Retrieve or update quality profile information for a project.
- `rule`: Fetch rule information.
- `source`: Retrieve source code and issue information for solution suggestions.
- `system`: Check SonarQube server and connectivity status.

## Configuration

| Name                     | Description                    | Default Value             |
| ------------------------ | ------------------------------ | ------------------------- |
| `SONARQUBE_URL`          | SonarQube server URL           | `"http://localhost:9000"` |
| `SONARQUBE_TOKEN`        | SonarQube authentication token |                           |
| `SONARQUBE_USERNAME`     | SonarQube Username / Token     | `None`                    |
| `SONARQUBE_PASSWORD`     | SonarQube Password             | `None`                    |
| `SONARQUBE_ORGANIZATION` | SonarQube organization name    | `None`                    |

## Installation

### Install from source

```bash
# Clone the repository
git clone https://github.com/nggocnn/sonarqube-mcp.git
cd sonarqube-mcp

# Install the package
pip install .
# or using uv
uv pip install .
```

### Install from PyPI (once published)

```bash
pip install sonarqube-mcp
```

## Integration

The MCP Server supports the following transport methods: `stdio`, `sse`, or `streamable-http`.

#### stdio

```json
"sonarqube_stdio": {
    "command": "sonarqube-mcp",
    "args": [
        "--transport",
        "stdio"
    ],
    "env": {
        "SONARQUBE_URL": "<sonarqube_url>",
        "SONARQUBE_TOKEN": "<sonarqube_token>"
    }
}
```

Alternatively, you can use the Python module directly:

```json
"sonarqube_stdio": {
    "command": "python",
    "args": [
        "-m",
        "sonarqube_mcp",
        "--transport",
        "stdio"
    ],
    "env": {
        "SONARQUBE_URL": "<sonarqube_url>",
        "SONARQUBE_TOKEN": "<sonarqube_token>"
    }
}
```

#### sse

```bash
export SONARQUBE_URL="<sonarqube_url>"
export SONARQUBE_TOKEN="<sonarqube_token>"

sonarqube-mcp --transport sse

# or using the Python module
python -m sonarqube_mcp --transport sse
```

```json
"sonarqube_sse": {
    "type": "sse",
    "url": "http://127.0.0.1:8000/sse"
}
```

## Configuration Validation

Check your configuration and test the connection:

```bash
sonarqube-mcp --check-config
```

This will:
- Validate all required environment variables are set
- Test the connection to your SonarQube server
- Display the current configuration status

## Usage

View all available options and environment variables:

```bash
sonarqube-mcp --help
```

## Testing

You can use MCP Inspector to test and debug this MCP Server.

```bash
npx @modelcontextprotocol/inspector --config config.json --server sonarqube
```
