(() => {
  const data = window.AFE_SITE_DATA || { catalog: { agents: [], teams: [], recipes: [], counts: {} }, graph: { edges: [] }, leaderboard: [] };
  const agents = data.catalog.agents || [];
  const edges = data.graph.edges || [];
  const lbMap = Object.fromEntries((data.leaderboard || []).map((r) => [r.agent_id, r]));

  const statsEl = document.getElementById("stats");
  const counts = data.catalog.counts || {};
  statsEl.innerHTML = [
    `Agents: ${counts.agents ?? agents.length}`,
    `Teams: ${counts.teams ?? 0}`,
    `Recipes: ${counts.recipes ?? 0}`,
    `MCP Servers: ${counts.mcp_servers ?? 0}`,
    `Compat Edges: ${edges.length}`,
  ].map((s) => `<span class="stat-pill">${s}</span>`).join("");

  const famSelect = document.getElementById("family");
  [...new Set(agents.map((a) => a.family))].sort().forEach((f) => {
    const opt = document.createElement("option");
    opt.value = f;
    opt.textContent = f;
    famSelect.appendChild(opt);
  });

  const searchEl = document.getElementById("search");
  const prioEl = document.getElementById("priority");
  const safetyEl = document.getElementById("safety");
  const matEl = document.getElementById("maturity");
  const listEl = document.getElementById("agentList");
  const countEl = document.getElementById("resultsCount");
  const inspEl = document.getElementById("inspector");
  let selectedId = null;

  function renderInspector(agent) {
    selectedId = agent.id;
    const lb = lbMap[agent.id];
    const incoming = edges.filter((e) => e.to === agent.id).slice(0, 12);
    const outgoing = edges.filter((e) => e.from === agent.id).slice(0, 12);
    inspEl.innerHTML = `
      <h2>${agent.name}</h2>
      <div class="card-id">${agent.id}</div>
      <p class="muted">${agent.summary}</p>
      <div class="badges">
        <span class="badge">${agent.family}/${agent.category}</span>
        <span class="badge">${agent.priority}</span>
        <span class="badge ${agent.maturity}">${agent.maturity}</span>
        <span class="badge">${agent.safety_level}</span>
        <span class="badge">${agent.autonomy}</span>
      </div>
      ${lb ? `<p class="muted">Eval pass rate: <strong>${Math.round(lb.pass_rate * 100)}%</strong> (${lb.passed}/${lb.cases})</p>` : ""}
      <h3>CLI Usage</h3>
      <pre>afe add ${agent.id}\nafe test ${agent.id}\nafe export ${agent.id} --as skill</pre>
      <h3>Composes (uses_agents)</h3>
      <ul class="edge-list">${(agent.uses_agents || []).length ? agent.uses_agents.map((u) => `<li><code>${u}</code></li>`).join("") : "<li>None (atomic)</li>"}</ul>
      <h3>Compatible Upstream (${incoming.length})</h3>
      <ul class="edge-list">${incoming.length ? incoming.map((e) => `<li><code>${e.from}</code></li>`).join("") : "<li>None matched</li>"}</ul>
      <h3>Compatible Downstream (${outgoing.length})</h3>
      <ul class="edge-list">${outgoing.length ? outgoing.map((e) => `<li><code>${e.to}</code></li>`).join("") : "<li>None matched</li>"}</ul>
    `;
  }

  function render() {
    const q = searchEl.value.toLowerCase().trim();
    const fam = famSelect.value;
    const prio = prioEl.value;
    const saf = safetyEl.value;
    const mat = matEl.value;

    const filtered = agents.filter((a) => {
      if (fam && a.family !== fam) return false;
      if (prio && a.priority !== prio) return false;
      if (saf && a.safety_level !== saf) return false;
      if (mat && a.maturity !== mat) return false;
      if (!q) return true;
      const hay = `${a.id} ${a.name} ${a.summary} ${(a.tags || []).join(" ")}`.toLowerCase();
      return q.split(/\s+/).every((t) => hay.includes(t));
    });

    countEl.textContent = `Showing ${filtered.length} of ${agents.length} agents`;
    listEl.innerHTML = "";
    filtered.forEach((a) => {
      const card = document.createElement("div");
      card.className = "card" + (a.id === selectedId ? " active" : "");
      card.innerHTML = `
        <div class="card-title">${a.name}</div>
        <div class="card-id">${a.id}</div>
        <div class="badges">
          <span class="badge">${a.priority}</span>
          <span class="badge ${a.maturity}">${a.maturity}</span>
          <span class="badge">${a.safety_level}</span>
          <span class="badge">${a.tier}</span>
        </div>
        <div class="card-summary">${a.summary}</div>
      `;
      card.onclick = () => {
        renderInspector(a);
        render();
      };
      listEl.appendChild(card);
    });
  }

  [searchEl, famSelect, prioEl, safetyEl, matEl].forEach((el) => el.addEventListener("input", render));
  if (agents.length) renderInspector(agents[0]);
  render();
})();
