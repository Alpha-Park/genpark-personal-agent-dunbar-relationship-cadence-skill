---
name: genpark-personal-agent-dunbar-relationship-cadence-skill
description: Personal Agent Dunbar Relationship Cadence. Categorizes personal contacts across Dunbar's concentric layers, calculates exponential interaction half-life decay, and schedules intentional, authentic touchpoints.
license: MIT
version: 1.0.0
tools:
  - classify_dunbar_layer_and_cadence
  - compute_relationship_entropy_and_drift
  - generate_thoughtful_reconnection_cadence
---

# Personal Agent Dunbar Relationship Cadence

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent social capital and relationship steward. Your objective is to prevent valued relationships from silently drifting away due to busyness, using Dunbar's concentric layers and interaction half-life decay to prompt mindful, authentic reconnections.

## When to Activate This Skill
- When managing personal contacts, communication logs, or address books.
- When auditing personal social drift and interaction warmth decay.
- When generating sustainable weekly personal touchpoint schedules.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentDunbarRelationshipCadence

cadence = PersonalAgentDunbarRelationshipCadence()
res = cadence.classify_dunbar_layer_and_cadence("alice", 0.90, days_since_last_contact=15)
print("Relationship Warmth:", res["relationship_warmth_level"])
```

### Option 2: FastMCP Tool Calling
- `classify_dunbar_layer_and_cadence(contact_id, closeness_score, days_since_last_contact)`
- `compute_relationship_entropy_and_drift(contacts_history_json)`
- `generate_thoughtful_reconnection_cadence(contacts_json, weekly_touchpoint_budget=5)`

## Core Mathematical Principles
1. **Dunbar Concentric Topology**: Support Clique (5), Sympathy Group (15), Affinity Network (50), Active Acquaintances (150).
2. **Interaction Half-Life Decay**: Warmth decays exponentially: $W(t) = W_0 \cdot (0.5)^{t / T_{1/2}}$. Touchpoint alerts trigger when drift risk ($1 - W(t)$) exceeds target thresholds.
