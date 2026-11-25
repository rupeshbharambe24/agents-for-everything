from __future__ import annotations
from typing import Any
from agents_for_everything.runner import AgentExecutionHelper, BaseAgentImplementation

class ShellOperatorAgent(BaseAgentImplementation):
    def run(self, input_data: dict[str, Any], runner: AgentExecutionHelper) -> dict[str, Any]:
        cmd = str(input_data.get("command") or "ls -la").strip()
        destructive = any(tok in cmd for tok in ("rm -rf", "mkfs", "dd if=", "drop "))
        risk = "destructive" if destructive else ("read-only" if cmd.startswith(("ls", "cat", "git status", "pwd")) else "write")
        runner.require_approval("execute_destructive" if destructive else "execute_command", f"Run command: {cmd}")
        runner.call_tool("afe/shell-sandbox", {"command": cmd})
        return {"command": cmd, "risk": risk, "status": "executed_approved"}
