(() => {
  const data = window.AFE_SITE_DATA || {
    catalog: { agents: [], teams: [], recipes: [], mcp_servers: [], counts: {} },
    graph: { edges: [] },
    leaderboard: [],
  };
  const agents = data.catalog.agents || [];
  const teams = data.catalog.teams || [];
  const recipes = data.catalog.recipes || [];
  const servers = data.catalog.mcp_servers || [];
  const edges = data.graph.edges || [];
  const agentMap = Object.fromEntries(agents.map((a) => [a.id, a]));
  const lbMap = Object.fromEntries((data.leaderboard || []).map((r) => [r.agent_id, r]));

  const statsEl = document.getElementById("stats");
  const counts = data.catalog.counts || {};
  statsEl.innerHTML = [
    `Agents: ${counts.agents ?? agents.length} (${counts.verified_agents ?? agents.filter((a) => a.verified).length} verified)`,
    `Teams: ${counts.teams ?? teams.length}`,
    `Recipes: ${counts.recipes ?? recipes.length}`,
    `MCP Servers: ${counts.mcp_servers ?? servers.length}`,
    `Compat Edges: ${edges.length}`,
  ].map((s) => `<span class="stat-pill">${s}</span>`).join("");

  const famSelect = document.getElementById("family");
  const catSelect = document.getElementById("category");
  [...new Set(agents.map((a) => a.family))].sort().forEach((f) => {
    const opt = document.createElement("option");
    opt.value = f;
    opt.textContent = f;
    famSelect.appendChild(opt);
  });
  function populateCategories() {
    const fam = famSelect.value;
    const prev = catSelect.value;
    catSelect.innerHTML = '<option value="">All Categories</option>';
    [...new Set(agents.filter((a) => !fam || a.family === fam).map((a) => a.category))]
      .sort()
      .forEach((c) => {
        const opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        catSelect.appendChild(opt);
      });
    if ([...catSelect.options].some((o) => o.value === prev)) catSelect.value = prev;
  }
  populateCategories();

  const searchEl = document.getElementById("search");
  const prioEl = document.getElementById("priority");
  const safetyEl = document.getElementById("safety");
  const matEl = document.getElementById("maturity");
  const listEl = document.getElementById("agentList");
  const countEl = document.getElementById("resultsCount");
  const inspEl = document.getElementById("inspector");
  const tabs = document.querySelectorAll("#viewTabs .tab");
  let activeView = "agents";
  let selectedId = null;

  function renderAgentInspector(agent) {
    selectedId = agent.id;
    const lb = lbMap[agent.id];
    const incoming = edges.filter((e) => e.to === agent.id).slice(0, 14);
    const outgoing = edges.filter((e) => e.from === agent.id).slice(0, 14);
    const a2aCard = {
      name: agent.name,
      id: agent.id,
      version: agent.version || "0.1.0",
      description: agent.summary,
      skills: [{ id: agent.id, name: agent.name, tags: agent.tags || [] }],
      metadata: {
        safetyLevel: agent.safety_level,
        autonomyLevel: agent.autonomy || "L1",
        maturity: agent.maturity,
        verificationBadge: agent.badge || (agent.verified ? "verified" : "unverified"),
        digest: agent.digest || "",
      },
    };
    inspEl.innerHTML = `
      <h2>${agent.name}</h2>
      <div class="card-id">${agent.id}</div>
      <p class="muted">${agent.summary}</p>
      <div class="badges">
        <span class="badge">${agent.family}/${agent.category}</span>
        <span class="badge">${agent.priority}</span>
        <span class="badge ${agent.maturity}">${agent.maturity}</span>
        <span class="badge ${agent.verified ? "verified" : "unverified"}">${agent.badge || (agent.verified ? "verified" : "unverified")}</span>
        <span class="badge">${agent.safety_level}</span>
        <span class="badge">${agent.autonomy || "L1"}</span>
      </div>
      ${lb ? `<p class="muted">Eval pass rate: <strong>${Math.round(lb.pass_rate * 100)}%</strong> (${lb.passed}/${lb.cases})</p>` : ""}
      <p class="muted"><strong>Tools:</strong> ${((agent.tools && agent.tools.required) || []).join(", ") || "None (pure compute)"}<br/><strong>Locales:</strong> ${(agent.locales || ["en"]).join(", ")}</p>
      <h3>CLI Usage</h3>
      <pre>afe add ${agent.id}\nafe verify ${agent.id}\nafe migrate ${agent.id}\nafe export ${agent.id} --as a2a</pre>
      <details>
        <summary class="muted"><strong>A2A Agent Card Preview</strong></summary>
        <pre>${JSON.stringify(a2aCard, null, 2)}</pre>
      </details>
      <h3>Composes (uses_agents)</h3>
      <ul class="edge-list">${(agent.uses_agents || []).length ? agent.uses_agents.map((u) => `<li><button class="edge-jump" data-agent="${u}">${u}</button></li>`).join("") : "<li>None (atomic)</li>"}</ul>
      <h3>Compatible Upstream (${incoming.length})</h3>
      <ul class="edge-list">${incoming.length ? incoming.map((e) => `<li><button class="edge-jump" data-agent="${e.from}">${e.from}</button></li>`).join("") : "<li>None matched</li>"}</ul>
      <h3>Compatible Downstream (${outgoing.length})</h3>
      <ul class="edge-list">${outgoing.length ? outgoing.map((e) => `<li><button class="edge-jump" data-agent="${e.to}">${e.to}</button></li>`).join("") : "<li>None matched</li>"}</ul>
    `;
    inspEl.querySelectorAll(".edge-jump").forEach((btn) => {
      btn.onclick = () => {
        const target = agentMap[btn.dataset.agent];
        if (target) {
          renderAgentInspector(target);
          render();
        }
      };
    });
  }

  function render() {
    const q = searchEl.value.toLowerCase().trim();
    const showAgentFilters = activeView === "agents";
    [famSelect, catSelect, prioEl, safetyEl, matEl].forEach((el) => {
      el.style.display = showAgentFilters ? "" : "none";
    });

    listEl.innerHTML = "";
    if (activeView === "agents") {
      const fam = famSelect.value;
      const cat = catSelect.value;
      const prio = prioEl.value;
      const saf = safetyEl.value;
      const mat = matEl.value;
      const filtered = agents.filter((a) => {
        if (fam && a.family !== fam) return false;
        if (cat && a.category !== cat) return false;
        if (prio && a.priority !== prio) return false;
        if (saf && a.safety_level !== saf) return false;
        if (mat && a.maturity !== mat) return false;
        if (!q) return true;
        const hay = `${a.id} ${a.name} ${a.family} ${a.category} ${a.summary} ${(a.tags || []).join(" ")}`.toLowerCase();
        return q.split(/\s+/).every((t) => hay.includes(t));
      });
      countEl.textContent = `Showing ${filtered.length} of ${agents.length} agents`;
      filtered.forEach((a) => {
        const card = document.createElement("div");
        card.className = "card" + (a.id === selectedId ? " active" : "");
        card.innerHTML = `
          <div class="card-title">${a.name}</div>
          <div class="card-id">${a.id}</div>
          <div class="badges">
            <span class="badge">${a.priority}</span>
            <span class="badge ${a.maturity}">${a.maturity}</span>
            <span class="badge ${a.verified ? "verified" : "unverified"}">${a.badge || (a.verified ? "verified" : "unverified")}</span>
            <span class="badge">${a.safety_level}</span>
            <span class="badge">${a.tier}</span>
          </div>
          <div class="card-summary">${a.summary}</div>
        `;
        card.onclick = () => { renderAgentInspector(a); render(); };
        listEl.appendChild(card);
      });
    } else if (activeView === "teams") {
      const filtered = teams.filter((t) => !q || `${t.id} ${t.name} ${t.summary} ${(t.members || []).join(" ")}`.toLowerCase().includes(q));
      countEl.textContent = `Showing ${filtered.length} of ${teams.length} teams`;
      filtered.forEach((t) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <div class="card-title">${t.name}</div>
          <div class="card-id">teams/${t.id}</div>
          <div class="badges"><span class="badge">${t.priority}</span><span class="badge">${t.pattern}</span><span class="badge">${(t.members || []).length} members</span></div>
          <div class="card-summary">${t.summary}</div>
        `;
        card.onclick = () => {
          inspEl.innerHTML = `<h2>${t.name}</h2><div class="card-id">teams/${t.id}</div><p class="muted">${t.summary}</p><h3>Members</h3><ul class="edge-list">${(t.members || []).map((m) => `<li><code>${m}</code></li>`).join("")}</ul><pre>afe graph ${t.id}</pre>`;
        };
        listEl.appendChild(card);
      });
    } else if (activeView === "recipes") {
      const filtered = recipes.filter((r) => !q || `${r.id} ${r.name} ${r.summary}`.toLowerCase().includes(q));
      countEl.textContent = `Showing ${filtered.length} of ${recipes.length} recipes`;
      filtered.forEach((r) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <div class="card-title">${r.name}</div>
          <div class="card-id">recipes/${r.id}</div>
          <div class="badges"><span class="badge">${r.priority}</span><span class="badge">${(r.agents || []).length} agents</span></div>
          <div class="card-summary">${r.summary}</div>
        `;
        card.onclick = () => {
          inspEl.innerHTML = `<h2>${r.name}</h2><div class="card-id">recipes/${r.id}</div><p class="muted">${r.summary}</p><h3>Agents Used</h3><ul class="edge-list">${(r.agents || []).map((a) => `<li><code>${a}</code></li>`).join("")}</ul>`;
        };
        listEl.appendChild(card);
      });
    } else {
      const filtered = servers.filter((s) => !q || `${s.id} ${s.name} ${s.summary}`.toLowerCase().includes(q));
      countEl.textContent = `Showing ${filtered.length} of ${servers.length} MCP servers`;
      filtered.forEach((s) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <div class="card-title">${s.name}</div>
          <div class="card-id">${s.id}</div>
          <div class="badges"><span class="badge">${s.transport}</span></div>
          <div class="card-summary">${s.summary}</div>
        `;
        listEl.appendChild(card);
      });
    }
  }

  tabs.forEach((t) => {
    t.onclick = () => {
      tabs.forEach((b) => b.classList.remove("active"));
      t.classList.add("active");
      activeView = t.dataset.view;
      render();
    };
  });
  famSelect.addEventListener("change", () => { populateCategories(); render(); });
  [searchEl, catSelect, prioEl, safetyEl, matEl].forEach((el) => el.addEventListener("input", render));
  if (agents.length) renderAgentInspector(agents[0]);
  render();
})();
