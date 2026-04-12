"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All 3 formatting conditions produced correct answers with the 70B model on the
clean baseline dataset. The plain format picked Haymarket Vaults while XML and
sandwich both picked The Albanach — both are valid since they satisfy all constraints.
The strong model handled all formats equally well, showing no sensitivity to structure
when the data is clean and unambiguous.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the most dangerous distractor because it satisfies two out of
three constraints — capacity 160 and vegan yes — and only fails on status=full.
A model that skims the data without carefully checking all three constraints would
likely select it over The Haymarket Vaults which appears immediately after.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran because both A and B were all-correct, switching to the smaller 8B model
to find where formatting starts to matter. Surprisingly, the 8B model also got all
three conditions correct and consistently picked The Haymarket Vaults across all
formats. This suggests the dataset, even with near-miss distractors, still has a
high enough signal-to-noise ratio for even the smaller model to handle correctly.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal-to-noise ratio is low — when there
are many similar-looking options, when the correct answer is buried in the middle of
a long list, or when using smaller, less capable models. Strong frontier models can
overcome poor formatting on clean datasets, but as data complexity increases or model
size decreases, structured formats like XML and sandwich that exploit primacy and
recency attention biases become critical for reliable extraction.
"""
