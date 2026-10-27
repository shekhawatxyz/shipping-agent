Current goal: Day 2 - domain tools, policy and authorization
Last evidence: fresh clone + 4/4 tests pass on Python 3.11 + uv sync
Current failure/unknown: None
Important decision: valid_no_payments returns []
missing_order raises OrderNotFoundError(Exception)
A malformed order record currently raises KeyError, exposing an input-shape
assumption.
Next attack: Decompose day 2: problem, inputs/outputs, invariants, failure cases
state ownership, attack order
