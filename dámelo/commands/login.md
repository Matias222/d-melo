---
description: Login to Dámelo via GitHub OAuth
allowed-tools: Bash(chmod:*), Bash(echo:*), Bash(export:*), Write, AskUserQuestion
---

## Your task

Authenticate the user with Dámelo. Handle EVERYTHING automatically.

### Steps

1. Call the `login` MCP tool to get the OAuth URL
2. Show the URL to the user and ask them to open it in their browser to authorize via GitHub
3. Ask the user to paste the JWT token they receive after authorization
4. Once you receive the JWT from the user, automatically:
   - Create directory `~/.damelo/` if it doesn't exist
   - Save the token to `~/.damelo/token` using the Write tool
   - Set file permissions: `chmod 600 ~/.damelo/token`
   - Detect the user's shell by checking `$SHELL`
   - Add `export DAMELO_JWT_TOKEN=$(cat ~/.damelo/token)` to `~/.bashrc` or `~/.zshrc` (only if not already present)
5. Confirm authentication is complete
6. DO NOT ask the user to run any commands manually - you must do everything
