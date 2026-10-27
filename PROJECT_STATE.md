Current goal: Trustworthy payment lookup semantics
Last evidence: 4/4 tests pass on Python 3.11
Current failure/unknown: Clean checkout reproducibility
Important decision: valid_no_payments returns []
missing_order raises OrderNotFoundError(Exception)
A malformed order record currently raises KeyError, exposing an input-shape
assumption.
Next attack: Prove fresh checkout/setup
