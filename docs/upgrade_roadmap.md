# 🚀 Halal Warmachine: Upgrade Roadmap

> All future upgrades from legacy and evolution threads compiled + tracked below. Updated automatically.

---

## ✅ Phase 1: Stability Layer (COMPLETE)
| Module | Description | Status |
|--------|-------------|--------|
| `cmd_watcher.py` | Watches terminal output live | ✅
| `log_intelligence_router.py` | Categorises log lines into summary | ✅
| `file_integrity_watchdog.py` | Detects any file changes or corruption | ✅
| `resource_usage_watchdog.py` | Monitors CPU/RAM load | ✅
| `multi_terminal_sentinel.py` | Detects new command windows | ✅
| `log_watcher.py` | Detects error keywords in logs | ✅
| `loop_warden.py` | Detects freeze via log silence | ✅

---

## 🧠 Phase 2: Coordination + Control (ACTIVE)
| Module | Description | Status |
|--------|-------------|--------|
| `redis_client.py` | Shared memory access for all agents | ✅
| `loop_commander.py` | Oversees system risk flags and coordination | ✅
| `patch_smith.py` | Auto-applies patches on crash or trigger | ✅
| `drive_sync_agent.py` | Google Drive log and patch sync | ✅

---

## 🔄 Phase 3: Intelligence & Learning
| Upgrade | Description | Status |
|---------|-------------|--------|
| `evolver_memory_layer.py` | Recalls past winning/losing patterns | ✅
| `vector_memory_store.py` | Persistent pattern memory with ChromaDB | 🔄 (in progress)
| Redis state machine | Inter-agent memory and live triggers | ✅
| Telegram alerts | On crash/error/patch | 🔄 (to be integrated)
| GPT call tier controller | Use fast models for routine logic | ❌ (GPT-only for now)

---

## 🌐 Phase 4: AI System Layer (Queued)
| Feature | Tech Stack | Status |
|---------|------------|--------|
| Multi-agent orchestration | `CrewAI` | 🔜
| Agent routing / state graph | `LangGraph` | 🔜
| Cost-reduction AI fallback | `Legacy` / offline GPT | 🔜
| Source scanner agent | `source_scavenger.py` for GitHub/Reddit/Forums | 🔄 (tab-only now)
| Fast LLM tier fallback | Claude Haiku, GPT-3.5 | ❌ (not in use)

---

## ✅ Integration Tracking
- [x] Chrome GPT Tabs migrated ✅
- [x] Redis installed and live ✅
- [x] Chroma installed ✅
- [x] Agents reconnected to redis_client ✅
- [x] Folder structure doc + reference sync ✅
- [ ] Telegram alerts wired to crash flow ❌
- [ ] Trading rules exposure to Redis ❌

---

### 🧠 Next Priorities
- Vector memory: strategy/clone/spoof patterns → ChromaDB
- Telegram alert bridge (agent crash, patch applied, restart, error)
- GPT budget controller for live run (daily cap + critical-only logic)
- Source-Scavenger rewrite into `.py`
- Trigger `CrewAI` + `LangGraph` setup post-live stability

---

*This roadmap will be updated live. You never need to remember anything — it’s all logged right here.*
