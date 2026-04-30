---
name: Permission Sound Configure
description: Configure the permission-sound plugin: change sound, enable/disable, or test it. Triggers on "permission sound", "notification sound", "alert sound", or "configure sound".
---

# Permission Sound Configuration

You are configuring the **permission-sound** plugin, which plays a sound when Claude Code needs user permission for a tool call.

## What You Can Do

### Change the notification sound

Available macOS sounds in `/System/Library/Sounds/`:

| Sound | Character |
|-------|-----------|
| Basso | Deep bass |
| Blow | Short blow |
| Bottle | Bottle pop |
| Frog | Frog croak |
| Funk | Funk tone |
| **Glass** | Light ting (default) |
| Hero | Hero sound |
| Morse | Morse code |
| Ping | Ping |
| Pop | Pop sound |
| Purr | Soft purr |
| Sosumi | Classic Mac |
| Submarine | Sonar |
| Tink | Light tink |

To change the sound, edit the `SOUND` variable in `${CLAUDE_PLUGIN_ROOT}/scripts/permission-sound.py`:

```python
SOUND = '/System/Library/Sounds/Hero.aiff'  # Change to desired sound
```

### Test the sound

Run this command to verify the current sound works:

```bash
afplay /System/Library/Sounds/Glass.aiff
```

### Disable the plugin

Remove the hook entry from `hooks/hooks.json` or disable the plugin in Claude Code settings.

### Check plugin status

Verify the hook is configured:
```bash
cat "${CLAUDE_PLUGIN_ROOT}/hooks/hooks.json"
```

## How It Works

1. On every `PreToolUse` event, the hook runs `permission-sound.py`
2. The script reads the tool name from stdin JSON
3. It checks the tool against `permissions.allow` in `~/.claude/settings.json`
4. If the tool is NOT auto-allowed → plays Glass.aiff
5. If the tool is auto-allowed (Read, Edit, Bash(*), mcp__*, etc.) → silent

