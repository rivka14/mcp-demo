# Heart Data MCP Server

A Model Context Protocol (MCP) server that provides access to heart disease dataset analysis tools for Claude Desktop.

## Features

This MCP server exposes the following tools:
- `get_age`: Query heart disease data by age
- `get_sex`: Query heart disease data by sex (0=female, 1=male)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Claude Desktop app

## Installation

1. Clone this repository:
```bash
git clone https://github.com/rivka14/mcp-demo.git
cd mcp-demo
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastmcp pandas
```

## Running the Server

To test the server locally:
```bash
python server.py
```

## Connecting to Claude Desktop

### Configuration

1. Locate your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the MCP server configuration to the file:

```json
{
  "mcpServers": {
    "heart-data": {
      "command": "python",
      "args": [
        "/absolute/path/to/mcp-demo/server.py"
      ],
      "env": {
        "PYTHONPATH": "/absolute/path/to/mcp-demo"
      }
    }
  }
}
```

**Important:** Replace `/absolute/path/to/mcp-demo` with the actual absolute path to your mcp-demo directory.

3. If using a virtual environment, update the configuration to use the virtual environment's Python:

```json
{
  "mcpServers": {
    "heart-data": {
      "command": "/absolute/path/to/mcp-demo/venv/bin/python",
      "args": [
        "/absolute/path/to/mcp-demo/server.py"
      ]
    }
  }
}
```

4. Restart Claude Desktop for the changes to take effect.

### Verification

Once configured, you can verify the connection in Claude Desktop by asking:
- "What MCP tools are available?"
- "Show me heart data for age 50"
- "Get heart disease data for males"

## Dataset

The server uses `heart.csv`, which contains heart disease patient data with the following columns:
- age
- sex (0=female, 1=male)
- chest pain type
- resting blood pressure
- cholesterol
- fasting blood sugar
- resting ECG results
- max heart rate
- exercise induced angina
- and more...

## Troubleshooting

### Server not appearing in Claude Desktop
- Verify the absolute paths in your configuration are correct
- Check that Python and dependencies are installed
- Restart Claude Desktop after making configuration changes
- Check Claude Desktop logs for error messages

### Import errors
- Ensure you've installed all dependencies: `pip install fastmcp pandas`
- If using a virtual environment, make sure it's activated or reference it in the config

