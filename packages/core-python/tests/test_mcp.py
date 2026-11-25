"""Extended local MCP tool registry tests."""

import unittest
from pathlib import Path

from agents_for_everything.manifest import discover_mcp_servers
from agents_for_everything.mcp import LocalMCPRegistry


class MCPRegistryTests(unittest.TestCase):
    def test_phase2_mcp_servers_discovered_and_callable(self) -> None:
        root = Path(__file__).resolve().parents[3]
        servers = discover_mcp_servers(root)
        self.assertGreaterEqual(len(servers), 30)

        reg = LocalMCPRegistry(workspace_root=root)
        self.assertEqual(reg.call("afe/policy-engine", {"action": "read_file"})["decision"], "allow")
        self.assertEqual(reg.call("afe/policy-engine", {"action": "drop_db"})["decision"], "deny")
        self.assertIn("results", reg.call("afe/news-api", {"query": "MCP"}))
        self.assertIn("places", reg.call("afe/maps", {"query": "Pune"}))
        self.assertIn("issues", reg.call("afe/issue-tracker", {"op": "list"}))
        self.assertIn("alerts", reg.call("afe/observability", {"service": "api"}))
        self.assertIn("resources", reg.call("afe/cloud", {"op": "inventory"}))


if __name__ == "__main__":
    unittest.main()
