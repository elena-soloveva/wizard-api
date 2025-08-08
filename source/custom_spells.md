# Creating Your Own Spells 🧪

You can define your own spells using the `@spell` decorator.

```python
from wizardapi import spell

@spell(name="rain_of_cats")
def rain_of_cats(target):
    return f"☔ It's raining cats on {target}!"
```

Registering the spell:

```python
caster.register_custom_spell(rain_of_cats)

print(caster.cast("rain_of_cats", target="orc"))
```
