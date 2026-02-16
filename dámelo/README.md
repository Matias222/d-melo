# Dámelo Plugin

Share and manage AI assistant sessions (Claude Code, Cursor, etc.) with your teams.

## Features

- **Export Sessions**: Save complete or thematic session summaries
- **Import Sessions**: Load sessions shared by teammates
- **List Sessions**: Browse your sessions, team sessions, or repository sessions
- **Team Collaboration**: Share work context across your organization

## Installation

1. Copy this plugin directory to `~/.claude/plugins/`
2. Start the MCP server:
   ```bash
   cd /path/to/damelo/mcp
   source venv/bin/activate
   python server.py
   ```
3. Restart Claude Code

## First Time Setup

1. Authenticate with Dámelo:
   - Ask Claude: "login to dámelo"
   - Open the OAuth URL in your browser
   - Authorize via GitHub
   - Your JWT token will be saved automatically

## Available MCP Tools

- `login` - Authenticate via GitHub OAuth
- `list_own_creations` - List your personal sessions
- `list_team_sessions` - List sessions shared with a team
- `list_repo_sessions` - List sessions for a specific repository
- `import_session` - Import a session by ID
- `export_session` - Export current session (full or thematic)

## Usage Examples

```
"Show me my sessions"
"List sessions for the frontend team"
"Import session abc-123-def"
"Export this session about authentication work"
```

## Requirements

- Dámelo MCP server running on `http://localhost:8080`
- GitHub account for authentication
- Backend API configured at `DAMELO_API_URL`

## Author

Matias Avendano
