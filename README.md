# 🧙‍♂️ WizardAPI

**WizardAPI** is a magical Python framework that lets developers cast spells as
if they were powerful wizards. Whether you want to throw fireballs at bugs or
summon dragons to help with debugging — WizardAPI has you covered.

> Because coding is already magic. Let's make it official.

---

## ✨ Features

- 🔥 `fireball(target)` — Deal damage to your enemies.
- 🐉 `summon_familiar(type)` — Summon your magical companion.
- 🛡️ `shield(strength)` — Protect your code from crashes.
- 🕵️ `invisibility(duration)` — Hide from stack traces.
- 🧪 Create your own spells with `@spell` decorator.
- 🪄 Designed to be fun, educational, and Sphinx-demo friendly.

---

## 📦 Installation

```bash
pip install wizardapi
````

Or, from source:

```bash
git clone https://github.com/elena-soloveva/wizardapi.git
cd wizardapi
python setup.py install
```

Requires:

* Python 3.8+
* Mana ≥ 50 MP

---

## 🚀 Quick Start

```python
from wizardapi import SpellCaster

caster = SpellCaster(api_key="your-secret-scroll")
caster.cast("fireball", target="bug")
```

Output:

```
🔥 You cast Fireball on Bug!
Bug takes 42 fire damage.
```

---

## 📚 Documentation

Full documentation is available at:
👉 [https://elena-soloveva.github.io/wizardapi/](https://elena-soloveva.github.io/wizardapi/)

Built with [Sphinx](https://www.sphinx-doc.org) using Markdown and [MyST
Parser](https://myst-parser.readthedocs.io/).

---

## 🧪 Creating Custom Spells

You can write your own spells with the `@spell` decorator:

```python
from wizardapi import spell

@spell(name="rain_of_cats")
def rain_of_cats(target):
    return f"☔ It's raining cats on {target}!"
```

Register the spell:

```python
caster.register_custom_spell(rain_of_cats)
caster.cast("rain_of_cats", target="orc")
```

---

## 🧙‍♀️ Contributing

Pull requests are welcome — especially if you're a level 5+ mage.
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance.

---

## 📜 License

This project is licensed under the **MIT License**.
No actual mana or spell components required.

```

