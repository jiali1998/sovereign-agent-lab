"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = [
    "search_venues",
    "get_venue_details"
]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venues found. The search returned 0 matches for 300 guests with vegan options — no venue in the known list meets that capacity requirement."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Modified the VENUES data in mcp_venue_server.py (added a new venue or changed
existing venue data), then reran exercise4_mcp_client.py without touching it.
The client immediately reflected the updated venue list — query_1 now returned
only The Haymarket Vaults (count: 1) instead of both venues from the first run.
exercise4_mcp_client.py required zero changes. This confirms the key MCP property:
the server is the single source of truth for tool definitions and data; agents
connect and discover tools at runtime rather than importing them at code level.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP decouples the tool layer from the agent entirely. Both the LangGraph agent and
the Rasa CALM agent can connect to the same MCP server and share identical tools
without either needing to import or know about the other. When a tool changes or
a new venue is added, only the server is updated — no agent code changes, no
redeployment of agents.

"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The LangGraph Headless Automator handles open-ended research tasks because it can reason autonomously through unknowns, pivot when venues are unavailable, and sequence tool calls without predetermined steps.
- The Rasa CALM Digital Employee handles the confirmation call because every decision must be deterministic and auditable, with hard Python guards preventing the agent from exceeding Rod's authorised deposit or capacity limits.
- A shared MCP venue server exposes search_venues and get_venue_details to both agents so tool updates propagate automatically without touching agent code.
- A vector store provides the Automator with memory of past sessions so it can recall previously researched venues and avoid repeating work across weeks.
- An observability layer tracks token usage, tool call latency, and safety guardrail hits so production failures can be diagnosed without re-running entire agent sessions.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph handles the research and CALM handles the confirmation call. Swapping
them feels wrong because of what each agent does when it hits the unexpected.

In Task C Scenario 1, the LangGraph agent autonomously pivoted from The Bow Bar
to The Guilford Arms to The Albanach without being told — it reasoned its way
through an unplanned sequence. That flexibility is essential for research where
the path cannot be predetermined. But in a phone call with a pub manager,
that same improvisation is dangerous: the agent might reason "£250 fee plus
£100 insurance is technically two payments under £300" and accept a deposit
we never authorised.

CALM's inability to go off-script is precisely what makes it safe for the call.
When asked about parking mid-conversation, it deflected and held its position
in the flow. It cannot call a tool that isn't in flows.yml. It cannot accept
terms beyond MAX_DEPOSIT_GBP=300 no matter how the manager phrases it.
LangGraph doing the call would create legal exposure. CALM doing the research
would stall on the first unexpected venue name it hadn't been trained on.
"""
