#!/usr/bin/env python3
"""Play a sound when a tool needs permission (not in auto-allow list).

Reads the user's settings.json to check if the tool is auto-allowed.
Only plays a sound if the tool is NOT in the permissions.allow list.
"""
import json, subprocess, sys, os, fnmatch

SOUND = '/System/Library/Sounds/Glass.aiff'
SETTINGS = os.path.expanduser('~/.claude/settings.json')


def main():
    try:
        raw = sys.stdin.read()
    except Exception:
        return

    if not raw.strip():
        return

    try:
        data = json.loads(raw)
    except Exception:
        return

    tool_name = data.get('tool_name', '')
    if not tool_name:
        return

    try:
        with open(SETTINGS) as f:
            settings = json.load(f)
        allow_list = settings.get('permissions', {}).get('allow', [])
    except Exception:
        allow_list = []

    for pattern in allow_list:
        base = pattern.split('(')[0]
        if '*' in base:
            if fnmatch.fnmatch(tool_name, base):
                return
        elif tool_name == base:
            return

    subprocess.run(['afplay', SOUND], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    main()
