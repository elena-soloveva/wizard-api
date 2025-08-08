# Magic Errors and Exceptions 🧨

Sometimes, spells go wrong. Here's how to handle magical mishaps.

## Common exceptions

- `SpellNotFoundError` — You tried to cast a spell that doesn't exist.
- `NotEnoughManaError` — You ran out of MP (mana points).
- `SummoningCircleCorrupted` — Invalid glyphs in your summoning parameters.

## Example:

```python
try:
    caster.cast("resurrect_unicorn")
except SpellNotFoundError:
    print("This spell is forbidden in your realm.")
```
