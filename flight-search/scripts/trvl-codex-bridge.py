#!/opt/homebrew/bin/python3
"""Proxy trvl's stdio MCP and remove response fields Codex 0.151 cannot decode."""

from __future__ import annotations

import json
import subprocess
import sys
import threading
from typing import Any


TRVL_BIN = "/opt/homebrew/bin/trvl"


def sanitize_result(message: Any) -> Any:
    """Keep trvl results compatible with Codex's MCP response decoder."""
    if not isinstance(message, dict) or not isinstance(message.get("result"), dict):
        return message

    result = message["result"]
    content = result.get("content")
    if not isinstance(content, list):
        return message

    sanitized_content = []
    changed = False
    for block in content:
        if isinstance(block, dict) and block.get("type") == "resource_link":
            changed = True
            continue
        if isinstance(block, dict) and "annotations" in block:
            block = dict(block)
            block.pop("annotations")
            changed = True
        sanitized_content.append(block)

    if not changed:
        return message

    sanitized = dict(message)
    sanitized_result = dict(result)
    sanitized_result["content"] = sanitized_content
    sanitized["result"] = sanitized_result
    return sanitized


def forward_requests(child: subprocess.Popen[str]) -> None:
    try:
        for line in sys.stdin:
            child.stdin.write(line)
            child.stdin.flush()
    except BrokenPipeError:
        return
    finally:
        try:
            child.stdin.close()
        except BrokenPipeError:
            pass


def main() -> int:
    child = subprocess.Popen(
        [TRVL_BIN, "mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        text=True,
        bufsize=1,
    )
    input_thread = threading.Thread(target=forward_requests, args=(child,), daemon=True)
    input_thread.start()

    try:
        for line in child.stdout:
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                sys.stdout.write(line)
            else:
                sys.stdout.write(
                    json.dumps(
                        sanitize_result(message),
                        separators=(",", ":"),
                        ensure_ascii=False,
                    )
                    + "\n"
                )
            sys.stdout.flush()
    finally:
        if child.poll() is None:
            child.terminate()
        child.wait()

    return child.returncode or 0


if __name__ == "__main__":
    raise SystemExit(main())
