# -*- coding: utf-8 -*-
"""
Personal Agent Dunbar Relationship Cadence FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentDunbarRelationshipCadence

mcp = FastMCP("genpark-personal-agent-dunbar-relationship-cadence-skill")
cadence = PersonalAgentDunbarRelationshipCadence()

@mcp.tool()
def classify_dunbar_layer_and_cadence(
    contact_id: str,
    closeness_score: float,
    days_since_last_contact: int
) -> str:
    """
    Classifies contact into Dunbar concentric layer and computes relationship decay warmth.
    """
    res = cadence.classify_dunbar_layer_and_cadence(contact_id, closeness_score, days_since_last_contact)
    return json.dumps(res, indent=2)

@mcp.tool()
def compute_relationship_entropy_and_drift(contacts_history_json: str) -> str:
    """
    Audits network-wide relationship decay and identifies high-drift reconnections.
    """
    contacts = json.loads(contacts_history_json)
    res = cadence.compute_relationship_entropy_and_drift(contacts)
    return json.dumps(res, indent=2)

@mcp.tool()
def generate_thoughtful_reconnection_cadence(
    contacts_json: str,
    weekly_touchpoint_budget: int = 5
) -> str:
    """
    Schedules mindful personal reconnection touchpoints within weekly cognitive budget.
    """
    contacts = json.loads(contacts_json)
    res = cadence.generate_thoughtful_reconnection_cadence(contacts, weekly_touchpoint_budget)
    return json.dumps(res, indent=2)

def main():
    print("Testing Dunbar Cadence FastMCP Server:")
    print(classify_dunbar_layer_and_cadence("alice_bff", 0.95, 12))

if __name__ == "__main__":
    main()
