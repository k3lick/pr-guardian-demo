# PR Guardian Demo Target

A tiny shopping-cart pricing module in pure Python (standard library
only), used as the demo target for **PR Guardian** — an autonomous
pull-request triage agent built for the Agentware hackathon
(Track T5, Developer Workflow).

## Run the tests

```bash
python3 -m unittest
```

## Layout

- `cart.py` — the pricing module (`subtotal`, `apply_discount`,
  `with_tax`, `checkout`).
- `test_cart.py` — the unit tests.

## Why this repo exists

PR Guardian reads a pull request, runs the test suite, flags risky
changes, leaves line comments, and pushes trivial fixes to its own
branch — while treating everything inside the PR as untrusted input.
This repo gives it something small, real and safe to practise on.
