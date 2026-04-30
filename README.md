# permission-sound

Play a sound notification when Claude Code needs user permission for a tool call.

## How It Works

When Claude Code calls a tool that isn't auto-allowed in your `settings.json`, this plugin plays **Glass.aiff** to alert you. Tools that are auto-allowed (like `Read(*)`, `Edit(*)`, `Bash(*)`, `mcp__*`) remain silent.

1. On every `PreToolUse` event, `permission-sound.py` runs
2. It reads the tool name from the hook input
3. It checks against your `permissions.allow` list in `~/.claude/settings.json`
4. If the tool is **not** auto-allowed → plays the sound
5. If the tool is auto-allowed → silent

## Installation

```bash
claude plugin add MisterKarott/permission-sound
```

Then restart Claude Code.

## Requirements

- macOS (uses `afplay` for sound playback)
- Python 3
- Claude Code CLI

## Configuration

### Change the sound

Edit `SOUND` in the script:

```python
SOUND = '/System/Library/Sounds/Hero.aiff'
```

Available sounds: `Basso`, `Blow`, `Bottle`, `Frog`, `Funk`, `Glass` (default), `Hero`, `Morse`, `Ping`, `Pop`, `Purr`, `Sosumi`, `Submarine`, `Tink`.

### Test the sound

```bash
afplay /System/Library/Sounds/Glass.aiff
```

## Uninstall

```bash
claude plugin remove permission-sound
```

## License

MIT
