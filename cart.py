"""A tiny shopping-cart pricing module.

This repository is the demo target for PR Guardian, an autonomous
pull-request triage agent built for the Agentware hackathon. The code
here is deliberately small so that a reviewer (human or agent) can read
the whole thing in a minute.
"""


def subtotal(items):
    """Return the sum of price * qty for every item in the cart.

    Each item is a dict with 'price' and 'qty' keys. An empty cart
    has a subtotal of 0.0.
    """
    total = 0.0
    for item in items:
        total += item["price"] * item["qty"]
    return total


def apply_discount(total, percent):
    """Return total reduced by percent (0 to 100)."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return total * (1 - percent / 100)


def with_tax(total, rate=0.075):
    """Return total with tax added at the given rate."""
    return total * (1 + rate)


def checkout(items, discount_percent=0, tax_rate=0.075):
    """Return the final amount payable for a cart."""
    amount = subtotal(items)
    amount = apply_discount(amount, discount_percent)
    amount = with_tax(amount, tax_rate)
    return round(amount, 2)
