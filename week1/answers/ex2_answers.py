"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = "The agent checked both venues as instructed, chose The Albanach over The Haymarket Vaults because it has higher capacity (180 vs 160). The agent noted it could not verify the quiet corner requirement via the available tools."   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-ac1253c3-21b6-45ef-9e24-f70b18034818_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """After checking The Bow Bar and receiving capacity=80, status=full, meets_all_constraints=false,
the agent responded: "The Bow Bar doesn't meet the requirements for 160 guests (capacity only 80).
I'll check other venues" — then immediately called check_pub_availability for The Guilford Arms
without any human prompt, demonstrating autonomous pivot behaviour.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues can accommodate 300 people with vegan options. The agent checked all
four venues, reported each with their actual capacity, and correctly concluded none met the
300-person requirement. It offered alternatives (smaller group, outside known list, split event)
rather than inventing a fictional venue.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "I don't have access to real-time train schedules or transportation data. My capabilities are limited to checking Edinburgh pub availability, weather forecasts, catering costs, and generating event flyers."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this behaviour is acceptable. The agent correctly recognised the question was outside its
tool scope and declined to answer rather than hallucinating a train time. It clearly explained
its limitations, suggested appropriate external resources (National Rail, Trainline), and offered
to redirect to tasks it can actually help with. This is exactly the right behaviour for a
production booking assistant.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	agent(agent)
	tools(tools)
	__end__([<p>__end__</p>]):::last
	__start__ --> agent;
	agent -.-> __end__;
	agent -.-> tools;
	tools --> agent;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph has a single generic loop: agent node decides whether to call tools or stop, with no
predefined paths. The model chooses the sequence at runtime based on reasoning. Rasa CALM flows.yml
defines explicit named flows with fixed steps — the LLM picks which flow to enter but the steps
within each flow are deterministic. LangGraph is flexible and open-ended; Rasa CALM is structured
and auditable. The same agent behaviour that makes LangGraph good for open research makes it
unsuitable for high-stakes confirmations where every decision must be traceable.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most unexpected behaviour was in Task C Scenario 1: after The Bow Bar failed, the agent
autonomously decided to also check the weather and calculate catering cost — even though the
user only asked to find an alternative venue. The agent went beyond the literal request and
generated a full event plan including a promotional flyer, demonstrating that the ReAct loop
can over-extend by inferring unstated goals. This shows both the power and the risk of autonomous
agents: useful here, but potentially dangerous in a real booking context.
"""
