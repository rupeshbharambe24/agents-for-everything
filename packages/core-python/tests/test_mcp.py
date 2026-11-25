"""Extended local MCP tool registry tests."""

import unittest
from pathlib import Path

from agents_for_everything.manifest import discover_mcp_servers
from agents_for_everything.mcp import LocalMCPRegistry


class MCPRegistryTests(unittest.TestCase):
    def test_phase2_mcp_servers_discovered_and_callable(self) -> None:
        root = Path(__file__).resolve().parents[3]
        servers = discover_mcp_servers(root)
        self.assertGreaterEqual(len(servers), 36)

        reg = LocalMCPRegistry(workspace_root=root)
        self.assertEqual(reg.call("afe/policy-engine", {"action": "read_file"})["decision"], "allow")
        self.assertEqual(reg.call("afe/policy-engine", {"action": "drop_db"})["decision"], "deny")
        self.assertIn("results", reg.call("afe/news-api", {"query": "MCP"}))
        self.assertIn("places", reg.call("afe/maps", {"query": "Pune"}))
        self.assertIn("issues", reg.call("afe/issue-tracker", {"op": "list"}))
        self.assertIn("alerts", reg.call("afe/observability", {"service": "api"}))
        self.assertIn("resources", reg.call("afe/cloud", {"op": "inventory"}))
        self.assertEqual(reg.call("afe/git", {"op": "status"})["branch"], "main")
        self.assertEqual(reg.call("afe/erp", {"op": "read_inventory"})["status"], "ok")
        self.assertEqual(reg.call("afe/payments", {})["status"], "read_only")
        self.assertIn("crisis_resources", reg.call("afe/medical-kb", {}))
        self.assertIn("events", reg.call("afe/logistics", {"tracking_id": "AWB123"}))
        self.assertEqual(reg.call("afe/compliance-reg", {})["status"], "screened_for_review")


if __name__ == "__main__":
    unittest.main()
