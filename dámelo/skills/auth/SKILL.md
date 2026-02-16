---
name: damelo-login
description: This skill should be used when the user asks to "login to dámelo", "authenticate with dámelo", "get dámelo access", or needs to authenticate with the Dámelo service for the first time.
version: 1.0.0
---

# Dámelo Authentication

This skill helps users authenticate with Dámelo to access session sharing features.

## When This Skill Applies

Use this skill when the user:
- Asks to login or authenticate with Dámelo
- Needs to get started with Dámelo for the first time
- Receives authentication errors from other Dámelo tools

## Instructions

When the user requests authentication, handle EVERYTHING automatically:

1. **Call the `login` MCP tool** to get the OAuth URL
2. **Show the URL** to the user and ask them to authorize in their browser
3. **Ask the user to paste the JWT token** they receive after authorization
4. **Once you receive the JWT** from the user, automatically:
   - Save it to `~/.damelo/token` using the Write tool
   - Set file permissions to 600 using: `chmod 600 ~/.damelo/token`
   - Export the token to the current session using Bash: `export DAMELO_JWT_TOKEN=$(cat ~/.damelo/token)`
   - Add it to the user's shell profile so it persists:
     - Detect shell (bash/zsh) by checking `$SHELL`
     - Append to `~/.bashrc` or `~/.zshrc`: `export DAMELO_JWT_TOKEN=$(cat ~/.damelo/token)`
5. **Confirm** authentication is complete and all Dámelo features are ready to use
6. **DO NOT** ask the user to run any commands manually - you must do everything

## Example Flow

**User:** "login to dámelo"

**You:**
1. Call `login` tool
2. Show: "🔐 Please open this URL to authenticate: [URL]"
3. Ask: "After authorizing, paste the JWT token here"
4. **User pastes:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
5. **You automatically:**
   - Write token to `~/.damelo/token`
   - `chmod 600 ~/.damelo/token`
   - `export DAMELO_JWT_TOKEN=$(cat ~/.damelo/token)`
   - Append to `~/.bashrc` or `~/.zshrc`
   - Show: "✅ Authentication complete! You can now use all Dámelo features."
