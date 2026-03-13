# nova-agent-starter
Starter template for integrating the Sharpe Nova OS decision context primitive into autonomous capital agents.

# Nova Agent Starter

Starter template for integrating the **Sharpe Nova OS decision context primitive** into autonomous capital agents.

Nova provides **decision-support infrastructure for autonomous capital systems**.

Agents query Nova before meaningful capital decisions to understand:

- current market regime  
- advisory guardrails  
- historical memory context  

Nova does **not** execute trades or control capital.

Nova informs decisions.  
Agents execute strategies.

---

# Design Philosophy

Sharpe Nova OS follows four principles:

Query the past  
Classify the present  
Support decisions  
Never control capital

Nova provides **decision context**, not execution logic.

---

# Core Primitive

Agents interact with Nova through a single primitive:

```python
ctx = nova.context()
